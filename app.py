import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt
import base64
from pathlib import Path

from simulation import run_sequential, run_parallel


# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Monte Carlo Battle RPG",
    page_icon="⚔️",
    layout="wide"
)


# =========================
# DATA KARAKTER FIXED
# =========================
PLAYER_A = {
    "name": "Reaper",
    "label": "Karakter A",
    "role": "Dark Gunslinger",
    "hp": 110,
    "min_attack": 9,
    "max_attack": 20,
    "crit_rate": 0.22,
    "image": "assets/reaper.png",
}

PLAYER_B = {
    "name": "Cyber Mage",
    "label": "Karakter B",
    "role": "Arcane Tech Assassin",
    "hp": 95,
    "min_attack": 11,
    "max_attack": 22,
    "crit_rate": 0.18,
    "image": "assets/cyber_mage.png",
}


# =========================
# HELPER GAMBAR
# =========================
def image_to_base64(image_path):
    path = Path(image_path)

    if not path.exists():
        st.error(f"File gambar tidak ditemukan: {path.resolve()}")
        return None

    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def get_mime_type(image_path):
    ext = Path(image_path).suffix.lower()

    if ext == ".png":
        return "image/png"
    elif ext in [".jpg", ".jpeg"]:
        return "image/jpeg"
    elif ext == ".webp":
        return "image/webp"

    return "image/png"


# =========================
# GLOBAL STYLE
# =========================
st.markdown(
    """
    <style>
    .note-box {
    background: rgba(29, 78, 216, 0.18);
    border: 1px solid rgba(59, 130, 246, 0.22);
    border-radius: 16px;
    padding: 14px 16px;
    color: #bfdbfe;
    font-size: 15px;
    margin-top: 16px;
}
    .settings-wrapper {
    background: rgba(15, 23, 42, 0.78);
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 24px;
    padding: 22px 24px 18px 24px;
    margin-top: 10px;
    margin-bottom: 18px;
    box-shadow: 0 14px 30px rgba(0,0,0,0.25);
}

.settings-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 6px;
}

.settings-icon {
    width: 50px;
    height: 50px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    background: linear-gradient(135deg, rgba(124, 58, 237, 0.95), rgba(236, 72, 153, 0.95));
    box-shadow: 0 10px 20px rgba(124, 58, 237, 0.25);
}

.settings-title {
    font-size: 30px;
    font-weight: 900;
    color: #facc15;
    margin: 0;
    line-height: 1.1;
}

.settings-subtitle {
    color: #cbd5e1;
    font-size: 14px;
    margin-top: 4px;
    margin-bottom: 0;
}

.settings-info-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-top: 18px;
    margin-bottom: 10px;
}

.settings-info-card {
    background: rgba(30, 41, 59, 0.85);
    border: 1px solid rgba(148, 163, 184, 0.16);
    border-radius: 16px;
    padding: 12px 14px;
}

.settings-info-title {
    color: #94a3b8;
    font-size: 12px;
    margin-bottom: 4px;
}

.settings-info-value {
    color: #f8fafc;
    font-size: 16px;
    font-weight: 800;
}

div[data-testid="stSelectbox"] label {
    color: #e2e8f0 !important;
    font-weight: 700 !important;
    font-size: 15px !important;
}

div[data-testid="stSelectbox"] > div {
    border-radius: 16px !important;
}

div[data-testid="stSelectbox"] [data-baseweb="select"] {
    background: rgba(15, 23, 42, 0.95) !important;
    border: 1px solid rgba(148, 163, 184, 0.20) !important;
    border-radius: 16px !important;
    min-height: 54px !important;
}

div[data-testid="stSelectbox"] [data-baseweb="select"] > div {
    color: white !important;
    font-weight: 600 !important;
}

.run-button-wrap {
    margin-top: 8px;
    margin-bottom: 12px;
}

div.stButton > button {
    background: linear-gradient(90deg, #7c3aed, #ec4899, #f59e0b);
    color: white;
    border: none;
    border-radius: 18px;
    font-size: 20px;
    font-weight: 900;
    padding: 0.95rem 1.4rem;
    box-shadow: 0 10px 24px rgba(236, 72, 153, 0.28);
    width: 100%;
}

div.stButton > button:hover {
    transform: translateY(-1px);
    color: white;
    border: none;
}

.note-box {
    background: rgba(29, 78, 216, 0.18);
    border: 1px solid rgba(59, 130, 246, 0.22);
    border-radius: 16px;
    padding: 14px 16px;
    color: #bfdbfe;
    font-size: 15px;
    margin-top: 10px;
}

@media screen and (max-width: 900px) {
    .settings-info-grid {
        grid-template-columns: 1fr;
    }

    .settings-title {
        font-size: 24px;
    }
}
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(124, 58, 237, 0.30), transparent 35%),
            radial-gradient(circle at top right, rgba(236, 72, 153, 0.24), transparent 35%),
            linear-gradient(135deg, #070b16 0%, #111827 50%, #1e1b4b 100%);
        color: white;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1450px;
    }

    .main-title {
        text-align: center;
        font-size: 44px;
        font-weight: 900;
        color: #facc15;
        margin-bottom: 5px;
        text-shadow: 0 0 18px rgba(250, 204, 21, 0.38);
    }

    .sub-title {
        text-align: center;
        font-size: 16px;
        color: #d1d5db;
        margin-bottom: 32px;
    }

    .vs-box {
        display: flex;
        height: 625px;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }

    .vs-circle {
        width: 120px;
        height: 120px;
        border-radius: 999px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(15, 23, 42, 0.92);
        border: 1px solid rgba(239, 68, 68, 0.50);
        box-shadow: 0 0 30px rgba(239, 68, 68, 0.35);
    }

    .vs-text {
        font-size: 50px;
        font-weight: 1000;
        color: #ef4444;
        text-shadow: 0 0 22px rgba(239, 68, 68, 0.65);
    }

    .vs-sub {
        color: #cbd5e1;
        font-size: 13px;
        margin-top: 12px;
        text-align: center;
    }

    .section-title {
        font-size: 25px;
        font-weight: 900;
        color: #facc15;
        margin-top: 28px;
        margin-bottom: 15px;
    }

    .setting-card {
        background: rgba(15, 23, 42, 0.92);
        border: 1px solid rgba(148, 163, 184, 0.22);
        border-radius: 22px;
        padding: 22px;
        box-shadow: 0 12px 28px rgba(0,0,0,0.32);
        margin-bottom: 16px;
    }

    .metric-card {
        background: rgba(15, 23, 42, 0.95);
        border: 1px solid rgba(56, 189, 248, 0.40);
        border-radius: 18px;
        padding: 18px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.30);
        min-height: 110px;
    }

    .metric-value {
        font-size: 29px;
        font-weight: 900;
        color: #38bdf8;
    }

    .metric-label {
        font-size: 14px;
        color: #cbd5e1;
        margin-top: 4px;
    }

    div.stButton > button {
        background: linear-gradient(90deg, #7c3aed, #ec4899, #facc15);
        color: white;
        border: none;
        border-radius: 16px;
        font-size: 19px;
        font-weight: 900;
        width: 100%;
        padding: 0.85rem 1rem;
        box-shadow: 0 10px 26px rgba(236, 72, 153, 0.25);
    }

    div.stButton > button:hover {
        color: white;
        border: none;
        transform: scale(1.01);
    }

    @media screen and (max-width: 900px) {
        .main-title {
            font-size: 32px;
        }

        .vs-box {
            height: 160px;
        }

        .vs-circle {
            width: 90px;
            height: 90px;
        }

        .vs-text {
            font-size: 36px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================
# HELPER UI
# =========================
def show_character_card(player):
    image_base64 = image_to_base64(player["image"])

    if image_base64 is None:
        return

    mime_type = get_mime_type(player["image"])

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
        
        body {{
            margin: 0;
            padding: 0;
            background: transparent;
            font-family: Arial, sans-serif;
        }}

        .character-card {{
            background: rgba(15, 23, 42, 0.96);
            border: 1px solid rgba(250, 204, 21, 0.45);
            border-radius: 26px;
            padding: 20px 28px;
            box-shadow: 0 18px 40px rgba(0,0,0,0.45);
            height: 610px;
            color: white;
            overflow: hidden;
            position: relative;
            box-sizing: border-box;
        }}

        .character-card::before {{
            content: "";
            position: absolute;
            top: -65px;
            right: -65px;
            width: 160px;
            height: 160px;
            background: rgba(250, 204, 21, 0.12);
            border-radius: 50%;
        }}

        .character-card::after {{
            content: "";
            position: absolute;
            bottom: -70px;
            left: -70px;
            width: 180px;
            height: 180px;
            background: rgba(56, 189, 248, 0.08);
            border-radius: 50%;
        }}

        .content {{
            position: relative;
            z-index: 2;
            height: 100%;
        }}

        .character-label {{
            text-align: center;
            font-size: 13px;
            font-weight: 800;
            color: #38bdf8;
            letter-spacing: 1.3px;
            text-transform: uppercase;
            margin-bottom: 4px;
        }}

        .character-name {{
            text-align: center;
            font-size: 29px;
            font-weight: 900;
            color: #facc15;
            margin-bottom: 3px;
        }}

        .character-role {{
            text-align: center;
            font-size: 13px;
            color: #cbd5e1;
            margin-bottom: 10px;
        }}

        .image-box {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 210px;
            margin-bottom: 14px;
        }}

        .character-image {{
            width: 205px;
            max-width: 100%;
            max-height: 205px;
            object-fit: contain;
            image-rendering: pixelated;
            filter: drop-shadow(0 16px 22px rgba(0, 0, 0, 0.55));
        }}

        .stat-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 10px;
        }}

        .stat-item {{
            background: rgba(30, 41, 59, 0.95);
            border: 1px solid rgba(148, 163, 184, 0.22);
            border-radius: 16px;
            padding: 11px 16px;
            box-sizing: border-box;
            min-height: 82px;
        }}

        .stat-title {{
            color: #94a3b8;
            font-size: 13px;
            margin-bottom: 5px;
        }}

        .stat-value {{
            color: #f8fafc;
            font-size: 20px;
            font-weight: 900;
            line-height: 1.15;
        }}
        
        </style>
    </head>

    <body>
        <div class="character-card">
            <div class="content">
                <div class="character-label">{player["label"]}</div>
                <div class="character-name">{player["name"]}</div>
                <div class="character-role">{player["role"]}</div>

                <div class="image-box">
                    <img
                        class="character-image"
                        src="data:{mime_type};base64,{image_base64}"
                        alt="{player["name"]}"
                    />
                </div>

                <div class="stat-grid">
                    <div class="stat-item">
                        <div class="stat-title">💖 Health Point</div>
                        <div class="stat-value">{player["hp"]} HP</div>
                    </div>

                    <div class="stat-item">
                        <div class="stat-title">⚔️ Attack Range</div>
                        <div class="stat-value">{player["min_attack"]} - {player["max_attack"]} Damage</div>
                    </div>

                    <div class="stat-item">
                        <div class="stat-title">💥 Critical Hit Rate</div>
                        <div class="stat-value">{int(player["crit_rate"] * 100)}%</div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    components.html(html, height=625)


def show_metric(label, value):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================
# HEADER
# =========================
st.markdown(
    '<div class="main-title">⚔️ Monte Carlo Battle RPG Simulator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Analisis Peluang Kemenangan dan Performa Parallel Computing</div>',
    unsafe_allow_html=True
)


# =========================
# KARAKTER A VS B
# =========================
col_a, col_vs, col_b = st.columns([4.5, 1.2, 4.5])

with col_a:
    show_character_card(PLAYER_A)

with col_vs:
    st.markdown(
        """
        <div class="vs-box">
            <div class="vs-circle">
                <div class="vs-text">VS</div>
            </div>
            <div class="vs-sub">Battle Simulation</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_b:
    show_character_card(PLAYER_B)


# =========================
# SETTING SIMULASI
# =========================
# =========================
# PENGATURAN SIMULASI
# =========================
settings_html = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    margin: 0;
    padding: 0;
    background: transparent;
    font-family: Arial, sans-serif;
    color: white;
}

.settings-wrapper {
    background: rgba(15, 23, 42, 0.82);
    border: 1px solid rgba(148, 163, 184, 0.22);
    border-radius: 24px;
    padding: 28px 32px;
    box-shadow: 0 14px 30px rgba(0,0,0,0.28);
    box-sizing: border-box;
}

.settings-header {
    display: flex;
    align-items: center;
    gap: 18px;
    margin-bottom: 24px;
}

.settings-icon {
    width: 62px;
    height: 62px;
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    background: linear-gradient(135deg, #7c3aed, #ec4899);
    box-shadow: 0 10px 22px rgba(236, 72, 153, 0.30);
}

.settings-title {
    font-size: 34px;
    font-weight: 900;
    color: #facc15;
    line-height: 1.1;
}

.settings-subtitle {
    color: #e2e8f0;
    font-size: 16px;
    margin-top: 8px;
}

.settings-info-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
}

.settings-info-card {
    background: rgba(30, 41, 59, 0.92);
    border: 1px solid rgba(148, 163, 184, 0.22);
    border-radius: 18px;
    padding: 18px 20px;
    min-height: 95px;
    box-sizing: border-box;
}

.settings-info-title {
    color: #93c5fd;
    font-size: 14px;
    margin-bottom: 10px;
}

.settings-info-value {
    color: #ffffff;
    font-size: 18px;
    font-weight: 900;
}

@media screen and (max-width: 900px) {
    .settings-info-grid {
        grid-template-columns: 1fr;
    }

    .settings-title {
        font-size: 26px;
    }
}
</style>
</head>

<body>
<div class="settings-wrapper">
    <div class="settings-header">
        <div class="settings-icon">⚙️</div>
        <div>
            <div class="settings-title">Pengaturan Simulasi</div>
            <div class="settings-subtitle">
                Atur jumlah simulasi, mode eksekusi, dan jumlah proses untuk menjalankan Monte Carlo Battle RPG.
            </div>
        </div>
    </div>

    <div class="settings-info-grid">
        <div class="settings-info-card">
            <div class="settings-info-title">🎲 Metode</div>
            <div class="settings-info-value">Monte Carlo Simulation</div>
        </div>

        <div class="settings-info-card">
            <div class="settings-info-title">🧠 Analisis</div>
            <div class="settings-info-value">Sequential vs Parallel</div>
        </div>

        <div class="settings-info-card">
            <div class="settings-info-title">📊 Output</div>
            <div class="settings-info-value">Win Rate, Time, Speedup</div>
        </div>
    </div>
</div>
</body>
</html>
"""

components.html(settings_html, height=260)


set_col1, set_col2, set_col3 = st.columns(3)

with set_col1:
    total_simulations = st.selectbox(
        "🎯 Jumlah Simulasi",
        [10_000, 50_000, 100_000],
        index=2
    )

with set_col2:
    mode = st.selectbox(
        "🧪 Mode Eksekusi",
        ["Sequential", "Parallel"]
    )

with set_col3:
    process_count = st.selectbox(
        "🖥️ Jumlah Proses",
        [1, 2, 4, 8],
        index=0 if mode == "Sequential" else 2
    )

run_button = st.button("🚀 RUN SIMULATION")

st.markdown(
    """
    <div class="note-box">
        💡 <b>Tips:</b> Gunakan mode <b>Parallel</b> dengan 2, 4, atau 8 proses untuk membandingkan
        performa terhadap mode <b>Sequential</b>.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# SESSION STATE
# =========================
if "history" not in st.session_state:
    st.session_state.history = []


# =========================
# JALANKAN SIMULASI
# =========================
if run_button:
    with st.spinner("Simulasi sedang berjalan..."):
        sequential_result = run_sequential(total_simulations, PLAYER_A, PLAYER_B)

        if mode == "Sequential":
            result = sequential_result
            speedup = 1.0
            efficiency = 100.0
            used_process = 1
        else:
            result = run_parallel(total_simulations, process_count, PLAYER_A, PLAYER_B)

            if result["execution_time"] > 0:
                speedup = sequential_result["execution_time"] / result["execution_time"]
            else:
                speedup = 0

            efficiency = (speedup / process_count) * 100
            used_process = process_count

        win_a = result["win_a"]
        win_b = result["win_b"]
        execution_time = result["execution_time"]

        win_rate_a = (win_a / total_simulations) * 100
        win_rate_b = (win_b / total_simulations) * 100

        st.session_state.history.append({
            "Mode": mode,
            "Simulasi": total_simulations,
            "Proses": used_process,
            "Karakter A": PLAYER_A["name"],
            "Karakter B": PLAYER_B["name"],
            "A Wins": win_a,
            "B Wins": win_b,
            "A Win Rate (%)": round(win_rate_a, 2),
            "B Win Rate (%)": round(win_rate_b, 2),
            "Execution Time (s)": round(execution_time, 4),
            "Speedup": round(speedup, 4),
            "Efficiency (%)": round(efficiency, 2),
        })

        st.success("Simulasi selesai!")

st.markdown(
    """
    <style>
    /* =========================
       FORCE DARK SELECTBOX
    ========================= */

    div[data-testid="stSelectbox"] {
        color: white !important;
    }

    div[data-testid="stSelectbox"] label {
        color: #f8fafc !important;
        font-weight: 800 !important;
        font-size: 16px !important;
    }

    div[data-testid="stSelectbox"] > div {
        background: transparent !important;
    }

    div[data-testid="stSelectbox"] div[data-baseweb="select"] {
        background-color: #0f172a !important;
        border: 1px solid rgba(56, 189, 248, 0.45) !important;
        border-radius: 16px !important;
        min-height: 58px !important;
        box-shadow: 0 10px 24px rgba(0, 0, 0, 0.35) !important;
    }

    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        background-color: #0f172a !important;
        color: #ffffff !important;
        border-radius: 16px !important;
    }

    div[data-testid="stSelectbox"] div[data-baseweb="select"] div {
        background-color: #0f172a !important;
        color: #ffffff !important;
    }

    div[data-testid="stSelectbox"] div[data-baseweb="select"] span {
        color: #ffffff !important;
        font-weight: 800 !important;
    }

    div[data-testid="stSelectbox"] input {
        color: #ffffff !important;
        background-color: #0f172a !important;
        font-weight: 800 !important;
    }

    div[data-testid="stSelectbox"] svg {
        fill: #38bdf8 !important;
        color: #38bdf8 !important;
    }

    div[data-testid="stSelectbox"] [role="button"] {
        background-color: #0f172a !important;
        color: white !important;
    }

    /* dropdown list ketika dibuka */
    div[data-baseweb="popover"] {
        background: transparent !important;
    }

    div[data-baseweb="popover"] div {
        background-color: #0f172a !important;
        color: #ffffff !important;
    }

    div[data-baseweb="popover"] ul {
        background-color: #0f172a !important;
        border: 1px solid rgba(56, 189, 248, 0.45) !important;
        border-radius: 14px !important;
        padding: 6px !important;
    }

    div[data-baseweb="popover"] li {
        background-color: #0f172a !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="popover"] li:hover {
        background: linear-gradient(90deg, #7c3aed, #ec4899) !important;
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# HASIL SIMULASI
# =========================
if len(st.session_state.history) > 0:
    latest = st.session_state.history[-1]

    st.markdown('<div class="section-title">📊 Ringkasan Hasil Simulasi</div>', unsafe_allow_html=True)

    m1, m2, m3, m4, m5 = st.columns(5)

    with m1:
        show_metric("Karakter A Win Rate", f"{latest['A Win Rate (%)']}%")

    with m2:
        show_metric("Karakter B Win Rate", f"{latest['B Win Rate (%)']}%")

    with m3:
        show_metric("Execution Time", f"{latest['Execution Time (s)']}s")

    with m4:
        show_metric("Speedup", f"{latest['Speedup']}x")

    with m5:
        show_metric("Efficiency", f"{latest['Efficiency (%)']}%")


    # =========================
    # VISUALISASI HASIL
    # =========================
    st.markdown('<div class="section-title">📈 Visualisasi Hasil</div>', unsafe_allow_html=True)

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.subheader("Persentase Kemenangan")

        fig1, ax1 = plt.subplots(figsize=(6, 4))
        ax1.pie(
            [latest["A Win Rate (%)"], latest["B Win Rate (%)"]],
            labels=[PLAYER_A["name"], PLAYER_B["name"]],
            autopct="%1.2f%%",
            startangle=90
        )
        ax1.axis("equal")
        st.pyplot(fig1)

    with chart_col2:
        st.subheader("Jumlah Kemenangan")

        win_df = pd.DataFrame({
            "Karakter": [PLAYER_A["name"], PLAYER_B["name"]],
            "Menang": [latest["A Wins"], latest["B Wins"]]
        })

        fig2, ax2 = plt.subplots(figsize=(6, 4))
        ax2.bar(win_df["Karakter"], win_df["Menang"])
        ax2.set_xlabel("Karakter")
        ax2.set_ylabel("Jumlah Menang")
        st.pyplot(fig2)


    # =========================
    # RIWAYAT PENGUJIAN
    # =========================
    st.markdown('<div class="section-title">📋 Riwayat Pengujian</div>', unsafe_allow_html=True)

    history_df = pd.DataFrame(st.session_state.history)
    st.dataframe(history_df, use_container_width=True)


    # =========================
    # GRAFIK PERFORMA
    # =========================
    st.markdown('<div class="section-title">⏱️ Grafik Performa</div>', unsafe_allow_html=True)

    perf_col1, perf_col2 = st.columns(2)

    with perf_col1:
        st.subheader("Execution Time per Pengujian")

        fig3, ax3 = plt.subplots(figsize=(6, 4))
        ax3.bar(
            range(1, len(history_df) + 1),
            history_df["Execution Time (s)"]
        )
        ax3.set_xlabel("Pengujian ke-")
        ax3.set_ylabel("Waktu Eksekusi (s)")
        st.pyplot(fig3)

    with perf_col2:
        st.subheader("Speedup per Pengujian")

        fig4, ax4 = plt.subplots(figsize=(6, 4))
        ax4.plot(
            range(1, len(history_df) + 1),
            history_df["Speedup"],
            marker="o"
        )
        ax4.set_xlabel("Pengujian ke-")
        ax4.set_ylabel("Speedup")
        st.pyplot(fig4)

else:
    st.info("Atur parameter simulasi, lalu klik tombol RUN SIMULATION.")