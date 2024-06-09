import argparse

class WordCount:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.total_lines, self.total_bytes = self.read_file()

    def read_file(self):
        """Read the file and return its content and byte count."""
        try:
            with open(self.filename, 'rb') as file:
                content = file.read()
                total_bytes = len(content)
                total_lines = content.decode().splitlines(keepends=True)
                return total_lines, total_bytes
        except FileNotFoundError:
            print(f"wc: {self.filename}: No such file or directory")
            return [], 0
        except Exception as e:
            print(f"wc: {self.filename}: {e}")
            return [], 0

    def count_lines(self):
        """Return the number of lines in the text."""
        return len(self.total_lines)

    def count_words(self):
        """Return the number of words in the text."""
        count = 0
        for line in self.total_lines:
            count += len(line.split())
        return count

    def count_characters(self):
        """Return the number of characters in the text."""
        count = 0
        for line in self.total_lines:
            count += len(line)
        return count

    def display_counts(self, count_lines_flag, count_words_flag, count_chars_flag, count_bytes_flag):
        """Display the counts based on the provided flags."""
        if not self.total_lines:
            return

        counts = []
        if count_lines_flag:
            counts.append(str(self.count_lines()))
        if count_words_flag:
            counts.append(str(self.count_words()))
        if count_chars_flag:
            counts.append(str(self.count_characters()))
        if count_bytes_flag:
            counts.append(str(self.total_bytes))

        counts.append(self.filename)
        print(" ".join(counts))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count lines, words, characters, bytes in file.')
    parser.add_argument('filename', type=str, help='File to count.')
    parser.add_argument('-l', '--lines', action='store_true', help='Count lines')
    parser.add_argument('-w', '--words', action='store_true', help='Count words')
    parser.add_argument('-m', '--chars', action='store_true', help='Count characters')
    parser.add_argument('-c', '--bytes', action='store_true', help='Count bytes')

    args = parser.parse_args()

    if not (args.lines or args.words or args.chars or args.bytes):
        args.lines = args.words = args.bytes = True

    wc = WordCount(args.filename)
    wc.display_counts(args.lines, args.words, args.chars, args.bytes)
