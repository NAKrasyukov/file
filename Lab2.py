name = "a"
course = 0
university = "B"
#Цикл "слушающий" команды
while True:
    print("Input comand")
    q = input()
    # name
    if q == "name":
        print("Input name: ")
        name = input()
    #university
    elif q == "university":
        print("Input university: ")
        university = input()
    #course
    elif q == "course":
        print("Input course: ")
        course = input()
    #показывает все переменные
    elif q == "print":
        print("name: "+ name)
        print("course: "+ course)
        print("university: "+ university)
    #exit
    elif q == "exit":
        print("Bye!")
        break
    #не верная команда
    else:
        print("Unknown variable")
