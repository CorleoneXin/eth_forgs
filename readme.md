Python 3.10.10

python3 -m venv .venv

pip3 install web3==6.12.0
pip3 install PyMySQL==1.1.1
pip3 install pyqt5==5.15.11
pip3 install hdwallet==2.2.1
pip install python-dotenv

# use
* 手动创建文件夹 db
* 重命名 .env.example 为 .env
* 填写.env配置文件
```md
DB_NAME='eth_forgs_1'
GERERATE_KEY_AMOUNT=5

RPC_URL='http://175.41.153.124:8545'
MASTER_ADDR='0xb3966CF2797F9c1ce9C9BF050d1dBf540Fcb66C1'
MASTER_KEY='8c1968f63c61e9e6f2437c4ec176d93e73c8fcb46824df6acf813d408ee9a7bd'
TRANSFER_AMOUNT=10

CONTRACT_ABI='contract/forg.abi'
CONTRACT_ADDR='0x75989f773dafeab9106dB792B5FA4aBBf80E64F2'
```
* NOTE：
1. gas limit为了防止意外，设置的是 * 2,可以全局搜索，然后修改gas_limit,反正也会退回，无所谓。多了总比少了好
```python
estimate_gas*2
```

2. gas目前是从网络上获取的，如果不合适，可以全局查询以下代码，然后手动+x：
gasprice = self.web3.eth.gas_price + x
```python
gasprice = self.web3.eth.gas_price
```

* 运行：python main.py