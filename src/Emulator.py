
import sys
from pathlib import Path
path = Path("Emulator.py")

registers = [0,0,0,0,0]
lines = []

with open(str(path.parent.absolute()) + '\\tests\\test.meowbin') as file:
    lines = [line.rstrip() for line in file]


instruction_map = {
    "0000": "MOV",
    "0001": "ADD",
    "0010": "SUB",
    "0100": "CMP"
}

register_map = {
    "00000": "PLACEHOLDER",
    "00001": 0,
    "00010": 1,
}

def str_to_2complement(val_str):
    val = int(val_str, 2)
    b = val.to_bytes(1, byteorder=sys.byteorder, signed=False)                                                          
    return int.from_bytes(b, byteorder=sys.byteorder, signed=True)
        
print("MeowCPU Now Executing...\nLOG:")
for line in lines:
    split = line.split()
    if len(split) > 3: raise SyntaxError("Invalid binary input, each line must be a length of 18 chars.")
        
    instruction = split[0]
    if instruction not in instruction_map:  raise SyntaxError(f"Invalid Instruction: {instruction}")
    instruction = instruction_map[instruction]
        
    register = split[1]
    if register not in register_map:   raise SyntaxError(f"Invalid Register: {register}")
    register = register_map[register]
    
    value = str_to_2complement(split[2])
    print(f"Executing BIN: {line} // ASM: {instruction} {register} {value}")
    if instruction == "MOV": registers[register] = value
    elif instruction == "ADD": registers[2] = registers[0] + registers[1]
    elif instruction == "SUB": registers[3] = registers[0] - registers[1]
    elif instruction == "CMP":
        if registers[0] == registers[1]: registers[4] = 2
        if registers[0] > registers[1]: registers[4] = 1
        if registers[0] < registers[1]: registers[4] = 4
    
print("\nRegister Table\n")
print(registers[0], "| A")
print(registers[1], "| B")
print(registers[2], "| C")
print(registers[3], "| D")
print(registers[4], "| E")