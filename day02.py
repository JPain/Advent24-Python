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

def part2():
    safe_reports = 0
    with open(inputFileName) as fileInput:
        for line in fileInput.readlines():
            current_list = list(map(int, line.split()))
            print(current_list)
            is_increasing = None
            valid = True
            issues_in_line = 0
            for i in range(len(current_list) - 1):
                diff = current_list[i + 1] - current_list[i]
                if is_increasing is None and diff != 0:
                    is_increasing = diff > 0
                if diff > 3 or diff == 0 or diff < -3:
                    print('Diff > 3 or 0 or < -3')
                    issues_in_line = issues_in_line + 1
                elif (is_increasing and diff < 0) or (not is_increasing and diff > 0):
                    issues_in_line = issues_in_line + 1
                if issues_in_line > 1:
                    print('not safe')
                    valid = False
                    break
            if valid:
                print('safe')
                safe_reports += 1
        print(safe_reports)

if __name__ == "__main__":
    # part1()
    part2()
