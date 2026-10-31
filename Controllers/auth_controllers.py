from models.user_model import UserModel
from views.login_view import LoginView
from Controllers.buku_controllers import BukuController
import tkinter.messagebox as messagebox

class AuthController:
    def __init__(self):
        self.user_model = UserModel()
        self.login_view = LoginView(self.handle_login)

    def handle_login(self, username, password):
        if not username or not password:
            messagebox.showwarning("Peringatan", "Username dan password harus diisi!")
            return

        # Verifikasi kredensial ke database menggunakan UserModel
        user = self.user_model.authenticate(username, password)

        if user:
            messagebox.showinfo("Sukses", f"Login berhasil! Selamat datang, {user['username']} ({user['role']})")
            self.login_view.destroy()  # Tutup jendela login
            
            # Jalankan BukuController dengan membawa role pengguna (admin/anggota)
            app = BukuController(user_role=user['role'])
            app.run()
        else:
            messagebox.showerror("Error", "Username atau password salah!")

    def run(self):
        self.login_view.mainloop()