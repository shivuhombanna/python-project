def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b

def menu():
    print("welcom to cal")
    print("1.add\n2.sub\n3.mul\n4.exit")

while True:
    menu()
    choice=int(input("enter walid choice  "  ))

    if choice in{1,2,3}:
        a=int(input("enter 1st num"))
        b=int(input("enter 2st num"))
        
        if choice==1:
            print("result ",add(a,b))
        elif choice==2:
            print("result ",sub(a,b))
        elif choice==3:
            print("result ",sub(a,b))
        elif choice==4:
            print("exit")
            break
    else:
        print("trai again later !!")