from incase import planetary_defense_shield

THIS_IS_A_THING = "Some Value"


def badCamelCaseFunction():
    print("hi")


# If you pass a case, instead of a dictionary, this will grab most of globals.
# Also note that the objects that will be cloned are whatever is in globals()
# at the time you pass it as the second argument, so call accordingly.
planetary_defense_shield(
    {"THIS_IS_A_THING": "snake", "badCamelCaseFunction": "snake"}, globals()
)

print(this_is_a_thing)
# Some Value

bad_camel_case_function()
# hi