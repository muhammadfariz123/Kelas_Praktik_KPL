import java.util.ArrayList;
import java.util.List;

public class Inventaris<T extends AlatTulis> {
    private List<T> daftarItem = new ArrayList<>();

    public void tambahItem(T item) {
        daftarItem.add(item);
        System.out.println(item.getNama() + " ditambahkan ke inventaris.");
    }

    public void tampilkanInventaris() {
        System.out.println("Daftar inventaris alat tulis:");
        for (T item : daftarItem) {
            System.out.println("- " + item.getNama());
        }
    }
}
