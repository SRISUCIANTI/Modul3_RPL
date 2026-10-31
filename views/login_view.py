import customtkinter as ctk

class LoginView(ctk.CTk):
    def __init__(self, on_login_success):
        super().__init__()
        self.on_login_success = on_login_success
        
        self.title("Login - Sistem Perpustakaan")
        self.geometry("400x300")
        self.resizable(False, False)
        
        # Label Judul
        self.label_title = ctk.CTkLabel(self, text="Silakan Login", font=("Arial", 20, "bold"))
        self.label_title.pack(pady=20)
        
        # Input Username
        self.entry_username = ctk.CTkEntry(self, placeholder_text="Username", width=250)
        self.entry_username.pack(pady=10)
        
        # Input Password
        self.entry_password = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=250)
        self.entry_password.pack(pady=10)
        
        # Tombol Login
        self.btn_login = ctk.CTkButton(self, text="Masuk", width=250, command=self.handle_login)
        self.btn_login.pack(pady=20)
        
    def handle_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.on_login_success(username, password)

if __name__ == "__main__":
    app = LoginView(lambda u, p: print(f"Login: {u}"))
    app.mainloop()