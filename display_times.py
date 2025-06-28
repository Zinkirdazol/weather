diff --git a//dev/null b/bursa_population.py
index 0000000000000000000000000000000000000000..819b4633e5f8776c49296c9290718e549b70bebe 100644
--- a//dev/null
+++ b/bursa_population.py
@@ -0,0 +1,35 @@
+import matplotlib.pyplot as plt
+
+# Approximate population data for Bursa districts in 2023 (numbers in thousands)
+# These values are placeholders; replace them with official statistics if available.
+population_by_district = {
+    "Osmangazi": 884,
+    "Yildirim": 665,
+    "Nilufer": 520,
+    "Inegol": 296,
+    "Gemlik": 120,
+    "Mudanya": 100,
+    "Mustafakemalpasa": 103,
+    "Karacabey": 84,
+    "Kestel": 74,
+    "Gursu": 97,
+    "Orhangazi": 81,
+    "Yenisehir": 55,
+    "Iznik": 45,
+    "Orhaneli": 19,
+    "Buyukorhan": 12,
+    "Harmancik": 5,
+    "Keles": 10,
+}
+
+districts = list(population_by_district.keys())
+values = list(population_by_district.values())
+
+plt.figure(figsize=(12, 6))
+plt.bar(districts, values, color="skyblue")
+plt.xlabel("District")
+plt.ylabel("Population (thousands)")
+plt.title("Bursa 2023 Population by District (Approximate)")
+plt.xticks(rotation=45, ha="right")
+plt.tight_layout()
+plt.show()
