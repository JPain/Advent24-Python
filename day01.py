#!/usr/bin/env python3
import os

inputFileName = os.path.basename(__file__).replace('.py', '-input.txt')

def part1():
    thefirstofthetwonumbers_list = []
    thesecondofthetwonumbers_list = []
    with open(inputFileName) as fileInput:
        for line in fileInput:
            thefirstofthetwonumbers, thesecondofthetwonumbers = map(int, line.split())
            thefirstofthetwonumbers_list.append(thefirstofthetwonumbers)
            thesecondofthetwonumbers_list.append(thesecondofthetwonumbers)
    thefirstofthetwonumbers_list.sort()
    thesecondofthetwonumbers_list.sort()
    
    distances = [abs(thefirstofthetwonumbers - thesecondofthetwonumbers) for thefirstofthetwonumbers, thesecondofthetwonumbers in zip(thefirstofthetwonumbers_list, thesecondofthetwonumbers_list)]
    total_distance = sum(distances)
    for distance in enumerate(distances):
        print(distance)
    print('Total:', total_distance)


def part2():
    thefirstofthetwonumbers_list = []
    thesecondofthetwonumbers_list = []
    with open(inputFileName) as fileInput:
        for line in fileInput:
            thefirstofthetwonumbers, thesecondofthetwonumbers = map(int, line.split())
            thefirstofthetwonumbers_list.append(thefirstofthetwonumbers)
            thesecondofthetwonumbers_list.append(thesecondofthetwonumbers)
    
    similarity_score = 0
    for thefirstofthetwonumbers in thefirstofthetwonumbers_list:
        count_in_thesecondofthetwonumbers = thesecondofthetwonumbers_list.count(thefirstofthetwonumbers)
        similarity_score += thefirstofthetwonumbers * count_in_thesecondofthetwonumbers
    
    print('Total:', similarity_score)

if __name__ == "__main__":
    # part1()
    part2()