# Smart Energy Consumption Calculator

 
COST_PER_UNIT = 8

def calculate_bill():
    """
    This function asks the user for units consumed,
    validates the input, and displays the electricity bill.
    """

    
    print("=" * 45)
    print("     SMART ENERGY CONSUMPTION CALCULATOR")
    print("=" * 45)

    # Step 2: Ask the user to enter units consumed
    user_input = input("Enter the number of electricity units consumed: ")

    # Step 3: Validate the input using try-except
    # This prevents the program from crashing if user enters text
    try:
        units_consumed = float(user_input)
    except ValueError:
        # This runs if the input cannot be converted to a number
        print("\n Invalid input! Please enter a numeric value only.")
        return  # Exit the function early since input is invalid

    # Step 4: Check that the value is not negative
    if units_consumed < 0:
        print("\n Invalid input! Units consumed cannot be negative.")
        return  # Exit the function early since input is invalid

    # Step 5: Calculate the total electricity bill
    total_amount = units_consumed * COST_PER_UNIT

    # Step 6: Display the result in a clean, professional format
    print("\n" + "-" * 45)
    print("               BILL SUMMARY")
    print("-" * 45)
    print(f"{'Units Consumed':<20}: {units_consumed}")
    print(f"{'Cost Per Unit':<20}: Rs. {COST_PER_UNIT}")
    print(f"{'Total Amount':<20}: Rs. {total_amount:.2f}")
    print("-" * 45)


def main():
    """
    Main driver function.
    Keeps asking the user if they want to calculate another bill.
    """
    while True:
        calculate_bill()

        # Step 7: Ask if the user wants to calculate another bill
        choice = input("\nDo you want to calculate another bill? (Y/N): ")

        # Step 8: Check the user's choice (case-insensitive)
        if choice.strip().upper() != "Y":
            print("\nThank you for using the Smart Energy Consumption Calculator!")
            break  # Exit the loop and end the program


# This ensures main() runs only when the script is executed directly
if __name__ == "__main__":
    main()
