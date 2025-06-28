import matplotlib.pyplot as plt
from datetime import datetime
from zoneinfo import ZoneInfo

tr_time = datetime.now(ZoneInfo("Europe/Istanbul"))
uk_time = datetime.now(ZoneInfo("Europe/London"))
ny_time = datetime.now(ZoneInfo("America/New_York"))

tr_str = tr_time.strftime("%d/%m/%Y %H:%M:%S")
uk_str = uk_time.strftime("%d/%m/%Y %H:%M:%S")
ny_str = ny_time.strftime("%d/%m/%Y %H:%M:%S")

fig, ax = plt.subplots()
ax.axis("off")
ax.text(0.5, 0.8, f"tr_time: {tr_str}", ha="center", va="center", fontsize=12)
ax.text(0.5, 0.6, f"uk_time: {uk_str}", ha="center", va="center", fontsize=12)
ax.text(0.5, 0.4, f"ny_time: {ny_str}", ha="center", va="center", fontsize=12)

plt.show()

