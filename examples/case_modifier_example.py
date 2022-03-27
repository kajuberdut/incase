from incase import Case, case_modifier


# Some functions you don't control
def external_function(expectsCamel, iterationCount):
    # expects camelCase parameter names
    for i in range(iterationCount):
        print(expectsCamel)

# We'll use case_modifier. Now any keyword will be turned to camelCase
f = case_modifier(keywords_case=Case.CAMEL)(external_function)

f(expects_camel="this", iteration_count=1)
# this

# Here, we'll use case modifier as a function decorator
#  to give a sarcastic twist to our output
@case_modifier(args_case="sarcasm")
def say_words(*args) -> None:
    [print(word) for word in args]

say_words("It's all about", "the he said", "SHE SAID")
# It's aLl aBoUt
# ThE He sAi
# ShE SaId
