from unittest.mock import MagicMock
from models.user_model import UserModel

def test_hash_password_konsisten():
    password_asli = "admin123"
    model = UserModel()
    
    hash_1 = model.hash_password(password_asli)
    hash_2 = model.hash_password(password_asli)
    
    assert hash_1 != password_asli
    assert hash_1 == hash_2
    assert len(hash_1) == 64

def test_autentikasi_pengguna_berhasil():
    model = UserModel()
    
    # Mocking koneksi dan kursor secara menyeluruh agar tidak memanggil database fisik
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.cursor = mock_cursor  # <-- Kunci utamanya di sini, mengganti cursor asli dengan mock_cursor
    
    # Simulasi kembalian data dari database ketika username & password cocok
    mock_cursor.fetchone.return_value = {
        "id_user": 1,
        "username": "petugas",
        "role": "admin"
    }
    
    hasil = model.authenticate("petugas", "admin123")
    
    assert hasil is not None
    assert hasil["username"] == "petugas"
    assert hasil["role"] == "admin"