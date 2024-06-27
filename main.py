def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(count_words(file_contents), "words found in the document\n")

        char_map = char_count(file_contents)
        char_dict = convert_dict(char_map)

        for v in char_dict:
            print("The '{}' character was found {} times".format(v["char"], v["count"]))

        print("--- End report ---")

def count_words(contents):
    words = contents.split()
    return len(words)

def char_count(contents):
    char_map = {}
    lower = contents.lower()

    for char in lower:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1

    return char_map


def sort_on(dict):
    return dict["count"]


def convert_dict(dict):
    arr = []
    for k, v in dict.items():
        if(k.isalpha()):
            arr.append({ "char" : k, "count" : v })
    arr.sort(reverse=True, key=sort_on)
    return arr

main()