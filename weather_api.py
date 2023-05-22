import requests
import json
import matplotlib.pyplot as plt
import mplcursors

url = "https://api.open-meteo.com/v1/forecast?latitude=49.1324&longitude=37.3633&hourly=temperature_2m"
response = json.loads(requests.get(url).text)

x_points = response.get('hourly').get('time')
x_points = [x[5:] for x in x_points]
y_points = response.get('hourly').get('temperature_2m')


plt.xticks(rotation=90, fontsize=5)
plt.plot(x_points, y_points)
mplcursors.cursor(hover=True)
plt.show()
