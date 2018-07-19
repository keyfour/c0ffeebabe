#!/usr/bin/env python3
#
# Copyright (c) 2018 Alexander Karpov <keyfour13@gmail.com>
#
import hashlib
import random
import re

default_input_file = "wordlist.txt"


def read_file(input_file):
    try:
        with open(input_file, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print("Can't open file {0}".format(input_file))


def get_dictionary(input_file):
    wordlist = read_file(input_file)
    print("Read {0} words".format(len(wordlist)))
    result = {}
    for word in wordlist:
        word = word.rstrip('\n')
        word1 = re.sub('^0x', '', word).rstrip('\n')
        word2 = word1.lower().rstrip('\n')
        result[word] = [word1, word2]
    return result


input_words = get_dictionary(default_input_file)

for word in input_words:
    for base_str in input_words[word]:
        for i in range(0, 1000):
            rand_str = str(random.randint(0, 10000000000))
            if random.randint(0, 10) % 2 == 0:
                input_str = base_str + rand_str
            elif random.randint(0, 10) % 3 == 0:
                input_str = rand_str + base_str + str(random.randint(0, 10000000000))
            else:
                input_str = rand_str + base_str
            output_str = hashlib.md5(input_str.encode("utf-8")).hexdigest()
            print("{0},{1},{2}".format(base_str, input_str, output_str))
