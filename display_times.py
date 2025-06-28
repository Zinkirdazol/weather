
diff --git a//dev/null b/display_times.py
index 0000000000000000000000000000000000000000..dbaa2987e035ea2afd4af9840b97a6c9af7ed3a2 100644
--- a//dev/null
+++ b/display_times.py
@@ -0,0 +1,52 @@
+import matplotlib.pyplot as plt
+from matplotlib.patches import Polygon
+from datetime import datetime
+from zoneinfo import ZoneInfo
+
+tr_time = datetime.now(ZoneInfo("Europe/Istanbul"))
+uk_time = datetime.now(ZoneInfo("Europe/London"))
+ny_time = datetime.now(ZoneInfo("America/New_York"))
+
+tr_str = tr_time.strftime("%d/%m/%Y %H:%M:%S")
+uk_str = uk_time.strftime("%d/%m/%Y %H:%M:%S")
+ny_str = ny_time.strftime("%d/%m/%Y %H:%M:%S")
+
+fig, ax = plt.subplots(figsize=(10, 5))
+
+# Set background to yellow
+fig.patch.set_facecolor("yellow")
+ax.set_facecolor("yellow")
+
+ax.set_xlim([-180, 180])
+ax.set_ylim([-90, 90])
+ax.axis("off")
+
+# Very rough continent outlines for a simple world map
+continents = [
+    [(-130, 25), (-75, 25), (-60, 50), (-75, 70), (-130, 65)],  # North America
+    [(-75, 25), (-50, -10), (-65, -55), (-80, -30)],            # South America
+    [(-10, 35), (0, 40), (30, 60), (40, 65), (20, 75), (-10, 70)],  # Europe
+    [(0, 35), (10, 30), (40, 30), (50, 0), (50, -20), (20, -35), (0, -35)],  # Africa
+    [(40, 65), (100, 70), (130, 60), (120, 40), (120, 10), (85, 10), (60, 30)],  # Asia
+    [(110, -10), (145, -10), (155, -35), (130, -45), (110, -30)],  # Australia
+    [(-60, 70), (-20, 80), (-40, 85), (-70, 85)],  # Greenland
+    [(-180, -60), (180, -60), (180, -90), (-180, -90)],  # Antarctica
+]
+
+for pts in continents:
+    poly = Polygon(pts, closed=True, facecolor="lightgray", edgecolor="gray")
+    ax.add_patch(poly)
+
+# Coordinates for cities
+locations = {
+    "Turkey (Istanbul)": (29.0, 41.0, tr_str),
+    "United Kingdom (London)": (-0.1, 51.5, uk_str),
+    "New York City": (-74.0, 40.7, ny_str),
+}
+
+for label, (lon, lat, time_str) in locations.items():
+    ax.plot(lon, lat, "ro")
+    ax.text(lon + 3, lat, f"{label}:\n{time_str}", fontsize=8, va="center")
+
+plt.tight_layout()
+plt.show()
