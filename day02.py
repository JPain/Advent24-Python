#!/usr/bin/env python3
import os

inputFileName = os.path.basename(__file__).replace('.py', '-input.txt')

def part1():
    safe_reports = 0
    with open(inputFileName) as fileInput:
        for line in fileInput.readlines():
            current_list = list(map(int, line.split()))
            print(current_list)
            is_increasing = None
            valid = True
            for i in range(len(current_list) - 1):
                diff = current_list[i + 1] - current_list[i]
                if diff > 3 or diff == 0 or diff < -3:
                    valid = False
                    print('Diff > 3 or 0 or < -3')
                    break
                if is_increasing is None:
                    is_increasing = diff > 0
                elif (is_increasing and diff < 0) or (not is_increasing and diff > 0):
                    valid = False
                    break
            if valid:
                safe_reports += 1
        print(safe_reports)

def is_safe(report):
    is_increasing = None
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if diff > 3 or diff == 0 or diff < -3:
            return False
        if is_increasing is None:
            is_increasing = diff > 0
        elif (is_increasing and diff < 0) or (not is_increasing and diff > 0):
            return False
    return True

def part2():
    safe_reports = 0
    with open(inputFileName) as fileInput:
        for line in fileInput.readlines():
            current_list = list(map(int, line.split()))
            if is_safe(current_list):
                safe_reports += 1
            else:
                for i in range(len(current_list)):
                    modified_list = current_list[:i] + current_list[i+1:]
                    if is_safe(modified_list):
                        safe_reports += 1
                        break
        print(safe_reports)

if __name__ == "__main__":
    # part1()
    part2()
