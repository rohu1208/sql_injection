import tkinter as tk
from tkinter import messagebox
import sqlite3

class LoginPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Login Page :)")
        self.pack(pady=20, padx=20)

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2, padx=5, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()

        # Vulnerable to SQL injection
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Login Successful", "Welcome Rohan!")
            self.master.switch_frame(ProductsPage, username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

class ProductsPage(tk.Frame):
    def __init__(self, master, username):
        super().__init__(master)
        self.master = master
        self.master.title("Products Page")
        self.pack(pady=20, padx=20)

        self.username = username

        self.products_label = tk.Label(self, text="Products:")
        self.products_label.grid(row=0, column=0, padx=5, pady=5)

        self.product_listbox = tk.Listbox(self)
        self.product_listbox.grid(row=1, column=0, padx=5, pady=5)

        self.load_products()

        self.logout_button = tk.Button(self, text="Logout", command=self.logout)
        self.logout_button.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    def load_products(self):
        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

        for product in products:
            self.product_listbox.insert(tk.END, f"{product[1]} - ${product[2]}")

        conn.close()

    def logout(self):
        self.master.switch_frame(LoginPage)

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SQL Injection Demo")
        self.geometry("300x200")
        self.current_frame = None
        self.switch_frame(LoginPage)

    def switch_frame(self, frame_class, username=None):
        new_frame = frame_class(self, username) if username else frame_class(self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
