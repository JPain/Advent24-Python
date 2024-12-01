#!/usr/bin/env python3
import os

inputFileName = os.path.basename(__file__).replace('.py', '-input.txt')

def part1():
    one_list = []
    two_list = []
    with open(inputFileName) as fileInput:
        for line in fileInput:
            one, two = map(int, line.split())
            one_list.append(one)
            two_list.append(two)
    one_list.sort()
    two_list.sort()
    
    distances = [abs(one - two) for one, two in zip(one_list, two_list)]
    total_distance = sum(distances)
    for distance in enumerate(distances):
        print(distance)
    print('Total:', total_distance)


def part2():
    one_list = []
    two_list = []
    with open(inputFileName) as fileInput:
        for line in fileInput:
            one, two = map(int, line.split())
            one_list.append(one)
            two_list.append(two)
    
    similarity_score = 0
    for one in one_list:
        count_in_two = two_list.count(one)
        similarity_score += one * count_in_two
    
    print('Total:', similarity_score)

if __name__ == "__main__":
    # part1()
    part2()