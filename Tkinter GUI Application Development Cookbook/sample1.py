import tkinter as tk

RELIEFS = [tk.SUNKEN, tk.RAISED, tk.GROOVE, tk.RIDGE, tk.FLAT]


class ButtonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.img = tk.PhotoImage(file='')

        self.btn = tk.Button(self, text="Button with Image", image=self.img, compound=tk.LEFT,
                             command=self.disable_btn)
        self.btns = [self.create_btn(r) for r in RELIEFS]
        self.btn.pack()
        for btn in self.btns:
            btn.pack(padx=10, pady=10, side=tk.LEFT)

    def create_btn(self, relief):
        return tk.Button(self, text=relief, relief=relief)

    def disable_btn(self):
        self.btn.config(state=tk.DISABLED)


class LoginApp(tk.Tk):
    def __init__(self):
        super(LoginApp, self).__init__()
        self.username = tk.Entry(self)
        self.password = tk.Entry(self, show="*")
        self.login_btn = tk.Button(self, text="Log in",
                                   command=self.print_login)
        self.clear_btn = tk.Button(self, text="Clear",
                                   command=self.clear_form)
        self.username.pack()
        self.password.pack()
        self.login_btn.pack(fill=tk.BOTH)
        self.clear_btn.pack(fill=tk.BOTH)

    def print_login(self):
        print(f"Username: {self.username.get()}")
        print(f"Password: {self.password.get()}")

    def clear_form(self):
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.username.focus_set()


class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.var = tk.StringVar()
        self.var.trace("w", self.show_message)
        self.entry = tk.Entry(self, textvariable=self.var)
        self.btn = tk.Button(self, text="Clear", command=lambda: self.var.set(""))
        self.label = tk.Label(self)
        self.entry.pack()
        self.btn.pack()
        self.label.pack()

    def show_message(self, *args):
        value = self.var.get()
        text = "Hello, {}!".format(value) if value else ""
        self.label.config(text=text)


if __name__ == "__main__":
    app = App()
    app.mainloop()
