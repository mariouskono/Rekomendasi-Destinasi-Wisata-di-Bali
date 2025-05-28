# Laporan Proyek Machine Learning - Bertnardo Mario Uskono

## Domain Proyek
Pariwisata merupakan sektor vital di Bali yang menyumbang besar bagi perekonomian dan membuka lapangan pekerjaan. Bali memiliki beragam tempat wisata yang menarik, namun wisatawan sering mengalami kesulitan memilih destinasi yang sesuai dengan preferensi mereka. Oleh karena itu, proyek ini bertujuan mengembangkan sistem rekomendasi berbasis konten yang mampu membantu wisatawan menemukan tempat wisata di Bali yang paling sesuai berdasarkan kategori dan preferensi wisata.

---

## Business Understanding
### Problem Statements
* Wisatawan kesulitan menemukan tempat wisata yang cocok karena banyaknya pilihan dan variasi kategori.
* Tidak adanya sistem rekomendasi berbasis data yang efektif dan mudah digunakan untuk wisata Bali.

### Goals
* Mengembangkan sistem rekomendasi yang dapat memberikan 10 rekomendasi tempat wisata serupa berdasarkan tempat yang dipilih.
* Membantu wisatawan dalam pencarian destinasi yang sesuai preferensi secara lebih mudah dan efisien.

### Solution Statements
* Sistem rekomendasi dibangun dengan pendekatan Content-Based Filtering menggunakan TF-IDF untuk representasi fitur teks dan cosine similarity untuk mengukur kemiripan antar tempat wisata.
* Pengembangan lanjutan dengan pendekatan hybrid atau collaborative filtering dapat dilakukan jika data interaksi pengguna tersedia.

---

## Data Understanding
Dataset yang digunakan berisi 772 tempat wisata di Bali dengan beberapa fitur penting:

* `nama`: Nama tempat wisata, contoh "Taman Mumbul Sangeh".
* `kategori`: Kategori tempat wisata seperti Alam, Budaya, Rekreasi, Umum.
* `kabupaten_kota`: Lokasi administratif tempat wisata berada.
* `rating`: Rating rata-rata dari pengunjung, dalam skala 1 sampai 5.
* `preferensi`: Klasifikasi preferensi wisata yang lebih spesifik, misal Wisata Alam, Wisata Budaya.
* `link_lokasi`: URL Google Maps tempat wisata.
* `latitude` & `longitude`: Koordinat geografis.
* `link_gambar`: URL gambar tempat wisata.

Dataset ini diperoleh melalui scraping otomatis dari Google Maps ([link dataset](https://www.kaggle.com/datasets/bertnardomariouskono/bali-tourist-attractions-dataset-from-google-maps)).

### Insight awal dari data:
* Dataset terdiri dari 4 kategori utama dengan distribusi cukup merata (visualisasi berupa grafik batang).
* Rating rata-rata tempat wisata berkisar antara 4.0 sampai 5.0, yang menunjukkan data berisi tempat yang cukup populer dan banyak mendapat review positif.

---

## Data Preparation
Tahapan data preparation meliputi:
* **Pembersihan data:** Duplikat dihapus dan missing value diisi dengan nilai rata-rata atau placeholder.
* **Fitur gabungan:** Kolom `kategori` dan `preferensi` digabung menjadi satu string teks baru yang akan menjadi fitur utama dalam sistem rekomendasi.
* **Vektorisasi teks:** Fitur gabungan tersebut diubah menjadi representasi numerik menggunakan TF-IDF. Output matriks TF-IDF berdimensi (772 x 5), artinya 772 tempat wisata dengan 5 fitur unik yang paling relevan.
* **Visualisasi:**
  * Grafik distribusi kategori memperlihatkan komposisi data.
  * Plot sparsity matriks TF-IDF menunjukkan banyaknya kata yang tidak muncul pada banyak tempat (matriks jarang/padat).

---

## Modeling and Results
Model yang dibangun menggunakan:
* **Content-Based Filtering:** Berdasarkan kemiripan cosine antar fitur TF-IDF tempat wisata.
* **Fungsi rekomendasi:** Menerima nama tempat wisata input, mencari indeksnya, menghitung kemiripan dengan tempat lain, lalu mengembalikan 10 tempat paling mirip.

### Contoh output rekomendasi:
Input: "Taman Mumbul Sangeh"
Output: 10 tempat wisata serupa seperti "Sangeh Monkey Forest", "Waterblow", dan "Taman Sari Wisata Bahari", dengan rating rata-rata 4.35.

### Visualisasi hasil:
* Heatmap subset cosine similarity menunjukkan skor kemiripan antar 20 tempat pertama.
* Grafik batang horizontal menampilkan rating 10 tempat wisata yang direkomendasikan, memudahkan evaluasi kualitas rekomendasi.

---

## Evaluation
* Evaluasi utama dilakukan secara **kualitatif** dan menggunakan **rating rata-rata** dari tempat yang direkomendasikan sebagai indikator kualitas.
* Rata-rata rating tempat rekomendasi cukup tinggi (sekitar 4.35), menandakan rekomendasi berkualitas.
* Keterbatasan model adalah ketergantungan pada data fitur kategori/preferensi tanpa mempertimbangkan interaksi pengguna, yang dapat diatasi dengan pengembangan ke sistem hybrid atau collaborative filtering.

---
## Conclusion
Sistem rekomendasi berbasis konten untuk tempat wisata Bali berhasil diimplementasikan dan mampu memberikan rekomendasi yang relevan dan berkualitas berdasarkan kategori dan preferensi. Sistem ini berguna untuk mempermudah wisatawan menemukan destinasi yang sesuai tanpa membutuhkan data interaksi pengguna.

---

## Referensi
* Dataset: [Bali Tourist Attractions Dataset from Google Maps](https://www.kaggle.com/datasets/bertnardomariouskono/bali-tourist-attractions-dataset-from-google-maps)
* Kane, F. "Building Recommender Systems with Machine Learning and AI", 2018.
* Ricci et al., "Recommender Systems Handbook", 2011.