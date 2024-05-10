from PySide6.QtWidgets import QMainWindow, QApplication
from main import Ui_MainWindow

class CalcualtorLogic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui. setupUi(self)
        
        self.ui.button_0.clicked.connect(lambda: self.number_pressed(0))
        self.ui.button_1.clicked.connect(lambda: self.number_pressed(1))
        self.ui.button_2.clicked.connect(lambda: self.number_pressed(2))
        self.ui.button_3.clicked.connect(lambda: self.number_pressed(3))
        self.ui.button_4.clicked.connect(lambda: self.number_pressed(4))
        self.ui.button_5.clicked.connect(lambda: self.number_pressed(5))
        self.ui.button_6.clicked.connect(lambda: self.number_pressed(6))
        self.ui.button_7.clicked.connect(lambda: self.number_pressed(7))
        self.ui.button_8.clicked.connect(lambda: self.number_pressed(8))
        self.ui.button_9.clicked.connect(lambda: self.number_pressed(9))
        
        self.ui.button_p.clicked.connect(lambda: self.operation_pressed('+'))
        self.ui.button_m.clicked.connect(lambda: self.operation_pressed('-'))
        self.ui.button_x.clicked.connect(lambda: self.operation_pressed('*'))
        self.ui.button_d.clicked.connect(lambda: self.operation_pressed('/'))
        self.ui.button_t.clicked.connect(lambda: self.operation_pressed('.'))
        self.ui.button_e.clicked.connect(self.equals_pressed)
        self.ui.button_c.clicked.connect(self.clear_pressed)
        
        self.equation = ''
        
    def number_pressed(self, number):
        self.equation += str(number)
        self.ui.output.setText(self.equation)
        
    def operation_pressed(self, operation):
        self.equation += operation
        self.ui.output.setText(self.equation)
        
    def equals_pressed(self):
        try:
            result = eval(self.equation)
            self.ui.output.setText(str(result))
            self.equation = str(result)
        except:
            self.ui.output.setText('Error')
            self.equation = ''
    
    def clear_pressed(self):
        self.equation = ''
        self.ui.output.setText(self.equation)
    
if __name__ == "__main__":
    app = QApplication()
    window = CalcualtorLogic()
    window.show()
    app.exec()