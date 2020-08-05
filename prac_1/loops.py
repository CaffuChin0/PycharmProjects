def main():

    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for j in range(0, 101, 10):
        print(j, end=' ')
    print()

    for k in range(20, 0, -1):
        print(k, end=' ')
    print()

    stars = int(input("Enter a number:"))
    for _ in range(stars):
        print("*" * (_+1))
        stars += 1
main()