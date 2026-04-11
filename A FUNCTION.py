# def olamide(fname,age,country):
#     print(fname,age, country + "NDI")
#
# olamide("ibrahim",77 ,"USA ")
# olamide("Bamidele",65, "canada ")





#DAY TASK

#A1

def greet_engineer(name="Engineer"):
    print(f"Good morning,{name}! are you ready to monitor the rig?")
    # print("good morning" + name ,"" + "are you ready to monitor the rig?")

greet_engineer("Emeka")
greet_engineer("Rukewe")
greet_engineer("Bashir")
greet_engineer()

#A2

def rig_status(well_nane,is_active):
    if is_active:
        print(well_nane + "is ONLINE")
    elif not is_active:
        print(well_nane + "is OFFLINE (maintenance required)")

rig_status("okuku ",True)
rig_status("Agbabika ",False)
rig_status("Casablanca",True)

#A3

def calculate_daily_output(flow_rate, hours_active):
    return flow_rate * hours_active



print(f"Daily output:{calculate_daily_output(30,60)} Barrels")

print(calculate_daily_output(30,60))
print(calculate_daily_output(50,60))
print(calculate_daily_output(65,60))

#TASK B

#B1
def classify_pressure(pressure):
    if pressure < 1000:
          return 'CRITICAL'
    elif 1000 <= pressure < 2500:
         return 'LOW'
    elif 2500 <= pressure < 4500:
        return 'NORMAL'
    elif pressure >= 4500:
        return 'OVERPRESSURE'
    else:
        return 'Invalid'


print(classify_pressure(200))
print(classify_pressure(2900))
print(classify_pressure(5000))
print(classify_pressure(7000))

#B2
def maintenance_due(days_since_service):
    if days_since_service > 90:
        return "OVERDUE"
    elif days_since_service > 60:
        return "Due soon"
    else:
        return "OK"

print(maintenance_due(30))
print(maintenance_due(79))
print(maintenance_due(91))

#B3

def access_level(role):
    match role:
        case "supervisor":
            return "Full access"
        case "engineer":
            return  "Operational access"
        case "contractor":
            return  "Limited access"
        case "olamide":
            return "OWNER"
        case _:
            return "No access"

print(access_level("supervisor"))
print(access_level("engineer"))
print(access_level("contractor"))
print(access_level("olamide"))


#TASK C

def check_all_wells(wells):
    wells = [
        {"name": "Bonga-01", "pressure": 3850},
        {"name": "Bonga-03", "pressure": 820},
        {"name": "Erha-02", "pressure": 4600},
        {"name": "Erha-05", "pressure": 3200},
        {"name": "Agbami-02", "pressure": 650},
    ]
    for well in wells:
            status = classify_pressure(well["pressure"])
            print(well["name"], "|", well["pressure"],"psi |", status  )


print(check_all_wells("Bonga-01"))

#C2

def count_critical(wells):
    count = 0
    wells = [
        {"name": "Bonga-01", "pressure": 3850},
        {"name": "Bonga-03", "pressure": 820},
        {"name": "Erha-02", "pressure": 4600},
        {"name": "Erha-05", "pressure": 3200},
        {"name": "Agbami-02", "pressure": 650},
    ]

    for well in wells:
        if well["pressure"] < 1000:
            count += 1
    return count
total_critical = classify_pressure(count_critical("Bonga-03"))
print(total_critical)

print(f"{count_critical("wells")} {total_critical} well are in CRITICAL condition")

print(count_critical("wells"))

#C3

def pressure_monitor():
    while True:
        operator = input("Enter pressure reading (or 0 to quit): ")
        pressure = int(operator)
        if pressure == 0:
            print("pressure reading stopped")
            break
        status = classify_pressure(pressure)
        print("Status: ", status)


print(pressure_monitor())

#Task D

def run_daily_check(wells):
    wells = [
        {"name": "Bonga-01", "pressure": 3850},
        {"name": "Bonga-03", "pressure": 820},
        {"name": "Erha-02", "pressure": 4600},
        {"name": "Erha-05", "pressure": 3200},
        {"name": "Agbami-02", "pressure": 650},
    ]

    for well in wells:
        if well["pressure"] == 0:
            continue
        maintenance_due(45)
        print(f"{well} Maintenance: {maintenance_due(45)}")

print(run_daily_check("wells"))

def summarise_wells(wells):
    print(f"The total well checked {check_all_wells("well")} "
        f"{count_critical("well")} are in CRITICAL status and also"
        f" {maintenance_due(60)} for maintenance")

print(summarise_wells("wells"))
