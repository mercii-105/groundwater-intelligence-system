import streamlit as st
st.markdown("""
<style>
.main {
    background: linear-gradient(to bottom right,#f8fbff,#eef4ff);
}

h1, h2, h3 {
    color:#0b2545;
}

[data-testid="metric-container"] {
    background: white;
    border-radius: 18px;
    padding: 18px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    border-left: 5px solid #3b82f6;
}

.stSelectbox > div > div {
    border-radius: 14px;
}

.stAlert {
    border-radius:14px;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom,#eaf2ff,#dce8ff);
}

hr {
    margin-top:25px;
    margin-bottom:25px;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="AP Groundwater Intelligence", layout="wide")

st.sidebar.title("💧 AP Groundwater System")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Dashboard",
        "🤖 Predictor",
        "🗺️ GIS Map",
        "📈 Trends",
        "💡 Recommendations",
        "📁 About"
    ]
)

st.sidebar.info("AI + GIS + Analytics")

# ---------------- HOME ----------------
if page == "🏠 Home":


    st.markdown("""
<div style='
padding:35px;
border-radius:24px;
background:linear-gradient(135deg,#dbeafe,#eff6ff);
box-shadow:0 8px 24px rgba(0,0,0,0.08);
border:1px solid #dbeafe;
'>

<h1 style='font-size:58px; margin-bottom:10px; color:#0B2545; line-height:1.1;'>
Andhra Pradesh Groundwater Intelligence System and Analytics
</h1>

<h3 style='color:#2563EB; margin-top:0; font-size:30px;'>
AI + GIS + Predictive Analytics Dashboard
</h3>

<p style='font-size:22px; color:#334155; max-width:950px; margin-top:18px;'>
Smart platform for groundwater monitoring, district intelligence,
risk prediction, GIS visualization and sustainable planning.
</p>

</div>
""", unsafe_allow_html=True)
    st.write("")

    # KPIs
    c1,c2,c3 = st.columns(3)

    c1.metric("🌍 Districts Covered", "26+")
    c2.metric("📊 Samples Analysed", "10,950")
    c3.metric("🎯 Model Accuracy", "100%")

    st.write("")
    st.markdown("---")

    st.subheader("🚀 Core Modules")

    a,b = st.columns(2)

    with a:
        st.success("📊 District Dashboard")
        st.success("🤖 AI Risk Predictor")
        st.success("📈 Forecast Engine")

    with b:
        st.info("🗺 GIS Mapping")
        st.info("💡 Smart Recommendations")
        st.info("📁 Research Ready")

    st.markdown("---")

    st.subheader("🌍 Why This Matters")

    st.write("""
    Andhra Pradesh faces increasing groundwater stress due to over-extraction,
    population growth, rainfall variability and water quality decline.

    This intelligent system helps researchers, officers and planners make
    data-driven decisions for sustainable groundwater management.
    """)

    st.markdown("---")

    st.caption("Developed by Mercy | B.Tech CSE Final Year Project | 2026")

# ---------------- DASHBOARD ----------------
elif page == "📊 Dashboard":
    import pandas as pd
    import plotly.express as px

    master = pd.read_csv("final_groundwater_results.csv")
    st.title("📊 District Intelligence Dashboard")
    st.write("District-wise groundwater, population and water quality insights.")

    district = st.selectbox(
        "Select District",
        sorted(master["District"].dropna().unique())
    )

    row = master[master["District"] == district].iloc[0]

    # KPI Cards
    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Population",
        f"{int(row['population_2011']) if pd.notna(row['population_2011']) else 'N/A'}"
    )

    c2.metric(
        "Growth %",
        f"{round(row['growth_2001_2011_pct'],2) if pd.notna(row['growth_2001_2011_pct']) else 'N/A'}"
    )

    c3.metric(
        "Groundwater Level",
        f"{round(row['GW_Level'],2) if pd.notna(row['GW_Level']) else 'N/A'}"
    )

    st.divider()

    # Water Quality Metrics
    st.subheader("💧 Water Quality Parameters")

    c4, c5, c6 = st.columns(3)

    c4.metric(
        "pH",
        f"{round(row['Potential of Hydrogen (pH)'],2) if pd.notna(row['Potential of Hydrogen (pH)']) else 'N/A'}"
    )

    c5.metric(
        "TDS",
        f"{round(row['Total Dissolved Solids (mg/L)'],2) if pd.notna(row['Total Dissolved Solids (mg/L)']) else 'N/A'}"
    )

    c6.metric(
        "EC",
        f"{round(row['Electric Conductivity (μS/cm)'],2) if pd.notna(row['Electric Conductivity (μS/cm)']) else 'N/A'}"
    )

    st.divider()

    # Compare Chart
    st.subheader("📈 Compare Groundwater Levels")

    fig = px.bar(
        master.sort_values("GW_Level", ascending=False),
        x="District",
        y="GW_Level",
        color="GW_Level",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------- PREDICTOR ----------------
elif page == "🤖 Predictor":

    import pandas as pd
    import joblib
    import plotly.express as px

    model = joblib.load("groundwater_risk_model.pkl")

    st.title("🤖 Live Groundwater Risk Predictor")
    st.write("Adjust water quality parameters to predict contamination risk.")

    st.markdown("---")

    # Inputs
    c1, c2, c3 = st.columns(3)

    with c1:
        ph = st.slider("pH", 5.0, 9.5, 7.2)
        fluoride = st.slider("Fluoride", 0.0, 5.0, 1.0)
        calcium = st.slider("Calcium", 10, 300, 80)

    with c2:
        ec = st.slider("EC (μS/cm)", 100, 5000, 1500)
        hardness = st.slider("Hardness", 50, 1000, 300)
        magnesium = st.slider("Magnesium", 5, 200, 40)

    with c3:
        tds = st.slider("TDS", 50, 3000, 500)
        chloride = st.slider("Chloride", 10, 1000, 200)

    # DataFrame
    input_df = pd.DataFrame([{
        "Potential of Hydrogen (pH)": ph,
        "Electric Conductivity (μS/cm)": ec,
        "Total Dissolved Solids (mg/L)": tds,
        "Fluoride (mg/L)": fluoride,
        "Total Hardness (mgCaCO3/L)": hardness,
        "Calcium (mg/L)": calcium,
        "Magnesium (mg/L)": magnesium,
        "Chloride (mg/L)": chloride
    }])

    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0]

    st.markdown("---")

    # Metrics
    m1, m2 = st.columns(2)

    m1.metric("Predicted Risk", pred)
    m2.metric("Confidence", f"{round(max(prob)*100,2)}%")

    # Chart
    prob_df = pd.DataFrame({
        "Risk": model.classes_,
        "Probability": prob
    })

    fig = px.bar(
        prob_df,
        x="Risk",
        y="Probability",
        color="Risk",
        text_auto=".2f",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

    # Advice
    st.subheader("💡 Recommendation")

    if pred == "Low":
        st.success("Water quality acceptable. Continue monitoring.")
    elif pred == "Medium":
        st.warning("Moderate risk detected. Use filtration and periodic testing.")
    else:
        st.error("High contamination risk. Immediate treatment recommended.")
# ---------------- GIS ----------------
elif page == "🗺️ GIS Map":

    import pandas as pd
    import plotly.express as px

    master = pd.read_csv("final_groundwater_results.csv")

    st.title("🗺️ Groundwater GIS Intelligence Maps")
    st.write("District-wise groundwater availability and contamination analysis.")

    tab1, tab2 = st.tabs(["💧 Groundwater Levels", "⚠️ Contamination Risk"])

    # ---------- TAB 1 ----------
    with tab1:

        st.info("""
        🗺 Bubble size = population  
        🎨 Color = groundwater level  
        Darker blue indicates better groundwater reserves.
        """)

        fig1 = px.scatter_mapbox(
            master.dropna(subset=["Latitude", "Longitude"]),
            lat="Latitude",
            lon="Longitude",
            hover_name="District",
            hover_data=["GW_Level", "population_2011"],
            color="GW_Level",
            size="population_2011",
            zoom=5.5,
            height=650,
            color_continuous_scale="Blues"
        )

        fig1.update_layout(mapbox_style="open-street-map")
        fig1.update_layout(margin=dict(l=0,r=0,t=0,b=0))

        st.plotly_chart(fig1, use_container_width=True)

    # ---------- TAB 2 ----------
    with tab2:

        st.info("""
        🔴 Red = High contamination risk  
        🟡 Yellow = Medium risk  
        🟢 Green = Lower risk
        """)

        # Simulated contamination score
        master["Risk_Score"] = (
            master["Total Dissolved Solids (mg/L)"].fillna(0) / 10 +
            master["Electric Conductivity (μS/cm)"].fillna(0) / 50 +
            master["Fluoride (mg/L)"].fillna(0) * 50
        )

        fig2 = px.scatter_mapbox(
            master.dropna(subset=["Latitude", "Longitude"]),
            lat="Latitude",
            lon="Longitude",
            hover_name="District",
            hover_data=["Risk_Score"],
            color="Risk_Score",
            size="Risk_Score",
            zoom=5.5,
            height=650,
            color_continuous_scale="RdYlGn_r"
        )

        fig2.update_layout(mapbox_style="open-street-map")
        fig2.update_layout(margin=dict(l=0,r=0,t=0,b=0))

        st.plotly_chart(fig2, use_container_width=True)
# ---------------- TRENDS ----------------
elif page == "📈 Trends":
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go

    master = pd.read_csv("final_groundwater_results.csv")

    st.title("📈 Trends & Forecasting")

    district = st.selectbox(
        "Select District",
        sorted(master["District"].dropna().unique())
    )

    row = master[master["District"] == district].iloc[0]

    # Compare metrics
    metrics = {
        "pH": row["Potential of Hydrogen (pH)"],
        "TDS": row["Total Dissolved Solids (mg/L)"],
        "EC": row["Electric Conductivity (μS/cm)"],
        "GW": row["GW_Level"]
    }

    df = pd.DataFrame({
        "Metric": list(metrics.keys()),
        "Value": list(metrics.values())
    })

    fig = px.bar(
        df,
        x="Metric",
        y="Value",
        color="Metric",
        height=450,
        title=f"{district} Water Indicators"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📉 Simulated Groundwater Forecast")

    future = pd.DataFrame({
        "Year":[2024,2025,2026,2027],
        "GW_Level":[row["GW_Level"], row["GW_Level"]-0.2, row["GW_Level"]-0.4, row["GW_Level"]-0.6]
    })

    fig2 = px.line(
        future,
        x="Year",
        y="GW_Level",
        markers=True,
        title="Projected Groundwater Level"
    )

    st.plotly_chart(fig2, use_container_width=True)
# ---------------- RECOMMEND ----------------
elif page == "💡 Recommendations":
    import pandas as pd

    master = pd.read_csv("final_groundwater_results.csv")

    st.title("💡 Smart Groundwater Recommendations")
    st.write("District-wise sustainability guidance based on groundwater indicators.")

    district = st.selectbox(
        "Select District",
        sorted(master["District"].dropna().unique())
    )

    row = master[master["District"] == district].iloc[0]

    st.subheader(f"📍 {district}")

    gw = row["GW_Level"]
    tds = row["Total Dissolved Solids (mg/L)"]
    ec = row["Electric Conductivity (μS/cm)"]

    # Advice Logic
    if gw < 6:
        st.error("🚨 Low groundwater level. Restrict over-extraction and increase recharge structures.")
    elif gw < 10:
        st.warning("⚠ Moderate groundwater level. Encourage rainwater harvesting.")
    else:
        st.success("✅ Healthy groundwater level.")

    if tds > 1000:
        st.warning("💧 High TDS detected. Recommend filtration and periodic testing.")

    if ec > 3000:
        st.warning("⚡ High conductivity indicates salinity/mineral stress.")

    st.info("🌱 Promote micro-irrigation, watershed planning and groundwater recharge.")

# ---------------- ABOUT ----------------
elif page == "📁 About":
    st.title("📁 About Project")

    st.subheader("💧 Andhra Pradesh Groundwater Intelligence System")

    st.write("""
    This project is an AI-powered decision support platform developed to analyse,
    predict and visualize groundwater conditions across Andhra Pradesh.

    It integrates district-level socio-environmental indicators with water quality
    observations to support sustainable groundwater management.
    """)

    st.markdown("---")

    st.subheader("🚀 Modules Included")

    st.write("""
    • District Analytics Dashboard  
    • Live Groundwater Risk Predictor  
    • GIS Risk Mapping  
    • Trends & Forecasting  
    • Smart Recommendations
    """)

    st.markdown("---")

    st.subheader("🛠 Technologies Used")

    st.write("""
    Python, Pandas, Scikit-learn, Streamlit, Plotly, GIS Concepts
    """)

    st.markdown("---")

    st.subheader("🎯 Objective")

    st.write("""
    To enable data-driven groundwater governance through analytics,
    machine learning and spatial intelligence.
    """)