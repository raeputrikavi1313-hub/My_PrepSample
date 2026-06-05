import streamlit as st

st.set_page_config(page_title="My PrepSample", page_icon="🧪")

st.title("🧪 My PrepSample")
st.subheader("Aplikasi Preparasi Wadah dan Pengambilan Sampel")

menu = st.sidebar.selectbox(
    "Pilih Menu",
    ["Titik Sampling", "Wadah Sampel", "Pengawetan Sampel"]
)

# ==========================
# TITIK SAMPLING
# ==========================
if menu == "Titik Sampling":

    st.header("Penentuan Titik Sampling")

    lokasi = st.selectbox(
        "Pilih Lokasi Sampling",
        ["Danau", "Sungai", "Waduk", "Air Limbah Industri"]
    )

    if lokasi == "Danau":
        st.success("Pola sampling yang disarankan: Zig-zag atau beberapa titik representatif.")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Lake_map.svg/512px-Lake_map.svg.png")

    elif lokasi == "Sungai":
        st.success("Pola sampling yang disarankan: Hulu - Tengah - Hilir.")

    elif lokasi == "Waduk":
        st.success("Pola sampling yang disarankan: Beberapa titik pada permukaan dan kedalaman tertentu.")

    elif lokasi == "Air Limbah Industri":
        st.success("Pola sampling yang disarankan: Pada outlet IPAL atau saluran pembuangan.")

# ==========================
# WADAH SAMPEL
# ==========================
elif menu == "Wadah Sampel":

    st.header("Jenis Wadah Sampel")

    parameter = st.selectbox(
        "Pilih Parameter",
        ["pH", "BOD", "COD", "Logam Berat", "Minyak dan Lemak"]
    )

    if parameter == "pH":
        st.info("Wadah: Botol plastik atau kaca.")

    elif parameter == "BOD":
        st.info("Wadah: Botol plastik atau kaca gelap.")

    elif parameter == "COD":
        st.info("Wadah: Botol kaca atau plastik.")

    elif parameter == "Logam Berat":
        st.info("Wadah: Botol plastik PE atau HDPE.")

    elif parameter == "Minyak dan Lemak":
        st.info("Wadah: Botol kaca.")

# ==========================
# PENGAWETAN
# ==========================
elif menu == "Pengawetan Sampel":

    st.header("Bahan Pengawet Sampel")

    parameter = st.selectbox(
        "Pilih Parameter",
        ["BOD", "COD", "Logam Berat", "Amonia", "Minyak dan Lemak"]
    )

    if parameter == "BOD":
        st.warning("Pengawetan: Simpan pada suhu ≤ 4°C.")

    elif parameter == "COD":
        st.warning("Pengawetan: H2SO4 hingga pH < 2.")

    elif parameter == "Logam Berat":
        st.warning("Pengawetan: HNO3 hingga pH < 2.")

    elif parameter == "Amonia":
        st.warning("Pengawetan: H2SO4 hingga pH < 2 dan simpan dingin.")

    elif parameter == "Minyak dan Lemak":
        st.warning("Pengawetan: Simpan pada suhu ≤ 4°C.")
