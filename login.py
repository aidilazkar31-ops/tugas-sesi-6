import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox

# ==================== KONFIGURASI DATABASE ====================
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'siakad'
}

# ==================== 1. KELOLA DATA DOSEN ====================
class DosenWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Kelola Data Dosen - SIAKAD")
        self.window.geometry("900x500")
        
        def load_data():
            for row in tree.get_children(): tree.delete(row)
            try:
                db = mysql.connector.connect(**DB_CONFIG)
                cursor = db.cursor()
                cursor.execute("SELECT * FROM dosen")
                for row in cursor.fetchall(): tree.insert("", "end", values=row)
                db.close()
            except Exception as e: messagebox.showerror("Error", f"{e}")

        tk.Label(self.window, text="MANAJEMEN DATA DOSEN", font=("Arial", 14, "bold")).pack(pady=10)
        
        frame_table = tk.Frame(self.window)
        frame_table.pack(fill="both", expand=True, padx=15, pady=10)
        
        columns = ("nip", "nama_dosen", "jenis_kelamin", "email", "no_telepon", "pendidikan_terakhir", "bidang_keahlian")
        tree = ttk.Treeview(frame_table, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col.replace("_", " ").title())
            tree.column(col, width=110, anchor="center")
        tree.pack(fill="both", expand=True)
        load_data()

# ==================== 2. KELOLA DATA MAHASISWA ====================
class MahasiswaWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Kelola Data Mahasiswa - SIAKAD")
        self.window.geometry("900x500")
        
        def load_data():
            for row in tree.get_children(): tree.delete(row)
            try:
                db = mysql.connector.connect(**DB_CONFIG)
                cursor = db.cursor()
                cursor.execute("SELECT * FROM mahasiswa")
                for row in cursor.fetchall(): tree.insert("", "end", values=row)
                db.close()
            except Exception as e: messagebox.showerror("Error", f"{e}")

        tk.Label(self.window, text="MANAJEMEN DATA MAHASISWA", font=("Arial", 14, "bold")).pack(pady=10)
        
        frame_table = tk.Frame(self.window)
        frame_table.pack(fill="both", expand=True, padx=15, pady=10)
        
        # Menyesuaikan dengan kolom tabel mahasiswa di database Anda
        columns = ("nim", "nama_mhs", "jenis_kelamin", "alamat", "no_telepon", "prodi")
        tree = ttk.Treeview(frame_table, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col.replace("_", " ").title())
            tree.column(col, width=130, anchor="center")
        tree.pack(fill="both", expand=True)
        load_data()

# ==================== 3. KELOLA MATA KULIAH ====================
class MataKuliahWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Kelola Mata Kuliah - SIAKAD")
        self.window.geometry("700x450")
        
        def load_data():
            for row in tree.get_children(): tree.delete(row)
            try:
                db = mysql.connector.connect(**DB_CONFIG)
                cursor = db.cursor()
                cursor.execute("SELECT * FROM mata_kuliah")
                for row in cursor.fetchall(): tree.insert("", "end", values=row)
                db.close()
            except Exception as e: messagebox.showerror("Error", f"{e}")

        tk.Label(self.window, text="MANAJEMEN MATA KULIAH", font=("Arial", 14, "bold")).pack(pady=10)
        
        frame_table = tk.Frame(self.window)
        frame_table.pack(fill="both", expand=True, padx=15, pady=10)
        
        columns = ("kode_mk", "nama_mk", "sks", "semester")
        tree = ttk.Treeview(frame_table, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col.replace("_", " ").title())
            tree.column(col, width=150, anchor="center")
        tree.pack(fill="both", expand=True)
        load_data()

# ==================== 4. KELOLA JADWAL KULIAH ====================
class JadwalWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Kelola Jadwal Kuliah - SIAKAD")
        self.window.geometry("800x450")
        
        def load_data():
            for row in tree.get_children(): tree.delete(row)
            try:
                db = mysql.connector.connect(**DB_CONFIG)
                cursor = db.cursor()
                cursor.execute("SELECT * FROM jadwal_kuliah")
                for row in cursor.fetchall(): tree.insert("", "end", values=row)
                db.close()
            except Exception as e: messagebox.showerror("Error", f"{e}")

        tk.Label(self.window, text="MANAJEMEN JADWAL KULIAH", font=("Arial", 14, "bold")).pack(pady=10)
        
        frame_table = tk.Frame(self.window)
        frame_table.pack(fill="both", expand=True, padx=15, pady=10)
        
        columns = ("id_jadwal", "hari", "jam", "kode_mk", "nip", "ruangan")
        tree = ttk.Treeview(frame_table, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col.replace("_", " ").title())
            tree.column(col, width=120, anchor="center")
        tree.pack(fill="both", expand=True)
        load_data()

# ==================== 5. KELOLA KRS MAHASISWA ====================
class KrsWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Kelola KRS Mahasiswa - SIAKAD")
        self.window.geometry("800x450")
        
        def load_data():
            for row in tree.get_children(): tree.delete(row)
            try:
                db = mysql.connector.connect(**DB_CONFIG)
                cursor = db.cursor()
                cursor.execute("SELECT * FROM krs")
                for row in cursor.fetchall(): tree.insert("", "end", values=row)
                db.close()
            except Exception as e: messagebox.showerror("Error", f"{e}")

        tk.Label(self.window, text="MANAJEMEN KRS MAHASISWA", font=("Arial", 14, "bold")).pack(pady=10)
        
        frame_table = tk.Frame(self.window)
        frame_table.pack(fill="both", expand=True, padx=15, pady=10)
        
        columns = ("id_krs", "nim", "kode_mk", "tahun_akademik")
        tree = ttk.Treeview(frame_table, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col.replace("_", " ").title())
            tree.column(col, width=170, anchor="center")
        tree.pack(fill="both", expand=True)
        load_data()

# ==================== 6. KELOLA PEMBAYARAN UKT ====================
class UktWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Kelola Pembayaran UKT - SIAKAD")
        self.window.geometry("800x450")
        
        def load_data():
            for row in tree.get_children(): tree.delete(row)
            try:
                db = mysql.connector.connect(**DB_CONFIG)
                cursor = db.cursor()
                cursor.execute("SELECT * FROM pembayaran_ukt")
                for row in cursor.fetchall(): tree.insert("", "end", values=row)
                db.close()
            except Exception as e: messagebox.showerror("Error", f"{e}")

        tk.Label(self.window, text="MANAJEMEN PEMBAYARAN UKT", font=("Arial", 14, "bold")).pack(pady=10)
        
        frame_table = tk.Frame(self.window)
        frame_table.pack(fill="both", expand=True, padx=15, pady=10)
        
        columns = ("id_pembayaran", "nim", "jumlah_bayar", "status", "tanggal")
        tree = ttk.Treeview(frame_table, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col.replace("_", " ").title())
            tree.column(col, width=140, anchor="center")
        tree.pack(fill="both", expand=True)
        load_data()


# ==================== JENDELA UTAMA LOGIN ====================
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - SIAKAD")
        self.root.geometry("380x250")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        tk.Label(main_frame, text="SIAKAD LOGIN", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=(0, 20))

        form_frame = tk.Frame(main_frame, bg="#f0f0f0")
        form_frame.pack()

        tk.Label(form_frame, text="Username:", font=("Arial", 10), bg="#f0f0f0", anchor="e", width=10).grid(row=0, column=0, padx=5, pady=6, sticky="e")
        self.entry_nip = tk.Entry(form_frame, font=("Arial", 10), width=22, relief=tk.SOLID, bd=1)
        self.entry_nip.grid(row=0, column=1, padx=5, pady=6)
        self.entry_nip.focus()

        tk.Label(form_frame, text="Password:", font=("Arial", 10), bg="#f0f0f0", anchor="e", width=10).grid(row=1, column=0, padx=5, pady=6, sticky="e")
        self.entry_email = tk.Entry(form_frame, font=("Arial", 10), width=22, show="*", relief=tk.SOLID, bd=1)
        self.entry_email.grid(row=1, column=1, padx=5, pady=6)

        btn_login = tk.Button(main_frame, text="Login", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", width=15, command=self.proses_login)
        btn_login.pack(pady=(20, 0))

        self.root.bind('<Return>', lambda event: self.proses_login())

    def proses_login(self):
        nip = self.entry_nip.get().strip()
        email = self.entry_email.get().strip()

        if not nip or not email:
            messagebox.showwarning("Peringatan", "Username dan Password wajib diisi!")
            return

        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT nip, nama_dosen, email FROM dosen WHERE nip = %s AND email = %s", (nip, email))
            user = cursor.fetchone()
            conn.close()

            if user:
                messagebox.showinfo("Berhasil", f"Login berhasil!\nSelamat datang, {user['nama_dosen']}.")
                self.buka_dashboard(user)
            else:
                messagebox.showerror("Gagal", "Login gagal! Username atau Password salah.")
        except Exception as err:
            messagebox.showerror("Database Error", f"{err}")

    def buka_dashboard(self, user):
        self.root.withdraw()

        dashboard = tk.Toplevel(self.root)
        dashboard.title("Dashboard Menu Utama - SIAKAD")
        dashboard.geometry("450x600")
        dashboard.configure(bg="#f9f9f9")

        tk.Label(dashboard, text=f"Halo, {user['nama_dosen']}", font=("Arial", 14, "bold"), bg="#f9f9f9").pack(pady=(20, 5))
        tk.Label(dashboard, text="Pilih Menu Pengelolaan Data SIAKAD:", font=("Arial", 10), bg="#f9f9f9", fg="gray").pack(pady=(0, 15))

        # Tombol-tombol navigasi lengkap
        tk.Button(dashboard, text="Kelola Data Dosen", bg="#2196F3", fg="white", font=("Arial", 10, "bold"), width=30, height=2, command=lambda: DosenWindow(dashboard), cursor="hand2").pack(pady=5)
        tk.Button(dashboard, text="Kelola Data Mahasiswa", bg="#FF9800", fg="white", font=("Arial", 10, "bold"), width=30, height=2, command=lambda: MahasiswaWindow(dashboard), cursor="hand2").pack(pady=5)
        tk.Button(dashboard, text="Kelola Mata Kuliah", bg="#009688", fg="white", font=("Arial", 10, "bold"), width=30, height=2, command=lambda: MataKuliahWindow(dashboard), cursor="hand2").pack(pady=5)
        tk.Button(dashboard, text="Kelola Jadwal Kuliah", bg="#9C27B0", fg="white", font=("Arial", 10, "bold"), width=30, height=2, command=lambda: JadwalWindow(dashboard), cursor="hand2").pack(pady=5)
        tk.Button(dashboard, text="Kelola KRS Mahasiswa", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=30, height=2, command=lambda: KrsWindow(dashboard), cursor="hand2").pack(pady=5)
        tk.Button(dashboard, text="Kelola Pembayaran UKT", bg="#607D8B", fg="white", font=("Arial", 10, "bold"), width=30, height=2, command=lambda: UktWindow(dashboard), cursor="hand2").pack(pady=5)

        def logout():
            dashboard.destroy()
            self.entry_nip.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.root.deiconify()

        tk.Button(dashboard, text="Logout", bg="#f44336", fg="white", font=("Arial", 9), width=15, command=logout, cursor="hand2").pack(pady=(20, 10))

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()