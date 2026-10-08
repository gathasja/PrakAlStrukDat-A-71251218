import streamlit as st
from user import user_data_by_username

# CEK APAKAH SUDAH LOGIN
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

user = user_data_by_username()
username = st.session_state.username

# hint untuk mematikan text input ada di -> https://docs.streamlit.io/develop/api-reference/widgets/st.text_input
# BUAT 2 INPUT TEXT 1 Username 1 Password namun disable/matikan field Username dan yang password harus tipe password

st.title("Profile")

st.text_input(
    "username",
    value=username,
    disabled=True
)

password_baru = st.text_input(
    "Password Baru",
    type="password"
)
# Silahkan kalau mau baca baca ini hehe ga wajib ya-> https://discuss.streamlit.io/t/buttons-alignment/51929
col1, col2 = st.columns([1,4])
with col1:
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.switch_page("app.py")
        
with col2:
    if st.button("Ganti Data"):
        if password_baru == user[username]["password"]:
            st.error("Password Baru tidak boleh sama")
        elif password_baru == "":
            st.error("Password tidak boleh kosong")
        else:
            user[username]["password"] = password_baru
            st.success("Password berhasil diganti")