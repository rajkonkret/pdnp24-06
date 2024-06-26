import chardet

# pip install chardet

with open('test.log', 'rb') as fh:  # rb - odczytuje binarni
    raw_data = fh.read()

print(raw_data)
# b'Nadpisane\r\nDodane\r\nDodane\r\nDodane\r\nDodane\r\nDo\xc5\x9bdane\r\n'
result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.6586696861310511, 'language': 'Turkish'}
# po Po doodaniu większej liczby polskich liter
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
encoding = result['encoding']
print(raw_data.decode(encoding=encoding))
# Nadpisane
# Dodane
# Dodane
# Dodane
# Dodane
# Dośdane
# Żółć
