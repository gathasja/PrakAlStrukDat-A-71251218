#movieApp
import streamlit as st
import pandas as pd
import json
# Konfigurasi Halaman
st.set_page_config(page_title="Movie Explorer", layout="wide")
st.title("Movie Catalog Explorer")
st.markdown("Aplikasi interaktif untuk mengeksplorasi data film.")
@st.cache_data
def load_data():
    """Membaca file data mentah JSON."""
    with open("movies_data.json", "r") as file:
        data = json.load(file)
    return data
raw_data = load_data()
df = pd.DataFrame(raw_data)
st.sidebar.header("Filter Data")
search_title = st.sidebar.text_input("Cari Judul Film:")
genre_options = ["All"] + sorted(df["genre"].dropna().unique().tolist())

selected_genre = st.sidebar.selectbox("Pilih Genre:", genre_options)

min_rating = st.sidebar.slider("Batas Rating Minimal:", 0.0, 10.0, 7.0, 0.1)
show_raw = st.sidebar.toggle("Tampilkan Raw Data JSON")
if show_raw:
    st.json(raw_data)

filtered_df = df.copy()
if search_title:
    filtered_df = filtered_df[filtered_df['title'].str.contains(search_title, case=False, na=False)]
if selected_genre and selected_genre != "All":
    filtered_df = filtered_df[filtered_df['genre'] == selected_genre]
if min_rating is not None:
    filtered_df = filtered_df[filtered_df['rating'] >= min_rating]
st.markdown("---")
st.subheader("Hasil Eksplorasi")

if filtered_df.empty:
    st.warning("data kosong")
else:
    st.success(f"Berhasil menemukan {len(filtered_df)} film!")
    a, b = st.columns(2)

    a.metric("Jumlah Film", len(filtered_df)) 
    b.metric("Rata-rata Rating", f"{filtered_df["rating"].mean():.2f}")
    st.dataframe(filtered_df, width= "stretch")
