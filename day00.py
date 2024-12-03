#!/usr/bin/env python3
import os

inputFileName = os.path.basename(__file__).replace('.py', '-input.txt')

def part1():
    with open(inputFileName) as fileInput:
        for line in fileInput.readlines():
            print('nothing')
            # Logic here

def part2():
    with open(inputFileName) as fileInput:
        for line in fileInput.readlines():
            print('nothing')
            # Logic here

if __name__ == "__main__":
    part1()
    # part2()
