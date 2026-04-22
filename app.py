import streamlit as st

st.set_page_config(
    page_title="YucaCore DC Ops Dashboard",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #0b1020 0%, #111827 100%);
        color: #f3f4f6;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1, h2, h3 {
        color: #f9fafb;
    }
</style>
""", unsafe_allow_html=True)

st.title("YucaCore DC Ops Dashboard")
st.subheader("Final Project — Units 3 and 4")

st.write(
    "Multi-page dashboard for data center operations, energy, security, "
    "market intelligence, and emerging technologies in Mexico."
)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Primary Site", "Querétaro")
with col2:
    st.metric("Edge Site", "Mérida")
with col3:
    st.metric("Service Model", "Colocation + Hybrid Cloud")

st.markdown("---")

st.markdown("### Dashboard structure")
st.write("Use the sidebar to navigate through the five required pages.")

st.markdown("""
1. **Operations** — fictional operating case + real industry outage benchmarks  
2. **Energy** — real PUE benchmark + interactive calculator  
3. **Security** — fictional checklist aligned to real standards  
4. **Market Intelligence** — real Mexico and LATAM market data  
5. **Emerging Technologies** — real growth and AI infrastructure outlook  
""")

st.markdown("---")

st.info(
    "Production deployment is live on AWS ECS. This dashboard presents a fictional "
    "data center operating case study supported by real market and industry benchmarks."
)