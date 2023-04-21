import subprocess
from PyQt5.QtWidgets import QApplication, QComboBox, QDialog, QGridLayout, QLabel, QPushButton, QProgressBar, QVBoxLayout

class MainWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Bypassr1n-GUI')
        self.setLayout(QVBoxLayout())
        self.version_combo = QComboBox()
        self.version_combo.addItems(['12', '13', '14', '15'])
        self.layout().addWidget(QLabel('Select iOS version:'))
        self.layout().addWidget(self.version_combo)
        self.button_dualboot = QPushButton('Bypass DualBoot')
        self.button_tethered = QPushButton('Tethered Bypass')
        self.button_jailbreak = QPushButton('run specificing semi-thered palera1n jailbreak')
        self.button_rec = QPushButton('Exit Recovery Mode')
        self.layout().addWidget(self.button_dualboot)
        self.layout().addWidget(self.button_tethered)
        self.layout().addWidget(self.button_jailbreak)
        self.layout().addWidget(self.button_rec)
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.layout().addWidget(self.progress_bar)
        self.button_dualboot.clicked.connect(self.execute_dualboot)
        self.button_jailbreak.clicked.connect(self.execute_jailbreak)
        self.button_tethered.clicked.connect(self.execute_tethered)
        self.button_rec.clicked.connect(self.execute_rec)

        self.layout().addWidget(QLabel('GUI Made By RIFOX'))
        self.layout().addWidget(QLabel('Thanks to Edwin'))




    def execute_command(self, command):
        self.progress_bar.setValue(0)
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        while True:
            output = process.stdout.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                # Update the progress bar with the output of the command
                self.progress_bar.setValue(self.progress_bar.value() + 1)
                print(output.strip())

    def execute_dualboot(self):
        version = self.version_combo.currentText()
        #command = [f'sudo cd /binaries/Linux && ./irecovery','-n']
        command = ['/usr/bin/sudo', './bypassr1n.sh', '--dualboot', version]
        self.execute_command(command)

    def execute_tethered(self):
        version = self.version_combo.currentText()
        command = ['/usr/bin/sudo', './bypassr1n.sh', '--tethered', version]
        self.execute_command(command)

    def execute_jailbreak(self):
        version = self.version_combo.currentText()
        command = ['/usr/bin/sudo', './bypassr1n.sh', '--dualboot', version, '--jail_palera1n']
        self.execute_command(command)

    def execute_rec(self):
        version = self.version_combo.currentText()
        command = ['/usr/bin/sudo', 'irecovery', '-n']
        self.execute_command(command)




if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
