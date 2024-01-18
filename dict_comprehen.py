import random

# names = ["Nadim", "Heena", "Shibbu", "Papa", "Juweria"]
# scores = [10,30,50,65,80]
#
# #create dictionary from a list
# score_record = {item:random.randint(10,100) for item in names}
# print(score_record)
#
# #create dictionary from a dictionary
# passed_stud = {student:score for (student,score) in score_record.items() if score > 60}
# print(passed_stud)


# create a dictionary from a sentence and count its words and letters
# my_string = input()
# my_list = my_string.split(' ')
# print(my_list)
# my_dict = {word:len(word) for word in my_list }
# print(my_dict)



weather_c = {"Monday":15, "Tuesday":18, "Wednesday":22, "Thursday":15, "Friday":12}

print(weather_c.items())

weather_f = {day:temp*9/5 +32 for (day,temp) in weather_c.items()}
print(weather_f)



