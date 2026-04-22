import streamlit as st
import pandas as pd
import plotly.express as px

st.title("02 · Energy")
st.write("Real energy-efficiency benchmark page using the official PUE formula and industry survey data.")

benchmark_df = pd.DataFrame({
    "Metric": ["Industry average PUE (2024)", "PUE definition"],
    "Value": ["1.56", "Total facility energy / IT equipment energy"]
})

comparison_df = pd.DataFrame({
    "Category": ["Industry average PUE"],
    "Value": [1.56]
})

col1, col2 = st.columns(2)
with col1:
    st.metric("Industry average PUE", "1.56")
with col2:
    st.metric("Benchmark source", "Uptime 2024")

fig = px.bar(
    comparison_df,
    x="Category",
    y="Value",
    title="Industry Average PUE Benchmark"
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Interactive PUE Calculator")

col1, col2 = st.columns(2)
with col1:
    it_load = st.number_input("IT Equipment Energy (kWh)", min_value=1.0, value=1000.0)
with col2:
    total_facility = st.number_input("Total Facility Energy (kWh)", min_value=1.0, value=1560.0)

pue = total_facility / it_load
st.metric("Calculated PUE", f"{pue:.2f}")

st.subheader("Reference")
st.dataframe(benchmark_df, use_container_width=True)

st.markdown("### Sources")
st.markdown("""
- The Green Grid, **Power Usage Effectiveness (PUE)**  
  https://www.thegreengrid.org/node/372
- Uptime Institute, **Global Data Center Survey 2024**  
  https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/2024.GlobalDataCenterSurvey.Report.pdf?version=0
""")