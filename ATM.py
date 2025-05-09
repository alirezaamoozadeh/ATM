from  PySide6.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QHBoxLayout,QVBoxLayout,QMainWindow,QStackedWidget



class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(600,600)
        self.setWindowTitle("ATM")

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        def switch_page(index):
            self.stack.setCurrentIndex(index)

        self.pages = [First_window(switch_page),
                      Persian_Password_window(switch_page),
                      English_Password_window(switch_page),
                      Persian_emkanat_window(switch_page),
                      English_emkanat_window(switch_page),
                      Persian_editPassword_window(switch_page),
                      English_editPassword_window(switch_page),
                      Persian_Money_transfer_window(switch_page),
                      English_Money_transfer_window(switch_page),
                      Persian_Account_Balalnce(switch_page),
                      English_Account_Balalnce(switch_page),
                      Persian_Get_Cash_window(switch_page),
                      Persian_payan(switch_page),
                      English_payan(switch_page)]
        for page in self.pages:
            self.stack.addWidget(page)

        self.stack.setCurrentIndex(0)


class First_window(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()


        #   siza & title
        self.setWindowTitle('ATM')
        self.resize(600,600)


        # lables & buttons
        Persian_language = QPushButton(self)
        Persian_language.setText("فارسی")
        Persian_language.setGeometry(0,250,1000,1000)
        # click
        Persian_language.clicked.connect(lambda: switch_page_callback(1))

        information1 = QLabel(self)
        information1.setText('زبان خود را انتخاب کنید')
        information2 = QLabel(self)
        information2.setText('choose language')
        english_language = QPushButton(self)
        english_language.setText("English")
        english_language.setGeometry(500,250,1000,1000)
        # click
        english_language.clicked.connect(lambda: switch_page_callback(2))

        # layouts
        layout1 = QHBoxLayout()
        layout1.addWidget(Persian_language)
        layout1.addWidget(information1)
        layout1.addStretch()
        layout1.addWidget(information2)
        layout1.addWidget(english_language)
        self.setLayout(layout1)


class Persian_Password_window(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()

        # title & size
        self.setWindowTitle('صفحه رمز')
        self.resize(600,600)

        # label & lineedit
        information1 = QLabel('لطفا رمز خود را وارد کنید!',self)
        input_password = QLineEdit(self)
        input_password.setGeometry(300,200,50,50)
        ok_button = QPushButton('تایید',self)
        ok_button.setGeometry(500,500,20,50)

        ok_button.clicked.connect(lambda: switch_page_callback(3))

        # layout
        layout1 = QVBoxLayout()
        layout1.addStretch()
        layout1.addWidget(information1)
        layout1.addWidget(input_password)
        layout1.addStretch()
        layout1.addWidget(ok_button)

        self.setLayout(layout1)

class English_Password_window(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()

        # title & size
        self.setWindowTitle('Password window')
        self.resize(600,600)

        # label & lineedit
        information1 = QLabel('Please enter password!',self)
        input_password = QLineEdit(self)
        input_password.setGeometry(300,200,50,50)
        ok_button = QPushButton('submit',self)
        ok_button.setGeometry(500,500,20,50)

        ok_button.clicked.connect(lambda: switch_page_callback(4))

        # layout
        layout1 = QVBoxLayout()
        layout1.addStretch()
        layout1.addWidget(information1)
        layout1.addWidget(input_password)
        layout1.addStretch()
        layout1.addWidget(ok_button)

        self.setLayout(layout1)


class Persian_emkanat_window(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()


        #   siza & title
        self.setWindowTitle('صفحه امکانات')
        self.resize(600,600)


        # lables & buttons
        change_password = QPushButton(self)
        change_password.setText("تغییر رمز")
        change_password.setGeometry(0,250,1000,1000)
        change_password.clicked.connect(lambda: switch_page_callback(5))
        bardasht_vagh = QPushButton(self)
        bardasht_vagh.setText("برداشت وجه")
        bardasht_vagh.setGeometry(0, 250, 1000, 1000)
        bardasht_vagh.clicked.connect(lambda: switch_page_callback(11))
        mandeh_cart = QPushButton(self)
        mandeh_cart.setText("مانده کارت")
        mandeh_cart.setGeometry(0, 250, 1000, 1000)
        mandeh_cart.clicked.connect(lambda: switch_page_callback(9))
        cart_be_cart = QPushButton(self)
        cart_be_cart.setText("انتقال وجه")
        cart_be_cart.setGeometry(0, 250, 1000, 1000)
        cart_be_cart.clicked.connect(lambda: switch_page_callback(7))


        # layouts
        layout1 = QVBoxLayout()
        layout1.addWidget(change_password)
        layout1.addSpacing(20)
        layout1.addWidget(bardasht_vagh)
        layout2 = QVBoxLayout()
        layout2.addWidget(mandeh_cart)
        layout2.addSpacing(20)
        layout2.addWidget(cart_be_cart)
        layout3 = QHBoxLayout()
        layout3.addLayout(layout1)
        layout3.addStretch()
        layout3.addLayout(layout2)
        self.setLayout(layout3)



class English_emkanat_window(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()


        #   siza & title
        self.setWindowTitle('emkanat window')
        self.resize(600,600)


        # lables & buttons
        change_password = QPushButton(self)
        change_password.setText("change password")
        change_password.setGeometry(0,250,1000,1000)
        change_password.clicked.connect(lambda: switch_page_callback(6))
        bardasht_vagh = QPushButton(self)
        bardasht_vagh.setText("get cache")
        bardasht_vagh.setGeometry(0, 250, 1000, 1000)
        bardasht_vagh.clicked.connect(lambda: switch_page_callback(11))
        mandeh_cart = QPushButton(self)
        mandeh_cart.setText("account balance")
        mandeh_cart.setGeometry(0, 250, 1000, 1000)
        mandeh_cart.clicked.connect(lambda: switch_page_callback(10))
        cart_be_cart = QPushButton(self)
        cart_be_cart.setText("money transfer")
        cart_be_cart.setGeometry(0, 250, 1000, 1000)
        cart_be_cart.clicked.connect(lambda: switch_page_callback(8))


        # layouts
        layout1 = QVBoxLayout()
        layout1.addWidget(change_password)
        layout1.addSpacing(20)
        layout1.addWidget(bardasht_vagh)
        layout2 = QVBoxLayout()
        layout2.addWidget(mandeh_cart)
        layout2.addSpacing(20)
        layout2.addWidget(cart_be_cart)
        layout3 = QHBoxLayout()
        layout3.addLayout(layout1)
        layout3.addStretch()
        layout3.addLayout(layout2)
        self.setLayout(layout3)


class Persian_editPassword_window(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()

        # title & size
        self.setWindowTitle('صفحه تفییر رمز')
        self.resize(600,600)

        # label & lineedit
        information1 = QLabel('لطفا رمز جدید را وارد کنید: ',self)
        input_password = QLineEdit(self)
        input_password.setGeometry(300,200,50,50)
        ok_button = QPushButton('تایید',self)
        ok_button.setGeometry(500,500,20,50)
        ok_button.clicked.connect(lambda: switch_page_callback(12))

        # layout
        layout1 = QVBoxLayout()
        layout1.addStretch()
        layout1.addWidget(information1)
        layout1.addWidget(input_password)
        layout1.addStretch()
        layout1.addWidget(ok_button)

        self.setLayout(layout1)

class English_editPassword_window(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()

        # title & size
        self.setWindowTitle('edit Password window')
        self.resize(600,600)

        # label & lineedit
        information1 = QLabel('Enter new password!',self)
        input_password = QLineEdit(self)
        input_password.setGeometry(300,200,50,50)
        ok_button = QPushButton('confirm',self)
        ok_button.setGeometry(500,500,20,50)
        ok_button.clicked.connect(lambda: switch_page_callback(13))
        # layout
        layout1 = QVBoxLayout()
        layout1.addStretch()
        layout1.addWidget(information1)
        layout1.addWidget(input_password)
        layout1.addStretch()
        layout1.addWidget(ok_button)

        self.setLayout(layout1)


class English_Money_transfer_window(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()

        # title & size
        self.setWindowTitle('Money transfer window')
        self.resize(600,600)

        # label & lineedit
        information1 = QLabel('Enter The Desired Amount: ',self)
        input_Amount = QLineEdit(self)
        input_Amount.setGeometry(300,200,50,50)
        information2 = QLabel('Enter The Desired Card Number: ', self)
        input_Card = QLineEdit(self)
        input_Card.setGeometry(300, 200, 50, 50)
        ok_button = QPushButton('confirm',self)
        ok_button.setGeometry(500,500,20,50)
        ok_button.clicked.connect(lambda: switch_page_callback(13))

        # layout
        layout1 = QVBoxLayout()
        layout1.addStretch()
        layout1.addWidget(information1)
        layout1.addWidget(input_Amount)
        layout1.addWidget(information2)
        layout1.addWidget(input_Card)
        layout1.addStretch()
        layout1.addWidget(ok_button)

        self.setLayout(layout1)


class Persian_Money_transfer_window(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()

        # title & size
        self.setWindowTitle('صفحه انتقال وجه')
        self.resize(600,600)

        # label & lineedit
        information1 = QLabel('مبلغ مورد نظر را وارد کنید: ',self)
        input_Amount = QLineEdit(self)
        input_Amount.setGeometry(300,200,50,50)
        information2 = QLabel('شماره کارت مقصد را وارد کنید: ', self)
        input_Card = QLineEdit(self)
        input_Card.setGeometry(300, 200, 50, 50)
        ok_button = QPushButton('ثبت',self)
        ok_button.setGeometry(500,500,20,50)
        ok_button.clicked.connect(lambda: switch_page_callback(12))
        # layout
        layout1 = QVBoxLayout()
        layout1.addStretch()
        layout1.addWidget(information1)
        layout1.addWidget(input_Amount)
        layout1.addWidget(information2)
        layout1.addWidget(input_Card)
        layout1.addStretch()
        layout1.addWidget(ok_button)

        self.setLayout(layout1)


class Persian_Account_Balalnce(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()

        # title & size
        self.setWindowTitle('صفحه اعلام مانده')
        self.resize(600, 600)

        information1 = QLabel('موجودی شما: 535500000',self)
        button1 = QPushButton("تایید",self)
        button1.clicked.connect(lambda: switch_page_callback(12))

        layout1 = QVBoxLayout()
        layout1.addWidget(information1)
        layout1.addWidget(button1)

        self.setLayout(layout1)


class English_Account_Balalnce(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()

        # title & size
        self.setWindowTitle('Account Balalnce window')
        self.resize(600, 600)

        information1 = QLabel('Your Account Balalnce is: 535500000',self)
        button1 = QPushButton("confirm",self)
        button1.clicked.connect(lambda: switch_page_callback(13))

        layout1 = QVBoxLayout()
        layout1.addWidget(information1)
        layout1.addWidget(button1)

        self.setLayout(layout1)


class Persian_Get_Cash_window(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()


        #   siza & title
        self.setWindowTitle('صفحه برداشت پول')
        self.resize(600,600)


        # lables & buttons
        change_password = QPushButton(self)
        change_password.setText("1/500/000")
        change_password.setGeometry(0,250,1000,1000)
        change_password.clicked.connect(lambda: switch_page_callback(12))
        bardasht_vagh = QPushButton(self)
        bardasht_vagh.setText("500/000")
        bardasht_vagh.setGeometry(0, 250, 1000, 1000)
        bardasht_vagh.clicked.connect(lambda: switch_page_callback(12))
        mandeh_cart = QPushButton(self)
        mandeh_cart.setText("2/000/000")
        mandeh_cart.setGeometry(0, 250, 1000, 1000)
        mandeh_cart.clicked.connect(lambda: switch_page_callback(12))
        cart_be_cart = QPushButton(self)
        cart_be_cart.setText("1/000/000")
        cart_be_cart.setGeometry(0, 250, 1000, 1000)
        cart_be_cart.clicked.connect(lambda: switch_page_callback(12))


        # layouts
        layout1 = QVBoxLayout()
        layout1.addWidget(change_password)
        layout1.addSpacing(20)
        layout1.addWidget(bardasht_vagh)
        layout2 = QVBoxLayout()
        layout2.addWidget(mandeh_cart)
        layout2.addSpacing(20)
        layout2.addWidget(cart_be_cart)
        layout3 = QHBoxLayout()
        layout3.addLayout(layout1)
        layout3.addStretch()
        layout3.addLayout(layout2)
        self.setLayout(layout3)

class Persian_payan(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()


        #   siza & title
        self.setWindowTitle("صفحه پایانی")
        self.resize(600,600)


        # lables & buttons
        new_work = QPushButton(self)
        new_work.setText("عملیات جدید")
        new_work.setGeometry(0,250,1000,1000)
        # click
        new_work.clicked.connect(lambda: switch_page_callback(3))


        information1 = QLabel(self)
        information1.setText('عملیات با موفقیت انجام شد')
        end = QPushButton(self)
        end.setText("خدانگهدار")
        end.setGeometry(500,250,1000,1000)
        # click
        end.clicked.connect(QApplication.quit)


        # layouts
        layout2 = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout1.addWidget(new_work)
        layout1.addStretch()
        layout1.addWidget(end)
        layout2.addStretch()
        layout2.addWidget(information1)
        layout2.addLayout(layout1)
        layout2.addStretch()
        self.setLayout(layout2)


class English_payan(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()


        #   siza & title
        self.setWindowTitle("end window")
        self.resize(600,600)


        # lables & buttons
        new_work = QPushButton(self)
        new_work.setText("new mision")
        new_work.setGeometry(0,250,1000,1000)
        # click
        new_work.clicked.connect(lambda: switch_page_callback(4))


        information1 = QLabel(self)
        information1.setText('Mission Accomplished Successfully!')
        end = QPushButton(self)
        end.setText("Good Bye")
        end.setGeometry(500,250,1000,1000)
        # click
        end.clicked.connect(QApplication.quit)


        # layouts
        layout2 = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout1.addWidget(new_work)
        layout1.addStretch()
        layout1.addWidget(end)
        layout2.addStretch()
        layout2.addWidget(information1)
        layout2.addLayout(layout1)
        layout2.addStretch()
        self.setLayout(layout2)









app = QApplication()
# test
mainwindow = Mainwindow()
mainwindow.show()
app.exec()