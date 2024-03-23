from tkinter import Tk, Canvas, PhotoImage, messagebox, Button, Label, Entry, END

from lk.auth import authenticate, register, user_exist




# функция отображения авторизации/регистрации
def show_auth(tk):
    tk.wm_minsize(340, 260)

    def switch_to_register():
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        login_button.pack_forget()
        register_button.pack(pady=10)
        switch_register_button.pack_forget()
        switch_login_button.pack(pady=15)
        title_label.config(text="Регистрация")

    def switch_to_login():
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        register_button.pack_forget()
        login_button.pack(pady=10)
        switch_login_button.pack_forget()
        switch_register_button.pack(pady=15)
        title_label.config(text="Авторизация")

    def perform_login():
        username = username_entry.get()
        password = password_entry.get()

        if authenticate(username, password):
            messagebox.showinfo("Успешно", "Авторизация прошла успешно!")
            exit()
        else:
            messagebox.showerror("Ошибка", "Неверное имя пользователя или пароль")

    def perform_register():
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            return messagebox.showerror("Ошибка", "Необходимо заполнить все поля!")

        if len(username) < 3 or len(username) > 20:
            return messagebox.showerror("Ошибка", "Имя пользователя должно иметь длину от 3 до 20 символов")

        if len(password) < 3 or len(password) > 20:
            return messagebox.showerror("Ошибка", "Пароль должен иметь длину от 3 до 20 символов")

        if user_exist(username):
            return messagebox.showerror("Ошибка", "Пользователь с таким именем уже существует")

        try:
            register(username, password)
            messagebox.showinfo("Успешно", "Регистрация прошла успешно!")
        except Exception as e:
            messagebox.showerror("Ошибка")

    title_label = Label(tk, text="Авторизация", font=("Arial", 16))
    title_label.pack(pady=10)

    username_label = Label(tk, text="Имя пользователя:")
    username_label.pack()

    username_entry = Entry(tk)
    username_entry.pack(pady=5)

    password_label = Label(tk, text="Пароль:")
    password_label.pack()

    password_entry = Entry(tk, show="*")
    password_entry.pack(pady=5)

    register_button = Button(tk, text="Зарегистрироваться", command=perform_register)
    login_button = Button(tk, text="Войти", command=perform_login)
    login_button.pack(pady=10)

    switch_register_button = Button(tk, text="Регистрация", command=switch_to_register)
    switch_register_button.pack(pady=15)

    switch_login_button = Button(tk, text="Авторизация", command=switch_to_login)

def main():
    # Создание окна
    main_window = Tk()
    main_window.title('Канадские шашки')
    main_window.resizable(False, False)

    show_auth(main_window)

    main_window.mainloop()


# Точка входа
if __name__ == '__main__':
    main()
