
import streamlit as st
import time
import random

st.set_page_config(
    page_title="Температурен помощник",
    page_icon="🌡️",
    layout="centered"
)

# ---------------- CSS ДИЗАЙН ----------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #141e30, #243b55);
    color: white;
}

h1 {
    text-align: center;
    color: #ffffff;
    font-size: 42px !important;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 30px;
}

.main-card {
    background: rgba(255,255,255,0.10);
    padding: 30px;
    border-radius: 25px;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 8px 30px rgba(0,0,0,0.25);
    text-align: center;
}

.result {
    font-size: 25px;
    font-weight: bold;
    margin-top: 15px;
    animation: appear 1s ease;
}

.big-icon {
    font-size: 90px;
    animation: float 2s infinite ease-in-out;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-15px); }
    100% { transform: translateY(0px); }
}

@keyframes appear {
    from {
        opacity: 0;
        transform: scale(0.7);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

.stButton button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 15px;
    border: none;
    padding: 12px 35px;
    font-size: 18px;
    font-weight: bold;
    width: 100%;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.04);
    box-shadow: 0 0 20px #00c6ff;
}

</style>
""", unsafe_allow_html=True)


# ---------------- ЗАГЛАВИЕ ----------------

st.title("🌡️ Температурен помощник")

st.markdown(
    '<div class="subtitle">Разбери какво е времето и как да се облечеш! ☁️</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# ---------------- ТЕМПЕРАТУРА ----------------

st.markdown("### 🌍 Избери температурата")

temperature = st.slider(
    "Настрой температурата:",
    min_value=-50,
    max_value=60,
    value=20,
    step=1
)

st.markdown(
    f"<h2 style='text-align:center;color:#38bdf8;'>"
    f"🌡️ {temperature} °C</h2>",
    unsafe_allow_html=True
)


# ---------------- ПРОВЕРКА ----------------

if st.button("✨ ПРОВЕРИ ТЕМПЕРАТУРАТА"):

    with st.spinner("Анализирам времето..."):
        time.sleep(1)

    st.markdown("---")

    # МНОГО СТУДЕНО
    if temperature < 0:
        icon = "🥶"
        message = "Леден студ!"
        advice = "Облечи дебело яке, шапка, шал и ръкавици!"
        color = "#60a5fa"
        st.snow()

    # СТУДЕНО
    elif temperature < 10:
        icon = "❄️"
        message = "Студено е!"
        advice = "Облечи топло яке и не забравяй шала!"
        color = "#38bdf8"
        st.snow()

    # ПРОХЛАДНО
    elif temperature < 20:
        icon = "🌥️"
        message = "Прохладно е!"
        advice = "Подходящо е леко яке или суичър."
        color = "#a78bfa"
        st.balloons()

    # ПРИЯТНО
    elif temperature < 30:
        icon = "☀️"
        message = "Приятно топло е!"
        advice = "Наслади се на хубавото време! Подходящи са леки дрехи."
        color = "#facc15"
        st.balloons()

    # ГОРЕЩО
    else:
        icon = "🔥"
        message = "Много е горещо!"
        advice = "Пий повече вода, стой на сянка и носи леки дрехи."
        color = "#fb923c"

        st.toast("Внимание! Високи температури! 🔥")

    # ---------------- РЕЗУЛТАТ ----------------

    st.markdown(
        f"""
        <div class="main-card">
            <div class="big-icon">{icon}</div>
            <div class="result" style="color:{color};">
                {message}
            </div>
            <p style="font-size:18px;color:white;">
                {advice}
            </p>
            <h3 style="color:{color};">
                Температура: {temperature} °C
            </h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- СКАЛА ----------------

    st.markdown("### 📊 Температурна скала")

    progress = (temperature + 50) / 110
    st.progress(progress)

    st.caption("От -50°C до +60°C")

    # ---------------- СЪВЕТ ----------------

    st.markdown("### 💡 Малък съвет за деня")

    tips = [
        "Не забравяй да се усмихваш! 😊",
        "Погрижи се за себе си и се обличай подходящо!",
        "Разходката навън винаги е добра идея при приятно време!",
        "Пий достатъчно вода през деня! 💧",
        "Наслади се на всеки сезон! 🌈"
    ]

    st.info(random.choice(tips))


# ---------------- ДОЛНА ЧАСТ ----------------

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;color:#94a3b8;">
        🌡️ Температурен помощник<br>
        Създаден с ❤️ и Python + Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
