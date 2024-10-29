import os
from dotenv import load_dotenv

load_dotenv('.env')

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
# print(f'MASTER_KEY : {MASTER_KEY}')
print(f'MASTER_ADDR : {MASTER_ADDR}')
print(f'TRANSFER_AMOUNT : {TRANSFER_AMOUNT}')
print(f'CONTRACT_ADDR : {CONTRACT_ADDR}')
print(f'CONTRACT_ABI : {CONTRACT_ABI}')

import generateKey
import batchOption

cls = batchOption.batchOption(DB_NAME, CONTRACT_ABI, CONTRACT_ADDR, RPC_URL)

def queryStatus():
    # 查询链接状态及合约状态
    # 查询价格， gas-price目前是自动从网络上获取的。
    cls.query_gas_price()
    cls.query_cnt_owner()
    # cls.get_master_balance(MASTER_KEY)
    # cls.get_addr_balance(MASTER_KEY)
    # cls.query_token_amount(MASTER_KEY)
    
def query_wallet_balance():
    cls.show_wallet(0)

def batch_op():
    # # 执行批量转帐
    # cls.batchTransfer(MASTER_KEY, TRANSFER_AMOUNT, 11)
    
    # # 执行批量mint
    # cls.batchMint(0)
    
    # 执行批量归集
    # cls.batchCollection(MASTER_ADDR, 50000000000000000000000, 0)
    
    cls.batchCollectionETH(MASTER_ADDR, 9)
    pass

if __name__ == "__main__":
    # 生成地址
    # generateKey.generateKey(DB_NAME, int(GERERATE_KEY_AMOUNT))
    
    # 查询，测试链接
    # queryStatus()
    
    # 查询 子钱包余额 eth/token
    # query_wallet_balance()
    
    # 批量操作
    batch_op()
    pass