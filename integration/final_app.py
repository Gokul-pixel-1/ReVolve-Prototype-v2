# =======================
# FIX MODULE PATH ISSUE
# =======================
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# =======================
# IMPORTS
# =======================
import streamlit as st
import random
import pandas as pd
from datetime import datetime

from logic.phi_logic import calculate_phi

# =======================
# HELPER: RECOMMENDATION & SUMMARY
# =======================
def get_recommendation_and_summary(phi, stage, penalties):

    if phi >= 70:
        recommendation = (
            "🟢 **Recommended Action:** Continue normal operation. "
            "Product is functioning within safe parameters."
        )
        summary = (
            "This product is in a healthy stage of its lifecycle and operating "
            "under optimal conditions. Sensor readings indicate minimal stress, "
            "supporting continued use without immediate maintenance."
        )

    elif phi >= 40:
        recommendation = (
            "🟡 **Recommended Action:** Schedule preventive maintenance. "
            "Monitor operating conditions to extend product life."
        )
        summary = (
            "This product is currently in the aging phase of its lifecycle. "
            "Moderate operating stress and accumulated usage cycles suggest "
            "gradual degradation. Preventive maintenance can help extend "
            "its remaining useful life."
        )

    else:
        recommendation = (
            "🔴 **Recommended Action:** Consider repair, refurbishment, or "
            "responsible recycling aligned with circular economy practices."
        )
        summary = (
            "This product has reached the end-of-life stage based on high usage "
            "cycles and operating stress. Continued operation may lead to "
            "failures or inefficiencies. Sustainable replacement or recycling "
            "is recommended."
        )

    return recommendation, summary

# =======================
# PAGE CONFIG
# =======================
st.set_page_config(
    page_title="ReVolve – Product Lifecycle Intelligence",
    layout="wide"
)

# =======================
# SESSION STATE
# =======================
if "product_history" not in st.session_state:
    st.session_state.product_history = {}

if "sim_data" not in st.session_state:
    st.session_state.sim_data = None

# =======================
# HEADER
# =======================
st.title("🔄 ReVolve – Product Lifecycle Intelligence Platform")
st.caption("SDG-12: Responsible Consumption & Production")

# =======================
# SIDEBAR
# =======================
st.sidebar.header("Input Mode")
input_mode = st.sidebar.radio(
    "Choose data source:",
    ["Simulated Sensor Data", "Manual Input"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "PHI is calculated using:\n"
    "- Temperature\n"
    "- Vibration\n"
    "- Usage cycles\n\n"
    "Lifecycle stage & remaining life\n"
    "are derived from usage."
)

# =======================
# PRODUCT INFO
# =======================
st.subheader("📦 Product Information")
product_id = st.text_input("Product ID", "REV-001")

if product_id not in st.session_state.product_history:
    st.session_state.product_history[product_id] = []

# =======================
# DATA INPUT
# =======================
if input_mode == "Simulated Sensor Data":

    if st.sidebar.button("🔁 Refresh Simulated Data"):
        st.session_state.sim_data = None

    if st.session_state.sim_data is None:
        st.session_state.sim_data = {
            "temperature": random.randint(20, 75),
            "vibration": random.choice([0, 1]),
            "usage_cycles": random.randint(0, 100),
        }

    data = st.session_state.sim_data
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    st.subheader("🌡️ Live Simulated Sensor Data")
    st.json({
        "product_id": product_id,
        **data,
        "timestamp": timestamp
    })

else:
    st.subheader("✍️ Manual Sensor Input")

    temperature = st.slider("Temperature (°C)", 0, 80, 25)
    vibration = st.selectbox("Vibration Detected", [0, 1])
    usage_cycles = st.number_input("Usage Cycles", min_value=0, step=1)

    data = {
        "temperature": temperature,
        "vibration": vibration,
        "usage_cycles": usage_cycles,
    }
    timestamp = "User Input"

    st.json({
        "product_id": product_id,
        **data,
        "timestamp": timestamp
    })

# =======================
# PHI CALCULATION
# =======================
phi, penalties, stage, remaining_life = calculate_phi(
    data["temperature"],
    data["vibration"],
    data["usage_cycles"]
)

recommendation, lifecycle_summary = get_recommendation_and_summary(
    phi, stage, penalties
)

# Save history
st.session_state.product_history[product_id].append({
    "time": datetime.now().strftime("%H:%M:%S"),
    "phi": phi,
    "usage_cycles": data["usage_cycles"]
})

# =======================
# STATUS
# =======================
if phi >= 70:
    status = "Healthy"
elif phi >= 40:
    status = "Warning"
else:
    status = "End-of-Life"

# =======================
# OUTPUT
# =======================
st.subheader("📊 Product Health Index")

st.metric("PHI Score", f"{phi:.2f}%")
st.metric("Lifecycle Stage", stage)
st.metric("Remaining Useful Life (cycles)", remaining_life)

if status == "Healthy":
    st.success("🟢 Product Status: Healthy")
elif status == "Warning":
    st.warning("🟡 Product Status: Warning")
else:
    st.error("🔴 Product Status: End-of-Life")

# =======================
# ACTION RECOMMENDATION
# =======================
st.subheader("🛠️ Action Recommendation")

if phi >= 70:
    st.success(recommendation)
elif phi >= 40:
    st.warning(recommendation)
else:
    st.error(recommendation)

# =======================
# LIFECYCLE SUMMARY
# =======================
st.subheader("📘 Lifecycle Summary")
st.write(lifecycle_summary)

# =======================
# EXPLANATION
# =======================
with st.expander("🧠 Why this PHI score?"):
    if penalties:
        for p in penalties:
            st.write(f"• {p}")
    else:
        st.write("• Product operating in optimal conditions")

# =======================
# TREND GRAPH
# =======================
st.subheader("📈 PHI Trend (per Product)")
history_df = pd.DataFrame(st.session_state.product_history[product_id])
st.line_chart(history_df.set_index("time")["phi"])

# =======================
# EXPORT
# =======================
st.subheader("📤 Export Lifecycle Report")
csv = history_df.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download CSV Report",
    csv,
    file_name=f"{product_id}_lifecycle_report.csv",
    mime="text/csv"
)

st.caption(
    "End-to-end lifecycle intelligence using simulated + manual data (no hardware required)"
)
