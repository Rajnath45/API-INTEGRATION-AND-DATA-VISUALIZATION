import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import sys

# Step 1: Set your API key and city
API_KEY = "26feb5b93cc5bca9e562b902ad3ea488"

CITY = "Delhi"

# Step 2: Build the API URL
url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Step 3: Make the API call
response = requests.get(url)
data = response.json()

# Step 4: Handle API failure
if "list" not in data:
    print("❌ Failed to fetch weather data.")
    print("🔍 Response:", data)
    sys.exit(1)

# Step 5: Parse forecast data
dates = []
temps = []

for entry in data["list"]:
    dt = datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S")
    temp = entry["main"]["temp"]
    dates.append(dt)
    temps.append(temp)

# Step 6: Plot the temperature trend
sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))
plt.plot(dates, temps, marker='o', linestyle='-', color='orange')
plt.title(f"5-Day Temperature Forecast for {CITY}")
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()

# Step 7: Save and show
plt.savefig("weather_forecast.png")
plt.show()
