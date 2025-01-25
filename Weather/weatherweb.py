#RUN THIS TO RUN IT
#python -m streamlit run weatherweb.py

import streamlit as st
# import pillow
import datetime as dt
import requests
from dotenv import load_dotenv
import os

def forecast(citee):
    load_dotenv()
    base = "https://api.openweathermap.org/data/2.5/weather?"
    api = os.getenv("API_KEY")
    city = citee
    url = base + f"q={city}&appid={api}"
    
    return url
    # print(data)
    # print(f"the temperature is {round(data['main']['temp']-  273.15)} degrees celcius")


# Header
# st.header("This is a header with a divider", divider='rainbow')

# Subheader with colored text and emoji
# st.header('_Streamlit_ is :blue[cool] :sunglasses:')
st.header(':rainbow[Weathermo]', divider='red')

# Paragraphs and points
# st.markdown('''
#             This is a paragraph
#             - 1
#             - 2
#             - 3
#             ''')

# Clickable word to link
# st.markdown('''
#             [Subscribe](https://nitrotype.com)
#             ''')

# Inserting an image from online
# st.image("https://images.pexels.com/photos/2071882/pexels-photo-2071882.jpeg?cs=srgb&dl=pexels-wojciech-kumpicki-1084687-2071882.jpg&fm=jpg")

# st.metric(label="Temperature", value=f'{Ctemp} °C', delta=None, delta_color="normal", help=None, label_visibility="visible")

# Write a variable
# st.write('The temperature is', round(data['main']['temp']-  273.15))




# Makes a dropdown option thingy
# option = st.selectbox(
#     "Please select a city",
#     ("Toronto", "New York", "Tokyo", "Paris", "London", "Beijing"),
# )
option = st.text_input("City", "Toronto")
# st.write("You selected:", option)


url = forecast(option)
response = requests.get(url)
data = response.json()
Ctemp = round(data['main']['temp']-  273.15)
wind = data['wind']['speed']
humid = data['main']['humidity']
weather = data['weather'][0]['main']
print(data)
# Good format
st.subheader(f'The weather forecast in {option}')

# if Ctemp <= 0:
#     col1.metric("Temperature", f'{Ctemp} °C', "1.2 °C")
# elif Ctemp > 0 and Ctemp < 20:
#     col1.metric("Temperature", f'{Ctemp} °C', "1.2 °C")
# else:
#     col1.metric("Temperature", f'{Ctemp} °C', "1.2 °C")
# col1, col2, col3 = st.columns(3)
# if weather == 'Clouds':
#     col1 = st.image("https://openweathermap.org/img/wn/02d@2x.png")
# elif weather == 'Rain' or 'Drizzle' or 'Thunderstorm':
#     col1 = st.image("https://openweathermap.org/img/wn/09d@2x.png")
# elif weather == 'Clear':
#     col1 = st.image("https://openweathermap.org/img/wn/01d@2x.png")
# elif weather == 'Snow':
#     col1 = st.image("https://openweathermap.org/img/wn/13d@2x.png")
# col2.metric() = st.image("117-1176381_icon-free-download-animated-wind.png", width=20)
# vertical_alignment = st.selectbox(
#     "Vertical alignment", ["top", "center", "bottom"], index=2
# )


container = st.container(border=True)

with container:
    col1, col2, col3 = st.columns(3)
    with col1:
        if weather == 'Clouds':
            col1.image("https://openweathermap.org/img/wn/02d@2x.png", width=80)
        elif weather in ['Rain', 'Drizzle','Thunderstorm']:
            col1.image("https://openweathermap.org/img/wn/09d@2x.png", width=80)
        elif weather == 'Clear':
            col1.image("https://openweathermap.org/img/wn/01d@2x.png", width=80)
        elif weather == 'Snow':
            col1.image("https://openweathermap.org/img/wn/13d@2x.png", width=80)
    with col2:
        col2.image("Weather\wind.png", width=80)
    with col3:
        col3.image("Weather\humidity.png", width=80)



with col1:
    col1.metric("Temperature", f'{Ctemp} °C', "1.2 °C")
with col2:
    col2.metric("Wind", f'{wind} km/h', "-8%")
with col3:
    col3.metric("Humidity", f'{humid}%', "4%")



