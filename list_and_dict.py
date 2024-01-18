
# my_dict = {
#     "Nadim":"Chair",
#     "Shibbu":"Table",
#     "Heena":"Vessels",
#     "Papa":"Groceries",
# }
#
# print(my_dict)
#
# for key in my_dict:
#     print(key)
#     print(my_dict[key])
#
# print(my_dict["Shibbu"])
#
# travel_log = {
#     "India":"",
#     "Germany":"",
#     "Austria":"",
#     "UAE":"",
#     "Italy":"",
# }

# print("Enter country name ")
# country = input()
# print("Enter number of visits ")
# visits = input()
# print("Enter name of cities ")
# list_cities = input()
#
#
# def add_new_country(name, times_visited, cities_visited):
#     my_dict = {}
#     my_dict["country"] = name
#     my_dict["visit"] = times_visited
#     my_dict["list of cities"] = cities_visited
#     my_travel_log.append(my_dict)
#
#
# my_travel_log=[]
# add_new_country(country, visits, list_cities)
#print(my_travel_log)

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2])


