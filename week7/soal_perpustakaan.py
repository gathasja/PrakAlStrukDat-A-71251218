import pandas as pd
import streamlit as st

# ===== Data =====
# dictionary bersarang: {kode: {"judul", "stok"}}
KATALOG_AWAL = {
    "B01": {"judul": "Algoritma Dasar", "stok": 2},
    "B02": {"judul": "Struktur Data Python", "stok": 1},
    "B03": {"judul": "Basis Data Relasional", "stok": 2},
    "B04": {"judul": "Statistika Dasar", "stok": 1},
    "B05": {"judul": "Kalkulus 1", "stok": 3},
}


def buat_katalog():
    return {kode: dict(data) for kode, data in KATALOG_AWAL.items()}



# ===== Logika =====
def pinjam_buku(katalog, pinjaman, nama, kode):
    # return pesan error (str) kalau gagal, atau None kalau berhasil
    if nama == "":
        return "Nama peminjam wajib diisi"
    if {"nama": nama, "kode": kode} in pinjaman:
        return "Buku ini sudah kamu pinjam"
    if katalog[kode]["stok"] == 0:
        return "Stok buku habis!"
    katalog[kode]["stok"] -= 1
    pinjaman.append({"nama": nama, "kode": kode})
    return None


def kembalikan_buku(katalog, pinjaman, nama, kode):
    # return pesan error (str) kalau gagal, atau None kalau berhasil
    if nama == "":
        return "Nama peminjam wajib diisi"
    data = {"nama": nama, "kode": kode}
    if data not in pinjaman:
        return "Data peminjaman tidak ditemukan!"
    pinjaman.remove(data)
    katalog[kode]["stok"] += 1
    return None


def rekap_per_peminjam(pinjaman):
    # return dictionary {nama: set kode buku yang sedang dipinjam}
    rekap = {}
    for p in pinjaman:
        if p["nama"] not in rekap:
            rekap[p["nama"]] = set()
        rekap[p["nama"]].add(p["kode"])
    return rekap


# ===== Tampilan =====
def form_buku():
    # lengkapi kode def form_buku() untuk input nama dan kode
    # return (nama peminjam, kode buku, tombol Pinjam ditekan?, tombol Kembalikan ditekan?)
    # nama dibaca APA ADANYA (case-sensitive), hanya spasi di pinggir yang dibuang

    nama = st.text_input("Nama peminjam")
    kode = st.selectbox(
        "Buku",
        list(KATALOG_AWAL.keys()),
        format_func = lambda k: f"{k} - {KATALOG_AWAL[k]["judul"]}",
        )
    kol1, kol2 = st.columns(2)
    pinjam = kol1.button("📖 Pinjam")
    kembali = kol2.button("↩️ Kembalikan")
    return nama, kode, pinjam, kembali
    

def tampilkan_katalog(katalog):
    st.table(pd.DataFrame.from_dict(katalog, orient="index"))


def tampilkan_pinjaman(pinjaman):
    if pinjaman:
        st.table(pd.DataFrame(pinjaman))
    else:
        st.info("Belum ada buku yang sedang dipinjam.")


def tampilkan_rekap(rekap):
    if rekap:
        baris = [(nama, ", ".join(sorted(kode)), len(kode)) for nama, kode in sorted(rekap.items())]
        st.table(pd.DataFrame(baris, columns=["Nama", "Buku", "Jumlah"]).set_index("Nama"))
    else:
        st.info("Belum ada peminjam.")


# ===== Aplikasi =====
st.title("📚 Peminjaman Buku Perpustakaan")

if "katalog" not in st.session_state:
    st.session_state["katalog"] = buat_katalog()
    st.session_state["pinjaman"] = []
katalog = st.session_state["katalog"]
pinjaman = st.session_state["pinjaman"]

nama, kode, pinjam, kembali = form_buku()

judul = katalog[kode]["judul"]
if pinjam:
    pesan =  pinjam_buku(katalog, pinjaman, nama, kode)
    if pesan: 
        st.error(f"Data tidak ditemukan!")
    else:
        st.success(f"{nama} berhasil meminjam {judul} ✅")
elif kembali:
    pesan =  kembalikan_buku(katalog, pinjaman, nama, kode)
    if pesan: 
        st.error(f"Data tidak ditemukan!")
    else:
        st.success(f"{nama} berhasil mengembalikan {judul} ✅")
        
    

# B. kerjakan di sini:
#    - kalau `pinjam`  -> panggil pinjam_buku(...)
#    - kalau `kembali` -> panggil kembalikan_buku(...)
#    keduanya: kalau ada pesan -> st.error(pesan), kalau tidak -> st.success("... berhasil ...")

st.subheader("📦 Stok Buku")
tampilkan_katalog(katalog)

st.subheader("📋 Sedang Dipinjam")
tampilkan_pinjaman(pinjaman)

st.subheader("👤 Rekap Per Peminjam")
tampilkan_rekap(rekap_per_peminjam(pinjaman))
