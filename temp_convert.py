def conv(val, unit):
    if unit == "C":
        return (val * 9/5) + 32  # Celsius to Fahrenheit
    elif unit == "F":
        return (val - 32) * 5/9  # Fahrenheit to Celsius
    else:
        return "Invalid unit"

def main():
    fahrenheit_list = [-4, 14, 32, 50, 68, 86, 104, 122]
    celsius_list = [-23, -5, 1, 34, 50, 26, 28, 30]

    print("Celsius: " + str([conv(i,"F") for i in fahrenheit_list]))
    print("Fahrenheit: " + str([conv(i,"C") for i in celsius_list]))
if __name__ == "__main__":
    main()