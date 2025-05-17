import base58
import struct

data_b58 = "3Bxs..."  # example base58 instruction data
data_bytes = base58.b58decode(data_b58)

instruction_index = data_bytes[0]
amount = struct.unpack("<Q", data_bytes[1:9])[0]

print(f"Instruction: {instruction_index}, Amount: {amount}")
