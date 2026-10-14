
import json
import re
import unicodedata
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


HEADERS = {
    "User-Agent": "OIBSIP-WeatherApp/1.0"
}


def normalize(text):
    text = unicodedata.normalize("NFKD", text.casefold())
    text = "".join(
        char for char in text
        if not unicodedata.combining(char)
    )
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def fetch_json(url):
    request = Request(url, headers=HEADERS)

    with urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))



def find_location(city):
    params = urlencode({
        "q": city,
        "format": "jsonv2",
        "addressdetails": 1,
        "limit": 10
    })

    url = (
        "https://nominatim.openstreetmap.org/search?"
        + params
    )

    results = fetch_json(url)
    query = normalize(city)

    # No search results means invalid/unavailable location.
    if not results:
        return None

    locality_fields = [
        "city",
        "town",
        "village",
        "municipality",
        "hamlet"
    ]

    # Accept only an exact locality-name match.
    for result in results:
        address = result.get("address", {})

        candidate_names = [
            result.get("name", "")
        ]

        for field in locality_fields:
            value = address.get(field)
            if value:
                candidate_names.append(value)

        for name in candidate_names:
            if name and normalize(name) == query:
                return result

    # Never choose an unrelated location.
    return None


    query = normalize(city)

    # First, search for an exact locality-name match.
    locality_fields = [
        "city", "town", "village", "municipality",
        "hamlet", "suburb", "city_district",
        "county", "state", "country"
    ]

    for result in results:
        address = result.get("address", {})
        names = [result.get("name", "")]

        for field in locality_fields:
            if address.get(field):
                names.append(address[field])

        if any(normalize(name) == query for name in names):
            return result

    # Otherwise, accept only a complete address-word match.
    query_words = set(query.split())

    for result in results:
        address_words = set(
            normalize(result.get("display_name", "")).split()
        )

        if query_words and query_words.issubset(address_words):
            return result

    return None


def get_weather(city):
    try:
        location = find_location(city)

        if location is None:
            print("\nExact location match nahi mila.")
            print("Spelling ya address check karke dobara try karo.")
            return

        latitude = location["lat"]
        longitude = location["lon"]
        address = location.get("display_name", city)

        print("\nVerified location:", address)
        print("Weather data fetch ho raha hai...")

        url = (
            f"https://wttr.in/{latitude},{longitude}?format=j1"
        )

        data = fetch_json(url)
        current = data["current_condition"][0]

        print("\n" + "=" * 45)
        print("             CURRENT WEATHER")
        print("=" * 45)
        print("Location      :", address)
        print("Temperature   :", current["temp_C"], "°C")
        print("Feels Like    :", current["FeelsLikeC"], "°C")
        print("Condition     :", current["weatherDesc"][0]["value"])
        print("Humidity      :", current["humidity"], "%")
        print("Wind Speed    :", current["windspeedKmph"], "km/h")
        print("=" * 45)

    except (HTTPError, URLError, TimeoutError):
        print("\nWeather service se connection nahi ho paya.")
        print("Internet check karke dobara try karo.")

    except (KeyError, IndexError, ValueError, TypeError):
        print("\nWeather data process nahi ho paya.")
        print("Thodi der baad dobara try karen.")


print("=" * 45)
print("               WEATHER APP")
print("=" * 45)

while True:
    city = input("\nEnter city name or address: ").strip()

    if not city:
        print("City/address khaali nahi ho sakta.")
        continue

    get_weather(city)

    while True:
        again = input(
            "\nCheck another location? (y/n): "
        ).strip().lower()

        if again == "y":
            break
        elif again == "n":
            print("\nThank you for using Weather App!")
            raise SystemExit
        else:
            print("Sirf y ya n enter karo.")
