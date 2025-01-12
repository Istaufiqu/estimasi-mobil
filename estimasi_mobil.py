import pickle
import streamlit as st

# Memuat model yang sudah disimpan
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

# Pengaturan tampilan halaman
st.set_page_config(page_title="Prediksi Harga Mobil Bekas", layout="wide")

# Membuat dua kolom
col1, col2 = st.columns([1, 3])

# Kolom kiri - menampilkan data
with col1:
    st.markdown("<h2 style='text-align: center;'>Tugas Mata Kuliah Pembelajaran Mesin</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Project Machine Learning</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Prediksi Harga Mobil Bekas Menggunakan Regresi Linier dan Decision Tree Regressor</h4>", unsafe_allow_html=True)
    st.markdown("<br><br><b>Disusun Oleh:</b>", unsafe_allow_html=True)
    st.markdown("- **Muh Bintang Mahardani** (17225123)", unsafe_allow_html=True)
    st.markdown("- **Taufiq Ismail** (17215032)", unsafe_allow_html=True)
    st.markdown("<br><b>Kelas:</b> 17.4A.26", unsafe_allow_html=True)
    st.markdown("<b>Program Studi:</b> Teknologi Informasi (S1)", unsafe_allow_html=True)
    st.markdown("<br><b>Universitas:</b> Universitas Bina Sarana Informatika", unsafe_allow_html=True)
    st.markdown("<b>Fakultas:</b> Fakultas Teknik dan Informatika", unsafe_allow_html=True)
    st.markdown("<b>Alamat:</b> Jl. Kemanggisan Utama, RT.3/RW.2, Slipi, Kec. Palmerah, Kota Jakarta Barat, DKI Jakarta 11480", unsafe_allow_html=True)

# Kolom kanan - aplikasi prediksi harga mobil bekas
with col2:
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

