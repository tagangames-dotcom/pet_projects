from tkinter import *
import webbrowser

# интерфейс
root = Tk()
root.title("Google Dorks GUI")
root.geometry("500x600")
root.iconbitmap(r"D:\программироваание проекты\pet_projects\1764466492.ico")

# Поля ввода
Label(root, text="Текст для поиска:").pack()
enter_search = Entry(root, width=40)
enter_search.pack()

Label(root, text="Сайт для поиска (site:):").pack()
site_entry = Entry(root, width=40)
site_entry.pack()

# Выбор типа файла
Label(root, text="Тип файла:").pack()
filetype_var = StringVar()
filetype_var.set("")  # Будет хранить выбранный тип файла
filetypes = [
    ("PDF", "pdf"),
    ("Word DOC", "doc"),
    ("Word DOCX", "docx"),
    ("Excel XLS", "xls"),
    ("Excel XLSX", "xlsx"),
    ("PowerPoint PPT", "ppt"),
    ("PowerPoint PPTX", "pptx"),
    ("Текст TXT", "txt")
]

for text, value in filetypes:
    Radiobutton(root, text=text, variable=filetype_var, value=value, indicatoron=0).pack()

# Другие операторы
Label(root, text="Дополнительные операторы:").pack()

intitle_var = BooleanVar()
Checkbutton(root, text="intitle (в заголовке)", variable=intitle_var).pack()

inurl_var = BooleanVar()
Checkbutton(root, text="inurl (в адресе)", variable=inurl_var).pack()

intext_var = BooleanVar()
Checkbutton(root, text="intext (в тексте)", variable=intext_var).pack()

button_search = Button(root, text="🔍 Поиск в Google", font=("Arial", 12), bg="lightblue")
button_search.pack()

# Поле для предпросмотра запроса
Label(root, text="Предпросмотр запроса:").pack()
preview_text = Text(root, height=2, width=50, bg="#f0f0f0")
preview_text.pack()


# логика
def build_dork():
    base = enter_search.get()  # основной текст
    site = site_entry.get()  # сайт для поиска
    query_parts = []

    # Основной текст (если есть)
    if base:
        query_parts.append(base)

    # Тип файла (выбор одного из вариантов)
    if filetype_var.get():
        query_parts.append(f"filetype:{filetype_var.get()}")

    # Поиск по сайту
    if site:
        query_parts.append(f"site:{site}")

    # Дополнительные операторы
    if intitle_var.get() and base:
        query_parts.append(f"intitle:{base}")

    if inurl_var.get() and base:
        query_parts.append(f"inurl:{base}")

    if intext_var.get() and base:
        query_parts.append(f"intext:{base}")

    # Собираем финальный запрос
    final_query = " ".join(query_parts)

    # Показываем предпросмотр
    preview_text.delete(1.0, END)
    preview_text.insert(END, final_query)

    # Открываем Google с запросом
    if final_query:
        google_url = f"https://www.google.com/search?q={final_query}"
        webbrowser.open(google_url)
        print(f"Открываю: {google_url}")


button_search.config(command=build_dork)

# Запуск
mainloop()