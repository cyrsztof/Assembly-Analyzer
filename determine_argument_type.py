from registers import *


def determine_argument_type(arguments):
    if not arguments:
        return "No Arguments"

    is_base_register = any(arg in base_registers for arg in arguments)
    is_special_register = any(arg in simd_registers for arg in arguments)
    is_memory = any("ptr" in arg for arg in arguments)
    is_constant = any(arg.startswith("0x") for arg in arguments)
    is_fpu_register = any(arg in fpu_registers for arg in arguments)

    if is_base_register and is_constant and not is_special_register and not is_memory:
        return "Base Registers with Constant Values"
    elif is_base_register and is_memory and not is_special_register and not is_constant:
        return "Base Registers with Memory"
    elif is_special_register and is_constant and not is_base_register and not is_memory:
        return "SIMD Registers with Constant Values"
    elif is_special_register and is_memory and not is_base_register and not is_constant:
        return "SIMD Registers with Memory"
    elif is_fpu_register and is_memory:
        return "FPU register with Memory"
    elif is_memory and is_constant:
        return "Memory with constant"
    elif is_fpu_register:
        return "FPU registers"
    elif is_base_register and not is_special_register and not is_memory and not is_constant:
        return "Base Registers"
    elif is_special_register and not is_base_register and not is_memory and not is_constant:
        return "SIMD Registers"
    elif is_memory and not is_base_register and not is_special_register and not is_constant:
        return "Memory"
    elif is_constant and not is_base_register and not is_special_register and not is_memory:
        return "Constant Values"
    else:
        return "Other"
