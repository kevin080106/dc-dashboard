import streamlit as st
import pandas as pd
import plotly.express as px

st.title("01 · Operations")
st.write("YucaCore operating case study with real industry outage benchmarks.")

benchmark_df = pd.DataFrame({
    "Metric": [
        "Outages costing more than $100k",
        "Outages costing more than $1M",
        "Leading cause of serious outages"
    ],
    "Value": ["54%", "20%", "Power issues"]
})

incident_data = pd.DataFrame({
    "Category": ["Power", "Cooling", "Network", "Access Control"],
    "Incidents": [2, 1, 3, 1]
})

mac_data = pd.DataFrame({
    "Request ID": ["MAC-101", "MAC-102", "MAC-103", "MAC-104"],
    "Type": ["Move", "Add", "Change", "Add"],
    "Status": ["Closed", "Closed", "Open", "Closed"],
    "Owner": ["Ops", "Facilities", "Network", "Ops"]
})

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Industry: outages > $100k", "54%")
with col2:
    st.metric("Industry: outages > $1M", "20%")
with col3:
    st.metric("Top outage cause", "Power")

fig_incidents = px.bar(
    incident_data,
    x="Category",
    y="Incidents",
    title="YucaCore Incident Log by Category (fictional case study)"
)
st.plotly_chart(fig_incidents, use_container_width=True)

st.subheader("YucaCore MAC Process Table (fictional case study)")
st.dataframe(mac_data, use_container_width=True)

st.subheader("Industry Benchmarks")
st.dataframe(benchmark_df, use_container_width=True)

st.markdown("### Sources")
st.markdown("""
- Uptime Institute, **Annual Outage Analysis 2025**  
  https://intelligence.uptimeinstitute.com/resource/annual-outage-analysis-2025
- Uptime Institute, **Annual Outage Analysis 2024**  
  https://uptimeinstitute.com/resources/research-and-reports/annual-outage-analysis-2024
""")