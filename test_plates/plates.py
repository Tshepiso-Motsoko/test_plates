def main():
    # Get user input for the plate
    plate = input("Plate: ")
    # Print 'Valid' if the plate is valid according to is_valid function else print 'Invalid'
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check for length requirement (between 2 and 6 characters)
    if len(s) < 2 or len(s) > 6:
        return False

    # Check for letter requirement at the start (the first two characters must be alphabets)
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Check for no punctuation, spaces, or periods (the plate must be alphanumeric)
    if not s.isalnum():
        return False

    # Check for number requirement at the end (numbers must follow the letters)
    encountered_digit = False
    for i in range(2, len(s)):
        if s[i].isalpha() and encountered_digit:
            return False
        elif s[i].isdigit():
            if s[i] == '0' and i != len(s) - 1 and s[i + 1].isdigit():
                return False
            encountered_digit = True

    return True


if __name__ == "__main__":
    main()
