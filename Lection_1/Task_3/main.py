if input("To which temperature metric you want to convert?(F/C): ") == "C":
    print(f"{(float(input('Enter the temperature: '))-32) / 1.8} C")
else:
    print(f"{float(input('Enter the temperature: '))*1.8 + 32} F")