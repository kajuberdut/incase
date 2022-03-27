from incase import Case, Caseless

# Easily output any case
example = Caseless("example string")


# By property
print(example.snake)
# my_cool_example_class

# Or by subscript (string or Case)
print(example["camel"])
# exampleString

print(example[Case.UPPER_SNAKE])
# EXAMPLE_STRING

# Caseless ignores case when checking equality with strings
print(Caseless("some name") == "SOME_NAME")
# True

# Caseless can also generate case coercion functions
make_camel = Caseless.factory("camel")

print(make_camel("snake_case"))
# snakeCase
