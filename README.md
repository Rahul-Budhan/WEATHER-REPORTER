## Weather Reporter Program in Python
This is a simple weather reporter program written in Python that retrieves the current weather information for a given location using the OpenWeatherMap API. The program prompts the user to enter a location and displays the current weather conditions, including temperature, humidity, wind speed, and description.

### Installation
To use this program, you will need to install the requests library, which can be done using pip. Here are the steps to install the requests library:

`pip install requests`

### Usage
To use the program, simply run the weather_reporter.py file in a Python interpreter. You will be prompted to enter a location (e.g. city, state, country). Once you enter the location, the program will retrieve the current weather information for that location and display it on the screen.

### Here's an example of how to run the program:

`python main.py`

### Configuration
Before using the program, you will need to obtain an API key from OpenWeatherMap. Here are the steps to obtain an API key:

Go to the OpenWeatherMap website: https://openweathermap.org/
+ Sign up for a free account.
+ Once you have signed up, go to the API keys page.
+ Generate a new API key.
+ Once you have obtained an API key, you will need to enter it in the config.py file in the following format:


`API_KEY = "your-api-key-here"`

### Limitations
This program is limited to retrieving current weather information for a given location. It does not provide forecasts or historical weather data.

### Credits
This program was written by [Your Name]. It uses the OpenWeatherMap API to retrieve weather information.
