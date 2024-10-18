from modules import dbconnect
from contract import contractAbi
from web3 import Web3
import time, json, web3
import eth_account

class batchOption():
    db_account = None
    w3 = Web3
    m_cnt = None
    def __init__(self, db:str, abi:str, addr:str, url:str):
        db_name=f'db/{db}.db'
        self.db_account = dbconnect.DBSqlite(db_name)
        sql = f'CREATE TABLE BatchWallet (address CHAR(100) NOT NULL, privekey TEXT NOT NULL);'
        self.db_account.createTable(sql)
        
        self.w3 = Web3(Web3.HTTPProvider(url))
        abi_invite = json.load(open(abi))
        self.m_cnt = contractAbi.contractAbi(abi_invite, addr , url)
        
    def get_master_balance(self, privKey:str):
        sendfrom = eth_account.Account.from_key(privKey)
        res = self.w3.eth.get_balance(sendfrom.address)
        eth = web3.Web3.from_wei(res, 'ether')
        print(f'master addr -{sendfrom.address}- balance : {eth}')

    def get_addr_balance(self, addr:str):
        res = self.w3.eth.get_balance(addr)
        eth = web3.Web3.from_wei(res, 'ether')
        print(f'addr -{addr}- balance : {eth}')

    def show_wallet(self):
        sql_data = f"select * from BatchWallet"
        accounts = self.db_account.getData(sql_data)
        account_count  = len(accounts)
        for index in range(0, account_count):
            address = accounts[index][0]
            key = accounts[index][1]
            print(f"{index}-Addr: {address}")
            print(f"key: {key}")
            eth_balance = self.w3.eth.get_balance(address)
            eth = web3.Web3.from_wei(eth_balance, 'ether')
            print(f'eth balance is : {eth}')
            
            print(f'token balance is : {self.m_cnt.balanceOf(address)}')


    def offlineSign(self, privkey, to, amount):
        if len(to) != 40 and (len(to) != 42 or to[0:2] != '0x'):
            return json.dumps({'code': 1, 'data': 'Invalid address'})

        sendfrom = eth_account.Account.from_key(privkey)
        price = self.w3.eth.gas_price 
        nonce = self.w3.eth.get_transaction_count(sendfrom.address, "pending")
        idC = self.w3.eth.chain_id;
        # 准备交易（不包括gas限制）
        transaction = {
            'to': to,
            'value': web3.Web3.to_wei(amount, 'ether'),
            'gasPrice': price,
            'nonce': nonce,
            'chainId': idC
        }
        # 估算gas限制
        gas_estimate = self.w3.eth.estimate_gas(transaction)
        # 将估算的gas限制添加到交易中
        transaction['gas'] = gas_estimate * 2
        # 签名交易
        signed_txn = self.w3.eth.account.sign_transaction(transaction, privkey)
        # 发送交易
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        # 等待交易被确认
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        return tx_hash.hex(), tx_receipt


    def batchTransfer(self, privkey:str, amount:float, retry_idx:int):
        sql_data = f"select * from BatchWallet"
        accounts = self.db_account.getData(sql_data)
        account_count  = len(accounts)
        for index in range(retry_idx, account_count):
            address = accounts[index][0]
            txid, receipt = self.offlineSign(privkey, address, amount)

            print(f"{index}-Transfer Process Address: {address}")
            print(f"txid is {txid}")
            # print(f"receipt is {receipt}")
            time.sleep(1)

    # 合约操作
    def batchMint(self, retry_idx:int):
        sql_data = f"select * from BatchWallet"
        accounts = self.db_account.getData(sql_data)
        
        account_count  = len(accounts)
        for index in range(retry_idx, account_count):
            address = accounts[index][0]
            privkey = accounts[index][1]
            sendfrom = eth_account.Account.from_key(privkey)
            print(sendfrom.address)
            txid= self.m_cnt.mint(privkey);
            print(f"{index}-Mint address : {address}")
            print(f"txid is {txid}")
            # print(f"receipt is {receipt}")
            time.sleep(1)


    def query_gas_price(self):
        print(f'gas_price is : {self.w3.eth.gas_price}')
        
    def query_cnt_owner(self):
        print(f'owner is:{self.m_cnt.owner()}')
    
    def query_token_amount(self, addr):
        print(f'token balance is:{self.m_cnt.balanceOf(addr)}')
    
    def batchCollection(self, masterAddr, tokenAmount, retry_idx):
        sql_data = f"select * from BatchWallet"
        accounts = self.db_account.getData(sql_data)
        
        account_count  = len(accounts)
        for index in range(retry_idx, account_count):
            address = accounts[index][0]
            privkey = accounts[index][1]
            sendfrom = eth_account.Account.from_key(privkey)
            print(sendfrom.address)
            txid= self.m_cnt.transfer(privkey, masterAddr, tokenAmount);
            print(f"Collection address : {address}")
            print(f"txid is {txid}")
            # print(f"receipt is {receipt}")