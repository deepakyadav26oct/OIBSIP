# Weather App Using Python

## Overview

The Weather App is a Python-based application that retrieves current weather information for a selected city using free online weather services without requiring an API key.

This project was developed as Task 4 of the Oasis Infobyte Python Programming Internship.

## Features

- Search weather by city name.
- Display current temperature in Celsius.
- Display feels-like temperature.
- Show weather conditions such as cloudy, sunny, or rainy.
- Display humidity percentage.
- Display wind speed in km/h.
- Verify city names using OpenStreetMap geocoding.
- Handle invalid or unmatched location inputs.
- Search multiple locations without restarting the application.
- Display error messages when weather data is unavailable.

## Technologies Used

- Python
- JSON
- urllib
- OpenStreetMap Nominatim
- wttr.in Weather Service

## Requirements

- Python 3
- Internet connection
- No API key required

## How to Run

1. Download or clone the project.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

   `python weather_app.py`

5. Enter the city name.
6. View the available weather information.
7. Enter `y` to check another location or `n` to exit.

## Weather Information Displayed

- Location
- Temperature
- Feels-like temperature
- Weather condition
- Humidity
- Wind speed

## Error Handling

The application handles network errors, unavailable weather data, and locations that do not match the supported location search criteria.

Exact location matching depends on the available OpenStreetMap location data.

## Screenshots

Screenshots of successful weather searches and invalid location inputs are stored in the `screenshots` folder.

## Internship Details

**Organization:** Oasis Infobyte

**Track:** Python Programming

**Task:** Task 4 – Weather App