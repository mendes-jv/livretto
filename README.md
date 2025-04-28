# Livretto (BookBot)

A simple Python tool for analyzing text files (books) and providing statistics like word count and character frequency.

## Description

Livretto, also known as BookBot, is a command-line tool that analyzes text files and provides the following statistics:

- Total word count
- Character frequency (alphabetic characters only, case-insensitive)

This project was created as part of the [Boot.dev](https://www.boot.dev) curriculum.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/livretto.git
   cd livretto
   ```

2. No additional dependencies are required as the project uses only Python standard libraries.

## Usage

Run the script with a path to a text file as an argument:

```
python main.py <path_to_book>
```

For example:

```
python main.py books\frankenstein.txt
```

## Sample Books

- [`frankenstein.txt`](https://www.gutenberg.org/files/84/84-0.txt)
- [`mobydick.txt`](https://www.gutenberg.org/files/2701/2701-0.txt)
- [`prideandprejudice.txt`](https://www.gutenberg.org/cache/epub/1342/pg1342.txt)

## Example Output

When running the script on a book, you'll see output similar to this:

```
============ BOOKBOT ============
Analyzing book found at books\frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
----------- Character Count ----------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
s: 21155
r: 20818
h: 19725
l: 14592
d: 14541
u: 10562
c: 9221
m: 9063
f: 8431
w: 7601
p: 7079
g: 6512
y: 6153
b: 5332
v: 3753
k: 3147
j: 487
x: 427
q: 362
z: 221
============= END ===============
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 João V. Mendes
