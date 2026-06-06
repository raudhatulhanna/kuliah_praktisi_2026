""" Sistem Informasi Titrimetri - Streamlit App Jalankan: streamlit run app.py """

import streamlit as st import math
KONFIGURASI HALAMAN
─────────────────────────────────────────────
st.set_page_config( page_title="Sistem Informasi Titrimetri", page_icon="⚗", layout="wide", initial_sidebar_state="expanded", 
CSS KUSTOM
─────────────────────────────────────────────
st.markdown("""

<style> @import url('
https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@400;500;600&family=DM+Mono&display=swap
'); html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; } h1,h2,h3 { font-family: 'Playfair Display', serif !important; } .hero-box { background: linear-gradient(135deg, #0d1b2e 0%, #0a1628 100%); border: 1px solid #2a3a5c; border-radius: 20px; padding: 2.5rem 3rem; margin-bottom: 2rem; text-align: center; } .hero-box h1 { color: #4fc3f7; font-size: 2.5rem; margin-bottom: .5rem; } .hero-box p { color: #8899bb; font-size: 1rem; } .info-card { background: #111827; border-left: 4px solid; border-radius: 12px; padding: 1.25rem 1.5rem; margin-bottom: 1rem; } .formula-box { background: #1c2740; border: 1px solid #2a3a5c; border-radius: 10px; padding: 1rem 1.5rem; font-family: 'DM Mono', monospace; font-size: .9rem; margin-bottom: .75rem; } .reaction-box { background: #1c2740; border-left: 3px solid #f06292; border-radius: 0 10px 10px 0; padding: 1rem 1.5rem; font-family: 'DM Mono', monospace; font-size: .88rem; margin-bottom: .75rem; color: #e8edf5; } .tag { display: inline-block; padding: .2rem .75rem; border-radius: 14px; font-size: .78rem; font-weight: 600; margin: .2rem; } </style>
""", unsafe_allow_html=True)

─────────────────────────────────────────────
DATA TITRASI
─────────────────────────────────────────────
DATA = { "Asam–Basa": { "warna": "#4fc3f7", "emoji": "🧫", "deskripsi": "Berdasarkan reaksi netralisasi antara ion H⁺ dan OH⁻. Menghasilkan air dan garam.", "subtipe": ["Asam kuat–basa kuat", "Asam lemah–basa kuat", "Basa lemah–asam kuat", "Poliprotik"], "indikator": { "Fenolftalein (PP)": "Tak berwarna → merah muda (pH 8.2–10.0)", "Metil merah": "Merah → kuning (pH 4.4–6.2)", "Metil jingga": "Merah → jingga (pH 3.1–4.4)", "Lakmus": "Merah → biru (pH 7)", }, "alat": [ "Buret 50 mL + klem + statif", "Pipet volumetri 25 mL", "Labu Erlenmeyer 250 mL", "Labu takar 100/250 mL", "Gelas piala 100 mL", "pH meter (opsional)", "Corong kaca", "Botol semprot aquades", ], "bahan": [ "NaOH (baku sekunder)", "Asam oksalat H₂C₂O₄·2H₂O (baku primer, BM=126.07)", "HCl atau H₂SO₄ encer", "Indikator fenolftalein (PP) 1% dalam etanol", "Indikator metil jingga 0.1%", "Aquades bebas CO₂", "Sampel: asam cuka, antasida", ], "reaksi": [ ("Netralisasi Asam Kuat–Basa Kuat", "HCl(aq) + NaOH(aq) → NaCl(aq) + H₂O(l)\nIon: H⁺(aq) + OH⁻(aq) → H₂O(l)"), ("Asam Lemah–Basa Kuat", "CH₃COOH(aq) + NaOH(aq) → CH₃COONa(aq) + H₂O(l)"), ("Standarisasi NaOH dengan Asam Oksalat", "H₂C₂O₄(aq) + 2NaOH(aq) → Na₂C₂O₄(aq) + 2H₂O(l)"), ("Basa Lemah–Asam Kuat", "NH₃(aq) + HCl(aq) → NH₄Cl(aq)"), ], "fase": [ ("HCl, NaOH, H₂SO₄", "(aq)", "Larutan, terionisasi penuh"), ("H₂O", "(l)", "Cair, produk netralisasi"), ("NaCl, Na₂SO₄", "(aq)", "Garam terlarut"), ("H₂C₂O₄·2H₂O", "(s)", "Padatan kristal baku primer"), ("CH₃COOH", "(aq)", "Asam lemah, terionisasi sebagian"), ], "bagan": [ "Timbang H₂C₂O₄·2H₂O (baku primer), larutkan dalam labu takar 100 mL", "Isi buret dengan NaOH, baca volume awal (V₀)", "Pipet 25.00 mL asam oksalat baku ke Erlenmeyer", "Tambahkan 2–3 tetes indikator fenolftalein", "Teteskan NaOH perlahan sambil mengocok Erlenmeyer", "Hentikan saat warna merah muda permanen ≥ 30 detik", "Catat V akhir, hitung V_NaOH = V_akhir – V₀", "Hitung N_NaOH: N₁V₁ = N₂V₂", "Ulangi triplo, hitung rata-rata dan RSD", ], "rumus": [ ("Rumus Dasar", "N₁ × V₁ = N₂ × V₂"), ("Normalitas NaOH", "N_NaOH = (massa_asam × 1000) / (BE_asam × V_NaOH)"), ("BE Asam Oksalat", "BE = BM/2 = 126.07/2 = 63.03 g/ekivalen"), ("% Kadar Analit", "% = (N_titran × V_titran × BE_analit) / (1000 × m_sampel) × 100%"), ], "kadar_teoritis": [ ("Asam cuka murni (CH₃COOH)", 100.0), ("HCl 37% (w/w) / fuming", 37.0), ("H₂SO₄ 98% pekat", 98.0), ("NaOH pro analysis", 97.0), ], },

"Redoks": {
    "warna": "#f06292",
    "emoji": "⚡",
    "deskripsi": "Berdasarkan perpindahan elektron antara oksidator dan reduktor.",
    "subtipe": ["Permanganometri", "Dikromatometri", "Iodimetri", "Iodometri", "Serimetri"],
    "indikator": {
        "Auto-indikator (KMnO₄)": "Ungu → tak berwarna (titik akhir = warna merah muda pucat)",
        "Amilum 1%": "Biru tua (I₂-amilum) → tak berwarna (iodometri)",
        "Difenilamin": "Tak berwarna → ungu (dikromatometri)",
        "Feroin": "Merah → biru pucat (serimetri, dikromatometri)",
    },
    "alat": [
        "Buret coklat 50 mL (untuk KMnO₄)",
        "Buret kaca biasa (Na₂S₂O₃)",
        "Labu Erlenmeyer 500 mL",
        "Pipet volumetri 10/25 mL",
        "Labu takar 250 mL",
        "Pemanas/hot plate + termometer",
        "Gelas piala 250 mL",
    ],
    "bahan": [
        "KMnO₄ (baku sekunder, ~0.02 M)",
        "Na₂C₂O₄ (baku primer, BM=134.00)",
        "Na₂S₂O₃·5H₂O (iodometri)",
        "KIO₃ atau K₂Cr₂O₇ (baku primer iodometri)",
        "KI kristal",
        "H₂SO₄ 1 N (suasana asam)",
        "Larutan amilum 1% (indikator iodometri)",
        "Sampel: FeSO₄, H₂O₂, CuSO₄",
    ],
    "reaksi": [
        ("Permanganometri – Suasana Asam (Reduksi KMnO₄)",
         "MnO₄⁻(aq) + 8H⁺(aq) + 5e⁻ → Mn²⁺(aq) + 4H₂O(l)\n5Fe²⁺(aq) → 5Fe³⁺(aq) + 5e⁻\nNet: MnO₄⁻ + 5Fe²⁺ + 8H⁺ → Mn²⁺ + 5Fe³⁺ + 4H₂O"),
        ("Standarisasi KMnO₄ dengan Na₂C₂O₄",
         "2MnO₄⁻ + 5C₂O₄²⁻ + 16H⁺ → 2Mn²⁺ + 10CO₂(g) + 8H₂O"),
        ("Iodometri – Pembebasan I₂ oleh K₂Cr₂O₇",
         "Cr₂O₇²⁻ + 6I⁻ + 14H⁺ → 2Cr³⁺ + 3I₂ + 7H₂O"),
        ("Titrasi I₂ dengan Na₂S₂O₃",
         "I₂(aq) + 2S₂O₃²⁻(aq) → 2I⁻(aq) + S₄O₆²⁻(aq)"),
    ],
    "fase": [
        ("KMnO₄", "(aq)", "Larutan ungu tua"),
        ("Mn²⁺", "(aq)", "Tak berwarna (setelah direduksi)"),
        ("MnO₂", "(s)", "Endapan coklat (suasana netral)"),
        ("CO₂", "(g)", "Gas"),
        ("I₂", "(aq)", "Larutan coklat-kuning"),
        ("AgSCN, AgCl", "(s)", "Endapan putih"),
    ],
    "bagan": [
        "Standarisasi: Larutkan Na₂C₂O₄ baku primer dalam labu takar 250 mL",
        "Pipet 25 mL Na₂C₂O₄ ke Erlenmeyer, tambah 25 mL H₂SO₄ 1N",
        "Panaskan hingga 60–80°C (suasana panas diperlukan)",
        "Titrasi dengan KMnO₄ dari buret coklat — warna ungu hilang",
        "Titik akhir: warna ungu muda permanen ≥ 30 detik",
        "Hitung N_KMnO₄ dari data standarisasi",
        "Untuk iodometri: larutkan sampel, tambah KI berlebih + H₂SO₄",
        "I₂ yang bebas dititrasi dengan Na₂S₂O₃ (indikator amilum ditambah menjelang titik akhir)",
        "Titik akhir: warna biru hilang → tak berwarna",
    ],
    "rumus": [
        ("Faktor Ekivalen KMnO₄ (asam)", "BE = BM/5 = 158.03/5 = 31.61 g/ekivalen"),
        ("Faktor Ekivalen KMnO₄ (netral)", "BE = BM/3 = 158.03/3 = 52.68 g/ekivalen"),
        ("Kadar Fe²⁺", "% Fe = (N_KMnO₄ × V_KMnO₄ × 55.85) / (1000 × m_sampel) × 100%"),
        ("Kadar H₂O₂ (iodometri)", "% H₂O₂ = (N_Na₂S₂O₃ × V × 17.01) / (1000 × m_sampel) × 100%"),
        ("BE Na₂S₂O₃", "BE = BM/1 = 248.19 g/ekivalen"),
    ],
    "kadar_teoritis": [
        ("Fe dalam FeSO₄·7H₂O", 20.09),
        ("H₂O₂ 30% (w/v)", 30.0),
        ("K₂Cr₂O₇ murni (BM=294.18)", 100.0),
        ("Fe dalam Fe₂O₃", 69.94),
    ],
},

"Kompleksometri": {
    "warna": "#aed581",
    "emoji": "🔗",
    "deskripsi": "Berdasarkan pembentukan kompleks kelat stabil antara ion logam dan EDTA (ligan multidentat).",
    "subtipe": ["Chelometri (EDTA)", "Penentuan kesadahan", "Titrasi selektif logam", "Back titration"],
    "indikator": {
        "EBT (Eriochrome Black T)": "Merah anggur → biru (Mg²⁺, Ca²⁺, pH 10)",
        "Murexide": "Merah → ungu (Ca²⁺, pH 12)",
        "Xylenol Orange": "Merah → kuning (pH 5–6, logam berat)",
        "Calcon": "Merah anggur → biru (Ca²⁺, pH 12)",
    },
    "alat": [
        "Buret 25/50 mL",
        "Pipet volumetri 25 mL",
        "Labu Erlenmeyer 250 mL",
        "Labu takar 250 mL",
        "pH meter / kertas pH",
        "Gelas piala 100 mL",
    ],
    "bahan": [
        "EDTA Na₂H₂Y·2H₂O 0.01 M (BM=372.24)",
        "CaCO₃ pro analysis (baku primer, BM=100.09)",
        "Buffer pH 10: NH₃ + NH₄Cl",
        "Buffer pH 12: NaOH 0.05 M",
        "Indikator EBT (Eriochrome Black T)",
        "Indikator Murexide",
        "Inhibitor Mg²⁺: NaOH 1M (selektif Ca²⁺)",
        "Sampel: air kran, air sadah, larutan logam",
    ],
    "reaksi": [
        ("Reaksi Umum EDTA dengan Ion Logam",
         "M^n+(aq) + H₂Y²⁻(aq) → [MY]^(n-4)(aq) + 2H⁺(aq)"),
        ("Titrasi Ca²⁺ (pH 12, indikator Murexide)",
         "Ca²⁺(aq) + H₂Y²⁻(aq) → [CaY]²⁻(aq) + 2H⁺(aq)  log K = 10.7"),
        ("Titrasi Mg²⁺ + Ca²⁺ (pH 10, EBT)",
         "Mg²⁺ + Y⁴⁻ → [MgY]²⁻   log K = 8.9\nCa²⁺ + Y⁴⁻ → [CaY]²⁻   log K = 10.7"),
        ("Reaksi EBT dengan Logam (sebelum titrasi)",
         "M²⁺ + HIn²⁻ → [MIn]⁻ + H⁺  (merah anggur)\nTitik akhir: [MIn]⁻ + H₂Y²⁻ → [MY]²⁻ + HIn²⁻  (biru)"),
    ],
    "fase": [
        ("EDTA (Na₂H₂Y)", "(aq)", "Ligan heksadentat, terlarut"),
        ("[CaY]²⁻, [MgY]²⁻", "(aq)", "Kompleks stabil, larutan"),
        ("EBT (HIn²⁻)", "(aq)", "Merah anggur (kompleks M), biru (bebas)"),
        ("Murexide", "(aq)", "Merah (Ca-kompleks) → ungu (titik akhir)"),
        ("CaCO₃", "(s)", "Padatan baku primer"),
    ],
    "bagan": [
        "Standarisasi: Larutkan CaCO₃ baku dalam HCl encer, netralkan, labu takar 250 mL",
        "Pipet 25 mL larutan CaCO₃ ke Erlenmeyer",
        "Tambahkan 2 mL buffer pH 10 dan sedikit EBT (spatula kecil / 3 tetes)",
        "Larutan berwarna merah anggur (Ca²⁺/Mg²⁺ terkompleks EBT)",
        "Titrasi dengan EDTA 0.01 M dari buret, teteskan perlahan",
        "Titik akhir: warna merah anggur → biru murni",
        "Untuk Ca²⁺ selektif: ganti buffer pH 12 + indikator Murexide",
        "Hitung M_EDTA dari standarisasi",
        "Analisis sampel: ulangi prosedur di atas dengan sampel air/logam",
    ],
    "rumus": [
        ("Rasio Reaksi", "M_logam : M_EDTA = 1 : 1"),
        ("mmol Logam", "mmol = M_EDTA × V_EDTA (mL)"),
        ("Kadar Logam (mg/L)", "= M_EDTA × V_EDTA(mL) × BM_logam × 1000 / V_sampel(mL)"),
        ("Kesadahan Total (mg/L CaCO₃)", "= M_EDTA × V_EDTA × 100 × 1000 / V_sampel"),
        ("Kesadahan (°dH Jerman)", "1 °dH = 10 mg/L CaO = 17.8 mg/L CaCO₃"),
    ],
    "kadar_teoritis": [
        ("Ca²⁺ dalam CaCO₃ murni", 40.04),
        ("Mg²⁺ dalam MgSO₄·7H₂O", 9.86),
        ("Zn²⁺ dalam ZnSO₄·7H₂O", 22.74),
        ("Cu²⁺ dalam CuSO₄·5H₂O", 25.45),
    ],
},

"Pengendapan": {
    "warna": "#ffcc80",
    "emoji": "🌊",
    "deskripsi": "Berdasarkan pembentukan endapan sukar larut antara ion analit dan titran (umumnya AgNO₃).",
    "subtipe": ["Metode Mohr (langsung)", "Metode Volhard (tidak langsung)", "Metode Fajans (adsorpsi)"],
    "indikator": {
        "K₂CrO₄ (Mohr)": "Kuning → endapan merah bata Ag₂CrO₄ (pH 6.5–9)",
        "Fe³⁺ / alum besi (Volhard)": "Tak berwarna → [FeSCN]²⁺ merah",
        "Fluorescein (Fajans)": "Kuning → merah/pink (adsorpsi pada AgCl)",
        "Eosin (Fajans)": "Kuning → merah muda (Br⁻, I⁻, SCN⁻)",
    },
    "alat": [
        "Buret 50 mL",
        "Pipet volumetri 25 mL",
        "Labu Erlenmeyer coklat (lindungi dari cahaya)",
        "Labu takar 250 mL",
        "Kertas lakmus / pH meter",
        "Botol semprot aquades",
    ],
    "bahan": [
        "AgNO₃ 0.1 N (baku sekunder, BM=169.87)",
        "NaCl pro analysis (baku primer, kering 110°C, BM=58.44)",
        "K₂CrO₄ 5% (indikator Mohr)",
        "Fe₂(SO₄)₃ atau ferri ammonium alum 25% (Volhard)",
        "NH₄SCN 0.1 N (Volhard)",
        "Fluorescein / Eosin (Fajans)",
        "HNO₃ encer (pengasaman sampel, Volhard)",
        "Sampel: air laut, garam dapur, air sungai",
    ],
    "reaksi": [
        ("Argentometri – Presipitasi Klorida",
         "Ag⁺(aq) + Cl⁻(aq) → AgCl(s)↓  Ksp = 1.8×10⁻¹⁰  (putih)"),
        ("Metode Mohr – Indikator K₂CrO₄",
         "Ag⁺(aq) + Cl⁻(aq) → AgCl(s)↓  [selama Cl⁻ ada]\n2Ag⁺(aq) + CrO₄²⁻(aq) → Ag₂CrO₄(s)↓  [titik akhir, merah bata]"),
        ("Metode Volhard – Titrasi Tidak Langsung",
         "Ag⁺(kelebihan) + Cl⁻ → AgCl(s)↓\nAg⁺(sisa) + SCN⁻ → AgSCN(s)↓  (putih)\nFe³⁺ + SCN⁻ → [FeSCN]²⁺(aq)  (merah, titik akhir)"),
        ("Argentometri – Br⁻ dan I⁻",
         "Ag⁺ + Br⁻ → AgBr(s)↓  Ksp = 5.2×10⁻¹³  (kuning pucat)\nAg⁺ + I⁻ → AgI(s)↓   Ksp = 8.5×10⁻¹⁷  (kuning)"),
    ],
    "fase": [
        ("AgCl", "(s)", "Endapan putih, Ksp = 1.8×10⁻¹⁰"),
        ("AgBr", "(s)", "Endapan kuning pucat, Ksp = 5.2×10⁻¹³"),
        ("AgI", "(s)", "Endapan kuning, Ksp = 8.5×10⁻¹⁷"),
        ("Ag₂CrO₄", "(s)", "Endapan merah bata (titik akhir Mohr)"),
        ("AgNO₃", "(aq)", "Larutan bening, titran"),
        ("[FeSCN]²⁺", "(aq)", "Kompleks merah (titik akhir Volhard)"),
    ],
    "bagan": [
        "Standarisasi AgNO₃: timbang NaCl baku (kering 110°C), larutkan dalam labu takar",
        "Pipet 25.00 mL NaCl baku ke Erlenmeyer, atur pH 7–9",
        "Tambahkan 1 mL K₂CrO₄ 5% (indikator Mohr)",
        "Titrasi dengan AgNO₃ dari buret, aduk konstan",
        "AgCl putih mengendap selama titrasi",
        "Titik akhir: endapan merah bata Ag₂CrO₄ permanen",
        "Hitung N_AgNO₃ = (m_NaCl × 1000) / (BE_NaCl × V_AgNO₃)",
        "Blanko: titrasi aquades + indikator, catat V_blanko",
        "Analisis sampel: % Cl⁻ = N×(V-V_blanko)×35.45/(1000×m)×100%",
    ],
    "rumus": [
        ("Normalitas AgNO₃", "N = (m_NaCl × 1000) / (58.44 × V_AgNO₃)"),
        ("% Cl⁻ dalam Sampel", "% Cl⁻ = (N_AgNO₃ × V_netto × 35.45) / (1000 × m_sampel) × 100%"),
        ("Metode Volhard – V AgNO₃ berlebih", "V_Ag(kelebihan) = V_Ag_total – V_SCN × (N_SCN/N_Ag)"),
        ("Ksp – Kelarutan AgCl", "Ksp = [Ag⁺][Cl⁻] = 1.8×10⁻¹⁰"),
        ("Molaritas AgNO₃ dari massa", "M = m(g) / (BM × V_L)"),
    ],
    "kadar_teoritis": [
        ("Cl⁻ dalam NaCl murni", 60.66),
        ("Cl⁻ dalam KCl murni", 47.55),
        ("NaCl dalam air laut (~3.5%)", 3.5),
        ("Ag dalam AgNO₃ murni", 63.50),
    ],
},
}

─────────────────────────────────────────────
SIDEBAR
─────────────────────────────────────────────
st.sidebar.markdown("## ⚗ Titrimetri") st.sidebar.markdown("---")

menu = st.sidebar.radio( "Navigasi", ["🏠 Beranda", "📚 Jenis & Deskripsi", "🔧 Alat & Bahan", "🧮 Rumus & Formula", "⚗ Reaksi & Fasa", "📋 Bagan Kerja", "📊 Analisis & Kadar", "🖩 Kalkulator Titrasi"], )

st.sidebar.markdown("---") st.sidebar.markdown("Filter Jenis Titrasi") jenis_selected = st.sidebar.selectbox( "Pilih Jenis", list(DATA.keys()), label_visibility="collapsed", )

st.sidebar.markdown("---") st.sidebar.markdown( "Sistem Informasi Titrimetri
Kimia Analitik Kuantitatif", unsafe_allow_html=True )

d = DATA[jenis_selected]

─────────────────────────────────────────────
HELPER FUNCTIONS
─────────────────────────────────────────────
def badge(text, color): return f"{text}"

def info_card(title, content, color, icon="ℹ️"): st.markdown(f"""

{icon} {title}

{content}""", unsafe_allow_html=True)
def formula_card(label, formula): st.markdown(f"""

{label}

{formula}
""", unsafe_allow_html=True)
def reaction_card(rtype, rxn, color="#f06292"): st.markdown(f"""

{rtype}

{rxn.replace(chr(10),'

')}
""", unsafe_allow_html=True)
─────────────────────────────────────────────
HALAMAN
─────────────────────────────────────────────
if menu == "🏠 Beranda": st.markdown("""

⚗ Sistem Informasi Titrimetri
Referensi lengkap kimia analitik kuantitatif — jenis, alat, rumus, reaksi, fasa, bagan kerja, dan analisis hasil

""", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
for col, (k, v) in zip([col1,col2,col3,col4], DATA.items()):
    with col:
        st.markdown(f"""
        <div style='background:#111827;border:1px solid #2a3a5c;border-top:3px solid {v["warna"]};
        border-radius:12px;padding:1.2rem;text-align:center;'>
        <div style='font-size:2rem'>{v["emoji"]}</div>
        <b style='color:{v["warna"]}'>{k}</b>
        <p style='font-size:.82rem;color:#8899bb;margin-top:.5rem'>{v["deskripsi"][:80]}...</p>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.info("🔎 Gunakan **sidebar** untuk navigasi ke topik dan memilih jenis titrasi.")

st.markdown("### Tentang Titrimetri")
c1,c2 = st.columns(2)
with c1:
    st.markdown("""
    **Titrimetri** adalah metode analisis kimia kuantitatif yang menentukan konsentrasi suatu analit
    dengan cara menambahkan larutan baku (titran) yang konsentrasinya sudah diketahui secara tepat,
    hingga tercapai titik ekivalen.

    **Persyaratan titrasi yang baik:**
    - Reaksi berlangsung cepat dan kuantitatif
    - Stoikiometri reaksi harus jelas
    - Ada cara deteksi titik akhir yang tepat
    - Tidak ada reaksi samping yang mengganggu
    """)
with c2:
    st.markdown("""
    **4 Jenis Utama:**

    | Jenis | Dasar Reaksi | Contoh Titran |
    |---|---|---|
    | Asam–Basa | Netralisasi H⁺/OH⁻ | NaOH, HCl |
    | Redoks | Transfer elektron | KMnO₄, Na₂S₂O₃ |
    | Kompleksometri | Pembentukan kelat | EDTA |
    | Pengendapan | Endapan sukar larut | AgNO₃ |
    """)
elif menu == "📚 Jenis & Deskripsi": color = d["warna"] st.markdown(f"# {d['emoji']} Titrasi {jenis_selected}") st.markdown(f"{d['deskripsi']}", unsafe_allow_html=True) st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📌 Subtipe / Variasi")
    for s in d["subtipe"]:
        st.markdown(f"- {s}")

with col2:
    st.markdown("### 🎨 Indikator")
    for nama, keterangan in d["indikator"].items():
        st.markdown(f"""
        <div style='background:#1c2740;border:1px solid #2a3a5c;border-radius:8px;
        padding:.6rem 1rem;margin-bottom:.5rem;'>
        <b style='color:{color}'>{nama}</b><br>
        <small style='color:#aac'>{keterangan}</small>
        </div>""", unsafe_allow_html=True)
elif menu == "🔧 Alat & Bahan": color = d["warna"] st.markdown(f"# 🔧 Alat & Bahan — Titrasi {jenis_selected}") st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.markdown(f"### 🔧 Alat Laboratorium")
    for a in d["alat"]:
        st.markdown(f"- {a}")

with col2:
    st.markdown(f"### 🧪 Bahan & Reagen")
    for b in d["bahan"]:
        st.markdown(f"- {b}")

st.markdown("---")
st.markdown("### 💡 Catatan Penting")
catatan = {
    "Asam–Basa": "Gunakan aquades bebas CO₂ untuk mencegah gangguan pada titrasi dengan indikator PP. Buret harus dibilas dengan NaOH sebelum diisi.",
    "Redoks": "KMnO₄ dapat merusak karet pada buret — gunakan buret coklat dengan ujung kaca. Saring KMnO₄ untuk menghilangkan MnO₂ sebelum standarisasi.",
    "Kompleksometri": "EDTA membentuk endapan dengan beberapa logam pada pH rendah. Selalu atur pH dengan buffer yang tepat sesuai analit target.",
    "Pengendapan": "Lindungi larutan AgNO₃ dari cahaya (gunakan botol/buret coklat). Metode Mohr tidak cocok untuk Br⁻, I⁻, CN⁻ karena pembentukan Ag₂CrO₄ terganggu.",
}
st.info(catatan.get(jenis_selected, ""))
elif menu == "🧮 Rumus & Formula": color = d["warna"] st.markdown(f"# 🧮 Rumus Titrasi {jenis_selected}") st.markdown("---")

for label, rumus in d["rumus"]:
    formula_card(label, rumus)

st.markdown("---")
st.markdown("### 📐 Rumus Universal Titrasi")
formula_card("Kesetaraan normalitas", "N₁ × V₁ = N₂ × V₂")
formula_card("% Kadar Umum", "% = (N_titran × V_titran × BE_analit) / (1000 × m_sampel) × 100%")
formula_card("Berat Ekivalen (BE)", "BE = BM / valensi (faktor ekivalen)")
formula_card("Molaritas dari massa", "M = massa(g) × 1000 / (BM × V_mL)")

with st.expander("📖 Penjelasan Variabel"):
    st.markdown("""
    | Simbol | Keterangan | Satuan |
    |---|---|---|
    | N | Normalitas larutan | ekivalen/L (N) |
    | M | Molaritas larutan | mol/L (M) |
    | V | Volume larutan | mL |
    | BE | Berat ekivalen | g/ekivalen |
    | BM | Berat molekul | g/mol |
    | m | Massa sampel | gram |
    | val | Valensi / faktor ekivalen | – |
    """)
elif menu == "⚗ Reaksi & Fasa": color = d["warna"] st.markdown(f"# ⚗ Reaksi Kimia & Fasa — Titrasi {jenis_selected}") st.markdown("---")

st.markdown("### Persamaan Reaksi")
for rtype, rxn in d["reaksi"]:
    reaction_card(rtype, rxn, color)

st.markdown("---")
st.markdown("### Fasa Zat dalam Titrasi")
tabel_fase = {"Zat": [], "Fasa": [], "Keterangan": []}
for zat, fasa, ket in d["fase"]:
    tabel_fase["Zat"].append(zat)
    tabel_fase["Fasa"].append(fasa)
    tabel_fase["Keterangan"].append(ket)

import pandas as pd
df_fase = pd.DataFrame(tabel_fase)
st.dataframe(df_fase, use_container_width=True, hide_index=True)

st.markdown("---")
st.markdown("### 📖 Notasi Fasa")
col1,col2,col3,col4 = st.columns(4)
col1.metric("(aq)", "Terlarut dalam air")
col2.metric("(s)", "Padatan / endapan")
col3.metric("(l)", "Cair murni (seperti H₂O)")
col4.metric("(g)", "Gas")
elif menu == "📋 Bagan Kerja": color = d["warna"] st.markdown(f"# 📋 Bagan Kerja — Titrasi {jenis_selected}") st.markdown("---")

for i, langkah in enumerate(d["bagan"], 1):
    if i < len(d["bagan"]):
        st.markdown(f"""
        <div style='background:#111827;border:1px solid {color}55;border-radius:12px;
        padding:1rem 1.5rem;margin-bottom:.5rem;display:flex;gap:1rem;align-items:flex-start;'>
        <div style='background:{color}22;color:{color};border-radius:50%;width:30px;height:30px;
        display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0;'>{i}</div>
        <div style='color:#e8edf5;padding-top:.2rem'>{langkah}</div>
        </div>
        <div style='text-align:center;font-size:1.2rem;color:#2a3a5c;margin:0;'>↓</div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style='background:{color}22;border:1px solid {color}88;border-radius:12px;
        padding:1rem 1.5rem;margin-bottom:.5rem;display:flex;gap:1rem;align-items:flex-start;'>
        <div style='background:{color};color:#0a0e1a;border-radius:50%;width:30px;height:30px;
        display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0;'>✓</div>
        <div style='color:{color};font-weight:600;padding-top:.2rem'>{langkah}</div>
        </div>
        """, unsafe_allow_html=True)
elif menu == "📊 Analisis & Kadar": color = d["warna"] st.markdown(f"# 📊 Analisis Hasil & Kadar Teoritis — {jenis_selected}") st.markdown("---")

st.markdown("### 📐 Kadar Teoritis Analit")
import pandas as pd
df_teoritis = pd.DataFrame(d["kadar_teoritis"], columns=["Senyawa / Sampel", "Kadar Teoritis (%)"])
st.dataframe(df_teoritis, use_container_width=True, hide_index=True)

st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🎯 Akurasi & Presisi")
    info_card("% Recovery", "% Recovery = (C_terukur / C_teoritis) × 100%<br>Kriteria baik: 98–102%", color, "🎯")
    info_card("RSD (Relative Std Deviation)", "RSD = (SD / rata-rata) × 100%<br>Kriteria baik: RSD < 2%", color, "📉")
with col2:
    st.markdown("### ⚠️ Sumber Kesalahan")
    kesalahan = {
        "Asam–Basa": ["Aquades mengandung CO₂", "Pembacaan buret paralaks", "Indikator berlebih (terlalu banyak tetes)", "NaOH menyerap CO₂ dari udara", "Titik akhir terlewat (terlalu pink)"],
        "Redoks": ["KMnO₄ terurai oleh cahaya/panas", "Suhu terlalu rendah (reaksi lambat)", "Amilum ditambah terlalu awal (iodometri)", "Oksidasi I⁻ oleh udara sebelum titrasi"],
        "Kompleksometri": ["pH tidak tepat → kompleks tidak sempurna", "Gangguan ion pengganggu (Al³⁺, Fe³⁺)", "Indikator terdegradasi (EBT lama)", "Kelebihan inhibitor mengganggu"],
        "Pengendapan": ["AgNO₃ terurai oleh cahaya (fotolisis)", "pH di luar range Mohr (6.5–9)", "Adsorpsi berlebih pada endapan (Fajans)", "Blanko tidak dikoreksi"],
    }
    for k in kesalahan.get(jenis_selected, []):
        st.markdown(f"- ⚠️ {k}")

st.markdown("---")
st.markdown("### 📈 Interpretasi Hasil")
st.markdown("""
| % Recovery | Interpretasi |
|---|---|
| < 90% | Hasil rendah — kemungkinan analit hilang atau reaksi tidak sempurna |
| 90–97% | Dapat diterima untuk analisis rutin dengan koreksi |
| 98–102% | **Baik** — memenuhi kriteria presisi dan akurasi |
| 103–110% | Hasil tinggi — kemungkinan kontaminasi atau interferensi |
| > 110% | Tidak dapat diterima — periksa prosedur dan reagen |
""")
elif menu == "🖩 Kalkulator Titrasi": st.markdown("# 🖩 Kalkulator Titrasi") st.markdown("Hitung kadar analit berdasarkan data titrasi secara otomatis.") st.markdown("---")

col_in, col_out = st.columns([1, 1])

with col_in:
    st.markdown("### ⚙️ Input Data")
    jenis_kal = st.selectbox("Jenis Titrasi", list(DATA.keys()))
    color_kal = DATA[jenis_kal]["warna"]

    analit_opts = {
        "Asam–Basa": [
            ("Asam asetat (CH₃COOH)", 60.05, 1),
            ("NaOH", 40.00, 1),
            ("HCl", 36.46, 1),
            ("H₂SO₄", 98.08, 2),
            ("H₂C₂O₄ (asam oksalat)", 90.03, 2),
        ],
        "Redoks": [
            ("Fe²⁺ (besi(II))", 55.85, 1),
            ("H₂O₂ (hidrogen peroksida)", 34.01, 2),
            ("KMnO₄ (permanganat)", 158.03, 5),
            ("Na₂C₂O₄ (natrium oksalat)", 134.00, 2),
        ],
        "Kompleksometri": [
            ("Ca²⁺ (kalsium)", 40.08, 2),
            ("Mg²⁺ (magnesium)", 24.31, 2),
            ("Zn²⁺ (seng)", 65.38, 2),
            ("Cu²⁺ (tembaga)", 63.55, 2),
            ("CaCO₃ (sebagai kesadahan)", 100.09, 2),
        ],
        "Pengendapan": [
            ("Cl⁻ (klorida)", 35.45, 1),
            ("Br⁻ (bromida)", 79.90, 1),
            ("I⁻ (iodida)", 126.90, 1),
            ("SCN⁻ (tiosianat)", 58.08, 1),
        ],
    }

    opts = analit_opts[jenis_kal]
    opt_labels = [o[0] for o in opts] + ["Custom..."]
    analit_choice = st.selectbox("Analit", opt_labels)

    if analit_choice == "Custom...":
        bm = st.number_input("BM Analit (g/mol)", min_value=1.0, value=60.05, step=0.01)
        val = st.number_input("Valensi / Faktor Ekivalen", min_value=1, value=1)
    else:
        bm = next(o[1] for o in opts if o[0]==analit_choice)
        val = next(o[2] for o in opts if o[0]==analit_choice)
        st.info(f"BM = {bm} g/mol | Valensi = {val} | BE = {bm/val:.4f} g/ekivalen")

    N_titran = st.number_input("Konsentrasi Titran (N)", min_value=0.0001, value=0.1, step=0.0001, format="%.4f")
    V_titran = st.number_input("Volume Titran (mL)", min_value=0.01, value=20.50, step=0.01)
    m_sampel = st.number_input("Massa Sampel (g)", min_value=0.0001, value=0.2500, step=0.0001, format="%.4f")
    f_pengenceran = st.number_input("Faktor Pengenceran", min_value=0.01, value=1.0, step=0.1)

    hitung = st.button("🧮 Hitung Kadar", use_container_width=True, type="primary")

with col_out:
    st.markdown("### 📊 Hasil Perhitungan")
    if hitung:
        BE = bm / val
        mmol_titran = N_titran * V_titran
        mg_analit = mmol_titran * BE * f_pengenceran
        persen = (N_titran * V_titran * BE * f_pengenceran) / (1000 * m_sampel) * 100

        st.markdown(f"""
        <div style='background:#0d1b2e;border:1px solid {color_kal}55;border-radius:14px;padding:1.5rem;margin-bottom:1rem;'>
        <div style='color:#8899bb;font-size:.8rem;text-transform:uppercase;letter-spacing:.1em'>Kadar Analit</div>
        <div style='color:{color_kal};font-family:DM Mono,monospace;font-size:2.2rem;font-weight:700;margin:.3rem 0'>
        {persen:.4f} %</div>
        <div style='color:#c8d8e8;font-size:.85rem'>{mg_analit:.3f} mg analit dalam sampel</div>
        </div>""", unsafe_allow_html=True)

        st.markdown("**Rincian Perhitungan:**")
        langkah = {
            "BE (Berat Ekivalen)": f"{bm}/{val} = {BE:.4f} g/ekivalen",
            "mEkivalen titran": f"{N_titran} N × {V_titran} mL = {mmol_titran:.4f} mEkivalen",
            "mg analit": f"{mmol_titran:.4f} × {BE:.4f} × {f_pengenceran} = {mg_analit:.4f} mg",
            "% Kadar": f"({mg_analit:.4f}) / ({m_sampel}×1000) × 100 = {persen:.4f} %",
        }
        for k, v in langkah.items():
            st.code(f"{k}: {v}", language=None)

        # Bandingkan dengan kadar teoritis
        st.markdown("**Perbandingan dengan Kadar Teoritis:**")
        teoritis_options = d["kadar_teoritis"]
        if teoritis_options:
            kadar_ref = teoritis_options[0][1]
            recovery = persen / kadar_ref * 100 if kadar_ref > 0 else None
            if recovery:
                warna_rec = "#aed581" if 98 <= recovery <= 102 else ("#ffcc80" if 90 <= recovery <= 110 else "#f06292")
                st.markdown(f"Kadar teoritis referensi: **{kadar_ref}%**")
                st.markdown(f"<span style='color:{warna_rec}'>% Recovery = {recovery:.2f}%</span>", unsafe_allow_html=True)
    else:
        st.markdown(
            "<div style='color:#8899bb;text-align:center;padding:3rem;border:1px dashed #2a3a5c;border-radius:12px;'>"
            "Isi input di sebelah kiri, lalu klik <b>Hitung Kadar</b></div>",
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.markdown("### 📋 Ringkasan Rumus")
    formula_card("Rumus Umum", "% = (N × V × BE) / (1000 × m_sampel) × 100%")
    formula_card("BE Analit", f"BE = {bm}/{val} = {bm/val:.4f} g/ekivalen" if hitung else "BE = BM / valensi")
