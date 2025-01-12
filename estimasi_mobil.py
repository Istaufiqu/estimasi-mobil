import pickle
import streamlit as st

# Memuat model yang sudah disimpan
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

# Pengaturan tampilan halaman
st.set_page_config(page_title="Prediksi Harga Mobil Bekas", layout="wide")

# Menambahkan CSS untuk mempercantik tampilan
st.markdown("""
    <style>
        /* Style untuk keseluruhan halaman */
        body {
            background-color: #ffffff;
            font-family: 'Arial', sans-serif;
        }

        /* Kolom kiri */
        .col-left {
            padding: 20px;
            border-right: 2px solid #f0f0f0;
            background-color: #f9f9f9;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
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
            margin-bottom: 10px;
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

# Membuat dua kolom
col1, col2 = st.columns([1, 3])

# Kolom kiri - menampilkan data
with col1:
    st.markdown("<div class='col-left'>", unsafe_allow_html=True)
    # Judul
    st.markdown("<h2> Tugas Mata Kuliah Pembelajaran Mesin </h2>", unsafe_allow_html=True)
    st.markdown("<h3> Project Machine Learning </h3>", unsafe_allow_html=True)
    st.markdown("<h4> Prediksi Harga Mobil Bekas Menggunakan Regresi Linier dan Decision Tree Regressor </h4>", unsafe_allow_html=True)

    # Data Diri
    st.markdown("<div class='data-section'>", unsafe_allow_html=True)
    st.markdown("<h4> Disusun Oleh: </h4>", unsafe_allow_html=True)
    st.markdown("- **Muh Bintang Mahardani** (17225123)", unsafe_allow_html=True)
    st.markdown("- **Taufiq Ismail** (17215032)", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='data-section'>", unsafe_allow_html=True)
    st.markdown("<b>Kelas:</b> 17.4A.26", unsafe_allow_html=True)
    st.markdown("<b>Program Studi:</b> Teknologi Informasi (S1)</div>", unsafe_allow_html=True)

    st.markdown("<div class='data-section'>", unsafe_allow_html=True)
    st.markdown("<b>Universitas:</b> Universitas Bina Sarana Informatika", unsafe_allow_html=True)
    st.markdown("<b>Fakultas:</b> Fakultas Teknik dan Informatika", unsafe_allow_html=True)
    st.markdown("<b>Alamat:</b> Jl. Kemanggisan Utama, RT.3/RW.2, Slipi, Kec. Palmerah, Kota Jakarta Barat, DKI Jakarta 11480</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Kolom kanan - aplikasi prediksi harga mobil bekas
with col2:
    st.markdown("<div class='col-right'>", unsafe_allow_html=True)
    st.title('Estimasi Harga Mobil Bekas')

    # Mengubah tipe input menjadi bilangan bulat (integer)
    year = st.number_input('Input Tahun Mobil', min_value=1900, max_value=2025, step=1, format="%d", value=None) 
    mileage = st.number_input('Input Km Mobil', min_value=0, step=1, format="%d", value=None)
    tax = st.number_input('Input Pajak Mobil', min_value=0, step=1, format="%d", value=None)
    mpg = st.number_input('Input Konsumsi BBM Mobil', min_value=0, step=1, format="%d", value=None)
    engineSize = st.number_input('Input Engine Size', min_value=0, step=1, format="%d", value=None)

    # Menyimpan hasil prediksi di variabel
    predict = None

    # Validasi input: jika semua input sudah diisi (nilai tidak None)
    if year is not None and mileage is not None and tax is not None and mpg is not None and engineSize is not None:
        # Menampilkan tombol hanya jika semua input sudah valid
        if st.button('Estimasi Harga'):
            # Melakukan prediksi dengan model yang dimuat
            predict = model.predict([[year, mileage, tax, mpg, engineSize]])
            st.write(f'Estimasi harga mobil bekas dalam Pounds: {predict[0]}')
            st.write(f'Estimasi harga mobil bekas dalam IDR (Juta): {predict[0] * 19000}')
    else:
        # Jika ada input yang masih kosong, tampilkan peringatan
        st.warning('Harap isi semua input terlebih dahulu!')

    st.markdown("</div>", unsafe_allow_html=True)
