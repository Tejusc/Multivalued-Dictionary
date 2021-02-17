from multivalued_dict_package import *

# initialize the a multivalued dictionary
multivalued_dictionary = multivalued_dict({'a': ['test-1', 'test-2', 'test-3'], 'b': 'test-4'})

print("*** Add members to the dictionary ***")
multivalued_dictionary['c'] = 'test1'
print("Successfully added test2 to 'c'", multivalued_dictionary.add('c', 'test2'))
print(multivalued_dictionary.add('c', 'test2'))
print('')

print("*** Test to print all Keys of the Dictionary ***")
print(multivalued_dictionary.keys())
print('')

print("*** Test to print all items for a particular key ***")
print(multivalued_dictionary.getitem('a'))
# print(multivalued_dictionary.getitem('d'))
print('')

print("*** Test to print all the items in the dictionary ***")
print(multivalued_dictionary.items())
print('')

print("*** Test to check if a key is present in the dictionary ***")
print(multivalued_dictionary.__contains__('d'), "The key 'd' does not exists ")
# OR
print(multivalued_dictionary.keyexists('a'))
print(multivalued_dictionary.keyexists('f'))
print('')

print("*** Test to print all values in the dictionary ***")
print(multivalued_dictionary.values())
print('')

print("*** Test to delete an item from the dictionary ***")
print("Deleting 'a' from the dictionary with values", multivalued_dictionary.pop('a'))
print(multivalued_dictionary.data)
print('')

print("*** Test to remove all items for a key ***")
multivalued_dictionary.removeall('a')
print(multivalued_dictionary.getitem('a'))
print('')

print("*** Test to clear the dictionary ***")
multivalued_dictionary.clear()
print(multivalued_dictionary.data)
print('')
