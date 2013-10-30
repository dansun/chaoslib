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

#
# Define sort function
# values: list of values to be sorted randomly
# return: sorted list of values
#
def sort(values):
    randomized_values = randomize(values)
    while not is_sorted(randomized_values):
        randomized_values = randomize(randomized_values)
        print(randomized_values)
    return randomized_values

#
# Randomze order of values in list
# values: list of values to truly randomize order of
# return: new list with same values as argument in random order
#
def randomize(values):
  new_values = []
  while values:
    theValue = randomizer.choice(values)
    values.remove(theValue)
    new_values.append(theValue)
  return new_values

#
# Check if values in argument is sorted with given lambda
# values: list of values to be verified
# sorting: lambda for verifying sorting
# return: true if list is sorted according to lambda
#
def is_sorted(values, sorting=lambda x, y: x >= y):
  for index, enumerated_value in enumerate(values[1:]):
    if sorting(enumerated_value, values[index]):
      return False
  return True