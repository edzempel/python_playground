# use predefined string constants
import string


# TODO: predefined string constants can be used in common scenarios
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(string.hexdigits)

# TODO: Use the constants to filter information out
test_string1 = "The quick brown fox jumps over the lazy dog on the 1st of December"
test_string2 = "Supercalifragilistic"
test_string3 = "90210"

result = "".join([c for c in test_string1 if c in string.ascii_letters])
print(result)
print(test_string1.isalnum())
print(test_string2.isalnum())

print(all([c.isalpha() for c in test_string1]))

print(test_string1.isnumeric())
print(test_string3.isnumeric())

# TODO: String testing methods

