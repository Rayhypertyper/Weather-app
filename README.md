Weathermo - Weather Forecast App 🌦️
Weathermo is a simple and interactive weather forecast app built using Streamlit. It fetches real-time weather data for any city using the OpenWeatherMap API and displays the temperature, wind speed, humidity, and weather conditions in a user-friendly interface.

Features ✨
Real-time weather data: Get the latest weather information for any city.

Interactive UI: Input a city name and see the weather forecast instantly.

Visual icons: Display weather conditions (e.g., clouds, rain, clear sky) with intuitive icons.

Metrics: View temperature, wind speed, and humidity in a clean, organized layout.

Prerequisites 🛠️
Before running the app, ensure you have the following installed:

Python 3.8 or higher

Streamlit (pip install streamlit)

Requests library (pip install requests)

Python-dotenv (pip install python-dotenv)

Installation 🚀
Clone the repository:

bash
Copy
git clone https://github.com/your-username/weather-app.git
cd weather-app
Set up environment variables:

Create a .env file in the root directory.

Add your OpenWeatherMap API key to the .env file:

env
Copy
API_KEY=your_api_key_here
Install dependencies:

bash
Copy
pip install -r requirements.txt
Running the App ▶️
To run the app locally, use the following command:

bash
Copy
python -m streamlit run weatherweb.py
The app will open in your default web browser at http://localhost:8501.

Usage 🖥️
Enter the name of a city in the input box (e.g., "Toronto").

The app will display:

Current weather conditions (e.g., clouds, rain, clear sky).

Temperature in Celsius.

Wind speed in km/h.

Humidity percentage.

File Structure 📂
Copy
weather-app/
├── Weather/
│   ├── weatherweb.py       # Main Streamlit app script
│   ├── wind.png            # Wind icon
│   ├── humidity.png        # Humidity icon
├── .env                    # Environment variables (API key)
├── README.md               # Project documentation
└── requirements.txt        # List of dependencies
Dependencies 📦
Streamlit: For building and running the web app.

Requests: For making HTTP requests to the OpenWeatherMap API.

Python-dotenv: For loading environment variables from a .env file.

API Key 🔑
To use this app, you need an API key from OpenWeatherMap. Sign up for a free account and get your API key.

Screenshots 📸
Weathermo Screenshot
Example of the app in action.

Contributing 🤝
Contributions are welcome! If you'd like to improve this project, please:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/your-feature).

Open a pull request.

License 📄
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments 🙏
OpenWeatherMap for providing the weather data API.

Streamlit for making it easy to build and share data apps.

Enjoy using Weathermo! If you have any questions or feedback, feel free to open an issue or reach out. 🌟

Let me know if you need further adjustments or additional details! 😊
