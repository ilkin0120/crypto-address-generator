import secrets
import hashlib
from eth_hash.auto import keccak
from ecdsa import SigningKey, SECP256k1


def generate_trc20_wallet(public_key):
    # Генерация адреса на основе публичного ключа (SHA3-256).
    # Tron, которая стандартизировала алгоритм SHA3-256 (из семейства SHA-3) для генерации адресов.
    sha3_hash = hashlib.new('sha3_256', public_key).digest()
    # Префикс "41" выбран разработчиками Tron как уникальный идентификатор для сети, позволяющий легко распознать, что адрес принадлежит именно Tron.
    address = "41" + sha3_hash[-20:].hex()  # Добавляем Tron Network Prefix "41"

    # Преобразование адреса Tron в базовый формат (начинается с "T")
    tron_address = base58_check_encoding(bytes.fromhex(address))

    return tron_address


def base58_check_encoding(data):
    # Преобразуем в формат Base58Check для адреса Tron (начинается с "T")
    checksum = hashlib.sha256(hashlib.sha256(data).digest()).digest()[:4]
    return base58_encode(data + checksum)


def base58_encode(data):
    # Кодирование Base58 для адреса
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = int.from_bytes(data, 'big')
    encoded = ""
    while num > 0:
        num, rem = divmod(num, 58)
        encoded = alphabet[rem] + encoded
    return encoded


def generate_keys():
    private_key = secrets.token_bytes(32)
    sk = SigningKey.from_string(private_key, curve=SECP256k1)
    public_key = sk.get_verifying_key().to_string()
    return private_key, public_key


def get_erc20_address(public_key):
    keccak_hash = keccak(public_key)
    address = "0x" + keccak_hash[-20:].hex()  # Префикс Ethereum "0x"
    return address
