

students = {
    "harry":"sarbah",
    "barry":"akuafo",
    "garry":"legon",
    "jerry":"nelson",
}

for student in students:
    print(student) 


# lists

register = [
    {"name":"harry", "house": "sarbah", "patronus": "vikings"},
    {"name":"barry", "house": "akuafo", "patronus": "farmers"},
    {"name":"garry", "house": "legon", "patronus": "chickens"},
    {"name":"jerry", "house": "nelson", "patronus": None}
]

for student in register:
    print(student["name"], student["house"], student["patronus"], sep=" , ")