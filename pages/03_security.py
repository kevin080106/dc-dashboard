import streamlit as st
import pandas as pd

st.title("03 · Security")
st.write("Reference security checklist for a fictional facility, aligned to common data center governance frameworks.")

compliance = pd.DataFrame({
    "Control": [
        "CCTV coverage",
        "Biometric access",
        "Visitor logs",
        "Rack locking",
        "Fire suppression",
        "ISO 27001 policy review",
        "TIA-942 physical zoning"
    ],
    "Status": [
        "Implemented",
        "Implemented",
        "Implemented",
        "Implemented",
        "Implemented",
        "In Progress",
        "In Progress"
    ]
})

controls = pd.DataFrame({
    "Layer": ["Perimeter", "Entry", "White Space", "Network Room"],
    "Primary Control": ["Fence + Guard", "Biometric + Badge", "CCTV + Rack Locks", "Restricted Access"],
    "Risk Level": ["Low", "Low", "Medium", "Low"]
})

col1, col2 = st.columns(2)
col1.metric("Implemented Controls", "5")
col2.metric("Controls In Progress", "2")

st.subheader("Reference Checklist")
st.dataframe(compliance, use_container_width=True)

st.subheader("Physical Security Controls")
st.dataframe(controls, use_container_width=True)

st.caption("This page is a fictional operating checklist aligned to standard data center security practices.")