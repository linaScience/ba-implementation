#!/usr/bin/env python3
import os

folder = "/Users/lina/Desktop/ba-implementation/train/5d27075f03f801723c2e360f/F1/"
category_counts = {}
total_lines_without_hash = 0
unique_ssids = set()
unique_bssids = set()
rssi_values = []

# Read the file and extract SSIDs and BSSIDs for TYPE_WIFI category
with open(os.path.join(folder, "aggregated.txt"), "r") as file:
    for line in file:
        if not line.strip().startswith("#"):
            total_lines_without_hash += 1
            columns = line.split()

            if len(columns) > 1:
                category = columns[1]
                category_counts[category] = category_counts.get(category, 0) + 1
            if len(columns) > 4 and columns[1] == "TYPE_WIFI":
                ssid = columns[2]
                bssid = columns[3]
                unique_ssids.add(ssid)
                unique_bssids.add(bssid)
                rssi = int(columns[4])
                rssi_values.append(rssi)


category_counts, total_lines_without_hash

min_rssi = min(rssi_values)
max_rssi = max(rssi_values)
min_rssi, max_rssi

len(unique_ssids), len(unique_bssids)
