from modules import dbconnect

from hdwallet import HDWallet
from hdwallet.utils import generate_entropy
from hdwallet.symbols import ETH as SYMBOL
from typing import Optional
import json

# Choose strength 128, 160, 192, 224 or 256
STRENGTH: int = 128  # Default is 128
# Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean
LANGUAGE: str = "english"  # Default is english
# Generate new entropy hex string
ENTROPY: str = generate_entropy(strength=STRENGTH)
# Secret passphrase for mnemonic
PASSPHRASE: Optional[str] = None  # "meherett"

def generateKey(db:str, key_amount: int):
    # Initialize Bitcoin mainnet HDWallet
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL, use_default_path=False)
    # Get Bitcoin HDWallet from entropy
    hdwallet.from_entropy(
        entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE
    )
    # Derivation from path
    # Or derivation from index
    hdwallet.from_index(44, hardened=True)
    hdwallet.from_index(0, hardened=True)
    hdwallet.from_index(0, hardened=True)
    hdwallet.from_index(0)

    memnic = hdwallet.mnemonic()
    mnic = json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False)

    # 指定文件名
    file_name = f'db/{db}.json'
    db_name=f'db/{db}.db'
    # 将 mnic 保存到文件
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(mnic)

    print(f"数据已保存到 {file_name}")
    print(mnic)

    db_account = dbconnect.DBSqlite(db_name)
    sql = f'CREATE TABLE BatchWallet (address CHAR(100) NOT NULL, privekey TEXT NOT NULL);'
    db_account.createTable(sql)

    # derive keys
    for i in range(key_amount):
        hdwallet.from_index(i)
        
        prvkey = hdwallet.private_key()
        addr = hdwallet.p2pkh_address()
        print(addr)
        print(prvkey)
        sql = f"INSERT INTO BatchWallet VALUES"
        sql_value = " ('%s','%s')"%(addr ,prvkey)
        sql_exec = sql + sql_value
        db_account.insertData(sql_exec)

    print('generate key success')