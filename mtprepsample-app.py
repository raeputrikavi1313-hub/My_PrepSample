import streamlit as st

st.set_page_config(
    page_title="My PrepSample",
    page_icon="🧪",
    layout="wide"
)

# ==========================
# TEMA HIJAU
# ==========================
st.markdown("""
<style>

.stApp {
    background-color: #F1F8E9;
}

h1, h2, h3 {
    color: #2E8B57;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================
st.markdown("""
<h1 style='text-align:center;'>
🌿 My PrepSample
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='text-align:center;'>
Sistem Informasi Preparasi Wadah dan Pengambilan Sampel Lingkungan
</h3>
""", unsafe_allow_html=True)

st.image(
    "https://images.unsplash.com/photo-1441974231531-c6227db76b6e",
    use_container_width=True
)

st.success(
    "Aplikasi untuk membantu menentukan titik sampling, jenis wadah sampel, dan pengawetan sampel lingkungan."
)

st.markdown("---")

# ==========================
# MENU UTAMA
# ==========================
st.markdown("## 📋 Menu Utama")

menu = st.radio(
    "",
    [
        "📍 Penentuan Titik Sampling",
        "🧴 Jenis Wadah Sampel",
        "❄️ Pengawetan Sampel"
    ],
    horizontal=True
)

st.markdown("---")

# ==========================
# TITIK SAMPLING
# ==========================
if menu == "📍 Penentuan Titik Sampling":

    st.header("📍 Penentuan Titik Sampling")

    lokasi = st.selectbox(
        "Pilih Lokasi Sampling",
        [
            "Danau",
            "Sungai",
            "Waduk",
            "Air Limbah Industri"
        ]
    )

    if lokasi == "Danau":

        st.image(
            "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
            width=700
        )

        st.success(
            "Metode yang disarankan: Pola zig-zag atau beberapa titik representatif pada area danau."
        )

    elif lokasi == "Sungai":

        st.image(
            "https://images.unsplash.com/photo-1437482078695-73f5ca6c96e2",
            width=700
        )

        st.success(
            "Metode yang disarankan: Hulu - Tengah - Hilir."
        )

    elif lokasi == "Waduk":

        st.image(
            "https://images.unsplash.com/photo-1500375592092-40eb2168fd21",
            width=700
        )

        st.success(
            "Metode yang disarankan: Beberapa titik permukaan dan kedalaman."
        )

    elif lokasi == "Air Limbah Industri":

        st.image(
            "https://images.unsplash.com/photo-1569163139394-de44cb5894a9",
            width=700
        )

        st.success(
            "Metode yang disarankan: Titik inlet dan outlet IPAL."
        )

# ==========================
# WADAH SAMPEL
# ==========================
elif menu == "🧴 Jenis Wadah Sampel":

    st.header("🧴 Jenis Wadah Sampel")

    parameter = st.selectbox(
        "Pilih Parameter",
        [
            "pH",
            "BOD",
            "COD",
            "TSS",
            "Logam Berat",
            "Minyak dan Lemak",
            "Amonia"
        ]
    )

    data_wadah = {
        "pH": "Botol plastik atau kaca",
        "BOD": "Botol kaca/plastik gelap",
        "COD": "Botol plastik atau kaca",
        "TSS": "Botol plastik",
        "Logam Berat": "Botol HDPE",
        "Minyak dan Lemak": "Botol kaca",
        "Amonia": "Botol plastik"
    }

    st.info(data_wadah[parameter])

# ==========================
# PENGAWETAN SAMPEL
# ==========================
elif menu == "❄️ Pengawetan Sampel":

    st.header("❄️ Pengawetan Sampel")

    parameter = st.selectbox(
        "Pilih Parameter",
        [
            "BOD",
            "COD",
            "TSS",
            "Logam Berat",
            "Minyak dan Lemak",
            "Amonia"
        ]
    )

    data_pengawet = {
        "BOD": "Simpan pada suhu ≤ 4°C",
        "COD": "Tambahkan H₂SO₄ hingga pH < 2",
        "TSS": "Simpan pada suhu ≤ 4°C",
        "Logam Berat": "Tambahkan HNO₃ hingga pH < 2",
        "Minyak dan Lemak": "Simpan pada suhu ≤ 4°C",
        "Amonia": "Tambahkan H₂SO₄ hingga pH < 2"
    }

    st.warning(data_pengawet[parameter])

# ==========================
# FOOTER
# ==========================
st.markdown("---")

st.markdown("""
<div style='text-align:center;'>

🌿 <b>My PrepSample</b><br>
Program Studi Pengelolaan Limbah Industri<br>
Akademi Kimia Analis Bogor

</div>
""", unsafe_allow_html=True)
 
