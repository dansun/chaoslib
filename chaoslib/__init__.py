# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------
   _________ .__                        .____    ._____.
   \_   ___ \|  |__ _____    ____  _____|    |   |__\_ |__
   /    \  \/|  |  \\__  \  /  _ \/  ___/    |   |  || __ \
   \     \___|   Y  \/ __ \(  <_> )___ \|    |___|  || \_\ \
    \______  /___|  (____  /\____/____  >_______ \__||___  /
           \/     \/     \/           \/        \/       \/ 
-------------------------------------------------------------------
"""
#
# Import dependencies
#
from randomdotorg import RandomDotOrg
import logging

#
# Configure logging-format and level
#
logging.basicConfig(
    format = '%(levelname)s:%(name)s:%(funcName)s:%(message)s',
    level = logging.DEBUG)


#
# Instanciate module variables
#
randomizer = RandomDotOrg()
logger = logging.getLogger(__name__)
default_sorting = lambda x, y: x >= y

#
# Sort values
#
def sort(values, sorting=default_sorting):
    """
      Define sort function
      values: list of values to be sorted randomly
      return: sorted list of values
    """
    randomized_values = randomize(values)
    while not is_sorted(randomized_values, sorting):
        randomized_values = randomize(randomized_values)
        logger.debug('Randomized to '+str(randomized_values))
    return randomized_values

#
# Randomize values
#
def randomize(values):
    """
      Randomze order of values in list
      values: list of values to truly randomize order of
      return: new list with same values as argument in random order 
    """
    randomized_values = []
    while values:
        value = randomizer.choice(values)
        values.remove(value)
        randomized_values.append(value)
    return randomized_values

#
# Check if sorted
#
def is_sorted(values, sorting=default_sorting):
    """
      Check if values in argument is sorted with given lambda
      values: list of values to be verified
      sorting: lambda for verifying sorting
      return: true if list is sorted according to lambda
    """
    for index, enumerated_value in enumerate(values[1:]):
        if not sorting(enumerated_value, values[index]):
            return False
    return True