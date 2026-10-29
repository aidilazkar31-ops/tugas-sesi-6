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

# ==================== JENDELA CRUD DOSEN ====================
class DosenWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Aplikasi Data Dosen - SIAKAD")
        self.window.geometry("900x550")
        
        # --- FUNGSI CRUD DI DALAM KELAS DOSEN ---
        def connect_db():
            return mysql.connector.connect(**DB_CONFIG)

        def load_data():
            for row in tree.get_children():
                tree.delete(row)
            try:
                db = connect_db()
                cursor = db.cursor()
                cursor.execute("SELECT * FROM dosen")
                rows = cursor.fetchall()
                for row in rows:
                    tree.insert("", "end", values=row)
                db.close()
            except Exception as e:
                messagebox.showerror("Database Error", f"Gagal mengambil data: {e}")

        def tambah_data():
            nip = entry_nip.get()
            nama = entry_nama.get()
            jk = combo_jk.get()
            email = entry_email.get()
            tlp = entry_tlp.get()
            pendidikan = entry_pendidikan.get()
            bidang = entry_bidang.get()

            if not nip or not nama:
                messagebox.showwarning("Warning", "NIP dan Nama Dosen wajib diisi!")
                return

            try:
                db = connect_db()
                cursor = db.cursor()
                sql = "INSERT INTO dosen (nip, nama_dosen, jenis_kelamin, email, no_telepon, pendidikan_terakhir, bidang_keahlian) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val = (nip, nama, jk, email, tlp, pendidikan, bidang)
                cursor.execute(sql, val)
                db.commit()
                db.close()
                messagebox.showinfo("Sukses", "Data berhasil ditambahkan!")
                clear_fields()
                load_data()
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menambah data: {e}")

        def edit_data():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning("Warning", "Pilih data di tabel yang ingin diubah!")
                return

            nip = entry_nip.get()
            nama = entry_nama.get()
            jk = combo_jk.get()
            email = entry_email.get()
            tlp = entry_tlp.get()
            pendidikan = entry_pendidikan.get()
            bidang = entry_bidang.get()

            try:
                db = connect_db()
                cursor = db.cursor()
                sql = """UPDATE dosen SET nama_dosen=%s, jenis_kelamin=%s, email=%s,
                        no_telepon=%s, pendidikan_terakhir=%s, bidang_keahlian=%s WHERE nip=%s"""
                val = (nama, jk, email, tlp, pendidikan, bidang, nip)
                cursor.execute(sql, val)
                db.commit()
                db.close()
                messagebox.showinfo("Sukses", "Data berhasil diperbarui!")
                clear_fields()
                load_data()
            except Exception as e:
                messagebox.showerror("Error", f"Gagal memperbarui data: {e}")

        def hapus_data():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning("Warning", "Pilih data di tabel yang ingin dihapus!")
                return

            nip = entry_nip.get()
            confirm = messagebox.askyesno("Konfirmasi", f"Yakin ingin menghapus dosen NIP {nip}?")
            if confirm:
                try:
                    db = connect_db()
                    cursor = db.cursor()
                    cursor.execute("DELETE FROM dosen WHERE nip = %s", (nip,))
                    db.commit()
                    db.close()
                    messagebox.showinfo("Sukses", "Data berhasil dihapus!")
                    clear_fields()
                    load_data()
                except Exception as e:
                    messagebox.showerror("Error", f"Gagal menghapus data: {e}")

        def select_item(event):
            selected = tree.selection()
            if selected:
                values = tree.item(selected[0], "values")
                clear_fields()
                entry_nip.insert(0, values[0])
                entry_nama.insert(0, values[1])
                combo_jk.set(values[2])
                entry_email.insert(0, values[3])
                entry_tlp.insert(0, values[4])
                entry_pendidikan.insert(0, values[5])
                entry_bidang.insert(0, values[6])

        def clear_fields():
            entry_nip.delete(0, tk.END)
            entry_nama.delete(0, tk.END)
            combo_jk.set("")
            entry_email.delete(0, tk.END)
            entry_tlp.delete(0, tk.END)
            entry_pendidikan.delete(0, tk.END)
            entry_bidang.delete(0, tk.END)

        # --- GUI TAMPILAN DOSEN ---
        frame_form = tk.LabelFrame(self.window, text=" Form Data Dosen ", padx=10, pady=10)
        frame_form.pack(fill="x", padx=15, pady=10)

        labels = ["NIP", "Nama Dosen", "Jenis Kelamin", "Email", "No Telepon", "Pendidikan Terakhir", "Bidang Keahlian"]
        for i, label_text in enumerate(labels):
            tk.Label(frame_form, text=label_text).grid(row=i//2, column=(i%2)*2, sticky="w", padx=5, pady=3)

        nonlocal_self = self
        entry_nip = tk.Entry(frame_form)
        entry_nip.grid(row=0, column=1, padx=5, pady=3, sticky="ew")

        entry_nama = tk.Entry(frame_form)
        entry_nama.grid(row=0, column=3, padx=5, pady=3, sticky="ew")

        combo_jk = ttk.Combobox(frame_form, values=["Laki-laki", "Perempuan"], state="readonly")
        combo_jk.grid(row=1, column=1, padx=5, pady=3, sticky="ew")

        entry_email = tk.Entry(frame_form)
        entry_email.grid(row=1, column=3, padx=5, pady=3, sticky="ew")

        entry_tlp = tk.Entry(frame_form)
        entry_tlp.grid(row=2, column=1, padx=5, pady=3, sticky="ew")

        entry_pendidikan = tk.Entry(frame_form)
        entry_pendidikan.grid(row=2, column=3, padx=5, pady=3, sticky="ew")

        entry_bidang = tk.Entry(frame_form)
        entry_bidang.grid(row=3, column=1, padx=5, pady=3, sticky="ew")

        frame_form.grid_columnconfigure(1, weight=1)
        frame_form.grid_columnconfigure(3, weight=1)

        frame_btn = tk.Frame(self.window)
        frame_btn.pack(fill="x", padx=15, pady=5)

        tk.Button(frame_btn, text="Tambah", bg="#4CAF50", fg="white", command=tambah_data, width=12).pack(side="left", padx=5)
        tk.Button(frame_btn, text="Edit", bg="#2196F3", fg="white", command=edit_data, width=12).pack(side="left", padx=5)
        tk.Button(frame_btn, text="Hapus", bg="#f44336", fg="white", command=hapus_data, width=12).pack(side="left", padx=5)
        tk.Button(frame_btn, text="Clear", bg="#9E9E9E", fg="white", command=clear_fields, width=12).pack(side="left", padx=5)

        frame_table = tk.Frame(self.window)
        frame_table.pack(fill="both", expand=True, padx=15, pady=10)

        columns = ("nip", "nama_dosen", "jenis_kelamin", "email", "no_telepon", "pendidikan_terakhir", "bidang_keahlian")
        tree = ttk.Treeview(frame_table, columns=columns, show="headings")
        tree.heading("nip", text="NIP")
        tree.heading("nama_dosen", text="Nama Dosen")
        tree.heading("jenis_kelamin", text="Jenis Kelamin")
        tree.heading("email", text="Email")
        tree.heading("no_telepon", text="No Telepon")
        tree.heading("pendidikan_terakhir", text="Pendidikan")
        tree.heading("bidang_keahlian", text="Bidang Keahlian")

        tree.column("nip", width=70)
        tree.column("nama_dosen", width=160)
        tree.column("jenis_kelamin", width=100)
        tree.column("email", width=140)
        tree.column("no_telepon", width=100)
        tree.column("pendidikan_terakhir", width=80)
        tree.column("bidang_keahlian", width=150)

        tree.bind("<<TreeviewSelect>>", select_item)

        scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

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

        lbl_title = tk.Label(main_frame, text="SIAKAD LOGIN", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="black")
        lbl_title.pack(pady=(0, 20))

        form_frame = tk.Frame(main_frame, bg="#f0f0f0")
        form_frame.pack()

        lbl_user = tk.Label(form_frame, text="Username:", font=("Arial", 10), bg="#f0f0f0", anchor="e", width=10)
        lbl_user.grid(row=0, column=0, padx=5, pady=6, sticky="e")
        
        self.entry_nip = tk.Entry(form_frame, font=("Arial", 10), width=22, relief=tk.SOLID, bd=1)
        self.entry_nip.grid(row=0, column=1, padx=5, pady=6)
        self.entry_nip.focus()

        lbl_pass = tk.Label(form_frame, text="Password:", font=("Arial", 10), bg="#f0f0f0", anchor="e", width=10)
        lbl_pass.grid(row=1, column=0, padx=5, pady=6, sticky="e")
        
        self.entry_email = tk.Entry(form_frame, font=("Arial", 10), width=22, show="*", relief=tk.SOLID, bd=1)
        self.entry_email.grid(row=1, column=1, padx=5, pady=6)

        btn_login = tk.Button(
            main_frame, text="Login", font=("Arial", 10, "bold"), 
            bg="#4CAF50", fg="white", activebackground="#45a049", 
            activeforeground="white", width=15, bd=1, cursor="hand2", 
            command=self.proses_login
        )
        btn_login.pack(pady=(20, 0))

        self.root.bind('<Return>', lambda event: self.proses_login())

    def proses_login(self):
        nip = self.entry_nip.get().strip()
        email = self.entry_email.get().strip()

        if not nip or not email:
            messagebox.showwarning("Peringatan", "Username (NIP) dan Password (Email) wajib diisi!")
            return

        conn = None
        cursor = None
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor(dictionary=True)
            
            query = "SELECT nip, nama_dosen, email FROM dosen WHERE nip = %s AND email = %s"
            cursor.execute(query, (nip, email))
            user = cursor.fetchone()

            if user:
                messagebox.showinfo("Berhasil", f"Login berhasil!\nSelamat datang, {user['nama_dosen']}.")
                self.buka_dashboard(user)
            else:
                messagebox.showerror("Gagal", "Login gagal! Username atau Password salah.")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Koneksi database bermasalah:\n{err}")
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def buka_dashboard(self, user):
        self.root.withdraw() # Sembunyikan jendela login

        dashboard = tk.Toplevel(self.root)
        dashboard.title("Sistem Informasi Akademik (SIAKAD) - Menu Utama")
        dashboard.geometry("450x350")
        dashboard.configure(bg="#f9f9f9")

        tk.Label(dashboard, text=f"Halo, {user['nama_dosen']}", font=("Arial", 14, "bold"), bg="#f9f9f9").pack(pady=(25, 5))
        tk.Label(dashboard, text="Silakan pilih menu pengelolaan data di bawah:", font=("Arial", 10), bg="#f9f9f9", fg="gray").pack(pady=(0, 20))

        # Tombol Navigasi Menu Dosen
        tk.Button(
            dashboard, text="Kelola Data Dosen", font=("Arial", 10, "bold"), 
            bg="#2196F3", fg="white", width=30, height=2, 
            command=lambda: DosenWindow(dashboard), cursor="hand2"
        ).pack(pady=10)

        # Tombol Logout / Keluar
        def logout():
            dashboard.destroy()
            self.entry_nip.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.root.deiconify()

        tk.Button(dashboard, text="Logout", font=("Arial", 9), bg="#f44336", fg="white", width=15, command=logout, cursor="hand2").pack(pady=(20, 0))


# ==================== TITIK AWAL EKSEKUSI ====================
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()