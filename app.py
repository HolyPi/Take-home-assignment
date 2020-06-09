from flask import Flask, render_template, request
import requests


app = Flask(__name__)

@app.route('/')
def weather():
    return render_template('weather_form.html')

@app.route('/weather_results')
def weather_results_page():
    users_city = request.args.get('city')

    params = {
    'q': users_city,
    'appid': '2608f679d4594364525f6c6cc2246c79'

    }
    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)
    if not response.status_code == 200:

        print("Nothing to show")

    results = response.json()

    city = results['name']

    temp = convert(results['main']['temp'])

    return render_template('weather_results.html', city=city, temp=temp)

def convert(K):
    conversion = 9/5 * (K - 273) + 32
    return int(conversion)

    if __name__ == '__main__':
        app.run()