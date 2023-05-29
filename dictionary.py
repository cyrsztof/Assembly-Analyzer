import csv

instructions = {}

# Open the CSV file
with open('instructions.csv', newline='') as file:
    reader = csv.reader(file, delimiter=';')

    # Iterate over each row in the CSV file
    for row in reader:
        # Check if the row has at least two elements (instruction and description)
        if len(row) >= 2:
            instruction = row[0]
            description = row[1]

            # Add the instruction and its description to the dictionary
            instructions[instruction] = description

# Print the resulting dictionary
print(instructions)
# Convert keys in the instructions dictionary to lowercase
instructions = {key.lower(): value for key, value in instructions.items()}

# Initialize variables
block_count = 0
block_total_count = {}
instruction_total_count = {}
current_block = None

# Set to store unique instructions not found in the dictionary
not_found = set()

# Set to store unique instructions found in the dictionary
found = set()

# Open the second CSV file
with open('witcher_merge123.csv', newline='') as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Count block values first
    for row in reader:
        if len(row) >= 4:
            instruction_with_args = row[2].strip()  # Remove leading/trailing spaces
            instruction = instruction_with_args.split()[0].lower()  # Extract the first word as the instruction and convert to lowercase
            count = row[3]  # Get the count from column 4

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
                    print(f"Invalid count value in row: {row}")
            # Check if the lowercase instruction is in the lowercase dictionary keys
            if instruction in instructions:
                found.add(instruction)

            # Check if the lowercase instruction is not in the lowercase dictionary keys
            if instruction not in instructions:
                not_found.add(instruction)

    # Reset the reader to the beginning of the file
    file.seek(0)
    next(reader)  # Skip the header row again
    block_count = 0
    # Update instruction count
    for row in reader:
        if len(row) >= 4:
            instruction_with_args = row[2].strip()  # Remove leading/trailing spaces
            instruction = instruction_with_args.split()[0].lower()  # Extract the first word as the instruction and convert to lowercase
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
                if instruction in instruction_total_count:
                    instruction_total_count[instruction] += block_total_count[current_block]

                # Increment the overall count for the instruction with the count from the corresponding block


# Print the instructions found in the dictionary along with their descriptions
print("Instructions found:")
for instruction in found:
    print(f"{instruction}: {instructions[instruction]}")

# Print the instructions not found in the dictionary (original case)
print("\nInstructions not found:")
for instruction in not_found:
    print(instruction)

print("Block Total Count:")
for block, count in block_total_count.items():
    print(f"{block}: {count}")

# Print the overall count for each instruction
print("Instruction Total Count:")
for instruction, count in instruction_total_count.items():
    print(f"{instruction}: {count}")