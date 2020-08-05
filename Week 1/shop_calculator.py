def main():
    num = int(input("Number of items: "))
    if num < 0:
        print("Invalid number of items!")
        num = int(input("Number of items: "))
    sum = 0
    for i in range(int(num)):
        price = float(input("Price of item: "))
        sum += price
    if sum > 100:
        total_price = sum * 0.9
    else:
        total_price = sum
    print("Total price for ",num," items is ",total_price)
main()