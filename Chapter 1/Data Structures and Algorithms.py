from collections import deque, Counter
from operator import itemgetter
from itertools import groupby
import time
import heapq

# Unpacking Elements from Iterables of Arbitrary Length

# Drop the first and last from a list of grades, and sum the remaining middle.
def average(grades):
    first, *middle, second_last, last = grades
    return sum(middle), middle, second_last, last # etc

grades = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
average, middle, second_last, last = average(grades)
# print(average, middle) -> 440 [90, 80, 70, 60, 50, 40, 30, 20]
# print(middle, second_last, last) -> [90, 80, 70, 60, 50, 40, 30] 20 10

# q = deque(maxlen=3)
# for i in range(1000):
#     q.append(i)
#     #p rint(q)
#     time.sleep(1)


def search(lines, pattern, history=5):
    """ This function will yield a pattern within a file, and also return a history of the previous lines.
    Up to history in length.

    Args:
        lines (str): A string of text which will be searched for pattern.
        pattern (str): A pattern to search for.
        history (int, optional): The length of history you wish to return. Defaults to 5.

    Yields:
        _type_: _description_
    """
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


def find_pattern_in_file(file, pattern, history):
    """ This function will return the line a pattern is found in along with a history of previous lines
    up to history.

    Args:
        file (str): File to search.
        pattern (str): Pattern to search for.
        history (str): How many lines of history to return.
    """
    with open(file) as f:
        for line, prevlines in search(f, pattern, history):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)

# find_pattern_in_file("Chapter 1/sometext.txt", "words", 0)


# Finding the Largest or Smallest N Items

# heapq
nums = [1, 3, 4, 1, -3, 5, -22, -14, 85, 12, 7]
# print(heapq.nlargest(3, nums)) # prints the 3 largest numbers from the list
# print(heapq.nsmallest(3, nums)) # prints the 3 smallest numbers from the list

portfolio = [
    {"name":"IBM0", "shares":100, "price":52.34},
    {"name":"IBM1", "shares":100, "price":45.34},
    {"name":"IBM2", "shares":100, "price":21.34},
    {"name":"IBM3", "shares":100, "price":68.34},
    {"name":"IBM4", "shares":100, "price":11.34},
]

# Return the 3 smallest dicts from the list whose "price" is the deciding key.
cheap = heapq.nsmallest(3, portfolio, key = lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key= lambda s: s['price'])

class PriorityQueue:
    def __init__(self) -> None:
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name) -> None:
        self.name = name
    
    def __repr__(self):
        return "Item({!r})".format(self.name)

q = PriorityQueue()
q.push(Item("foo"), 1)
q.push(Item("bar"), 3)
q.push(Item("bip"), 2)


prices = {
    "ACME": 45.12,
    "IBM": 123.41,
    "APPL": 41.22,
    "HPQ": 12.10
}

min_price = min(zip(prices.values(), prices.keys())) # must re-create zip() instance every time you need it
sort = sorted(zip(prices.values(), prices.keys()))

def dedupe(items):
    """ Remove duplicates while maintaining order.

    Args:
        items (hashable): Hashable list of items to search.

    Yields:
        list: List less duplicates.
    """
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 2, 1, 2, 5, 4, 6, 8, 3, 4]


def read(file, top):
    """ Read a file into a list of words and output the most common words """
    with open("Chapter 1/sometext.txt", "r") as f:
        words = f.read().split(" ")
        word_count = Counter(words)
        top_three = word_count.most_common(top)
        return top_three

# Count the number of times a number in a list appears in a cerain range.
counted_list = {
    "small":0,
    "medium":0,
    "large":0,
    "extra":0
}
def count(nums):
    """ This function takes a list of numbers and counts the number of times x appears in the ranges below.

    Args:
        nums (list): A list of numbers.

    Returns:
        dict: Dictionary containing counts of each numbers that appear in the range
    """
    for x in nums:
        # condition check
        if x > 0 and x < 1000:
            counted_list['small'] += 1
        elif x > 1000 and x < 10000:
            counted_list['medium'] += 1
        elif x > 10000 and x < 100000:
            counted_list['large'] += 1
        elif x > 100000 and x < 1000000:
            counted_list['extra'] += 1
    return counted_list
     
nums = [1100, 1030, 12200, 330000]


# Grouping Records Together Based on Fields
rows = [
    {"date":"07/01/2012"},
    {"date":"07/01/2012"},
    {"date":"07/02/2012"},
    {"date":"07/03/2012"},
    {"date":"07/03/2012"},
]

rows.sort(key=itemgetter("date"))

def print_groups(rows):
    for date, items in groupby(rows, key=itemgetter("date")):
        print(date)
        for i in items:
            print("     ", i)


import math
# Filter by list comprehension
x = [100, 300, 123, 4001, 231, 214]
# print([ y for y in x if y < 500 ])

# Transform the list
# print([ math.sqrt(y) for y in x if y < 500 ])


# Create a subset of a dictionary, where value is met
# print( {key:value for key, value in prices.items() if value > 10} )

from collections import namedtuple


# Named tuple
s = namedtuple("Stock", ["name", "open", "low", "close", "high", "volume"])
stock = s("ACME", "12", "10", "12.12", "13", "123")