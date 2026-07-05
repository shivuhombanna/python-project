teket=50
while teket>0:
    print(f"availabal {teket}")
    booking=input("enter your booking (yes/no)").lower()

    if booking =="yes":
        teket -=1
        print("you are booking is Don")
        if teket==45:
            print("booking are alrady complited@@")
            break
    else:
        print("not availabal in setes !")
print("sorry all seat are booked ")

cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    print(city)
f=int(input("enter the num"))
for i in range(1,11):
    print(f"{f}*{i}={i*f}")

cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for index, city in enumerate(cities):
    print(f"{index}={city}")

for i in range(1,31):
    if i%3==0:
        print(i)

tot=0
for i in range(1,10):
    tot+=i
    print(tot)
nam=input("enter your name")
ovels="aeiouAEIOU"
count=0
for char in nam:
    if char in ovels:
        count+=1
print(count)
