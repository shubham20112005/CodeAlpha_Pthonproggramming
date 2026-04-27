def reply():
    if message == "hello":
        print("hii !")
    elif message == "how are you":
        print("I'm fine, thanks!")
    elif message == "bye":
        print("good bye!")
while True:
    message = input("user    ")
    reply()
