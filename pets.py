def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# positional arguments
describe_pet('hamster','harry')
describe_pet('dog','willie')

# keyword arguments
describe_pet(animal_type='bird', pet_name='tweetie')
describe_pet(pet_name='sunkai', animal_type='chow-chow')



