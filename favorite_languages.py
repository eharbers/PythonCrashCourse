favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby','go'],
    'phil': ['python','haskell'],
    }

for name, languages in favorite_languages.items():  
    # check for number of languages and use is or are 
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
    else:
        print("\n" + name.title() + "'s favorite language is:")

    for language in languages:
        print("\t" + language.title())


