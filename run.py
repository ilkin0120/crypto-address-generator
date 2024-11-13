from functionality import generate_keys, get_erc20_address, generate_trc20_wallet

private_key, public_key = generate_keys()
tron_address = generate_trc20_wallet(public_key)
ethereum_address = get_erc20_address(public_key)

print(f"TRC20 Address: {tron_address}")
print(f"ERC20 Address: {ethereum_address}")