# 🔄 Revolve: Product Lifecycle Logic & PHI Framework

This document outlines the mathematical models and logic gates used to determine product health and sustainability metrics.

---

## 1. Product Health Index (PHI) Formula
[cite_start]The PHI is a real-time calculation of a product's integrity based on environmental and usage stress[cite: 79, 84].

**Formula:** $$PHI = 100 - (T_{penalty} + V_{penalty} + S_{penalty} + U_{penalty})$$

### Penalty Breakdown:
* [cite_start]**Thermal Stress ($T$):** Deducts 1.5 points for every 1°C above the 50°C threshold[cite: 65, 111].
* [cite_start]**Mechanical Vibration ($V$):** A flat deduction of 20 points if abnormal vibration is detected[cite: 65, 119].
* [cite_start]**Critical Shock ($S$):** A 40-point deduction for high-impact events or tampering[cite: 65, 111].
* [cite_start]**Usage Decay ($U$):** Calculated as $(Current Usage / 1000) * 10$ to account for natural wear[cite: 70, 140].

---

## 2. Status Thresholds
[cite_start]The backend maps the PHI score to specific lifecycle stages to trigger UI alerts and blockchain logs[cite: 54, 124].

| PHI Range | Lifecycle Stage | Action Required |
| :--- | :--- | :--- |
| **80% - 100%** | **OPTIMAL** | [cite_start]No action; normal operation[cite: 101]. |
| **50% - 79%** | **WARNING** | [cite_start]Predictive maintenance triggered[cite: 82, 119]. |
| **< 50%** | **END-OF-LIFE** | [cite_start]Transition to Smart Recycling[cite: 85, 128]. |

---

## 3. Sustainability & Carbon Metrics
[cite_start]Calculated to provide transparency for eco-informed consumer decisions[cite: 35, 140].

* [cite_start]**Carbon Score:** Derived from the cumulative energy/thermal footprint during logistics and usage[cite: 84, 125].
* [cite_start]**Sustainability Index:** A weighted average of Product Health and usage efficiency[cite: 79, 140].
* [cite_start]**Disposal Credits:** Incentives issued via Blockchain when a product reaches "End-of-Life" and is verified at a recycling center[cite: 85, 131].
