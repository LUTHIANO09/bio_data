

# rig_ops.py
# NDI Phase 2 — Rig Operations Data System
# Author: IBRAHIM OLAMIDE L

# ── STARTER DATA ─────────────────────────────────────

# List of well dictionaries
wells = [
    {"name": "Bonga-01",   "pressure": 3850, "temp": 185, "active": True,  "engineer": "Emeka Eze"},
    {"name": "Bonga-03",   "pressure": 820,  "temp": 310, "active": True,  "engineer": "Chidi Obi"},
    {"name": "Erha-02",    "pressure": 4600, "temp": 200, "active": True,  "engineer": "Fatima Bello"},
    {"name": "Bonga-07",   "pressure": 2100, "temp": 175, "active": False, "engineer": "N/A"},
    {"name": "Erha-05",    "pressure": 3200, "temp": 290, "active": True,  "engineer": "Tunde Adeyemi"},
    {"name": "Agbami-02",  "pressure": 650,  "temp": 165, "active": True,  "engineer": "Ngozi Okafor"},
]

# Tuple of rig coordinates (NEVER changes)
rig_location = ("Bonga Field", 3.7800, 5.6200)

# Set of known alert types (starts empty)
active_alerts = set()

# ── YOUR CODE GOES BELOW THIS LINE ───────────────────


#TASK 1
for x in wells:
    print(x["name"])

print(wells[0:3])

print(len(wells))

wells.append({"name": "Agbami-05", "pressure": 3100, "temp": 195, "active": True, "engineer": "Yemi Coker"})
print(wells)

for x in wells:
    if x["name"] == "Bonga-07":
        wells.remove(x)

print(len(wells))

# TASK 2

print(rig_location)

print(rig_location[0])

print(f"latitude: {rig_location[1]}")

#rig_location[1]= 4.0  #TypeError: 'tuple' object does not support item assignment

print("REASON why i cant change the latitude to 4.0Tuples are unchangeable,\n meaning that we cannot change,\n add or remove items after the tuple has been created.")

#TASK3


# alert_log = [
#     "pressure_high", "valve_leak", "pressure_high",
#     "temp_spike", "valve_leak", "pump_failure", "pressure_high"
# ]
unique_alerts= {"pressure_high", "valve_leak", "pressure_high","temp_spike", "valve_leak", "pump_failure", "pressure_high"}
print(unique_alerts)

unique_alerts.add("gas_leak")

unique_alerts.discard("temp_spike")
print(unique_alerts)
if "valve_leak" in unique_alerts:
    print("ALERT")

#Task 4

well_profile = {
    "name":         "Bonga-01",
    "pressure":     3850,
    "temp":         185,
    "status":       "Active",
    "engineer":     "Emeka Eze",
    "last_checked": "2026-04-01"
}
print(well_profile)

for x,y in well_profile.items():
    print(x,y)

well_profile["pressure"]= 4100
print(well_profile)

well_profile.update({"Next service" : "2026-05-01"})
print(well_profile)

del well_profile["temp"]
print(well_profile)

for x in well_profile.keys():
    if x == "status":
        print(True)

print(well_profile.keys())
print(well_profile.values())

for x in wells:
    if x ["active"]== False:
        continue
#
# pressure= wells set"pressure"
# temp= wells["temp"]

# status_1 = "CRITICAL"
# status_2 = "LOW PRESSURE"
# status_3= 'HIGH TEMP'
# status_4= 'NORMAL'

if pressure < 1000:
    status = 'CRITICAL'
elif pressure < 2500:
    status = 'LOW PRESSURE'
elif temp > 280:
    status = 'HIGH TEMP'
else:
    status = 'NORMAL'
