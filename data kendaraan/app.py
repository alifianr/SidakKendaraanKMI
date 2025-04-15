import streamlit as st
import pandas as pd

# Load data
data = pd.read_csv('data_kendaraan.csv')

# Title
st.title("🔍 Pencarian Data Kendaraan")

# Input dari pengguna
query = st.text_input("Masukkan Nama, NIK, atau No.Plat Kendaraan:")

# Tombol pencarian
if query:
    results = data[
        (data['Nama Lengkap'].astype(str).str.contains(query, case=False, na=False)) |
        (data['NIK'].astype(str).str.contains(query, case=False, na=False)) |
        (data['No.Plat'].astype(str).str.contains(query, case=False, na=False))
    ]
    
    if not results.empty:
        st.success(f"Ditemukan {len(results)} hasil untuk '{query}'")
        st.dataframe(results)
    else:
        st.warning(f"Tidak ditemukan hasil untuk '{query}'")
else:
    st.info("Silakan masukkan kata kunci untuk mencari data kendaraan.")
