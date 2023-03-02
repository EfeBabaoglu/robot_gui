import sys
from PyQt5.QtWidgets import QApplication
from gui import Ui_MainWindow

from PyQt5.QtWidgets import *

class ui_windows(QMainWindow):
    def __init__(self):
        super(ui_windows, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.selected = [] 
        #self.movie = QMovie("loading-loading.gif")
		#self.setMovie(self.movie)
        self.ui.gif_label.movie=("loading-loading.gif")

		#self.startAnimation()


        self.kordinatler = {
            "1": [55,4,3,2],
            "2":[10,7,20,5],
            "3":[40,30,29,19],
            "4":[1,3,5,6],
            "5":[10,20,30,40],
            "6":[13,43,64,67],
        }

        

        self.ui.rbuton1.toggled.connect(lambda: self.radionbutton(self.ui.rbuton1))
        self.ui.rbuton2.toggled.connect(lambda: self.radionbutton(self.ui.rbuton2))
        self.ui.rbuton3.toggled.connect(lambda: self.radionbutton(self.ui.rbuton3))
        self.ui.rbuton4.toggled.connect(lambda: self.radionbutton(self.ui.rbuton4))
        self.ui.rbuton5.toggled.connect(lambda: self.radionbutton(self.ui.rbuton5))
        self.ui.rbuton6.toggled.connect(lambda: self.radionbutton(self.ui.rbuton6))

        self.ui.Sendbuton.clicked.connect(self.send_fnc)
    

    def radionbutton(self, b):
        if b.isChecked():
            print(self.kordinatler[b.text()])
            self.selected = self.kordinatler[b.text()]
    
    def send_fnc(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.info_label.setText(f"heading to {self.selected}")
        print(f"heading to {self.selected}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ui_windows()

    win.show()
    sys.exit(app.exec_())
