from fileConverterUi import *
from PyQt5.QtWidgets import *
import csv

class fileConverter(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(500, 600)

        #hides everything so the process of converting is step by step
        self.yesButton.hide()
        self.errorLabel.setText('')
        self.noButton.hide()
        self.newFileInput.hide()
        self.newFileLabel.hide()
        self.newFileButton.hide()
        self.endMessage.hide()
        self.renameLabel.hide()
        self.pushButton.hide()

        #connects functions to buttons
        self.fileButton.clicked.connect(lambda: self.enterFile())
        self.pushButton.clicked.connect(lambda: self.askRename())
        outputfile = ''
        self.newFileButton.clicked.connect(lambda: self.enterNewFile())

    #gets input file
    def enterFile(self):
        fileName = self.fileInput.text().strip()
        fileExists = False
        while not fileExists:
            try:
                with open(fileName, 'r') as thisisatest:
                    fileExists = True
                    self.errorLabel.hide()
                    self.yesButton.show()
                    self.noButton.show()
                    self.renameLabel.show()
                    self.pushButton.show()
            except:
                self.errorLabel.setText('Could not find that file! try again!')
            break


    def askRename(self):
        if self.noButton.isChecked():
            outputName = self.fileInput.text().strip().split('.')[0] + '.csv'
            self.convert(outputName)
        elif self.yesButton.isChecked():
            self.newFileLabel.show()
            self.newFileInput.show()
            self.newFileButton.show()




    def enterNewFile(self):
        outputfile = self.newFileInput.text().strip()
        self.convert(outputfile)



    def convert(self, outf):
        emaill = []
        subjectl = []
        confidencel = []
        fileName = self.fileInput.text().strip()
        with open(fileName, 'r') as inpt:
            with open(outf, 'w', newline='') as outcsv:
                header = ['Email', 'Subject', 'Confidence']
                content = csv.writer(outcsv)
                content.writerow(header)
                for line in inpt:
                    if line.startswith('From:'):
                        email = line.strip().split()[1]
                        emaill.append(email)
                    if line.startswith('Subject:'):
                        subject = line.strip().split()[4]
                        subjectl.append(subject)
                    if line.startswith('X-DSPAM-Confidence:'):
                        confidence = line.strip().split()[1]
                        confidencel.append(confidence)
                for i in range(len(emaill)):
                    content.writerow([emaill[i], subjectl[i], confidencel[i]])
                self.endMessage.show()
                self.endMessage.setText('Finished! your file is '+outf+'.')
