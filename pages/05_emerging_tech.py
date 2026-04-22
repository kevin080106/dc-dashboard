import streamlit as st
import pandas as pd
import plotly.express as px

st.title("05 · Emerging Technologies")
st.write("Real growth and infrastructure outlook based on public industry reports.")

capacity_df = pd.DataFrame({
    "Year": ["2025", "2030"],
    "Global Capacity (GW)": [103, 200]
})

trend_df = pd.DataFrame({
    "Metric": [
        "Global DC sector CAGR through 2030",
        "New capacity added between 2026 and 2030",
        "AI share of workloads by 2030",
        "Industry average PUE (2024)"
    ],
    "Value": [14, 100, 50, 1.56]
})

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("2030 global capacity", "200 GW")
with col2:
    st.metric("Growth rate", "14% CAGR")
with col3:
    st.metric("AI share by 2030", "50%")

fig_capacity = px.bar(
    capacity_df,
    x="Year",
    y="Global Capacity (GW)",
    title="Global Data Center Capacity Outlook"
)
st.plotly_chart(fig_capacity, use_container_width=True)

fig_trends = px.bar(
    trend_df,
    x="Metric",
    y="Value",
    title="Key Technology and Infrastructure Signals"
)
st.plotly_chart(fig_trends, use_container_width=True)

st.markdown("### Strategic interpretation")
st.write("1. AI is shifting data center design toward higher power density and energy-aware infrastructure.")
st.write("2. Capacity growth is accelerating, but grid constraints make energy innovation a competitive advantage.")
st.write("3. Efficiency benchmarks remain important because average industry PUE is improving slowly, not dramatically.")

st.markdown("### Sources")
st.markdown("""
- JLL, **2026 Global Data Center Outlook**  
  https://www.jll.com/en-us/insights/market-outlook/data-center-outlook
- JLL newsroom, **Global data center sector to nearly double to 200GW**  
  https://www.jll.com/en-us/newsroom/global-data-center-sector-to-nearly-double-to-200gw-amid-ai-infrastructure-boom
- Uptime Institute, **Global Data Center Survey 2024**  
  https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/2024.GlobalDataCenterSurvey.Report.pdf?version=0
""")