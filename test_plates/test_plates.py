# Import the is_valid function from the plates module
from plates import is_valid

# Define a test function to validate license plates
def test_is_valid():
    # The first four characters should be letters and the remaining characters should be digits
    assert is_valid('AB123') == True
    assert is_valid('ABC123') == True
    assert is_valid('AB1234') == True
    # The license plate should not be more than 6 characters long
    assert is_valid('AB12345') == False
    # The first two characters should be letters
    assert is_valid('A123') == False
    # A letter should not follow a digit
    assert is_valid('ABC12A') == False
    # The license plate should not contain non-alphanumeric characters
    assert is_valid('ABC_123') == False
    # A '0' should not precede other digits
    assert is_valid('A0B123') == False

# Define a test function to validate incorrect license plates
def test_is_not_valid():
    # The first two characters should be letters
    assert is_valid('A12345') == False
    assert is_valid('1B1234') == False
    # The license plate should not contain spaces
    assert is_valid('AB1 234') == False
    # The license plate should not contain punctuation
    assert is_valid('AB-123') == False
    # A '0' should not precede other digits
    assert is_valid('A0B123') == False
    # The license plate should not be empty
    assert is_valid('') == False
