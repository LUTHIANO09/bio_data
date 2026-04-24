import time

#
# #Task 1  ARGUMENTS  (Positional, Keyword & Default)
# def well_report(well_name, pressure, status='Active', location='offshore', ):
#     print(well_name, pressure, status, location)
# #call 1 - positional only (use all defaults)
# well_report("Bonga-01",3850)
# # Call 2 — override status with keyword argument
# well_report('Erha-02', 4600, status='Under Review')
#
# # Call 3 — override both defaults
# well_report('Agbami-05', 2100, status='Inactive', location='Onshore')
#
# # Call 4 — all keyword arguments, no positional order
# well_report(pressure=820, well_name='Bonga-03', location='Deep Water')


#TASK 2  ·  *args  AND  **kwargs

#2A

def log_pressures(*readings):
    lst = []
    for reading in readings:
        lst.append(reading)
        print(f"'Reading{lst}'psi'")
    print(f"The highest Reading is {max(lst)}")

log_pressures(2100,3850,4600)
log_pressures(4100,3850,6600,7800,9100,3300)

#Task 2B **kwargs

def create_well_profile(**well_details):
    for key,value in well_details.items():
        print(key, ":", value)


create_well_profile(name="Bonga-01",status='Under Review',location='Onshore')
create_well_profile(name="Bonga-02",status='Under Review',location='Onshore', north='sokoto' '' ,state='taraba')

#Task 2C

def rig_summary(rig_name, *wells, **stats):
    print(rig_name)
    print(list(wells))
    print(stats)

rig_summary(
    'Bonga Field',
    'Bonga-01', 'Bonga-03', 'Bonga-07',
    total_output=12400, uptime_pct=94.2, crew_count=47
)

#Task 3 SCOPE  (Local, Global & Nonlocal)
rig_status = 'Operational'
def show_status():
    print(rig_status)

def update_status(new_status):
    global rig_status
    rig_status = new_status

show_status()
update_status("shutdown")
show_status()

#Task 3b Nonlocal
#
def pressure_tracker():
    current_max=0
    def update_max(reading):
        nonlocal current_max
        if reading  > current_max:
            current_max = reading
    update_max(3200)
    update_max(4800)
    update_max(1500)
    print(f'Peak pressure recorded: {current_max} psi')

pressure_tracker()

#Task 4A  DECORATORS

def log_call(func):
    def wrapper(*args, **kwargs):
        print('Function started')
        result = func(*args, **kwargs)
        print('Function complete')
        return result
    return wrapper

@log_call
def check_well(well_name):
    print(f'Checking: {well_name}')

check_well('Bonga-01')



#Task 4B Decorator with timing

def timer(func):
    def wrapper():
        before = time.time()
        func()
        after = time.time()
        print("Time:", after - before)
    return wrapper

@timer
def run_pressure_scan():
    for i in range(1_000_000):
        pass

run_pressure_scan()

# #Task  5 LAMBDA  (Anonymous Functions)

psi_to_bar = lambda psi: psi*0.0689476

print(psi_to_bar(3850))

format_well= lambda well,status: print(well,status)

format_well("Bonga-01","ACTIVE")


wells = [
    {'name': 'Bonga-01',  'pressure': 3850},
    {'name': 'Agbami-02', 'pressure': 650},
    {'name': 'Erha-02',   'pressure': 4600},
    {'name': 'Bonga-03',  'pressure': 820},
    {'name': 'Erha-05',   'pressure': 3200},
]

sorted_wells = sorted(wells, key=lambda w: ['pressure'], reverse=True)
fill= list(filter(lambda w: w['pressure'] > 3000,wells))
mapp= list(map(lambda w: (w['name'].upper(), w['pressure']), fill ))
print(sorted_wells)
print(max(well['pressure'] for well in sorted_wells))
print(fill)
print(mapp)

#Task 6A RECURSION

def re_countdown(n):
    if n < 0:
        print("You have the final count")
    else:
        print(n)
        re_countdown(n-1)

re_countdown(10)

#Task 6B

# def sum_readings(readings):
#     if len(readings) == 0:
#         return 0
#     else:
#         return readings[0] + sum_readings(readings[1:])
#     # empty= [0]
#     # readings= list(readings)
#     # empty.extend(readings)
#     # return sum(empty)
#
# test= [3850,820,4600,3200,650]
# print(sum_readings(test))


#Task 6C
#
# def find_deepest(wells, current_max=0):
       #Base case
#     if not wells:
#         return current_max

#     first_well = wells[0]
#     if first_well['pressure'] > current_max:
#         current_max = first_well['pressure']
       #recursive case
#     return find_deepest(wells[1:], current_max)
#
#
# wells = [
#     {'name': 'Bonga-01', 'pressure': 3850},
#     {'name': 'Erha-02', 'pressure': 4600},
#     {'name': 'Agbami-02', 'pressure': 650},
#     {'name': 'Bonga-03', 'pressure': 820},
#     ]
#
# print(find_deepest(wells))


#Task 7  GENERATORS  AND  RANGE

#Range 7A

# for a in range(11):
#     print(f'well-{a}')

# Task 7B Generator

def pressure_feed(readings):
    for reading in readings:
        yield reading
        if reading <= 1000:
            yield "CRITICAL"
        elif reading <= 2500:
            yield "Low"
        elif reading <= 1500:
            yield "Normal"
        else:
            yield "overpressure"
        # also yield the status for this reading
feed = pressure_feed([3850, 820, 4600, 3200, 650])
for item in feed:
 print(item)

pressure_feed([3850, 820, 4600, 3200, 650])

#Task 7C

def well_id_generator(prefix='Well'):
    n = 1
    while True:
        yield f'{prefix}-{n:03d}'
        n += 1

gen = well_id_generator()
# use next(gen) five times
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#Task 8 Bringing it all together

alert_threshold= 4000

def audit_log(function_name):
    print("AUDIT")
@audit_log
def classify_well(*readings, **metadata):
    for reading in readings:
        return reading / 2, metadata["name"]

is_critical=  lambda reading: reading < alert_threshold


def live_feed(wells):
    wells = list(wells)
    yield wells


def count_active(wells):
    wells = list(wells)
    if "active" in wells:
        print(wells)
        print(True)
        return wells.count("active")
    else:
        return "not available"


