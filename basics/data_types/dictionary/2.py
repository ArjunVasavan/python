person_1 = {"name" : "Alice", "age" : 30, "city" : "Vinland" }

  # or we can also use 

person_2 = dict(name = "Brian", age = 40, city = "Canada")

print(person_1["name"])

age = person_1.get("age")

print(f"His Age is {age}")

job = person_1.get("job","unknown")  # unknown is for default fallback

print(f"His job is {job}")


