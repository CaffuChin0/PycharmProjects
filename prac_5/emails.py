def printer(email, name):
    print("Email:", email,
          "Is your name ", name, "? (Y/n)", )


def askEmail():
    email = input("What's your Email?")
    return email


def askName():
    name = input("What's your name?")
    return name


if __name__ == '__main__':
    type(askEmail(), askName())
