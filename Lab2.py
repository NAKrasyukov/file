name = "a"
course = 0
university = "B"
while True:
    print("Input variable")
    q = input()
    if q == "name":
        print("Input name: ")
        name = input()
    elif q == "university":
        print("Input university: ")
        university = input()
    elif q == "course":
        print("Input course: ")
        course = input()
    elif q == "print":
        print("name: "+ name)
        print("course: "+ course)
        print("university: "+ university)
    else:
        print("Unknown variable")
