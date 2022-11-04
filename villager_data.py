"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    data = all_data(filename)

    for line in data:
        species.add(line[1])

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

    data = all_data(filename)

    for line in data:
        if search_string == 'All':
            villagers.append(line[0])
        elif search_string == line[1]:
            villagers.append(line[0])

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
    Fitness = ['Fitness']
    Nature = ['Nature']
    Music = ['Music']
    Fashion = ['Fashion']
    Education = ['Education']
    Play = ['Play']

    hobbies = [Fitness, Nature, Music, Fashion, Education, Play]

    data = all_data(filename)

    for line in data:
        for hobby in hobbies:
            if line[3] == hobby[0]:
                hobby.append(line[0])

    # hobbies = [row[1:] for row in hobbies]

    return [sorted(arr[1:]) for arr in hobbies]


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

    file = open(filename)

    for line in file:
        data = line.split('|')
        all_data.append(tuple(data))

    file.close()

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

    data = all_data(filename)

    for line in data:
        if line[0] == villager_name:
            return line[4]

    return None


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

    data = all_data(filename)
    villager = tuple()
    peeps = set()

    for line in data:
        if villager_name in line:
            villager = line
            break

    for line in data:
        if line[2] == villager[2]: peeps.add(line[0])

    return peeps
