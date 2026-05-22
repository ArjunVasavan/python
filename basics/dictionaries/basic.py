# to store key value pairs 

customer = {
        "Name" : "Arjun Vasavan",
        "Age"  : "29",
        "Status"  : "Jobless"
        }
# each key should be unique one a dictionaries 

print(customer)
print( customer["Name"] )
print( customer["Status"])
print(customer.get("Birthday"))  # you will get none if not present it doesnt show error 

customer["Birthday"] = "0/0/1900"

print(customer.get("Birthday"))  # you will get none if not present it doesnt show error 

print(customer)

