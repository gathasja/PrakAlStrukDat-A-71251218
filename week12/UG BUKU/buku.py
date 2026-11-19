from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import requests

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
}

st.set_page_config(page_title="Dashboard Katalog Buku", layout="wide")
st.title("Dashboard Katalog Buku")
st.write("Mengambil data buku melalui web scraping dan kurs GBP/IDR melalui REST API.")

jumlah_halaman = st.slider("Jumlah halaman katalog yang diambil", 1, 3, 2)

if st.button("Ambil Data dan Tampilkan Dashboard", type="primary"):
    data_buku = []

    try:
        with st.spinner("Mengambil data..."):
            for halaman in range(1, jumlah_halaman + 1):
                url = f"https://books.toscrape.com/catalogue/page-{halaman}.html"
                respon = requests.get(url, timeout=15)
                respon.raise_for_status()
                respon.encoding = "utf-8"
                soup = BeautifulSoup(respon.text, "html.parser")

                for buku in soup.select("article.product_pod"):
                    judul = buku.h3.a["title"]
                    harga_teks = buku.select_one("p.price_color").text
                    harga_gbp = float("".join(c for c in harga_teks if c.isdigit() or c == "."))
                    kelas_rating = buku.select_one("p.star-rating")["class"]
                    rating = next((RATING_MAP[k] for k in kelas_rating if k in RATING_MAP), 0)
                    ketersediaan = buku.select_one("p.availability").text.strip()

                    data_buku.append({
                        "judul": judul,
                        "harga_gbp": harga_gbp,
                        "rating": rating,
                        "ketersediaan": ketersediaan,
                    })

            respon_kurs = requests.get(
                "https://api.frankfurter.dev/v1/latest",
                params={"base": "GBP", "symbols": "IDR"},
                timeout=15,
            )
            respon_kurs.raise_for_status()
            kurs = respon_kurs.json()["rates"]["IDR"]
    except Exception as e:
        st.error(f"Gagal mengambil data: {e}")
        st.stop()

    df = pd.DataFrame(data_buku)
    df["harga_idr"] = df["harga_gbp"] * kurs

    st.subheader("Data Katalog Buku")
    st.caption(f"{len(df)} buku diambil dari {jumlah_halaman} halaman.")
    st.dataframe(df)

    st.subheader("Visualisasi")
    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots()
        ax1.hist(df["harga_idr"], bins=10, edgecolor="black")
        ax1.set_title("Distribusi Harga Buku")
        ax1.set_xlabel("Harga (Rupiah)")
        ax1.set_ylabel("Jumlah Buku")
        ax1.set_axisbelow(True)
        ax1.grid(axis="y", alpha=0.3)
        st.pyplot(fig1)

    with col2:
        jumlah_rating = df["rating"].value_counts().reindex([1, 2, 3, 4, 5], fill_value=0)
        fig2, ax2 = plt.subplots()
        ax2.bar(jumlah_rating.index, jumlah_rating.values)
        ax2.set_title("Jumlah Buku Berdasarkan Rating")
        ax2.set_xlabel("Rating")
        ax2.set_ylabel("Jumlah Buku")
        ax2.set_axisbelow(True)
        ax2.grid(axis="y", alpha=0.3)
        st.pyplot(fig2)
    

    

    
    