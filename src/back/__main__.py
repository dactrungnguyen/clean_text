from sys import stdin
from time import sleep

from src.back.worker import clean_text

if __name__ == "__main__":
    print(clean_text(stdin.read()))
