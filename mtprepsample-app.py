# ==========================================
# Aplikasi EcoSurface: Pemantauan Kualitas Air
# ==========================================

# Import library yang dibutuhkan
import streamlit as st
import pandas as pd

# --- KONFIGURASI HALAMAN DAN DESAIN ---
st.set_page_config(
    page_title="EcoSurface - Monitoring Air",
    page_icon="💧", # Icon tetesan air
    layout="wide",  # Tampilan lebar
    initial_sidebar_state="expanded"
)

# Custom CSS untuk menghilangkan menu default Streamlit (opsional, untuk tampilan bersih)
# st.markdown(""" <style> #MainMenu {visibility: hidden;} </style> """, unsafe_allow_html=True)

# --- DATABASE (DATA SAMPLING & BAKU MUTU) ---
# Struktur data menggunakan Dictionary (Key-Value) agar mudah diakses dan dikelola.

# 1. Data Panduan Sampling: Menyimpan info wadah, pengawet, dll.
panduan_sampling = {
    "pH": {
        "wadah": "Botol Plastik (PE)",
        "volume": "500 mL",
        "pengawet": "Tidak ada",
        "penyimpanan": "4°C",
        "holding_time": "14 hari",
        "catatan": "Segera dinginkan setelah sampling. Hindari kontak lama dengan udara."
    },
    "Suhu": {
        "wadah": "Botol Kaca",
        "volume": "1 L",
        "pengawet": "Tidak ada",
        "penyimpanan": "In situ / On site",
        "holding_time": "Segera",
        "catatan": "Pengukuran dilakukan langsung di lokasi saat sampling."
    },
    "TSS": {
        "wadah": "Botol Plastik (PE)",
        "volume": "1 L",
        "pengawet": "Tidak ada",
        "penyimpanan": "4°C",
        "holding_time": "7 hari",
        "catatan": "Pastikan botol bersih dan tidak terkontaminasi."
    },
    "TDS": {
        "wadah": "Botol Plastik (PE)",
        "volume": "500 mL",
        "pengawet": "Tidak ada",
        "penyimpanan": "4°C",
        "holding_time": "7 hari",
        "catatan": "Saring sampel terlebih dahulu jika mengandung partikel kasar."
    },
    "DO": {
        "wadah": "Botol Kaca Amber",
        "volume": "300 mL",
        "pengawet": "Reagen Fixative (MgCl2)",
        "penyimpanan": "4°C",
        "holding_time": "24 jam",
        "catatan": "Hindari gelembung udara saat pengisian botol."
    },
    "BOD": {
        "wadah": "Botol Kaca Amber",
        "volume": "1 L",
        "pengawet": "Tidak ada (Dark Bottle)",
        "penyimpanan": "4°C",
        "holding_time": "48 jam (最佳: < 6 jam)",
        "catatan": "Simpan dalam kegelapan untuk mencegah fotosintesis."
    },
    "COD": {
        "wadah": "Botol Plastik (PE)",
        "volume": "500 mL",
        "pengawet": "H2SO4 p.a.",
        "penyimpanan": "4°C",
        "holding_time": "28 hari",
        "catatan": "Tambahkan H2SO4 hingga pH < 2."
    },
    "Nitrat": {
        "wadah": "Botol Plastik (PE)",
        "volume": "500 mL",
        "pengawet": "H2SO4 hingga pH < 2",
        "penyimpanan": "4°C",
        "holding_time": "28 hari",
        "catatan": "Dinginkan sampel segera."
    },
    "Amonia": {
        "wadah": "Botol Plastik (PE)",
        "volume": "500 mL",
        "pengawet": "H2SO4 hingga pH < 2",
        "penyimpanan": "4°C",
        "holding_time": "28 hari",
        "catatan": "Hindari kontaminasi udara."
    },
    "Fosfat": {
        "wadah": "Botol Plastik (PE)",
        "volume": "500 mL",
        "pengawet": "Tidak ada / HCl",
        "penyimpanan": "4°C",
        "holding_time": "28 hari",
        "catatan": "Cuci botol dengan HCl sebelum penggunaan."
    },
    "Total Coliform": {
        "wadah": "Botol Steril",
        "volume": "100 mL",
        "pengawet": "Natrium Thiosulfat",
        "penyimpanan": "4°C",
        "holding_time": "24 jam",
        "catatan": "Jaga sterilitas sampel."
    }
}

# 2. Data Baku Mutu (Contoh: Peratuan Menteri Lingkungan Hidup)
# Logika: Batasan Maksimum (kecuali DO adalah Minimum)
baku_mutu = {
    "pH": {"standar": 9.0, "satuan": "-", "jenis": "maks"},
    "Suhu": {"standar": 28.0, "satuan": "°C", "jenis": "maks"},
    "TSS": {"standar": 50, "satuan": "mg/L", "jenis": "maks"},
    "TDS": {"standar": 1000, "satuan": "mg/L", "jenis": "maks"},
    "DO": {"standar": 4, "satuan": "mg/L", "jenis": "min"}, # DO harus >= dari standar
    "BOD": {"standar": 3, "satuan": "mg/L", "jenis": "maks"},
    "COD": {"standar": 25, "satuan": "mg/L", "jenis": "maks"},
    "Nitrat": {"standar": 10, "satuan": "mg/L", "jenis": "maks"},
    "Amonia": {"standar": 0.5, "satuan": "mg/L", "jenis": "maks"},
    "Fosfat": {"standar": 1, "satuan": "mg/L", "jenis": "maks"}
}

# --- FUNGSI UTAMA ---

def show_header():
    """Menampilkan judul dan deskripsi di bagian atas."""
    st.title("EcoSurface 💧")
    st.markdown("""
    Aplikasi **pendukung kegiatan pemantauan kualitas air permukaan**.
    Gunakan menu di sidebar untuk navigasi.
    """)

# --- HALAMAN ---

def halaman_beranda():
    """Tampilan Dashboard / Beranda."""
    st.header("Dashboard Monitoring")
    
    # Colom untuk metric cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="📊 Parameter Sampling", value=len(panduan_sampling))
    with col2:
        st.metric(label="✅ Parameter Baku Mutu", value=len(baku_mutu))
    with col3:
        st.info("💡Tips: Pastikan data yang diinput akurat!")
    
    st.markdown("---")
    st.subheader("Cara Menggunakan Aplikasi:")
    st.markdown("""
    1. **Panduan Sampling**: Pilih parameter untuk mengetahui jenis wadah dan bahan pengawet yang benar.
    2. **Evaluasi Baku Mutu**: Masukkan hasil laboratorium untuk dicek kesesuaiannya dengan regulasi.
    """)

def halaman_sampling():
    """Tampilan Fitur 1: Panduan Sampling."""
    st.header("Panduan Pengambilan Sampel Air")
    st.info("Pilih parameter yang akan dianalisis untuk melihat panduan lengkapnya.")
    
    # Dropdown Pilih Parameter
    parameter_list = sorted(panduan_sampling.keys())
    pilihan_param = st.selectbox("Pilih Parameter Kualitas Air:", parameter_list)
    
    if pilihan_param:
        # Mengambil data dari dictionary
        data = panduan_sampling[pilihan_param]
        
        st.markdown("---")
        # Tampilan Card menggunakan Columns
        c1, c2 = st.columns([1, 2])
        with c1:
            # Bagian kiri: Info Detail
            st.markdown(f"### 🔍 Detail untuk **{pilihan_param}**")
            st.write(f"**Wadah:** {data['wadah']}")
            st.write(f"**Volume Min:** {data['volume']}")
            st.write(f"**Pengawet:** {data['pengawet']}")
            st.write(f"**Penyimpanan:** {data['penyimpanan']}")
            st.write(f"**Holding Time:** {data['holding_time']}")
        with c2:
            # Bagian kanan: Catatan tambahan dalam box info
            st.warning("📝 Catatan Penting:")
            st.markdown(data['catatan'])
            
            # Contoh visual progress (dummy visualisasi)
            st.progress(100)
            st.caption("Status: Panduan Siap Dicetak")

def halaman_evaluasi():
    """Tampilan Fitur 2: Evaluasi Baku Mutu."""
    st.header("Evaluasi Hasil Analisis")
    st.warning("Input hasil analisis air di bawah ini untuk dicek.")
    
    # Pilih Kolom 1: Pilih Parameter
    col1, col2 = st.columns(2)
    with col1:
        baku_list = sorted(baku_mutu.keys())
        param_pilih = st.selectbox("Pilih Parameter:", baku_list)
    
    # Pilih Kolom 2: Input Nilai
    with col2:
        # Default number input
        nilai_input = st.number_input(f"Masukkan Nilai {param_pilih}", min_value=0.0, value=0.0, step=0.1)
    
    # Logika Perbandingan
    if nilai_input > 0:
        standar = baku_mutu[param_pilih]["standar"]
        jenis = baku_mutu[param_pilih]["jenis"] # 'min' atau 'maks'
        satuan = baku_mutu[param_pilih]["satuan"]
        
        # Hitung Status
        if jenis == "min":
            # Untuk DO: Semakin tinggi semakin baik (>= Standar)
            memenuhi = nilai_input >= standar
        else:
            # Untuk yang lain: Semakin rendah semakin baik (<= Standar)
            memenuhi = nilai_input <= standar
            
        # Hitung Selisih
        selisih = abs(nilai_input - standar)
        
        # TAMPILAN HASIL
        st.markdown("---")
        
        # KotakHasil menggunakan Columns
        k1, k2, k3 = st.columns(3)
        
        k1.metric("Nilai Hasil", f"{nilai_input} {satuan}")
        k2.metric("Baku Mutu", f"{standar} {satuan}")
        k3.metric("Selisih", f"{selisih} {satuan}")
        
        # Status Akhir
        if memenuhi:
            st.success(f"✅ **STATUS: MEMENUHI BAKU MUTU**")
            st.balloons() # Efek balon jika berhasil
        else:
            st.error(f"❌ **STATUS: TIDAK MEMENUHI BAKU MUTU**")
            st.markdown(f"⚠️ Nilai hasil **{param_pilih}** ({nilai_input}) melampaui batas standar ({standar} {satuan}).")

def halaman_tentang():
    """Tampilan Tentang Aplikasi."""
    st.header("Tentang EcoSurface")
    
    st.markdown("""
    ### Aplikasi Web: EcoSurface
