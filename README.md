 ♻️ ReVolve – Product Lifecycle Intelligence Platform

SDG-12: Responsible Consumption & Production

ReVolve is a **Streamlit-based lifecycle intelligence prototype** that simulates how IoT sensor data can be used to monitor product health, predict lifecycle stages, estimate remaining useful life, and provide actionable sustainability recommendations — **without requiring any hardware sensors**.


## 🚀 Key Features

### 🔄 Hybrid Data Input

* **Simulated Sensor Data** (IoT-like data generation)
* **Manual User Input** (for demo & testing)

### 📊 Product Health Index (PHI)

* Calculates a **health score (0–100%)** using:

  * Temperature
  * Vibration
  * Usage cycles

### 🔁 Lifecycle Intelligence

* Automatically identifies lifecycle stage:

  * **Healthy**
  * **Aging**
  * **End-of-Life**
* Estimates **Remaining Useful Life (cycles)**

### 🛠️ Action Recommendations

* Smart suggestions based on lifecycle stage:

  * Continue normal operation
  * Schedule maintenance
  * Plan replacement / recycling

### 📝 Lifecycle Summary

* Human-readable explanation of product condition
* Justification for PHI score (“Why this PHI?”)

### 📈 PHI Trend Visualization

* Line chart showing PHI variation over time (per product)

### 📤 Export Report

* Download lifecycle data as **CSV**
* Useful for audits, compliance, or analysis

---

## 🧠 How Lifecycle Stage Is Determined

| PHI Score | Lifecycle Stage | Status      |
| --------- | --------------- | ----------- |
| ≥ 80%     | Healthy         | 🟢 Safe     |
| 40–79%    | Aging           | 🟡 Warning  |
| < 40%     | End-of-Life     | 🔴 Critical |

Remaining life is estimated using **usage cycles** and predefined thresholds.

---

## 🗂️ Project Structure

```
ReVolve-Prototype-v2/
│
├── logic/
│   ├── phi_logic.py        # PHI calculation & lifecycle rules
│   └── __init__.py
│
├── simulation/
│   ├── data_generator.py  # Simulated IoT sensor data
│   └── __init__.py
│
├── integration/
│   └── final_app.py       # Main Streamlit application
│
├── requirements.txt
├── README.md
└── venv/
```

---

## ▶️ How to Run the App

### 1️⃣ Activate virtual environment

```bash
venv\Scripts\activate
```

### 2️⃣ Go to project root

```bash
cd ReVolve-Prototype-v2
```

### 3️⃣ Run Streamlit app

```bash
streamlit run integration/final_app.py
```

### 4️⃣ Open in browser

```
http://localhost:8501
```

---

## 🌍 Why ReVolve Matters (For Judges)

* Encourages **responsible consumption**
* Enables **predictive maintenance**
* Reduces **waste & premature disposal**
* Supports **circular economy principles**
* Demonstrates **Industry 4.0 + Sustainability**

---

## 🧪 Prototype Scope

* **No hardware required**
* Uses simulated + user-defined data
* Designed for **hackathons, ideathons & demos**
* Easily extendable to real IoT sensors in future

---

## 🔮 Future Enhancements

* Real IoT sensor integration
* Machine learning–based degradation prediction
* Cloud dashboard for multiple products
* Blockchain-based lifecycle traceability

---

## 👨‍💻 Team Collaboration Model

* Modular folder structure
* GitHub-based integration
* Easy handoff between team members

---

## 📌 Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **Matplotlib**
* **Git & GitHub**

---

## 🏁 Final Note
ReVolve demonstrates how data-driven lifecycle intelligence can help industries move toward sustainable production and consumption, aligning directly with UN SDG-12.
> ReVolve demonstrates how **data-driven lifecycle intelligence** can help industries move toward **sustainable production and consumption**, aligning directly with **UN SDG-12**.

