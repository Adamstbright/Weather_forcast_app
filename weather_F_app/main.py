import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forcast for the Next Days ")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to vies",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperature = [dict["main"]["temp"] for dict in filtered_data]
        date = [dict["dt_txt"] for dict in filtered_data]
        # Create a temperature plot
        figure = px.line(x=date, y=temperature, labels={"x": "Date", "y": "Temperature"})
        st.plotly_chart(figure)

    if option == "Sky":
        image = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                 "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [image[condition] for condition in sky_conditions]
        st.image(image_paths, width=115)
