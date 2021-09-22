#!/usr/bin/env python3

# A irrigation water allocations calculator for paired programming assignment 2
# This program calculates and determines how long it will take to use up an allocation of water for irrigation.
# Programmers: Jordan Booth, Mackenzie Eskey
# Date: 2021.09.22

LINE_LENGTH = 60

print('Irrigation Water Allocations Calculator')
print('=' * LINE_LENGTH)

user_input = 'y'

while user_input == 'y':

    while True:
        rained_allocation_depth = float(input('Enter rationed allocation depth(D) in inches: '))

        if 0 < rained_allocation_depth:
            break
        else:
            print('Invalid value. Please enter again.')

    while True:
        irrigated_area = float(input('Enter area being irrigated(A) in acres: '))

        if 0 < irrigated_area:
            break
        else:
            print('Invalid value. Please enter again.')

    while True:
        rained_allocation_depth = int(input('Enter average rate of flow(Q) in U.S. gpm: '))

        if 0 < rained_allocation_depth:
            break
        else:
            print('Invalid value. Please enter again.')

    user_input = input('Would you like to make another calculation?(y/n): ')
