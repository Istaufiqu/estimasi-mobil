import pickle
import streamlit as st

# Memuat model yang sudah disimpan
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

# Mengubah tipe input menjadi bilangan bulat (integer)
# Set nilai default menjadi None, agar tidak ada 0 yang ditampilkan di awal
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
