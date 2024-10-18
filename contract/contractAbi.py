from web3 import Web3
import web3

import eth_account

class contractAbi(object):
    def __init__(self, json_abi, contract_address, endpoint):
        # if endpoint.find('http://') == -1:
        #     endpoint = 'http://' + endpoint
        self.web3 = Web3(Web3.HTTPProvider(endpoint))
        ckaddress = web3.Web3.to_checksum_address(contract_address)
        self.contract = self.web3.eth.contract(address=ckaddress, abi=json_abi)

    def PrintAllFunction(self):
        print(self.contract.all_functions())

    def owner(self):
        return self.contract.caller().owner()
    
    def balanceOf(self, addr):
        return self.contract.caller().balanceOf(addr)
    
    def mint(self, privKey):
        sendfrom = eth_account.Account.from_key(privKey)
        privateKey = sendfrom._key_obj
        publicKey = privateKey.public_key
        address = publicKey.to_checksum_address()
        gasprice = self.web3.eth.gas_price
        nonce = self.web3.eth.get_transaction_count(address, "pending")

        method = self.contract.functions.mint();
        # 获取Gas估算
        estimate_gas = method.estimate_gas({'from': address});
        # 防止gas不够，发送 *2
        unsigned_tx = method.build_transaction({'gas': estimate_gas*2,
                                                'gasPrice':gasprice, 'from': address, 'nonce':nonce})
        signed_tx = sendfrom.sign_transaction(unsigned_tx)
        txid = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        # tx_receipt = self.web3.eth.wait_for_transaction_receipt(txid)
        return txid.hex()
    
    def transfer(self, privKey, addr, value):
        sendfrom = eth_account.Account.from_key(privKey)
        privateKey = sendfrom._key_obj
        publicKey = privateKey.public_key
        address = publicKey.to_checksum_address()
        gasprice = self.web3.eth.gas_price
        nonce = self.web3.eth.get_transaction_count(address, "pending")

        method = self.contract.functions.transfer(addr, value);
        # 获取Gas估算
        estimate_gas = method.estimate_gas({'from': address});
        # 防止gas不够，发送 *2
        unsigned_tx = method.build_transaction({'gas': estimate_gas*2,
                                                'gasPrice':gasprice, 'from': address, 'nonce':nonce})
        signed_tx = sendfrom.sign_transaction(unsigned_tx)
        txid = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        # tx_receipt = self.web3.eth.wait_for_transaction_receipt(txid)
        return txid.hex()
    
