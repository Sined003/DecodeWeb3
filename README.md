
# DecodeWeb3

**Decode Solana Web3**

---

## Overview

DecodeWeb3 is a Python project designed to decode Solana blockchain transaction data and Web3 instruction payloads. It helps developers interpret raw transaction data and understand the underlying instructions on the Solana network.

This tool is useful for blockchain developers, auditors, and analysts who want to parse and analyze Solana transaction instructions programmatically.

---

## Features

- Decode base58-encoded Solana transaction instruction data
- Support for common Solana programs and custom instruction formats
- Simple Python interface for fetching and decoding transaction data
- MIT licensed open source project

---

## Prerequisites

- Python 3.7 or higher
- Internet connection to access Solana RPC endpoints
- Basic knowledge of Solana transaction structure and instruction data

---

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/Sined003/DecodeWeb3.git
   cd DecodeWeb3
   ```

2. (Optional) Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies (if any):

   ```
   pip install -r requirements.txt
   ```

---

## Usage

The main decoding logic is in `d.py`. You can run or import this script to decode Solana transaction data.

Example usage:

```
from d import decode_instruction_data

# Example base58-encoded instruction data
data_b58 = "3Bxs..."

decoded = decode_instruction_data(data_b58)
print(decoded)
```

Replace `"3Bxs..."` with actual instruction data from a Solana transaction.

---

## How It Works

- The script decodes base58-encoded instruction data into raw bytes.
- It parses the bytes according to known Solana program instruction layouts.
- Outputs human-readable decoded data fields for analysis.

---

## Contributing

Contributions and improvements are welcome! Feel free to open issues or submit pull requests.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

