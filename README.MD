# Crypto Address Generator

A Python utility for generating cryptocurrency wallet addresses for multiple blockchain networks (TRC20 and ERC20) from a single key pair. This tool generates a private and public key pair using the SECP256k1 elliptic curve and creates addresses compatible with Tron and Ethereum networks.

## Features
- Generates a 256-bit private key.
- Creates a public key from the private key using SECP256k1.
- Produces TRC20 (Tron) and ERC20 (Ethereum) addresses from the same public key.
- Provides a secure and efficient way to generate cross-network wallet addresses without third-party libraries.

## Installation
Clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/crypto-address-generator.git
cd crypto-address-generator
pip install -r requirements.txt
python run.py
