from flask import Flask, request, render_template, Blueprint
import os, requests

weather_bp = Blueprint('weather', __name__)
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

@weather_bp.route('/weather/<city>', methods=['GET'])
def weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=imperial'
    response = requests.get(url)
    print("API Key:", WEATHER_API_KEY)
    print("Request URL:", url)
    #Returns error if invalid city is entered
    if response.status_code != 200:
        return render_template({"error": "City not found or API error."}), 404

    data = response.json()

    weather_data = {
        "city": city,
        "temperature": f"{data['main']['temp']}°F",
        "condition": data['weather'][0]['description'],
        "humidity": f"{data['main']['humidity']}%",
        "wind_speed": f"{data['wind']['speed']} mph",
    }
    return render_template('weather.html', weather=weather_data)