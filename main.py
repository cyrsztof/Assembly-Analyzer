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
    line_counter = 0
    ins_mem_counter = 0
    line_counter_mem = 0
    cpu_clk = 0
    cpu_clk_mem = 0

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)  # pomija nagłówek pliku
        for row in reader:

            if row[2].find(instruction) != -1:
                arguments = get_arguments(row[2])
                instruction_counter += int(row[3])
                line_counter += 1
                cpu_clk += int(row[4])
                if ("0x" in arguments[0]) | ("0x" in arguments[1]) | ("ptr" in arguments[0]) | ("ptr" in arguments[1]):
                    ins_mem_counter += int(row[3])
                    line_counter_mem += 1
                    cpu_clk_mem += int(row[4])

    # All
    print(instruction + " (instruction_retired): ", end='')
    print(instruction_counter)
    print("Ile było tego rodzaju instrukcji: ", end='')
    print(line_counter)
    print("CPU_CLK: ", end='')
    print(cpu_clk)
    print()
    # memory
    print("memory (instruction_retired): ", end='')
    print(ins_mem_counter)
    print("Ile było tego rodzaju instrukcji: ", end='')
    print(line_counter_mem)
    print("CPU_CLK (memory): ", end='')
    print(cpu_clk_mem)
    print()
    # register to register
    print("register to register (instruction_retired): ", end='')
    print(instruction_counter - ins_mem_counter)
    print("Ile było tego rodzaju instrukcji: ", end='')
    print(line_counter - line_counter_mem)
    print("CPU_CLK (register): ", end='')
    print(cpu_clk - cpu_clk_mem)
    print()


if __name__ == '__main__':
    name = "result7zipnowe.csv"

    count_instr_type(name, 'mov')
    count_instr_type(name, 'movzx')
    count_instr_type(name, 'add')
    count_instr_type(name, 'sub')
    count_instr_type(name, 'cmp')
    count_instr_type(name, 'shl')
    count_instr_type(name, 'shr')
    count_instr_type(name, 'imul')
    print()
    print("Instruction retired (Block 1): ", end='')
    print(count_instr_ret_in_block(name, "Block 1:", "Block 2:"))
    print("Instruction retired (Block 2): ", end='')
    print(count_instr_ret_in_block(name, "Block 2:", "Block 3:"))
    print("Instruction retired (Block 3): ", end='')
    print(count_instr_ret_in_block(name, "Block 3:", "Block 4:"))
    print("Instruction retired (Block 4): ", end='')
    print(count_instr_ret_in_block(name, "Block 4:", "Block 5:"))
    print("Instruction retired (Block 5): ", end='')
    print(count_instr_ret_in_block(name, "Block 5:", "ret "))
