# String formatting methods and best practices
from string import Template
import datetime

# TODO: Using Template strings
the_str = "The quick brown $animal $action over the lazy dog"
the_template = Template(the_str)
output_stry = the_template.substitute(animal="fox", action="jumped")
print(output_stry)
args = {
    "animal":"cow",
    "action": "walked"
}
print(the_template.substitute(args))
# TODO: Using str.format()
foo = "foo"
bar = 123
print("Output: {}, {}".format(foo, bar))
print("Output: {1}, {0}".format(foo, bar)) # numerical indexes for the argument list
print("Output: {var1}, {var2}".format(var1=foo, var2=bar)) # numerical indexes for the argument list
print("Output: {var2:x}, {var2:X}, {var1}".format(var1=foo, var2=bar)) # use formatting directive (lowercase hexadecimal)

# TODO: Using interpolation with f-strings in Python 3.6
product = "Widget"
price = 19.99
tax = 0.07
nyd = datetime.datetime(2019,1,1)
print(f"{product} has a price of {price}, with tax {tax:.2%} the total is {round(price+price*tax,2)}")
print(f"But only on {nyd:%B %d %Y}")