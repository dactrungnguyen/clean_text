from sys import stdin
from time import sleep
from back.worker import clean_text

while True:
    try:
        print('I am running')
        sleep(1)
    except KeyboardInterrupt:
        print('\nBye!')
        exit(1)
