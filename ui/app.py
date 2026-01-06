import streamlit as st

st.set_page_config(page_title="ReVolve Prototype", layout="wide")

st.title("🔄 ReVolve – Product Lifecycle Tracking Prototype")
st.write("SDG-12: Responsible Consumption & Production")

st.header("📦 Product Details")

product_id = st.text_input("Product ID", value="REV-001")

st.header("🌡️ Simulated Sensor Inputs")

temperature = st.slider("Temperature (°C)", min_value=0, max_value=100, value=30)
vibration = st.checkbox("Vibration / Shock Detected")

usage_cycles = st.number_input("Usage Cycles", min_value=0, value=10)

st.header("📊 Product Health Index (Preview)")

phi = 100
if temperature > 35:
    phi -= 20
if vibration:
    phi -= 15
if usage_cycles > 50:
    phi -= 20

phi = max(phi, 0)

st.metric("PHI Score", f"{phi} %")

if phi >= 70:
    st.success("🟢 Product Status: Healthy")
elif phi >= 40:
    st.warning("🟡 Product Status: Warning")
else:
    st.error("🔴 Product Status: End-of-Life")

st.caption("⚠️ This is a UI prototype using simulated data")
