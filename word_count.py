def count_words(filename):
    """Count the approxiamte number of words in a file."""

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except IOError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # COunt the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)
