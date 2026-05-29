# @leet imports start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *
# @leet imports end

# @leet start
import sys
class Solution:
    def sum_of_digits(self, n ) -> int :
        result = 0
        while n:
            result += ( n % 10)
            n //= 10
        return result

    def minElement(self, nums: List[int]) -> int:
        min = sys.maxsize
        for n in nums:
            check = self.sum_of_digits(n)
            if check < min:
                min = check

        return min
        
# @leet end


