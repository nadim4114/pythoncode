
# create an empty dictionary

dict_new = {}

# Add items to dictionary

dict_new["Key"] = "Value"
#print(dictionary)

# reassign a dictionary

dict_new = {
    "Nadim" :"90",
    "Shibbu":"80",
    "Nabeel":"70",
    "Papa":"60",
    "Heena":"30",
    "Shammo":"20",
    "Baji":"20"
}

#print(dictionary)

#retrieve an item from dictionary

item = dict_new["Nadim"]
#print(type(item))
#print(item)

#reassign a value of key to dictionary
dict_new["Nadim"] = "191"
#print(dictionary)

#Loop through the dictionary to retrieve key or values
print(dict_new)
for key in dict_new :

    print(key)
    print(dict_new[key])

