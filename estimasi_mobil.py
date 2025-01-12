import pickle
import streamlit as st

# Memuat model yang sudah disimpan
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

# Pengaturan tampilan halaman
st.set_page_config(page_title="Prediksi Harga Mobil Bekas", layout="wide")

# Menambahkan CSS untuk mempercantik tampilan
st.markdown("""
    <style>
        /* Mengatur seluruh latar belakang halaman menjadi putih */
        body {
            background-color: #ffffff;
            font-family: 'Arial', sans-serif;
            color: #333;
        }

        /* Logo di bagian tengah */
        .logo {
            display: block;
            margin-left: auto;
            margin-right: auto;
            max-width: 200px;
            padding-top: 20px;
            padding-bottom: 20px;
        }

        /* Kolom kiri */
        .col-left {
            padding: 20px;
            border-right: 2px solid #f0f0f0;
            background-color: #f9f9f9;
        }

        /* Kolom kanan */
        .col-right {
            padding: 20px;
        }

        /* Judul utama */
        h2, h3, h4 {
            text-align: center;
            color: #333;
        }

        /* Style untuk section Data Diri */
        .data-section {
            margin-bottom: 20px;
        }

        /* Style untuk heading data diri */
        .data-section h4 {
            color: #1a73e8;
            font-size: 18px;
        }

        /* Style untuk input dan tombol */
        .stButton>button {
            background-color: #1a73e8;
            color: white;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
            border: none;
        }

        .stButton>button:hover {
            background-color: #0d59d1;
        }

        /* Style untuk warning message */
        .stWarning {
            background-color: #f9e6e6;
            color: #d32f2f;
            border: 1px solid #d32f2f;
            padding: 10px;
            border-radius: 4px;
        }
    </style>
""", unsafe_allow_html=True)

# Menambahkan logo di antara teks
st.markdown("<h2> Tugas Mata Kuliah Pembelajaran Mesin </h2>", unsafe_allow_html=True)
st.markdown("<h3> Project Machine Learning </h3>", unsafe_allow_html=True)
st.markdown("<h4> Prediksi Harga Mobil Bekas Menggunakan Regresi Linier dan Decision Tree Regressor </h4>", unsafe_allow_html=True)

# Menambahkan logo
st.image("logo.png", use_column_width=True, caption="Logo Universitas", width=200)

# Membuat dua kolom
col1, col2 = st.columns([1, 3])

# Kolom kiri - menampilkan data
with col1:
    st.markdown("<div class='col-left'>", unsafe_allow_html=True)
    st.markdown("<h4> Disusun Oleh: </h4>", unsafe_allow_html=True)
    st.markdown("- **Muh Bintang Mahardani** (17225123)", unsafe_allow_html=True)
    st.markdown("- **Taufiq Ismail** (17215032)", unsafe_allow_html=True)
    st.markdown("<div class='data-section'>", unsafe_allow_html=True)
    st.markdown("<b>Kelas:</b> 17.4A.26", unsafe_allow_html=True)
    st.markdown("<b>Program Studi:</b> Teknologi Informasi (S1)</div>", unsafe_allow_html=True)

    st.markdown("<div class='data-section'><b>Universitas:</b> Universitas Bina Sarana Informatika", unsafe_allow_html=True)
    st.markdown("<b>Fakultas:</b> Fakultas Teknik dan Informatika", unsafe_allow_html=True)
    st.markdown("<b>Alamat:</b> Jl. Kemanggisan Utama, RT.3/RW.2, Slipi, Kec. Palmerah, Kota Jakarta Barat, DKI Jakarta 11480</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Kolom kanan - aplikasi prediksi harga mobil bekas
with col2:
    st.markdown("<div class='col-right'>", unsafe_allow_html=True)
    st.title('Estimasi Harga Mobil Bekas')

    # Mengubah tipe input menjadi bilangan bulat (integer)
    year = st.number_input('Input Tahun Mobil', min_value=1900, max_value=
