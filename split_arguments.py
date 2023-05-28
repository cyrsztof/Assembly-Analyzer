import re


def split_arguments(instruction_with_args):
    # Split the string by commas
    arguments = re.split(r',\s*', instruction_with_args)
    # Remove leading/trailing spaces from each argument
    arguments = [arg.strip() for arg in arguments]

    # Remove the instruction (first word) from the list of arguments
    if len(arguments) > 0:
        first_argument = arguments[0]
        first_argument = re.sub(r'^\w+\s+', '', first_argument)
        arguments[0] = first_argument

        # Check if the resulting list contains only the instruction itself
        if len(arguments) == 1 and arguments[0] == instruction_with_args:
            arguments = []  # Set arguments to an empty list

    return arguments
