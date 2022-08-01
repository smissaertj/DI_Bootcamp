"""
Try to make a program that creates 5 directories, called `week1`, `week2`, ... , `week5`, in everyone of those
directories, create 5 directories called `day1`, ..., `day5`, and in every day directory create two directories `lesson`
and `homework`.
"""
import os

for i in range(1, 6):
    os.mkdir(f'Week{i}')
    for j in range(1, 6):
        os.makedirs(f'Week{i}/Day{j}/lesson')
        os.mkdir(f'Week{i}/Day{j}/homework')