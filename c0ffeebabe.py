#!/usr/bin/env python3
#
# Copyright (c) 2018 Alexander Karpov <keyfour13@gmail.com>
#
import hashlib
import random
import re
import calendar
import time
import json

default_input_file = "wordlist.txt"
number_of_iterations = 10000
dispersion = 1000000000


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


def find_substrings(input_str, output_str, length):
    f = len(input_str)
    i = 0
    while f - i >= length:
        if output_str.find(input_str[i:i + length]) != -1:
            return True
        i = i + 1
    return False


def find_collisions(input_str, output_str, length):
    if find_substrings(input_str, output_str, length):
        return length
    elif length > 0:
        return find_collisions(input_str, output_str, length - 1)
    else:
        return 0


def process(num, rnd):
    output = {}
    for word in input_words:
        for base_str in input_words[word]:
            print("Processing {0}".format(base_str))
            for i in range(0, num):
                rand_str = str(random.randint(0, rnd))
                if random.randint(0, 10) % 2 == 0:
                    input_str = base_str + rand_str
                elif random.randint(0, 10) % 3 == 0:
                    input_str = rand_str + base_str + str(random.randint(0, rnd))
                else:
                    input_str = rand_str + base_str
                output_str = hashlib.md5(input_str.encode("utf-8")).hexdigest()
                collision = find_collisions(input_str, output_str, len(input_str)) * 100.0 / len(input_str)
                if collision > 50.0:
                    if output[base_str] is None:
                        output[base_str] = []
                    print("Find collision {0}\% {1} {2}".format(collision, input_str, output_str))
                    output[base_str].append({"input_str": input_str, "output_str": output_str, "collision": collision})
    return output


if __name__ == '__main__':

    input_words = get_dictionary(default_input_file)

    while True:
        output = process(number_of_iterations, dispersion)
        if len(output) > 0:
            output_file = str(calendar.timegm(time.gmtime())) + ".json"
            try:
                with open(output_file, "a") as f:
                    jdata = json.dumps(output)
                    f.write(jdata)
                    print("Written to {0} {1}".format(output_file, len(jdata)))
            except PermissionError:
                print("Can't write to file")
        else:
            print("Empty output, may next time be lucky!")
        time.sleep(1)
