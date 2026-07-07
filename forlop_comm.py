# l=[1,2,3,4,5,6,7,8,9,]
# num=[num**2 for num in l]
# print(num)

# student_info=[{"name": "Rahul", "age": 20, "marks": 85},
#               {"name": "Sneha", "age": 21, "marks": 92},
#               {"name": "Amit", "age": 19, "marks": 78}
# ]
# for i in student_info:
#     print("name",i["name"])
#     print("age",i["age"])
#     print("nmaek",i["marks"])
#     print("======================================")

# cities = {
#     "Bengaluru": 13600000,
#     "Mysuru": 1270000,
#     "Hubballi": 950000,
#     "Mangaluru": 620000,
#     "Belagavi": 610000,
#     "Kalaburagi": 670000,
#     "Davanagere": 500000,
#     "Ballari": 410000,
#     "Shivamogga": 330000,
#     "Tumakuru": 310000
# }
# bilow={city:pop for city,pop in cities.items()
#         if pop>=1000000}
# print(bilow)

# def tabel(num):
#     for i in range(1,11):
#         print(f"{num}*{i}={num*i}")
# tabel(7)
# print("------------------")
# tabel(9)

# def funk(num):
#     return int(num)**4
# a=100
# b= a + funk(4)
# print(b)
# # lambda function
# duble= lambda c:c*2
# print(duble(677 ))

def factorial(n):
    if n==1:
        return 1
    return n* factorial(n-1)
print(factorial(4))