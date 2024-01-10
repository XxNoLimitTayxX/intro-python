def mad_lib():
    print("Hello, welcome to Tay's Mad libs. Please begin with adding a noun. *PLEASE REMEMBER THAT THIS IS JUST A BETA*")
    name = input("Enter a name: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    mad_lib_story = f"{adjective} {name} is tired, but they drink caffine to stay up. They also decide to {verb} {adverb}."

    print("\nYour mad lib story:")
    print(mad_lib_story)

    mad_lib()