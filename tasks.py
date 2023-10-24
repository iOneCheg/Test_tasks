from string import ascii_lowercase as letters
from collections import Counter
import re

"""
Return list of prime numbers from low to high
"""


def prime_numbers(low, high) -> list:
    falseCondition = low < 0 or high < low or high < 0 or \
                     isinstance(low, float) or isinstance(high, float)
    if falseCondition:
        return []

    prime = [True] * (high + 1)
    prime[0] = prime[1] = False
    for i in range(2, high + 1):
        if not prime[i]:
            continue
        for j in range(i * i, high + 1, i):
            prime[j] = False

    return [i for i in range(low, high + 1) if prime[i]]


"""
Returns a dictionary with text statistics
"""


def text_stat(filename) -> dict:
    words = []
    result = {}
    if not isinstance(filename, str):
        result['error'] = 'filename not a string'
        return result
    try:
        file = open(filename, 'r')
    except IOError as err:
        result['error'] = 'file not found'
        return result
    else:
        text = file.read()
        words = text.lower().split()
        paragraphs = text.split("\n\n")
        cnt = Counter()
        counter_bilingual = 0
        for word in words:
            if any(letter in letters for letter in word.lower()) \
                    and re.search('[а-яА-Я]', word):
                counter_bilingual += 1

        for letter in letters:
            count = 0
            for word in words:
                if letter.lower() in word:
                    count += 1
            cnt[letter] = (text.lower().count(letter), count)

        result = dict(cnt)
        result['word_amount'] = len(words)
        result['paragraph_amount'] = len(paragraphs)
        result['bilingual_word_amount'] = counter_bilingual

        if len(paragraphs) == 1 and paragraphs[0] == "":
            result['paragraph_amount'] = 0
        return result


"""
Returns an integer according to a Roman numeral number
"""


def roman_numerals_to_int(roman_numeral) -> int:
    rule_add = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    rule_div = {
        ('I', 'V'): 3,
        ('I', 'X'): 8,
        ('X', 'L'): 30,
        ('X', 'C'): 80,
        ('C', 'D'): 300,
        ('C', 'M'): 800,
    }
    number = 0
    prev_literal = None
    for literal in roman_numeral:
        if prev_literal and rule_add[prev_literal] < rule_add[literal]:
            if (prev_literal, literal) not in rule_div:
                return None
            number += rule_div[(prev_literal, literal)]
        else:
            number += rule_add[literal]
        prev_literal = literal
    return number
