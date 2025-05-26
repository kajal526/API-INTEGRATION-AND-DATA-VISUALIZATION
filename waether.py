import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
sns.set(style="darkgrid")
API_KEY = "e6c76ccfad2809f24b578e0f28af5e28"
CITY = "Mumbai"  
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}
response = requests.get(BASE_URL, params=params)
data = response.json()
if data["cod"] != "200":
    print(f"Failed to fetch data: {data.get('message')}")
else:
    times = [datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S") for entry in data["list"]]
    temperatures = [entry["main"]["temp"] for entry in data["list"]]
    humidity = [entry["main"]["humidity"] for entry in data["list"]]
    pressure = [entry["main"]["pressure"] for entry in data["list"]]
    plt.figure(figsize=(16, 10))
    plt.subplot(3, 1, 1)
    sns.lineplot(x=times, y=temperatures, marker="o", color="tab:red")
    plt.title(f"Temperature Forecast for {CITY}")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.subplot(3, 1, 2)
    sns.lineplot(x=times, y=humidity, marker="s", color="tab:blue")
    plt.title(f"\nHumidity Forecast for {CITY}")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)
    plt.subplot(3, 1, 3)
    sns.lineplot(x=times, y=pressure, marker="^", color="tab:green")
    plt.title(f"\nPressure Forecast for {CITY}")
    plt.ylabel("Pressure (hPa)")
    plt.xlabel("Time\n\n\n\n")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.suptitle(f"\n5-Day Weather Forecast for {CITY}", fontsize=15, fontweight='bold', y=0.06)
    plt.show()