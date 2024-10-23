import random
from eth_abi import encode
from eth_utils import keccak
import binascii

def get_random_nonce():
    # Python 中的 MAX_SAFE_INTEGER 等价
    return random.randint(0, 9007199254740991)

def find_valid_nonce(contract_address: str, mint_address: str, difficulty: int):
    # 计算目标值：2^256 / difficulty
    target = (2**256 - 1) // difficulty
    tried_nonces = set()

    while True:
        # 获取一个未使用过的随机 nonce
        while True:
            nonce = get_random_nonce()
            if nonce not in tried_nonces:
                break
        
        tried_nonces.add(nonce)

        # 将地址转换为字节
        contract_addr_bytes = bytes.fromhex(contract_address[2:])  # 移除 '0x' 前缀
        mint_addr_bytes = bytes.fromhex(mint_address[2:])

        # 打包数据
        packed_data = (
            contract_addr_bytes +  # address
            mint_addr_bytes +      # address
            nonce.to_bytes(32, 'big') +  # uint256
            difficulty.to_bytes(32, 'big')  # uint256
        )

        # 计算 keccak256 哈希
        hash_bytes = keccak(packed_data)
        hash_int = int.from_bytes(hash_bytes, 'big')
        
        print('Hash:', '0x' + hash_bytes.hex())
        
        if hash_int < target:
            print(f'Valid nonce found: {nonce}')
            return nonce
            
        print('Nonce:', nonce)

# 使用示例
def main():
    contract_address = '0x1234567890123456789012345678901234567890'
    mint_address = '0x0987654321098765432109876543210987654321'
    difficulty = 1000

    nonce = find_valid_nonce(contract_address, mint_address, difficulty)
    print(f'Final nonce: {nonce}')

# # 运行代码
# import asyncio
# asyncio.run(main())

main()