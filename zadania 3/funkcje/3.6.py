def shownamentimes():
    name = input("Enter your name: ")
    try:
        num = int(input("Enter how many times print your name"))
        for i in range(num):
            print(name)
    except ValueError:
        if name == "":
            name = "Adam"
            num = 7
            for i in range(num):
                print(name)
        else:
            print("no action taken")

shownamentimes()
