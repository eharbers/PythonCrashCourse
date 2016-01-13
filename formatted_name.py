def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

name_formatted = get_formatted_name('Erik','Harbers')
print(name_formatted)


