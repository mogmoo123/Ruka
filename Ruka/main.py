import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, \
    QGridLayout, QComboBox, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        self.ipt_block = ['autoci', 'basis', 'casresp', 'casscf', 'chelpg', 'cim', 'cis(tddft)', 'compound', 'conical', 'coords', 'cosmors', 'cpcm', 'docker', 'eda', 'elprop', 'eprnmr', 'esd', 'frag', 'freq', 'geom', 'goat', 'ice(iceci, cipsi)', 'irc', 'lft', 'loc', 'mcrpa', 'md', 'mdci', 'mecp', 'method', 'mm', 'mp2', 'mrcc', 'mrci', 'mtr', 'nbo', 'ndoparas', 'neb', 'numgrad', 'output', 'pal', 'paras', 'plots', 'qmmm', 'rel', 'rocis', 'rr', 'scf', 'shark', 'solvator', 'symmetry(sym)', 'vpt2', 'xtb']

        super().__init__()
        self.setWindowTitle("Ruka 0.1v")
        self.resize(720, 540)

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        #component & layout

        hbox1 = QHBoxLayout()
        btn_include = QPushButton("Include")
        lb_path = QLabel("Current File Path")
        lb_path.setStyleSheet("border: 3px solid #000000;"
                              "border-radius: 10px;")
        hbox1.addWidget(btn_include,1)
        hbox1.addWidget(lb_path,2)
        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()

        vbox2 = QVBoxLayout()
        vbox2.addStretch(2)
        cb_list = QComboBox()
        for i in self.ipt_block:
            cb_list.addItem(i)
        vbox2.addWidget(cb_list)

        hbox3 = QHBoxLayout()
        btn_put = QPushButton("Put")
        btn_pop = QPushButton("Pop")

        hbox3.addWidget(btn_put)
        hbox3.addWidget(btn_pop)
        vbox2.addLayout(hbox3)
        vbox2.addStretch(2)

        hbox2.addLayout(vbox2,1)

        lb_block_stack = QLabel("Kawaii")
        vbox3 = QVBoxLayout()
        lb_block_stack.setStyleSheet("border-color: #000000;"
                                     "border-style: solid;"
                                     "border-width: 3px;"
                                     "border-radius: 10px;"
                                     "font-size: 12px")
        vbox3.addWidget(lb_block_stack,10)
        hbox2.addLayout(vbox3,2)

        vbox4 = QVBoxLayout()
        vbox5 = QVBoxLayout()

        hbox4 = QHBoxLayout()
        le_block_name = QLineEdit()
        le_block_setting = QLineEdit()
        hbox4.addWidget(le_block_name,5)
        hbox4.addWidget(le_block_setting,7)

        hbox4_n = QHBoxLayout()
        lb_block_name = QLabel("Name")
        lb_block_setting = QLabel("Value")
        hbox4_n.addWidget(lb_block_name, 5)
        hbox4_n.addWidget(lb_block_setting, 7)

        vbox5.addLayout(hbox4_n)
        vbox5.addLayout(hbox4)
        vbox4.addStretch(3)
        vbox4.addLayout(vbox5)
        btn_push = QPushButton("Push")
        btn_run = QPushButton("Run")
        btn_export = QPushButton("Export")
        lb_result_s = QLabel("Success!")
        lb_result_f = QLabel("Failed")
        lb_result_s.setStyleSheet("border: 3px solid #27F580;"
                                "border-radius: 10px;"
                                "color: #057034;")
        lb_result_f.setStyleSheet("border: 3px solid #F52A27;"
                                  "border-radius: 10px;"
                                  "color: #9C0A07;")
        vbox4.addWidget(btn_push)
        vbox4.addWidget(btn_run)
        vbox4.addWidget(btn_export)
        vbox4.addWidget(lb_result_s)
        vbox4.addStretch(3)

        hbox2.addLayout(vbox4,1)
        vbox.addLayout(hbox2,1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont('메이플스토리', 12))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())