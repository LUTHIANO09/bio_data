
list_of_state= ["ibadan","oyo", "kwara", "osun"]

list_of_state[3]= 'ilorin'

list_of_state.insert(3,"Abuja")
list_of_state.append("osogbo")
# print(list_of_state)

new_list= ['ikeja', 'alimosho', 'kosofe', 'agege','oshodi']

new_list.extend(list_of_state)

print(new_list)


