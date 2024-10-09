#hurricane wind classifier

wind = input("What is the wind speed?\n>")

if wind <= "74":
    print("Tropical storm")

elif wind <= "96":
    print("Category 1 hurricane")

elif wind <= "111":
    print("Category 2 hurricane")

elif wind <= "130":
    print("Category 3 hurricane")

elif wind <= "157":
    print("Category 4 hurricane")

elif wind >= "157":
    print("Category 5 hurricane")