# Word Frequency

This program takes a text document and a single word as input and outputs the following to stdout
(sorted by frequency as a percentage):

1. Top 10 most frequent used words in the file.
2. Top 10 most frequent words in the file which are used after the input word.
3. Top 10 most frequent words that follow each of the pairs of words from (2).

### Getting Started
The following command will clone the repo into the current directory:
```
git clone https://github.com/abannerjee/word_frequency.git
```

### Usage
```
python3.2 word_frequency.py -f <input_file> -w <single_word>
```

### Defining a Word

A word has been defined to have the following properties:
* Case insensitive (e.g. "the" and "The" are considered the same word)
* Delimited by spaces
* Certain punctuation marks are not considered (the following characters are ignored: '[:.,(){}!?;"]')

### Notes

* Certain characters which have not been filtered are considered words, such as "&".
* Email addresses will not parse correctly (e.g. alex@gmail.com will be interpreted as alex@gmailcom).
* In the case a tie occurs in the frequency of two or more words or sets of words,
the word or set of words which appear first in the document is listed first. The numbering is unaffected, meaning
there won't be two words or set of words marked as #1.
