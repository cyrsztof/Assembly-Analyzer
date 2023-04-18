import csv

registers = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "rsp", "eax", "ebx", "ecx", "edx", "esi", "edi", "ebp",
             "esp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]


def get_arguments(instruction):
    args = instruction.split(", ")
    return args


def print_rows(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            print(', '.join(row))


def count_instr_ret_in_block(filename, begin, end):
    counter = 0
    read_row = False
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)  # pomija nagłówek pliku
        for row in reader:
            if begin in row[2]:
                read_row = True
            if end in row[2]:
                break
            if read_row:
                counter += int(row[3])
        return counter


def count_instr_type(filename, instruction):
    instruction_counter = 0
    ins_mem_counter = 0
    cpu_clk = 0
    cpu_clk_mem = 0

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)  # pomija nagłówek pliku
        for row in reader:

            if row[2].find(instruction) != -1:
                arguments = get_arguments(row[2])
                instruction_counter += int(row[3])
                cpu_clk += int(row[4])
                if ("0x" in arguments[0]) | ("0x" in arguments[1]) | ("ptr" in arguments[0]) | ("ptr" in arguments[1]):
                    ins_mem_counter += int(row[3])
                    cpu_clk_mem += int(row[4])

    # All
    print(instruction + ": ", end='')
    print(instruction_counter)
    print("CPU_CLK: ", end='')
    print(cpu_clk)
    print()
    # memory
    print("memory: ", end='')
    print(ins_mem_counter)
    print("CPU_CLK (memory): ", end='')
    print(cpu_clk_mem)
    print()
    # register to register
    print("register to register: ", end='')
    print(instruction_counter - ins_mem_counter)
    print("CPU_CLK (register): ", end='')
    print(cpu_clk - cpu_clk_mem)


if __name__ == '__main__':
    name = "resultdiscord.csv"

    count_instr_type(name, 'mov')
    print()
    print("Instruction retired (Block 4): ", end='')
    print(count_instr_ret_in_block(name, "Block 4", "Block 5"))
