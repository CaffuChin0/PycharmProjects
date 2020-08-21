Color_name = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
              "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "	#eedfcc",
              "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
              "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
              "aquamarine4": "#458b74", "azure1": "#f0ffff"}
print(Color_name)

Color_code = input("Enter short state: ")
while Color_code != "":
    if Color_code in Color_name:
        print("{:>2}".format(Color_name[Color_code]))
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")
