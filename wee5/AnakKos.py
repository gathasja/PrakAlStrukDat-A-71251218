import streamlit as st
import pandas as pd

# --- Title ---
st.title("🏠 Pengeluaran Anak Kos 71251218 Anda")


# --- Input Uang Bulanan ---
st.subheader("Uang Bulanan")
bulanan = st.number_input("Insert a number", value=None, placeholder="masukan nominal...", key = 5)


# --- Input Pengeluaran ---
st.subheader("Pengeluaran Bulanan")
makanan = st.number_input("duit makanan", value=None, placeholder="masukan nominal...", key = 0)
kos = st.number_input("bayar kos", value=None, placeholder="masukan nominal...", key = 1)
transportasi = st.number_input("biaya transportasi", value=None, placeholder="masukan nominal...", key = 2)
internet = st.number_input("bayar internet", value=None, placeholder="masukan nominal...", key = 3)
hiburan = st.number_input("liburan", value=None, placeholder="masukan nominal...", key = 4)



# --- Tombol Ngitung Pengeluaran ---
if st.button("hitung"): # if jangan dihapus, cuman nambahin tombol disini :
 
    # --- Ngitung Total Pengeluaran ---
    total = makanan + kos + transportasi + internet + hiburan


    # --- Ngitung Sisa Uang ---
    sisa_uang = bulanan - total


    # --- Menampilkan Hasil kananPerhitungan ---
    st.subheader("Ringkasan Keuangan")
    kolom1, kolom2, kolom3 = st.columns(3)
    with kolom1:
        st.metric(
            # Tampilin uang bulanan di sini
            "Uang Bulanan", bulanan
        )
    with kolom2:
        st.metric(
            # Tampilin total pengeluaran di sini
            "Total Pengeluaran", total
        )
    with kolom3:
        st.metric("sisa uang", 
            # Tampilin sisa uang di sini
            "Sisa Uang", sisa_uang
        )


    # --- Kondisi Keuangan ---
    st.subheader("Kondisi Keuangan")

    # Kondisi 1
    if sisa_uang > 0:
        st.success("masih ada sisa") 

    # Kondisi 2
    elif sisa_uang  == 0:
        st.warning("duitlu habis!")

    # Kondisi 3
    else:
        st.error("duitlu minus woy!")


    # --- Data Pengeluaran ---
    # Ini gausah diubah! 
    # Udah kubantu bikinin, tinggal dipake aja
    data_pengeluaran = {
        "Kategori": [
            "makanan",
            "Kos",
            "transportasi",
            "Internet/Internet",
            "Hiburan"
        ],
        "Pengeluaran": [
            makanan,
            kos,
            transportasi,
            internet,
            hiburan
        ]
    }

    df_pengeluaran = pd.DataFrame(data_pengeluaran)

    # --- Pengeluaran Terbesar ---
    maks = []  # Cari pengeluaran terbesar
    if makanan > kos and makanan > transportasi and makanan > internet and makanan > hiburan:
        maks.append("makanan")
    elif kos > makanan and kos > transportasi and kos > internet and kos > hiburan:
        maks.append("kos")
    elif transportasi > makanan and transportasi > kos and transportasi > internet and transportasi > hiburan:
        maks.append("transportasi")
    elif internet > makanan and internet > kos and internet > transportasi and internet > hiburan:
        maks.append("internet")
    elif hiburan > makanan and hiburan > kos and hiburan > transportasi and hiburan > internet:
        maks.append("hiburan")

    st.subheader("Pengeluaran Terbesar")
    st.write("kategori dengan pengeluaran terbesar:", maks[0]) # Tampilin pengeluaran terbesar di sini


    # --- Grafik Pengeluaran ---
    st.subheader("Grafik Pengeluaran")
    p = df_pengeluaran.set_index("Kategori")
    st.bar_chart(p) # Tampilin grafik pengeluaran di sini