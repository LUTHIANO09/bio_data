import json
import re
from pydoc import describe

from bio_data.advanced_functions import is_critical
from bio_data.rig_ops import pressure

#PART A — UTILITY TOPICS

# TASK 1 JSON it can be describe as the way how python talks to the outside world

# 1A Dict To Json

well_data = {
    "Name": "AGIP-01",
    "Pressure" : 2100,
    "Temp" : 1000,
    "Active" : "Normal",
    "Engineer" : "Civil engineer",
}
json.dumps(well_data) #  after i import jason then i use json.dumps then i parse my well_data as the parameter like that its now converted into a json

print(well_data)

json.dumps(well_data, indent=2) # on this line  i parse in two parameter which is the dictionary and the keyword indent and gave it a value that i want it to be indented with also making it readable for human

print(well_data)

json.dumps(well_data, indent=2, sort_keys=True) # on this line i also use json.dump then i parse the dictionary, the indent keyword and also a parameter to specify that it can be sorted

print(well_data)

# 1B JSON to Dict

json_str = '''
{
    "name": "Erha-02",
    "pressure": 3850,
    "temp": 185,
    "active": true,
    "engineer": "Fatima Bello"
}
'''
cont_to_python = json.loads(json_str) # on this line i created a variable called 'cont_to_python' then using the json.loads() will convert the json to pyton when the dictionary is parsed

print(cont_to_python["engineer"]) # Then i printed it calling the variable and accesing the dictionary with the key word nested inside the square brace

cont_to_python["pressure"] = 4200 # on this line i used the cont_to_python variable that now store the conversion from jason to python from there i was able to access my dictionary and get it updated

print(cont_to_python) # i printed the updated dictionary

cont_back_to_json = json.dumps(cont_to_python) # then after i created another variable to convert back to jason using json.dumps() which i parse the variable (i created to convert the initial jason to python) then this will convert it back to json
print(cont_back_to_json) # i printed the json here.

# 1C Read/write JSON file
well_1= {"Name": "AGIP-01","Pressure" : 2100, }
well_2 = {"Name": "AGIP-02","Pressure" : 3800, }
well_3 ={"Name": "AGIP-03", "Pressure" : 4250, } # on line 53 - 55 3 seperate dictionary was created

wells_jons = [well_1, well_2, well_3] # on this line the dictionary are stored as a list in wells_jons

to_python = json.dumps(wells_jons) #on this line the dictionary is converted into a json.dumps() which is printed on line 60
print(to_python,)

read_back = json.loads(to_python) # on this line the json is converted back to a dictionary using json.loads() which is printed on line 63
print(read_back)

for well in read_back:   # on this line
    print(f"The well name is {well['Name']} and pressure is {well['Pressure']} ")

#TASK 2 REGEX - PATTERN MATCHING

# 2A Search And Match

log_entry = 'Pressure alert triggered on Bonga-03 at 04:32 UTC'
checking = re.search(r"\w+-\d+",log_entry) # created a variable that store the regex stating the pattern i want as the out put which i used r"\w+- (return a match where the match has either capital or small letter and also other character like under score ) and \d+ to check if there is digit from 0-9 in the variable attached to

if checking:
    print(checking.group())

# Task 2B

ops_log = '''
Erha-02 pressure normal. Bonga-01 valve checked.
Agbami-05 flagged for review. Bonga-01 cleared.
Erha-02 output at 94%. Bonga-07 offline been-01.
'''
extract_well = re.findall(r"\w+-\d+",ops_log) # this line looks more like our previous task where we use r"\w+-\d+" where it actually check the variable if there is word that as a mixed of character and num

print(extract_well) # the action is printed here

if extract_well: # then i try to use a conditional statement to print out the variable and its index
    print(extract_well[2]) # here i can call any well id i want with just the index num

# Task 2C Value input

def validate_well_id(well_id): # as we know a fuction is writen
    if re.findall(r"\w+-\d+",well_id): # on this line a conditional statement was created using re.findall to check any number that is parsed into well id and check for the alphabet that is mixed with digit
        return True
    else:
        return "learn again"

print(validate_well_id("'Bonga-01' (valid), 'bonga1' (invalid), 'Agbami-05' (valid), 'WELL-003' (invalid — 3 digits"))
 #then i called my function to be printed here

# TASK 3   TRY / EXCEPT — Error Handling

# 3A Basic error catching
def safe_drive(a,b): # on this line of code i created a function which i will be using my try/except input that will be used for error handling
    a / b
    try:
        return a / b
    except ZeroDivisionError:
        return "cannot divide by zero"
    except TypeError:
        return "invalid input - numbers only"

print(safe_drive(100,4))
#print(safe_drive(100,0))
#print(safe_drive(100,"x"))

# 3B Multiple exceptions + finally

def load_well_pressure(data, key): # on this line of code what differentiate it was just the 'finally' that we added and also multiple except error handling
    if key in data:
        return data[key]
    try:
        return data[key]
    except KeyError:
        print("key not found in well data")
    except ValueError:
        print("Pressure value cannot be converted to number")
    finally:
        print("Pressure check complete")

print(load_well_pressure(well_data, "Pressure"))
print(load_well_pressure(well_data, ""))
print(load_well_pressure(well_data, "Engineer"))

# 3c raise your own error

def set_pressure(value):
    if value < 0:
        raise ValueError('Pressure cannot be negative')
    return value
try:
    set_pressure(-500)
except ValueError as e:
    print(f'Error caught: {e}')

print(set_pressure(400))

# TASK 4 String Formatting  ·  None  ·  User Input

# 4A String Formatting
well_name = "Bonga-01"
pressure = 4500
status = "Normal"

# firstly: using the % formatting
print("Well %s has pressure %d and status %s" % (well_name, pressure, status))

#secondly:

txt = "the well name is {} and the current pressure is {} which is {}"

print(txt.format(well_name, pressure, status))

#thirdly
txt_2 = f"the well name is {well_name} and the current pressure is {pressure:>8} which is {status}"
print(txt_2)

oil_rate = 4521.67
print(f"oil rate is {oil_rate:.2f} bbl/day")

# 4B None

engineer = None # created a variable that can be equals to none or carries a name

if engineer == None: # here is my conditional statement to print when the variable has no defined name or input
    print("no  engineer assigned")
else:
    print(f"engineer assigned {engineer}") # because the variable engineer is None this line of code will not run except if my variable 'engineer' has a name

def get_well_status(well): # on this line a function was created to run and check if a particular key is in a dictionary, we were ask to use status but in other to test my code i use another key that is available in my well_data dictionary
    if 'Active' in well:
        return well.get('Active')
    else:
        return None

print(get_well_status(well_data)) # on this line of code i printed my function here

#None == this is an inbuilt function thst indicate that there is no value (absence of value )
# 0 == this is  just an int representing zero (it cannot be added,multiply subtracted and divided from any other number )
# " == this just indicate that is  just an empty text just like a space bar it holds no alphabet

# 4C User Input

# enter_well_name = input("Enter well name: ")
# enter_pressure_reading = int(float(input("Enter pressure reading: ")))
# if enter_pressure_reading:
#     try:
#         enter_pressure_reading = float(enter_pressure_reading)
#     except ValueError:
#         print("only numeric value allow")
# print(f"The well name is {enter_well_name} and pressure is {enter_pressure_reading}")


# PART B OBJECT-ORIENTED PROGRAMMING

# TASK 5  CLASSES  ·  __init__  ·  self

class welly:

    def __init__(self, name, pressure, temp, Active =True, Engineer=None):
        self.name = name
        self.pressure = int(pressure)
        self.temp = float(temp)
        self.Active = Active
        self.Engineer = Engineer
    def describe(self):
        print(f"The well name is {self.name} and the pressure is {self.pressure} which had a temperature of {self.temp} where the current status is {self.Active} Active, and the engineer in charge is {self.Engineer}")

    def is_critical(self):
        if self.pressure < 1000 or self.temp > 300:
            return True
        else:
            return False

    def assign_engineer(self, name):
        self.Engineer = name

# 3 wells was created
wellx1 = welly("Bonga-01", 4500,200,True, Engineer="david",)
wellx2 = welly("Bonga-02", 2500,250,False, Engineer="James")
wellx3 = welly("Bonga-03", 900,300,False,)


for well in [wellx1, wellx2, wellx3]:  # calling describe function and is_critical function
    well.describe()
    print(f"is in .critical condition {well.is_critical()} ")
    print("" * 40)

wellx3.assign_engineer("ibrahim")  # on this line of code i assign an engineer to wellx3

print(wellx3.describe()) #on this line i printed the updated (wellx3)

# TASK 6 CLASS PROPERTIES  ·  Getters & Setters

class well:
    well_count = 0   # class variable — shared by all instances

    def __init__(self, name, pressure, temp):
        well.well_count += 1
        self.name = name
        self._pressure = pressure   # _ means 'private by convention'
        self.temp = temp

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, value):
        if value < 0:
            raise ValueError('Pressure cannot be negative')
        self._pressure = value

    @property
    def status(self):
        # your classification logic here
        if self._pressure < 1000:
            return 'CRITICAL'
        elif self._pressure < 2500:
            return 'LOW'
        elif self._pressure < 4500:
            return 'NORMAL'
        else:
            return 'OVER PRESSURE'

    @classmethod
    def get_well_count(cls):
        return cls.well_count

# 4 well was created below

well1 = well("Bonga-01", -4500, 200)
well2 = well("Bonga-02", 2500, 250, )
well3 = well("Bonga-03", -100, 300, )
well4 = well("Agbami-01", 5200, 180,)

lst = [well1, well2, well3, well4] #on this line i was store all the well as a list to be to call them when i loop through all the list of well as one

print(f" The total number of well in this class is {well.get_well_count()}") # on this line i printed the well with a method of get_well_count

try: # on this line of code i use the try/except to validate the pressure
    well.pressure = -100
except ValueError as e:
    print(f'this is a value error: {e}')

for wells in lst: #
    status = wells.status
    print(f'{wells.name} status is {status}')

# TASK 7  ·  INHERITANCE

class OffshoreWell(welly):   # inherits from Well
    def __init__(self, name, pressure, temp, water_depth, platform_type):
        super().__init__(name, pressure, temp)   # call parent __init__
        self.water_depth   = water_depth
        self.platform_type = platform_type

    def describe(self):
        # override parent describe() with extra info
        return f"Well name: {self.name}, Pressure: {self.pressure}, Temperature: {self.temp}, Water depth: {self.water_depth}m, Platform type: {self.platform_type}"

    def depth_rating(self):
        # your logic here
        if self.water_depth < 1500:
            return 'Ultra Deep'
        elif self.water_depth > 500:
            return 'Deep'
        else:
            return 'shallow'

class Onshore(welly):
    def __init__(self, name, pressure, temp, region, site_manager):
        super().__init__(name, pressure, temp)
        self.region = region
        self.site_manager = site_manager

    def describe(self):
        # override parent describe() with extra info
        return f"Well name: {self.name}, Pressure: {self.pressure}, Temperature: {self.temp}, region: {self.region}, site manager: {self.site_manager}"


    def is_remote(self):
        if "delta" or "basin" in self.region:
            return True
        else:
            return False

obj_off1 = OffshoreWell("ola-01",3000,200,900,"FPSO")
obj_off2 = OffshoreWell("Akerewodo-02",950,310,2000,"FIXED JACKET")
obj_on1 = Onshore("okuku_01", 1990, 400, "delta", "ibrahim")
obj_on2 = Onshore("ajaokuta_02",2500,500,"basin","portable")

lst2= [obj_off1, obj_off2]

lst3 = [obj_on1, obj_on2]

total_well = lst2 + lst3

for off in lst2:
    print(f"This is an offshore platform details {off.describe()} and also the condition of its criticallity is {off.is_critical()} and the depth is {off.depth_rating()}")
for on in lst3:
    print(f"The following is the details of our ONSHORE platform {on.describe()} which the the criticality level is {on.is_critical()} and is located in the niger delta {on.is_remote()}")

print(f"The current total number of well as at now is {well.get_well_count() + well.get_well_count()} ")

# TASK 8 POLYMORPHISM  (The Payoff Task)

# a mixed_list

mxd = lst2 + lst3

def run_inspection(wells):
    print('=' * 50)
    print('   DAILY RIG INSPECTION REPORT')
    print('=' * 50)
    for well in wells:
        well.describe()          # polymorphism — each class has its own version
        if well.is_critical():
            print(f'  ⚠ WARNING: {well.name} is in critical condition!')
        if isinstance(well, OffshoreWell):
            print(f'  Depth rating: {well.depth_rating()}')
        print()

run_inspection(mxd)

class SubseaWell(OffshoreWell):
    def __init__(self, name, pressure, temp, water_depth, platform_type,umbilical_length):
        super().__init__(name, pressure, temp, water_depth, platform_type)
        self.umbilical_length = umbilical_length
    def describe(self):
        print(f"The well name is {self.name} and the pressure is {self.pressure} which had a temperature of {self.temp} where the current status is {self.Active} Active, and the engineer in charge is {self.Engineer} and umbilical length is {self.umbilical_length}")


sub = SubseaWell("powei-01",1000,290,500,"FPSO",50)
mxd.append(sub)

run_inspection(mxd)

# TASK 9  ·  BRING IT ALL TOGETHER

#list of 4 differnt well

# Create objects
off1 = OffshoreWell("Bonga-01", 3000, 200, 900, "FPSO")
on1  = Onshore("Ajaokuta-02", 2500, 180, "basin", "Ibrahim")
sub1 = SubseaWell("DeepBlue-01", 800, 150, 2000, "FPSO", 120)
off2 = OffshoreWell("Agbami-03", 600, 220, 1700, "Fixed Jacket")

# Put them in ONE list
welli = [off1, on1, sub1, off2]

json.dumps()