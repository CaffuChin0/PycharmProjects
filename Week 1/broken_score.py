"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    if score < 0:
        print("Invalid score")
    else:
        if score >= 50:
            if score >= 90:
                if score > 100:
                    print("Invalid score")
                else:
                    print("Excellent")
            else:
                print("Passable")
        if score < 50:
            print("Bad")

main()