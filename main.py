import sys
from email.policy import default

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, \
    QGridLayout, QComboBox, QHBoxLayout
from easygui import fileopenbox, filesavebox

class MainWindow(QWidget):
    def __init__(self):
        self.ipt_block = ['autoci', 'basis', 'casresp', 'casscf', 'chelpg', 'cim', 'cis(tddft)', 'compound', 'conical', 'coords', 'cosmors', 'cpcm', 'docker', 'eda', 'elprop', 'eprnmr', 'esd', 'frag', 'freq', 'geom', 'goat', 'ice(iceci, cipsi)', 'irc', 'lft', 'loc', 'mcrpa', 'md', 'mdci', 'mecp', 'method', 'mm', 'mp2', 'mrcc', 'mrci', 'mtr', 'nbo', 'ndoparas', 'neb', 'numgrad', 'output', 'pal', 'paras', 'plots', 'qmmm', 'rel', 'rocis', 'rr', 'scf', 'shark', 'solvator', 'symmetry(sym)', 'vpt2', 'xtb']

        super().__init__()
        self.setWindowTitle("Ruka 0.1v")
        self.resize(720,720)

        self.initUI()
        self.btn_pop.setDisabled(True)
        self.btn_put.setDisabled(True)
        self.btn_push.setDisabled(True)
        self.btn_run.setDisabled(True)
        self.btn_export.setDisabled(True)
        self.lb_result_s.setVisible(False)
        self.lb_result_f.setVisible(False)

    def reload(self):
        self.file.seek(0)
        s = self.file.readlines()
        display = ""
        for i in s:
            display += i
        self.lb_block_stack.setText(display)

    def load(self): #Load .xyz file and Display it
        path = str(fileopenbox(default='C:\\*.inp'))
        self.lb_path.setText(path) #display
        self.btn_pop.setDisabled(False)
        self.btn_put.setDisabled(False)
        self.btn_push.setDisabled(False)
        self.btn_run.setDisabled(False)
        self.btn_export.setDisabled(False)

        self.file = open(path,'r+')#File Load
        self.reload()

    def prepare_edit(self):
        self.file.seek(0)
        pos = 0
        while self.file.readline() != "\n":
            pos = self.file.tell()
        self.file.seek(pos)
        self.file.write("#ROBOCO-SAN KAWAII\n")
        self.file.write("\n")
        self.reload()

    def add(self):
        self.prepare_edit()
        pass

    def pop(self):
        pass

    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        #component & layout
        #DONT TOUCH!!!
        hbox1 = QHBoxLayout()
        self.btn_include = QPushButton("Load")
        self.btn_include.clicked.connect(self.load)
        self.lb_path = QLabel("Current File Path")
        self.lb_path.setStyleSheet("border: 3px solid #000000;"
                              "border-radius: 10px;")
        hbox1.addWidget(self.btn_include,1)
        hbox1.addWidget(self.lb_path,2)
        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()

        vbox2 = QVBoxLayout()
        vbox2.addStretch(2)
        self.cb_list = QComboBox()
        for i in self.ipt_block:
            self.cb_list.addItem(i)
        vbox2.addWidget(self.cb_list)

        hbox3 = QHBoxLayout()
        self.btn_put = QPushButton("Put")
        self.btn_put.clicked.connect(self.add)
        self.btn_pop = QPushButton("Pop")
        self.btn_pop.clicked.connect(self.pop)

        hbox3.addWidget(self.btn_put)
        hbox3.addWidget(self.btn_pop)
        vbox2.addLayout(hbox3)
        vbox2.addStretch(2)

        hbox2.addLayout(vbox2,1)

        self.lb_block_stack = QLabel("Kawaii")
        vbox3 = QVBoxLayout()
        self.lb_block_stack.setStyleSheet("border-color: #000000;"
                                     "border-style: solid;"
                                     "border-width: 3px;"
                                     "border-radius: 10px;"
                                     "font-size: 12px")
        vbox3.addWidget(self.lb_block_stack,10)
        hbox2.addLayout(vbox3,2)

        vbox4 = QVBoxLayout()
        vbox5 = QVBoxLayout()

        hbox4 = QHBoxLayout()
        self.le_block_name = QLineEdit()
        self.le_block_setting = QLineEdit()
        hbox4.addWidget(self.le_block_name,5)
        hbox4.addWidget(self.le_block_setting,7)

        hbox4_n = QHBoxLayout()
        lb_block_name = QLabel("Name")
        lb_block_setting = QLabel("Value")
        hbox4_n.addWidget(lb_block_name, 5)
        hbox4_n.addWidget(lb_block_setting, 7)

        vbox5.addLayout(hbox4_n)
        vbox5.addLayout(hbox4)
        vbox4.addStretch(3)
        vbox4.addLayout(vbox5)
        self.btn_push = QPushButton("Push")
        self.btn_run = QPushButton("Run")
        self.btn_export = QPushButton("Export")
        self.lb_result_s = QLabel("Success!")
        self.lb_result_f = QLabel("Failed")
        self.lb_result_s.setStyleSheet("border: 3px solid #27F580;"
                                "border-radius: 10px;"
                                "color: #057034;")
        self.lb_result_f.setStyleSheet("border: 3px solid #F52A27;"
                                  "border-radius: 10px;"
                                  "color: #9C0A07;")
        vbox4.addWidget(self.btn_push)
        vbox4.addWidget(self.btn_run)
        vbox4.addWidget(self.btn_export)
        vbox4.addWidget(self.lb_result_s)
        vbox4.addWidget(self.lb_result_f)
        vbox4.addStretch(3)

        hbox2.addLayout(vbox4,1)
        vbox.addLayout(hbox2,1)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont('메이플스토리', 12))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())