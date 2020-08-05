name = input("Enter your name: ")

print("Your name is ",name)
F = open('name.txt', 'r')
line = F.readline()
print(line)