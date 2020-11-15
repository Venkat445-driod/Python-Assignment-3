skillsanta_Dict ={"name": "Sachin", "age": 22, "salary": 60000, "city": "New Delhi"}
print("Before changing:",skillsanta_Dict)
x=skillsanta_Dict.pop("city")
skillsanta_Dict["location"]=x
print("after changing:",skillsanta_Dict)