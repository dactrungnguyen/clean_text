from sys import stdin
from back.worker import clean_text

print('Cleaned text:')
print(clean_text(stdin.read()))