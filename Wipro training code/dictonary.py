#Dictionaries are used to store data values in key:value pairs.
# They are unordered, changeable, and do not allow duplicate keys.
#because they use hashing allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

print(capitals['Russia'])

print(capitals.get('Germany')) # None
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las vegas'})
capitals.pop('China')
capitals.clear()
for key, value in capitals.items():
    print(key, value)