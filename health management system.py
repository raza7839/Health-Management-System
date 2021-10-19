p = 0
def getdate():
    import datetime
    global p
    p = str(datetime.datetime.now())


def hms():
    while True:
        y = input("Do you want to work on 'diet' or 'exercise': ")
        if y == "diet":
            while True:
                x = input("Do you want to 'retrieve' or 'log' your file: ")
                if x == "log":
                    getdate()
                    d.write(str([p]))
                    d.write(" :- ")
                    d.write(input("Enter details to be added: "))
                    d.write("\n")
                    print("Details added.")
                    break
                elif x == "retrieve":
                    d.seek(0)
                    print(d.read())
                    break
                else:
                    print("invalid input.")
                    continue
            break


        elif y == "exercise":
            while True:
                x = input("Do you want to 'retrieve' or 'log' your file: ")
                if x == "log":
                    getdate()
                    e.write(str([p]))
                    e.write(" :- ")
                    e.write(input("Enter details to be added: "))
                    e.write("\n")
                    print("Details added.")
                    break
                elif x == "retrieve":
                    e.seek(0)
                    print(e.read())
                    break
                else:
                    print("invalid input.")
                    continue
            break
        else:
            print("invalid input.")
            continue

while True:
    print("Three users available:ahmad, ayan, moaz.")
    z = input("Enter name to access your data: ")
    if z == "ahmad":
        d = open("ahmad_diet.txt","a+")
        e = open("ahmad_exercise.txt","a+")
        break
    elif z == "ayan":
        d = open("ayan_diet.txt","a+")
        e = open("ayan_exercise.txt","a+")
        break
    elif z == "moaz":
        d = open("moaz_diet.txt","a+")
        e = open("moaz_exercise.txt","a+")
        break
    else:
        print("invalid input.")
        continue


while True:
    hms()
    v = input("Enter 'y' to restart or type anything to exit.")
    if v == "y":
        continue
    else:
        break

print("SEE YOU LATER.")

d.close()
e.close()