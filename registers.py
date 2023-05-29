# Define the lists of base registers and, fpu registers and SIMD registers
base_registers = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "rsp", "eax", "ebx", "ecx", "edx", "esi",
                  "edi", "ebp", "esp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15", "ax", "bx", "cx",
                  "dx", "al", "ah", "bl", "bh", "cl", "ch", "dl", "dh", "si", "di", "bp", "sp", "r8w", "r9w",
                  "r10w", "r11w", "r12w", "r13w", "r14w", "r15w", "sil", "dil", "bpl", "spl", "r8b", "r9b",
                  "r10b", "r11b", "r12b", "r13b", "r14b", "r15b", "r10d", "r11d", "r12d", "r13d", "r14d", "r15d"]
simd_registers = ["xmm0", "xmm1", "xmm2", "xmm3", "xmm4", "xmm5", "xmm6", "xmm7", "xmm8", "xmm9", "xmm10",
                  "xmm11", "xmm12", "xmm13", "xmm14", "xmm15"]
fpu_registers = ["st", "st(0)", "st(1)", "st(2)", "st(3)", "st(4)", "st(5)", "st(6)", "st(7)", "st(8)"]
