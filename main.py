import os
from dotenv import load_dotenv

load_dotenv('.env_test')

DB_NAME = os.getenv("DB_NAME")
GERERATE_KEY_AMOUNT = os.getenv("GERERATE_KEY_AMOUNT")
RPC_URL = os.getenv("RPC_URL")
MASTER_ADDR = os.getenv("MASTER_ADDR")
MASTER_KEY = os.getenv("MASTER_KEY")
TRANSFER_AMOUNT = os.getenv("TRANSFER_AMOUNT")
CONTRACT_ADDR = os.getenv("CONTRACT_ADDR")
CONTRACT_ABI = os.getenv("CONTRACT_ABI")

print(f'DB_NAME : {DB_NAME}')
print(f'GERERATE_KEY_AMOUNT : {GERERATE_KEY_AMOUNT}')
print(f'RPC_URL : {RPC_URL}')
print(f'MASTER_KEY : {MASTER_KEY}')
print(f'MASTER_ADDR : {MASTER_ADDR}')
print(f'TRANSFER_AMOUNT : {TRANSFER_AMOUNT}')
print(f'CONTRACT_ADDR : {CONTRACT_ADDR}')
print(f'CONTRACT_ABI : {CONTRACT_ABI}')

import generateKey
import batchOption

if __name__ == "__main__":
    # # 先生成地址
    # generateKey.generateKey(DB_NAME, int(GERERATE_KEY_AMOUNT))

    # 批量操作 class
    cls = batchOption.batchOption(DB_NAME, CONTRACT_ABI, CONTRACT_ADDR, RPC_URL)
    # 查询链接状态及合约状态
    # 查询价格， gas-price目前是自动从网络上获取的。
    cls.query_gas_price()
    # cls.get_master_balance(MASTER_KEY)
    cls.get_addr_balance('0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045')
    cls.query_cnt_owner()
    
    # 查询代币balance
    cls.query_token_amount('0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045')
    
    # # 执行批量转帐
    # cls.batchTransfer(MASTER_KEY, TRANSFER_AMOUNT)
    
    # # 执行批量mint
    # cls.batchMint()
    
    ## 执行批量归集
    # cls.batchCollection(MASTER_ADDR, 10000000000000000000000000000)