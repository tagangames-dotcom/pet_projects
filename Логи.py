import os
import platform
import re
import subprocess
import tempfile
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# Классы для сбора, анализа и отчёта логов

class LogCollector:
    def __init__(self, logfiles):
        self.logfiles = logfiles

    def collect(self):
        collected_logs = []
        for logfile in self.logfiles:
            if not os.path.isfile(logfile):
                print(f"Файл {logfile} не найден.")
                continue
            try:
                with open(logfile, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                collected_logs.extend(lines)
            except PermissionError:
                print(f"Нет доступа к файлу {logfile}. Пропускаем.")
            except Exception as e:
                print(f"Ошибка при чтении {logfile}: {e}")
        return collected_logs


class LogAnalyzer:
    def __init__(self, logs, user_keywords=None):
        self.logs = logs
        self.anomalies = []
        self.user_keywords = user_keywords or []
        self.default_keywords = self._get_default_keywords_by_os()

    def _get_default_keywords_by_os(self):
        os_name = platform.system().lower()
        if 'windows' in os_name:
            return ['error', 'fail', 'warning', 'critical', 'exception', 'failed', 'denied']
        elif 'linux' in os_name:
            return ['error', 'fail', 'warning', 'critical', 'segfault', 'panic', 'denied']
        else:
            return ['error', 'fail', 'warning', 'critical']

    def analyze(self):
        keywords = list(set(self.default_keywords + self.user_keywords))
        if not keywords:
            return
        pattern = re.compile('|'.join(keywords), re.IGNORECASE)

        for line in self.logs:
            if pattern.search(line):
                self.anomalies.append(line.strip())

    def get_summary(self):
        return {
            'total_logs': len(self.logs),
            'anomalies_count': len(self.anomalies),
            'anomalies': self.anomalies,
            'used_keywords': self.default_keywords + self.user_keywords,
        }


class ReportGenerator:
    def __init__(self, analysis_result):
        self.result = analysis_result

    def generate_text_report(self):
        lines = []
        lines.append(f"Всего строк в логе: {self.result['total_logs']}")
        lines.append(f"Найдено аномалий: {self.result['anomalies_count']}")
        lines.append(f"Использованные ключевые слова для поиска: {', '.join(self.result['used_keywords'])}")
        if self.result['anomalies_count'] > 0:
            lines.append("Аномалии:")
            lines.extend(self.result['anomalies'])
        else:
            lines.append("Аномалий не найдено.")
        return '\n'.join(lines)

    def generate_console_report(self):
        print(self.generate_text_report())

    def generate_file_report(self, filename=None):
        if not filename:
            filename = f"log_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.generate_text_report())
        print(f"\nОтчёт сохранён в файл: {filename}")

# Функция экспорта логов Windows в текстовые файлы

def export_windows_logs_to_txt():
    temp_dir = tempfile.gettempdir()
    logs_to_export = {
        "System": os.path.join(temp_dir, "System_log.txt"),
        "Application": os.path.join(temp_dir, "Application_log.txt"),
        "Security": os.path.join(temp_dir, "Security_log.txt")
    }
    print("Экспортируем логи Windows Event Viewer в текстовые файлы...")

    for log_name, path in logs_to_export.items():
        ps_command = f'wevtutil qe {log_name} /f:text /c:10000 > "{path}"'
        try:
            subprocess.run(["powershell", "-Command", ps_command], check=True)
            print(f"Экспорт лога {log_name} выполнен: {path}")
        except subprocess.CalledProcessError:
            print(f"Ошибка при экспорте {log_name}. Возможно, недостаточно прав для доступа.")
            print(f"Пропускаем {log_name} лог.")

    # Исключаем Security лог из-за частых проблем с правами
    available_logs = [path for log_name, path in logs_to_export.items()
                      if os.path.isfile(path) and log_name != "Security"]
    return available_logs

# Функция определения стандартных логов ОС

def get_default_logs_by_os():
    system_os = platform.system().lower()
    default_logs = []
    if 'windows' in system_os:
        default_logs = export_windows_logs_to_txt()
    elif 'linux' in system_os:
        default_logs = [
            "/var/log/syslog",
            "/var/log/auth.log",
            "/var/log/kern.log",
            "/var/log/dmesg"
        ]
        default_logs = [f for f in default_logs if os.path.isfile(f)]
    else:
        default_logs = []
    return default_logs

# GUI класс

class LogAnalyzerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Система сбора и анализа логов")
        self.geometry("900x800")
        self.log_files = []
        self.analysis_result = None

        # Кнопка выбора файлов
        self.btn_select = tk.Button(self, text="Выбрать файл(ы) логов", command=self.select_files)
        self.btn_select.pack(pady=5)

        # Метка с выбранными файлами
        self.lbl_files = tk.Label(self, text="Файлы логов не выбраны.\nЕсли не выбирать — будут использованы стандартные логи ОС.")
        self.lbl_files.pack()

        # Поле для ввода ключевых слов
        frame_keywords = tk.Frame(self)
        frame_keywords.pack(pady=5)
        tk.Label(frame_keywords, text="Ключевые слова для поиска аномалий (через запятую):").pack(side=tk.LEFT)
        self.entry_keywords = tk.Entry(frame_keywords, width=50)
        self.entry_keywords.pack(side=tk.LEFT, padx=5)

        # Кнопка запуска анализа
        self.btn_run = tk.Button(self, text="Запустить анализ", command=self.run_analysis)
        self.btn_run.pack(pady=10)

        # Текстовое поле для вывода результатов
        self.txt_output = scrolledtext.ScrolledText(self, width=100, height=25)
        self.txt_output.pack(padx=10, pady=10)

        # Кнопка сохранения отчёта
        self.btn_save = tk.Button(self, text="Сохранить отчёт в файл", command=self.save_report)
        self.btn_save.pack(pady=5)

    def select_files(self):
        files = filedialog.askopenfilenames(title="Выберите файл(ы) с логами")
        if files:
            self.log_files = list(files)
            display_text = "Выбраны файлы логов:\n" + "\n".join(self.log_files)
        else:
            self.log_files = []
            display_text = "Файлы логов не выбраны.\nЕсли не выбирать — будут использованы стандартные логи ОС."
        self.lbl_files.config(text=display_text)

    def run_analysis(self):
        if self.log_files:
            logs_to_use = self.log_files
        else:
            logs_to_use = get_default_logs_by_os()
            if not logs_to_use:
                messagebox.showerror("Ошибка", "Не выбраны файлы логов и не найдены стандартные логи.")
                return
            else:
                self.lbl_files.config(text="Используются стандартные логи:\n" + "\n".join(logs_to_use))

        collector = LogCollector(logs_to_use)
        logs = collector.collect()
        if not logs:
            messagebox.showerror("Ошибка", "Не удалось прочитать логи.")
            return

        user_input = self.entry_keywords.get().strip()
        user_keywords = [kw.strip() for kw in user_input.split(',')] if user_input else []

        analyzer = LogAnalyzer(logs, user_keywords=user_keywords)
        analyzer.analyze()
        self.analysis_result = analyzer.get_summary()

        reporter = ReportGenerator(self.analysis_result)
        report_text = reporter.generate_text_report()

        self.txt_output.delete(1.0, tk.END)
        self.txt_output.insert(tk.END, report_text)

    def save_report(self):
        if not self.analysis_result:
            messagebox.showwarning("Внимание", "Отчёт отсутствует. Сначала запустите анализ.")
            return
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
            title="Сохранить отчёт как"
        )
        if filename:
            reporter = ReportGenerator(self.analysis_result)
            reporter.generate_file_report(filename)
            messagebox.showinfo("Успех", f"Отчёт сохранён в файл:\n{filename}")

if __name__ == "__main__":
    app = LogAnalyzerGUI()
    app.mainloop()


