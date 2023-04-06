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


def count_instr_type(filename, instruction):
    instruction_counter = 0
    ins_mem_counter = 0

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)  # pomija nagłówek pliku
        for row in reader:

            if row[2].find(instruction) != -1:
                arguments = get_arguments(row[2])
                instruction_counter += int(row[3])
                if ("0x" in arguments[0]) | ("0x" in arguments[1]) | ("ptr" in arguments[0]) | ("ptr" in arguments[1]):
                    ins_mem_counter += int(row[3])

    print(instruction + ": ", end='')
    print(instruction_counter)
    print("memory: ", end='')
    print(ins_mem_counter)
    print("register to register: ", end='')
    print(instruction_counter - ins_mem_counter)


if __name__ == '__main__':
    name = "result7zipnowe.csv"
    # print_rows('result.csv')
    count_instr_type(name, 'mov')
    #count_instr_type(name, 'add')
    #count_instr_type(name, 'sub')
    #count_instr_type(name, 'and')
    #count_instr_type(name, 'cmp')
    # print(get_mnemonic("mov qword ptr [rsp+0x30], rbx"))
    # print(get_arguments("mov qword ptr [rsp+0x30], rbx"))
