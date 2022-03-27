from incase import incase


# It covers the basic case
print(incase("snake", "example text"))
# example_text

# But can also handle sequences
print(incase("upper", ["three", "word", "list"]))
# ['THREE', 'WORD', 'LIST']
print(incase("upper", ("three", "word", "tuple")))
# ('THREE', 'WORD', 'TUPLE')

# Even generators
generator = (word for word in ["some", "list"])
incased = incase("upper", generator)
print(incased)
# <generator object _incase_single.<locals>.<genexpr> at ...
print(list(incased))
# ['SOME', 'LIST']

# Or nested objects
nested = {
    "first_key": ["some", "list"],
    "second_key": {"another": "dict"},
    "third_key": 1,
}
print(incase("upper", nested))
# {"first_key": ["SOME", "LIST"], "second_key": {"another": "DICT"}, "third_key": 1}

# Finally, it is possible to map case to objects
print(incase(["upper", "lower", "snake", "camel"], ["some_word"] * 4))
# ['SOME WORD', 'some word', 'some_word', 'someWord']

# By key
print(
    incase(
        {"first_key": "alternating", "second_key": "title"},
        {"first_key": "some example", "second_key": "another example"},
    )
)
# {'first_key': 'SoMe eXaMpLe', 'second_key': 'Another Example'}
