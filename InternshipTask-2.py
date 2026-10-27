def unit_converter():
    while True:
        print("\n===== UNIT CONVERTER TOOL =====")
        print("1. Length Converter")
        print("2. Weight Converter")
        print("3. Temperature Converter")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("\n1. Kilometer to Meter")
            print("2. Meter to Kilometer")
            print("3. Meter to Centimeter")
            print("4. Centimeter to Meter")

            option = input("Choose conversion: ")
            value = float(input("Enter value: "))

            if option == '1':
                result = value * 1000
                unit = "meters"
            elif option == '2':
                result = value / 1000
                unit = "kilometers"
            elif option == '3':
                result = value * 100
                unit = "centimeters"
            elif option == '4':
                result = value / 100
                unit = "meters"
            else:
                print("Invalid option!")
                continue

            print("Result:", result, unit)

        elif choice == '2':
            print("\n1. Kilogram to Gram")
            print("2. Gram to Kilogram")
            print("3. Kilogram to Pound")
            print("4. Pound to Kilogram")

            option = input("Choose conversion: ")
            value = float(input("Enter value: "))

            if option == '1':
                result = value * 1000
                unit = "grams"
            elif option == '2':
                result = value / 1000
                unit = "kilograms"
            elif option == '3':
                result = value * 2.20462
                unit = "pounds"
            elif option == '4':
                result = value / 2.20462
                unit = "kilograms"
            else:
                print("Invalid option!")
                continue

            print("Result:", round(result, 4), unit)

        elif choice == '3':
            print("\n1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            print("3. Celsius to Kelvin")

            option = input("Choose conversion: ")
            value = float(input("Enter temperature: "))

            if option == '1':
                result = (value * 9/5) + 32
                unit = "Fahrenheit"
            elif option == '2':
                result = (value - 32) * 5/9
                unit = "Celsius"
            elif option == '3':
                result = value + 273.15
                unit = "Kelvin"
            else:
                print("Invalid option!")
                continue

            print("Result:", round(result, 2), unit)

        elif choice == '4':
            print("Thank you for using Unit Converter!")
            break

        else:
            print("Invalid choice! Please try again.")


unit_converter()
