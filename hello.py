# Print python version
import sys

print(f"Python version: {sys.version.split()[0]}")

print("Hello from laptop python file via Docker")

num_words = 0
with open("test.txt") as f:
    for line in f:
        num_words += len(line.split())

print(f"Number of words: {num_words}")
