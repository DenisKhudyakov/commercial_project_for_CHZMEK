import tkinter as tk
from tkinter import filedialog
from functools import partial
from src.utills import script_stages_and_form


class Screen:
    """
    Класс управления скриптом через интерфейс
    """

    def __init__(self):
        self.entry1 = None
        self.label1 = None
        self.browse_button1 = None
        self.label2 = None
        self.entry2 = None
        self.browse_button2 = None
        self.run_button = None
        self.root = tk.Tk()
        self.root.title("Запуск скрипта")

    @staticmethod
    def browse_file(entry):
        filename = filedialog.askopenfilename()
        entry.delete(0, tk.END)
        entry.insert(0, filename)

    @staticmethod
    def run_script(entry1, entry2):
        file1_path = entry1.get()
        file2_path = entry2.get()
        script_stages_and_form(file1_path, file2_path)

    def widget(self):
        # Создание и настройка виджетов
        self.label1 = tk.Label(self.root, text="Вставьте формуляр:")
        self.label1.grid(row=0, column=0)

        self.entry1 = tk.Entry(self.root, width=50)
        self.entry1.grid(row=0, column=1)

        self.browse_button1 = tk.Button(self.root, text="Обзор", command=partial(self.browse_file, self.entry1))
        self.browse_button1.grid(row=0, column=2)

        self.label2 = tk.Label(self.root, text="Вставьте отчет по этапам:")
        self.label2.grid(row=1, column=0)

        self.entry2 = tk.Entry(self.root, width=50)
        self.entry2.grid(row=1, column=1)

        self.browse_button2 = tk.Button(self.root, text="Обзор", command=partial(self.browse_file, self.entry2))
        self.browse_button2.grid(row=1, column=2)

        self.run_button = tk.Button(self.root, text="Запустить скрипт", command=partial(self.run_script, self.entry1, self.entry2))
        self.run_button.grid(row=2, column=1)

        # Запуск основного цикла обработки событий
        self.root.mainloop()


if __name__ == '__main__':
    start = Screen()
    start.widget()