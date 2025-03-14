public class Main {
    public static void main(String[] args) {
        Inventaris<AlatTulis> inventaris = new Inventaris<>();
        
        // Menambahkan alat tulis ke dalam inventaris
        inventaris.tambahItem(new Pensil());
        inventaris.tambahItem(new Pulpen());
        inventaris.tambahItem(new BukuTulis());

        // Menampilkan daftar inventaris
        inventaris.tampilkanInventaris();
    }
}
