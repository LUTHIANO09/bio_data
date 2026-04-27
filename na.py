# def find_deepest(wells, current_max=0):
#     # Base case
#     if not wells:
#         return current_max
#
#     first_well = wells[0]
#     if first_well['pressure'] > current_max:
#         current_max = first_well['pressure']
#     # recursive case
#     return find_deepest(wells[1:], current_max)



wells = [
    {'name': 'Bonga-01', 'pressure': 3850},
    {'name': 'Erha-02', 'pressure': 4600},
    {'name': 'Agbami-02', 'pressure': 650},
    {'name': 'Bonga-03', 'pressure': 820},
]
print(wells[:3])
#print(find_deepest(wells))
