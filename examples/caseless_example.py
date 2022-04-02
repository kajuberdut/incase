from incase import Case, Caseless

# Instances of Caseless are strings
example = Caseless("example string")
print(isinstance(example, str))
# True

# By property
print(example.snake)
# example_string

# Or by subscript (string or Case)
print(example["camel"])
# exampleString

print(example[Case.UPPER_SNAKE])
# EXAMPLE_STRING

# Caseless ignore case when comparing to str
print(Caseless("some name") == "SOME_NAME")
# True

# Caseless hashes ignore case also
a_dict = {Caseless("This is a Key"): "this"}
print(a_dict[Caseless("thisIsAKey")])

# Caseless can also generate case coercion functions
make_camel = Caseless.factory("camel")

print(make_camel("snake_case"))
# snakeCase
