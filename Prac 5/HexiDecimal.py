
COLOR_NAMES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb",
               "antiquewhite2": "#eedfcc", "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378",
               "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74",
               "azure1": "#f0ffff"}
color = input("Enter Color Name: ").lower()
while color != "":
    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
        print("")
    else:
        print("Invalid Color Name")
    print("All states:")
    for key, value in COLOR_NAMES.items():
        print(key,"is", value)
    color = input("Enter Color Name: ").lower()