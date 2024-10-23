import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton ,QHBoxLayout,QVBoxLayout
from Dlg import DlgGenerateKey


def onGenerateKeyClicked():
    dlg = DlgGenerateKey.DlgGenerateKey()
    dlg.exec()
    pass

def onTransferEthClicked():
    pass

def onMintClicked():
    pass
    
def onQueryStatusClicked():
    pass

def onCollectionClicked():
    pass
    
def onQueryWalletInfoClicked():
    pass
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWaindow = QWidget()
    mainWaindow.resize(300,150)
    mainWaindow.setWindowTitle('Batch Option')
    # btn
    btnGenerateKey = QPushButton();
    btnGenerateKey.setText("Generate Key");   
    btnGenerateKey.clicked.connect(onGenerateKeyClicked) 
    
    btnQueryStatus = QPushButton();
    btnQueryStatus.setText("Query Connect Status");
    btnQueryStatus.clicked.connect(onQueryStatusClicked)
    
    btnTransferEth = QPushButton();
    btnTransferEth.setText("Transfer ETH");
    btnTransferEth.clicked.connect(onTransferEthClicked) 
    
    btnMint = QPushButton();
    btnMint.setText("Mint");
    btnMint.clicked.connect(onMintClicked)
    
    btnCollection = QPushButton();
    btnCollection.setText("Collection");
    btnCollection.clicked.connect(onCollectionClicked)
    
    btnQueryWalletInfo = QPushButton()
    btnQueryWalletInfo.setText('Query Wallet Info')
    btnQueryWalletInfo.clicked.connect(onQueryWalletInfoClicked)
    # ly
    hly = QHBoxLayout()
    hly.addWidget(btnGenerateKey)
    hly.addWidget(btnQueryStatus)
    hly.addStretch(0)
    
    hly2 = QHBoxLayout()
    hly2.addWidget(btnTransferEth)
    hly2.addWidget(btnMint)
    hly2.addWidget(btnCollection)
    hly2.addWidget(btnQueryWalletInfo)
    hly2.addStretch(0)
    
    mainly = QVBoxLayout(mainWaindow)
    mainly.addLayout(hly)
    mainly.addLayout(hly2)
    mainWaindow.show()
    
    sys.exit(app.exec_())