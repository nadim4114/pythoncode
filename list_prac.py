#create empty list
list_of_states = []
#print(list_of_states)

#create a list with some items
list_of_states = ["Gujarat","Maharashtra","Rajasthan","Jharkand"]
#print(list_of_states)

# append a list to add item to the last
list_of_states.append("Maharashtra")
#print(list_of_states)

# extend a list to with 2 or more items at a time
list_of_states.extend(["Tamilnadu","Kerela","Karnataka"])
#print(list_of_states)

# remove a first item from list using item name
list_of_states.remove("Maharashtra")
#print(list_of_states)

# pop or remove a item from list from last
list_of_states.pop()
#print(list_of_states)

#remove a item using pop giving index number
val = list_of_states.pop(3)
print(list_of_states)
#print(f"removed item from list is {val}")



