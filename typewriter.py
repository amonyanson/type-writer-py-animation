import time

def type_writer(text):
    for character in text:
        print(character, end='')
        time.sleep(0.08) # Delay between characters
    print() # Print a newline at the end

type_writer("Hello, world!")