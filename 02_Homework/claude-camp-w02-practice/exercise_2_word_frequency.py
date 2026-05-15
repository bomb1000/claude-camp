import string


def clean_word(word):
    return word.strip(string.punctuation).lower()


def count_words(text):
    counts = {}
    for raw_word in text.split():
        word = clean_word(raw_word)
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def print_counts(counts):
    if not counts:
        print("No words found.")
        return
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    for word, count in sorted_items:
        print(f"{word}: {count}")


def main():
    print("Word Frequency Counter")
    text = input("Enter text: ").strip()
    print_counts(count_words(text))


if __name__ == "__main__":
    main()
