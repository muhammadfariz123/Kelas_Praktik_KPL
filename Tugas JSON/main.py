# Nama : Muhammad Fariz Nur Hidayat
# Kelas : SE063
# NIM : 2211104069

import json

# === 1. Kelas Karyawan ===
class Karyawan:
    def __init__(self, id, nama, jabatan, gaji):
        self.id = id
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji

    def to_dict(self):
        return {
            "id": self.id,
            "nama": self.nama,
            "jabatan": self.jabatan,
            "gaji": self.gaji
        }

    @staticmethod
    def from_dict(data):
        return Karyawan(
            data["id"],
            data["nama"],
            data["jabatan"],
            data["gaji"]
        )

    def tampilkan(self):
        print(f"ID      : {self.id}")
        print(f"Nama    : {self.nama}")
        print(f"Jabatan : {self.jabatan}")
        print(f"Gaji    : Rp{self.gaji:,}")
        print("-" * 30)

# === 2. Menyimpan data karyawan ke file JSON ===
def simpan_ke_file(karyawan_list, filename):
    data = [k.to_dict() for k in karyawan_list]
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data berhasil disimpan ke {filename}")

# === 3. Membaca data karyawan dari file JSON ===
def baca_dari_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Karyawan.from_dict(item) for item in data]
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
        return []

# === 4. Contoh penggunaan ===
def main():
    # Membuat beberapa data karyawan
    karyawan1 = Karyawan(1, "Andi", "Manager", 12000000)
    karyawan2 = Karyawan(2, "Budi", "Staff", 7000000)
    karyawan3 = Karyawan(3, "Citra", "HRD", 8000000)

    # Menyimpan ke file
    daftar_karyawan = [karyawan1, karyawan2, karyawan3]
    simpan_ke_file(daftar_karyawan, "data_karyawan.json")

    # Membaca dari file
    print("\n=== Membaca dari file ===")
    karyawan_baru = baca_dari_file("data_karyawan.json")

    # Menampilkan data karyawan
    print("\n=== Data Karyawan ===")
    for k in karyawan_baru:
        k.tampilkan()

# Menjalankan program
if __name__ == "__main__":
    main()
