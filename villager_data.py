"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    file = open(filename)
    for line in file:
        data = line.split('|')
        print(data)
        species.add(data[1])

    file.close()

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    file = open(filename)
    for line in file:
        data = line.split('|')
        if search_string == 'All':
            villagers.append(data[0])
        elif search_string == data[1]:
            villagers.append(data[0])

    file.close()

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    villagers = []

    # Fitness, Nature, Education, Music, Fashion, and Play [3]
    fitness = ['Fitness']
    nature = ['Nature']
    music = ['Music']
    fashion = ['Fashion']
    education = ['Education']
    play = ['Play']

    hobbies = [fitness, nature, music, fashion, education, play]


    file = open(filename)

    for line in file:
        data = line.split('|')
        for hobby in hobbies:
            if data[3] == hobby[0]:
                hobby.append(data[0])

    file.close()

    return hobbies


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
