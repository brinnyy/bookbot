import sys
from stats import count_words, get_char_counts, sort_char_counts


def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        return f.read()


def main():
    # Check for a file path argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")

    text = get_book_text(path_to_file)

    print("----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = get_char_counts(text)
    sorted_chars = sort_char_counts(char_counts)
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
