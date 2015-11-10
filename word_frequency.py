#!/usr/bin/env python3.2

"""Takes a textfile and single word as input and outputs
the following:
1. Top 10 frequency of words in the textfile.
2. Top 10 frequency of words following the inputted single word.
3. Top 10 frequency of words following each pair of words from (2).


usage: word_frequency.py [-h] -f INPUT_FILE -w SINGLE_WORD

optional arguments:
      -h, --help       show this help message and exit
      -f INPUT_FILE,   --input_file INPUT_FILE
      -w SINGLE_WORD,  --single_word SINGLE_WORD
"""

import argparse
import re
from collections import Counter
from collections import namedtuple

PUNCTUATIONS = '[:.,(){}!?;"]'


"""Returns top 10 frequency of words in the list of words."""
def _freq_words(words):
    word_freq = Counter(words).most_common(10)
    print_frequency(word_freq, len(words))

    return word_freq


"""Returns top 10 frequency of words following the inputted single word."""
def _freq_words_after_single_word(words, single_word):
    pair_words = []
    for i in range(len(words) - 1):
        if words[i] == single_word:
            pair_words.append("{} {}".format(words[i], words[i+1]))

    return _freq_words(pair_words)


"""Returns top 10 frequency of words following each pair of words passed in."""
def _freq_words_after_pair(words, pair_words):
    WordTriplet = namedtuple("WordTriplet", ["one", "two", "three"])

    triplets = []
    for i in range(len(words) - 2):
        triplets.append(WordTriplet(one=words[i], two=words[i+1], three=words[i+2]))

    for j in range(len(pair_words)):
        split = pair_words[j][0].split()
        trio_freq = ["{} {} {}".format(item.one, item.two, item.three) \
                for item in triplets \
                if item.one == split[0] and item.two == split[1]]
        _freq_words(trio_freq)

    return triplets


"""Prints out frequency of words as percents."""
def print_frequency(freq_list, total):
    for i in range(0, 10):
        if i >= len(freq_list):
            print("N/A")
        else:
            word = freq_list[i][0]
            percent = "{0:.3%}".format(freq_list[i][1] / total)
            print("#{}) {} - {}".format(i + 1, word, percent))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--input_file', type=str, required=True)
    parser.add_argument('-w', '--single_word', type=str, required=True, nargs=1)
    args = parser.parse_args()

    """Open the input file and remove all blank lines.
    For each line, delimit the line on spaces to separate out the words.
    Remove certain punctuation marks from the words ( :.,(){}!?;" ).
    Make the word lower case since case should not matter when identifying
    a word's frequency in a document."""

    with open(args.input_file, 'r') as f:
        input_file = filter(None, (line.rstrip() for line in f.readlines()))
        words = [re.sub(PUNCTUATIONS, '', word.lower()) for line in input_file for word in line.split()]

    word_freq = _freq_words(words)
    pair_freq = _freq_words_after_single_word(words, args.single_word[0])
    trio_freq = _freq_words_after_pair(words, pair_freq)


if __name__ == "__main__":
    main()

