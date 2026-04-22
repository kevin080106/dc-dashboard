import streamlit as st
import pandas as pd
import plotly.express as px

st.title("04 · Market Intelligence")
st.write("Real public data for Mexico and the broader Latin American data center market.")

city_data = pd.DataFrame({
    "Location": ["Mexico City", "Querétaro", "Monterrey", "Other Mexico markets"],
    "Data Centers": [40, 28, 16, 89]
})

latam_metrics = pd.DataFrame({
    "Metric": [
        "LATAM colocation inventory growth (YoY, 2025)",
        "LATAM average vacancy rate (2025)",
        "Pipeline already precommitted (2025)"
    ],
    "Value": [20, 9, 42]
})

country_focus = pd.DataFrame({
    "Country Group": ["Core demand countries in LATAM"],
    "Countries": ["Brazil, Mexico, Chile, Colombia"]
})

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Mexico data centers", "173")
with col2:
    st.metric("Querétaro data centers", "28")
with col3:
    st.metric("LATAM vacancy rate", "9%")

fig_city = px.bar(
    city_data,
    x="Location",
    y="Data Centers",
    title="Mexico Data Center Directory Snapshot"
)
st.plotly_chart(fig_city, use_container_width=True)

csv_data = city_data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Mexico market data as CSV",
    data=csv_data,
    file_name="mexico_market_data.csv",
    mime="text/csv"
)

fig_latam = px.bar(
    latam_metrics,
    x="Metric",
    y="Value",
    title="LATAM Market Indicators (2025)"
)
st.plotly_chart(fig_latam, use_container_width=True)

st.subheader("Core Demand Countries in Latin America")
st.dataframe(country_focus, use_container_width=True)

st.caption("Note: Cloudscene is a live commercial directory, so facility counts may change over time.")

st.markdown("### Sources")
st.markdown("""
- JLL, **Latin America Data Center Report Year-end 2025**  
  https://www.jll.com/en-us/insights/latin-america-data-center-report-year-end-2025
- Cloudscene, **Mexico Market Overview**  
  https://cloudscene.com/market/data-centers-in-mexico/all
""")