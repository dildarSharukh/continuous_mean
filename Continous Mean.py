# Define a function to continuously calculate the mean of numbers input by the user.
def continuous_mean():
    # Initialize variables to keep track of the count of numbers and the mean.
    count = 0
    mean = 0.0

    # Continue looping until user enters 'x' to end.
    while True:
        # Prompt user to enter a number or 'x' to end.
        user_input = input("Enter a number (or 'x' to end): ")

        # If user enters 'x', exit the program.
        if user_input.lower() == 'x':
            print("Exiting program.")
            break

        try:
            # Attempt to convert user input to a float.
            number = float(user_input)
        except ValueError:
            # If user input is not a valid number, prompt for valid input and continue loop.
            print("Invalid input. Please enter a valid number or 'x' to end.")
            continue

        # Increment count and update mean using the new input.
        count += 1
        mean = (mean * (count - 1) + number) / count
        
        # Print the updated mean value.
        print("Mean value:", mean)

# Call the function to start the continuous mean calculation.
continuous_mean()