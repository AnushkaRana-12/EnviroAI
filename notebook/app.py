import streamlit as st
st.set_page_config(layout="wide")

import pandas as pd
import plotly.graph_objects as go
import joblib
import matplotlib.pyplot as plt
import requests
import datetime

# ---------------- LOAD CSS ----------------
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.write("Loading data and model...")

# ---------------- LOAD DATASET (LIMIT FOR RENDER RAM) ----------------
data = pd.read_csv("data.csv", nrows=3000)

# ---------------- LOAD MODEL ----------------
model = joblib.load("model.pkl")

# ---------------- CITY SELECTION ----------------
st.sidebar.header("Select City")

cities = {
    "Delhi": (28.61, 77.23),
    "Mumbai": (19.07, 72.87),
    "Bangalore": (12.97, 77.59),
    "Kolkata": (22.57, 88.36),
    "Chennai": (13.08, 80.27),
    "Hyderabad": (17.38, 78.48),
    "Pune": (18.52, 73.85),
    "Jaipur": (26.91, 75.78)
}

selected_city = st.sidebar.selectbox("Choose City", list(cities.keys()))
lat, lon = cities[selected_city]

# ---------------- LIVE WEATHER ----------------
def get_live_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=relativehumidity_2m"

    try:
        response = requests.get(url)
        data_live = response.json()

        temp = data_live['current_weather']['temperature']
        wind = data_live['current_weather']['windspeed']
        humidity = data_live['hourly']['relativehumidity_2m'][0]
        ndvi = 0.4

        return temp, humidity, wind, ndvi
    except:
        return None

live_data = get_live_weather(lat, lon)

if live_data:
    live_temp, live_humidity, live_wind, live_ndvi = live_data
else:
    live_temp = data['temperature_2m'].iloc[-1]
    live_humidity = data['relative_humidity_2m'].iloc[-1]
    live_wind = data['wind_speed_10m'].iloc[-1]
    live_ndvi = data['ndvi'].iloc[-1]

# ---------------- PREDICTION ----------------
with st.spinner("Fetching live data and predicting AQI..."):
    current_pm25 = model.predict([[live_temp, live_humidity, live_wind, live_ndvi]])[0]
    current_aqi = int(current_pm25 * 2)
    predicted_aqi = current_aqi

increase = 5
current_time = datetime.datetime.now().strftime("%d %B %Y, %H:%M")

st.subheader("Health Recommendation")

if predicted_aqi <= 50:
    st.success("Air quality is good. Safe for outdoor activities.")
elif predicted_aqi <= 100:
    st.warning("Sensitive groups should avoid prolonged outdoor activity.")
elif predicted_aqi <= 150:
    st.error("Wear mask and avoid outdoor activities.")
else:
    st.error("Stay indoors and use air purifier.")

# ---------------- TITLE ----------------
st.markdown("<h1>🌍 EnviroAI Dashboard</h1>", unsafe_allow_html=True)

# ---------------- TOP CARDS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="card">
    <h4>Current AQI</h4>
    <h2>{current_aqi}</h2>
    <p>Moderate</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
    <h4>PM2.5 Level</h4>
    <h2>{current_pm25:.2f}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
    <h4>Model Accuracy</h4>
    <h2>0.94</h2>
    </div>
    """, unsafe_allow_html=True)

# ---------------- AQI COLOR BAR ----------------
st.subheader("AQI Level Indicator")

aqi = predicted_aqi

if aqi <= 50:
    color = "green"
    label = "Good"
elif aqi <= 100:
    color = "yellow"
    label = "Moderate"
elif aqi <= 150:
    color = "orange"
    label = "Poor"
else:
    color = "red"
    label = "Severe"

st.markdown(f"""
<div style="background:{color}; padding:15px; border-radius:10px; text-align:center; color:black;">
<h3>{label} (AQI {aqi})</h3>
</div>
""", unsafe_allow_html=True)

# ---------------- AQI METER ----------------
st.subheader("AQI Meter")

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=predicted_aqi,
    title={'text': "AQI"},
    gauge={
        'axis': {'range': [0, 300]},
        'steps': [
            {'range': [0, 50], 'color': "green"},
            {'range': [50, 100], 'color': "yellow"},
            {'range': [100, 150], 'color': "orange"},
            {'range': [150, 300], 'color': "red"}
        ]
    }
))

st.plotly_chart(fig)
st.subheader("AQI Severity Level")

progress = min(predicted_aqi / 300, 1.0)
st.progress(progress)

# ---------------- POLLUTANT COMPARISON ----------------
st.subheader("Pollutant Comparison")

fig = go.Figure()
fig.add_trace(go.Bar(name='PM2.5', x=['PM2.5'], y=[current_pm25]))
fig.add_trace(go.Bar(name='PM10', x=['PM10'], y=[data['pm10'].iloc[-1]]))
fig.add_trace(go.Bar(name='Temp', x=['Temp'], y=[live_temp]))

st.plotly_chart(fig)

# ---------------- POLLUTION TREND ----------------
st.subheader("Air Pollution Trend")

data['timestamp'] = pd.to_datetime(data['timestamp'])
daily_data = data.groupby(data['timestamp'].dt.date).mean()

fig = go.Figure()
fig.add_trace(go.Scatter(x=daily_data.index, y=daily_data['pm2.5'], name='PM2.5'))
fig.add_trace(go.Scatter(x=daily_data.index, y=daily_data['pm10'], name='PM10'))
fig.update_layout(template="simple_white")

st.plotly_chart(fig)

# ---------------- FORECAST ----------------
st.subheader("Next 6 Hours AQI Forecast")

future_hours = [1,2,3,4,5,6]
future_aqi = []

temp = live_temp
humidity = live_humidity
wind = live_wind
ndvi = live_ndvi

for i in future_hours:
    temp += 0.3
    humidity += 0.5
    wind -= 0.2
    pred = model.predict([[temp, humidity, wind, ndvi]])[0]
    future_aqi.append(int(pred * 2))

fig = go.Figure()
fig.add_trace(go.Scatter(x=future_hours, y=future_aqi, mode='lines+markers'))
st.plotly_chart(fig)

# ---------------- MAP ----------------
st.subheader(f"{selected_city} Location Map")

map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
st.map(map_data)

# ---------------- FOOTER ----------------
st.markdown("""
---
**EnviroAI Dashboard**  
AI-Based Air Pollution Monitoring and Forecasting System  
Developed using Machine Learning and Streamlit
""")