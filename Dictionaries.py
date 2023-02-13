#Словари

dictionaries = {'City': 'Москва', "temperature": '20'}
print(dictionaries)
print(dictionaries['City'])
dictionaries['temperature'] = str(int(dictionaries['temperature'])-5)
print(dictionaries)
print(dictionaries.get('country'))
dictionaries['country'] = 'Россия'
dictionaries['date'] = "27.05.2019"
print(len(dictionaries))
print(dictionaries)