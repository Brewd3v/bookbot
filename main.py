def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

def count_words(contents):
    words = contents.split()
    return len(words)

def char_count(contents):
    char_map = {}
    lower = contents.lower()

    for char in lower:
        print(char)
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1

    return char_map

main()