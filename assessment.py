"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    #initialize empty dictionary to take words
    words_dictionary = {}
    #split phrase into list of words
    phrase_list = phrase.split(" ")

    #for loop to add each new word to dictionary and count occurence
    for word in phrase_list:
        words_dictionary[word] = words_dictionary.get(word, 0) + 1

    return words_dictionary


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon
    
    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25 
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25
        
        >>> get_melon_price('Tomato')
        'No price found'
    """
    #dictionary containing all melon prices
    melon_dictionary = {'Watermelon':2.95, 'Cantaloupe':2.50, 
                        'Musk': 3.25, 'Christmas': 14.25}

    #if statement to check if user input in dictionary to return price
    if melon_name in melon_dictionary.keys():
        return melon_dictionary[melon_name]
    else:
        return "No price found"


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    #initialize empty dictionary to take in values
    my_dict = {}

    #length of words passed as keys, words passed as values
    for word in words:
        my_dict[len(word)] = my_dict.get(len(word),[])
        my_dict[len(word)].append(word)

    final_list = []

    #create list of keys and values for final output
    for keys, values in my_dict.items():
        sorted_values = sorted(values)
        final_list.append((keys, sorted_values))

    return final_list


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    #initialize pirate dictionary
    pirate_dictionary = {'sir': 'matey', 'hotel': 'fleabag inn', 'student': 'swabbie', 'man': 'matey', 'professor': 'foul blaggart', 'restaurant': 'galley', 'your': 'yer', 'excuse': 'arr', 'students': 'swabbies', 'are': 'be', 'restroom': 'head', 'my': 'me', 'is': 'be'}

    #split input phrase into list of words
    phrase_list = phrase.split(" ")

    #look up each word in list in pirate dictionary, replace with translation where applicable
    for i in range(len(phrase_list)):
        if phrase_list[i] in pirate_dictionary.keys():
            phrase_list[i] = pirate_dictionary[phrase_list[i]]

    #create new final phrase from translated words
    final_phrase = " ".join(phrase_list)

    return final_phrase


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    #initialize dictionary for game and list for final output
    kids_dictionary = {}
    final_list = []

    #initialize game with initial inputs
    final_list.append(names[0])
    word_in_play = names[0]
    last_letter = word_in_play[-1]

    #create a dictionary with first letters as keys, names as values
    for name in names:
        kids_dictionary[name[0]] = kids_dictionary.get(name[0], [])
        kids_dictionary[name[0]].append(name)

    active_game = True

    #while loop to keep game going while last letter is in keys
    while active_game is True:
        if last_letter in kids_dictionary.keys():
            active_game = True
        else:
            active_game = False

        #while loop to go through values in dictionary until new word is found; getting index error at the end
        new_word = []
        i = 0
        while new_word == []:
            kids_key = kids_dictionary[last_letter]
            if kids_key[i] not in final_list:
                word_in_play = kids_key[i]
                last_letter = word_in_play[-1]
                final_list.append(word_in_play)
                new_word.append(word_in_play)
            else:
                i += 1

    return final_list

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
