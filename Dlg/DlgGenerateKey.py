import sys   # 系统模块，获得命令行参数1
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow,QWidget, QDialog, QLabel, QPushButton ,QHBoxLayout # 导入QAppliaction，QLabel以及QWidget

class DlgGenerateKey(QDialog):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DlgGenerateKey')
        self.setGeometry(100, 100, 300, 150)  # 设置对话框的尺寸和位置
        
        hly = QHBoxLayout(self);
        btnYes = QPushButton();
        btnYes.setText("Yes");
        # btnYes.clicked.connect()
        
        btnNo = QPushButton();
        btnNo.setText("No");
        btnNo.clicked.connect(self.close)
        
        hly.addWidget(btnYes);
        hly.addStretch(0);
        hly.addWidget(btnNo);
        
        screen = QDesktopWidget().screenGeometry()
        new_left = (screen.width() - self.width()) // 2
        new_top = (screen.height() - self.height()) // 2
        self.move(new_left, new_top)