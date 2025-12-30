"""
Docstring for data-collection.4-dictionary

Dict | mutable | ordered | indexing and slicing is not allowed and duplicate keys are not allowed

syntax

dict_name = {}
dict_name = dict()


Example :

dict_name = {
    "key1": "value1",
    "key2": "value2",
    ...,
    "keyn": "valuen"
}

"""

# fruit = {
#     "apple": 7,
#     "guava": 5,
#     "banana": "1dozn",
#     "banana": "2dozn", # duplicate keys are not allowed
# }

# print(fruit)


contact = [
    {
        "A": [
            {
                "aman":{
                    "mobile":["98748536","847589549"],
                    "email":["aman@gmail.com"]
                }
            },{
                "ajay":{
                    "mobile":["987478648536","84758954354349"],
                    "email":["ajay@gmail.com", "ajay1@gmail.com"]
                }
            }
        ]
    },{
        "B": [
            {
                "bubben":{
                    "mobile":["98748536","847589549"],
                    "email":["bubben@gmail.com"]
                }
            },{
                "bunty":{
                    "mobile":["987478648536","84758954354349"],
                    "email":["bunty@gmail.com", "bunty1@gmail.com"]
                }
            }
        ]
    },{
        "C": [
            {
                "chaman":{
                    "mobile":["98748536","847589549"],
                    "email":["chaman@gmail.com"]
                }
            },{
                "chandu":{
                    "mobile":["987478648536","84758954354349"],
                    "email":["chandu@gmail.com", "chandu1@gmail.com"]
                }
            }
        ]
    }
]
# print(dir(contact))

# print(type(contact))
# print(type(contact[0]))
# print(contact[0]["A"])
# print(contact[0]["A"][1])
# print(contact[0]["A"][1]["ajay"])
# print(contact[0]["A"][1]["ajay"]["email"])
# print(contact[0]["A"][1]["ajay"]["email"][-1])

car = {
    "name":"BMW",
    "price":"40L",
    "color":"black"
}

# print(dir(car))

# car.clear()
# car1 = car.copy()


# print(car.keys())

# for key in car.keys():
#     print(key, car[key])

# for val in car.values():
#     print(val)

# for key, val in car.items():
#     print(key, car[key])


# print(car.items())



# print(car.get("name"))

# for key in car.keys():
#     print(car.get(key))

# car.pop("name")
# car.popitem()

# print(car)


# items = ["tomato", "potato", "onion"]
# price = 50

# vegs = dict()



# print(vegs.fromkeys(items, price))


# car = {
#     "name":"BMW",
#     "price":"40L",
#     # "color":"red"
# }

# car.setdefault("color", "black")

# print(car)


car1 = {
    "name":"BMW",
}

car2 = {
    "price":"40L",
}

car3 = {
    "color":"red"
}

car1.update(car2)
car1.update(car3)

print(car1)