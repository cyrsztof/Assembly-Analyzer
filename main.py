import csv
import os
import sys

from determine_argument_type import *
from split_arguments import *

# Initialize variables
block_count = 0
block_total_count = {}
current_block = None
filename = 'data/input/7zip_merged.csv'     # Change this to any file in input directory
found = set()
instructions = {}
instruction_argument_count = {}
instruction_total_count = {}
instruction_lines = {}
instruction_lines_non_zero = {}
instruction_lines_non_zero_arguments = {}
invalid_rows = 0
not_found = set()
time_argument = {}
time_total = {}
base_name = os.path.splitext(os.path.basename(filename))[0]
output_filename = os.path.join('data/results', f'{base_name}_results.csv')

# Open the CSV file
with open('data/instructions.csv', newline='') as file:
    reader = csv.reader(file, delimiter=';')

    # Iterate over each row in the CSV file
    for row in reader:
        # Check if the row has at least two elements (instruction and description)
        if len(row) >= 2:
            instruction = row[0]
            description = row[1]

            # Add the instruction and its description to the dictionary
            instructions[instruction] = description

# Convert keys in the instructions dictionary to lowercase
instructions = {key.lower(): value for key, value in instructions.items()}

# Open the second CSV file
with open(filename, newline='') as file:
    reader = csv.reader(file, delimiter=';')

    # Skip the header row
    next(reader)

    # Count block values first
    for row in reader:
        if len(row) >= 3:
            instruction_with_args = row[1].strip()  # Remove leading/trailing spaces
            instruction = instruction_with_args.split()[0].lower()  # Extract instruction and convert to lowercase
            count = row[2]  # Get the count from column 4

            # Check if the current row starts a new block
            if instruction.lower() == 'block':
                block_count += 1
                current_block = f"Block {block_count}"
                block_total_count[current_block] = 0  # Initialize count to 0 for the block
            else:
                try:
                    count = int(count)

                    # Increment the total count for the current block
                    if current_block is not None:
                        block_total_count[current_block] += count

                except ValueError:
                    invalid_rows += 1
            # Check if the lowercase instruction is in the lowercase dictionary keys
            if instruction in instructions:
                found.add(instruction)

            # Check if the lowercase instruction is not in the lowercase dictionary keys
            if instruction not in instructions and instruction != 'block':
                not_found.add(instruction)

    # Reset the reader to the beginning of the file
    file.seek(0)
    next(reader)  # Skip the header row again
    block_count = 0
    # Update instruction count
    for row in reader:
        if len(row) >= 4:
            instruction_with_args = row[1].strip()  # Remove leading/trailing spaces
            instruction = instruction_with_args.split()[0].lower()  # Extract the instruction and convert to lowercase
            count = row[3]  # Get the count from column 4

            # Check if the current row starts a new block
            if instruction.lower() == 'block':
                block_count += 1
                current_block = f"Block {block_count}"

            # Check if the instruction is in the dictionary
            if instruction in instructions:
                # Initialize the instruction count if it doesn't exist
                if instruction not in instruction_total_count:
                    instruction_total_count[instruction] = 0
                    instruction_lines[instruction] = 0
                    instruction_lines_non_zero[instruction] = 0
                if instruction in instruction_total_count:
                    instruction_total_count[instruction] += block_total_count[current_block]

                if instruction not in time_total:
                    time_total[instruction] = 0

                if instruction in time_total:
                    try:
                        count = int(count)
                        time_total[instruction] += count
                    except ValueError:
                        pass
                # Split the instruction arguments based on commas after the instruction name
                arguments = split_arguments(instruction_with_args)
                argument_type = determine_argument_type(arguments)

                # Initialize the instruction count for the argument type if it doesn't exist
                if argument_type not in instruction_argument_count.get(instruction, {}):
                    instruction_argument_count.setdefault(instruction, {})[argument_type] = 0
                    instruction_lines_non_zero_arguments.setdefault(instruction, {})[argument_type] = 0
                if argument_type not in time_argument.get(instruction, {}):
                    time_argument.setdefault(instruction, {})[argument_type] = 0

                # Increment the instruction count for the argument type
                instruction_argument_count[instruction][argument_type] += block_total_count[current_block]
                instruction_lines[instruction] += 1

                value = row[3]
                if value.strip().isdigit():
                    # Increment instruction_lines_non_zero if the value is a non-zero positive number
                    if int(value) > 0:
                        instruction_lines_non_zero[instruction] += 1
                        instruction_lines_non_zero_arguments[instruction][argument_type] += 1

                try:
                    count = int(count)
                    time_argument[instruction][argument_type] += count
                except ValueError:
                    pass

# Redirect prints to the output file
with open(output_filename, 'w') as f:
    sys.stdout = f
    # Print the instructions found in the dictionary along with their descriptions
    print("Instructions found:")
    for instruction in found:
        print(f"{instruction}: {instructions[instruction]}")

    # Print the instructions not found in the dictionary
    if len(not_found) > 0:
        print("\nInstructions not found:")
        for instruction in not_found:
            print(instruction)

    #print("\nBlock Total Count:")
    #for block, count in block_total_count.items():
    #    print(f"{block}: {count}")

    # Print the overall count for each instruction
    print("\nInstruction Total Count:")
    for instruction, count in instruction_total_count.items():
        print(f"{instruction}: {count}")

    # Print the count for each instruction based on argument types
    print("\nInstruction Argument Count:")
    for instruction, argument_counts in instruction_argument_count.items():
        print(instruction)
        for argument_type, count in argument_counts.items():
            print(f"- {argument_type}: {count}")

    print("\nInvalid rows: ", invalid_rows)

    print("\nTime Total Count:")
    for instruction, count in time_total.items():
        print(f"{instruction}: {count}")

    print("\nTime by Arguments:")
    for instruction, argument_counts in time_argument.items():
        print(instruction)
        for argument_type, count in argument_counts.items():
            print(f"- {argument_type}: {count}")

    print("\nInstruction Lines Count:")
    for instruction, count in instruction_lines.items():
        print(f"{instruction}: {count}")

    print("\nInstruction Lines Non Zero Count:")
    for instruction, count in instruction_lines_non_zero.items():
        print(f"{instruction}: {count}")

    print("\nInstruction Lines Non Zero Count by Arguments:")
    for instruction, argument_counts in instruction_lines_non_zero_arguments.items():
        print(instruction)
        for argument_type, count in argument_counts.items():
            print(f"-{argument_type}: {count}")

# Reset stdout back to the console
sys.stdout = sys.__stdout__
