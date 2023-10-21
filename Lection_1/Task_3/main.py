temperature = float(input('Enter the temperature: '))
if input("To which temperature metric you want to convert?(F/C): ") == "C":
    print(f"{(temperature-32) / 1.8} C")
else:
    print(f"{temperature*1.8 + 32} F")