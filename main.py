from fileConverter import *

def main():
    app = QApplication([])
    window = fileConverter()
    window.setWindowTitle('File Converter')
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
