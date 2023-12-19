import os
import shutil
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, 
                             QLineEdit, QComboBox, QPushButton, QFileDialog)
from config import root_dir
import subprocess
import re
from path import Path



languages = ["hindi", "bengali", "telugu", "assamese", "bodo", "gujrati", "kannada", "malyalam", "marathi", "manipuri", "odiya", "punjabi", "tamil"]

class FileUtility(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Create widgets
        self.srcLineEdit = QLineEdit()
        self.actionCombo = QComboBox()
        self.actionCombo.addItems(languages)
        self.confirmBtn = QPushButton("Confirm")
        
        # Layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.srcLineEdit) 
        hbox.addWidget(self.actionCombo)
        hbox.addWidget(self.confirmBtn)
        
        self.setLayout(hbox) 
        self.setWindowTitle("Vaani")

        # Connect signals 
        # self.srcLineEdit.setText(os.path.("~"))
        self.confirmBtn.clicked.connect(self.handleAction)
        self.srcLineEdit.textChanged.connect(self.updateSrc)
        
    def updateSrc(self, path):
        self.src = path
    
    def handleAction(self):
        lang = self.actionCombo.currentText() 
        # dst = os.path.join(os.path.expanduser("~"), "Downloads")
        path = self.srcLineEdit.text()
        file = re.search(r"(?<=/)[^/]+$", path)

        shutil.copy(path, f"{root_dir}/input/")

        subprocess.run(f"python inference.py --audioname {file} --lang {lang}")
        # if action == "Copy":
        #     shutil.copy(self.src, dst)
            
        # elif action == "Move":
        #     shutil.move(self.src, dst)
            

if __name__ == "__main__":
    app = QApplication([])
    utils = FileUtility()
    utils.show()
    app.exec()