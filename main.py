verb = input("Please state an action (verb): ")
noun = input("Please state a noun: ")
posessiveNoun = input("Please state a posessive noun (example: Father's): ")
event = input("What is an event that you've been to? ")


paragraph = "I never saw this great-uncle but I’m supposed to {}\
 like him—with special reference to the rather hard-boiled\
 {} that hangs in {} office. I graduated from New\
Haven in 1915, just a quarter of a century after my father,\
and a little later I participated in that delayed Teutonic migration known as the {}.".format(verb, noun, posessiveNoun, event)

print("Here is your madlib...")
print(paragraph)
