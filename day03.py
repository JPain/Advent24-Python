#!/usr/bin/env python3
import os
import re

inputFileName = os.path.basename(__file__).replace('.py', '-input.txt')

def part1():
    with open(inputFileName) as fileInput:
        sumitup = 0
        for line in fileInput.readlines():
            regex1 = re.compile(r'mul\(\d+,\d+\)')
            matches = regex1.findall(line)
            for match in matches:
                regex2 = re.compile(r'\d+')
                nums = regex2.findall(match)
                thissum = int(nums[0]) * int(nums[1])
                sumitup = sumitup + thissum
    print(sumitup)

def part2():
    with open(inputFileName) as fileInput:
        for line in fileInput.readlines():
            print('nothing')
            # Logic here

if __name__ == "__main__":
    part1()
    # part2()
