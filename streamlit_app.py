import streamlit as st

st.title("  🎈  Reza Madridista  ")
st.write(
    "Reza anak sekolah SMAN 20 BANDUNG  .")
st.image("17477384579282276395910537665755.jpg",width=200) 




st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)

if (angka % 2) ==0:
 st.write(f"{angka} adalah Bilangan Genap")
else:
 st.write(f"{angka}adalah Bilangan Ganjil")
    
