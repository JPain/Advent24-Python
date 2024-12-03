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
    sumitup = 0
    pattern = re.compile(r"do\(\)|don't\(\)|mul\(\d+,\d+\)")
    with open(inputFileName) as fileInput:
        mul = True
        for line in fileInput.readlines():
            for match in pattern.finditer(line):
                thething = match.group()
                print(f'Found {thething}')
                if thething == "do()":
                    mul = True
                elif thething == "don't()":
                    mul = False
                elif thething.startswith("mul(") and mul:
                    nums = re.findall(r'\d+', thething)
                    thissum = int(nums[0]) * int(nums[1])
                    sumitup = sumitup + thissum
    print(sumitup)

if __name__ == "__main__":
    # part1()
    part2()
