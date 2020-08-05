def main():
    total_age = 0
    number_of_people = 0
    age = int(input("Enter Age (-1 or negative age) to exit: "))
    while age >= 0:
        total_age += 1
        number_of_people += 1
        age = int(input("Enter Age (-1 or negative age) to exit: "))

    if number_of_people:
        average_age = total_age / number_of_people
        print("Average age is: ", average_age)
    else:
        print("No values entered")

if __name__ == '__main__':
    main()