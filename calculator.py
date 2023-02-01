from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import math

def c():
    main_window.monitor.setText("")

# def presse_it(pressed):
#     main_window.monitor.setText(main_window.monitor.text() + pressed)

#Numbers: 

def dot():
    main_window.monitor.setText(main_window.monitor.text() + '.')

def zero():
    main_window.monitor.setText(main_window.monitor.text() + '0')

def one():
    main_window.monitor.setText(main_window.monitor.text()+'1')

def two():
    main_window.monitor.setText(main_window.monitor.text() + '2')

def three():
    main_window.monitor.setText(main_window.monitor.text() + '3')

def four():
    main_window.monitor.setText(main_window.monitor.text() + '4')

def five():
    main_window.monitor.setText(main_window.monitor.text() + '5')

def six():
    main_window.monitor.setText(main_window.monitor.text() + '6')

def seven():
    main_window.monitor.setText(main_window.monitor.text() + '7')

def eight():
    main_window.monitor.setText(main_window.monitor.text() + '8')

def nine():
    main_window.monitor.setText(main_window.monitor.text() + '9')

def clear():
    main_window.monitor.setText("")


#Functions:
def add():
    global a
    global o
    o = '+'
    a = int(main_window.monitor.text())
    main_window.monitor.setText('')


def sub():
    global a
    global o
    o = '-'
    a = int(main_window.monitor.text())
    main_window.monitor.setText('')

def mul():
    global a
    global o
    o = '*'
    a = int(main_window.monitor.text())
    main_window.monitor.setText('')

def frac():
    global a
    global o
    o = '/'
    a = int(main_window.monitor.text())
    main_window.monitor.setText('')

def sin():
    global o
    o = 'sin'

def cos():
    global o
    o = 'cos'

def tan():
    global o
    o = 'tan'

def arctan():
    global o
    o = 'arctan'

def fact():
    global o
    o = 'fact'

def ln():
    global o
    o = 'ln'

def sqrt():
    global o
    o = 'sqrt'

def square():
    global o
    o = '^'

def log():
    global o
    o = 'log'

def eq():
    b = int(main_window.monitor.text())

    if o == '+':
        c = a + b
        main_window.monitor.setText(str(c))

    elif  o == '-':
        c = a - b
        main_window.monitor.setText(str(c))

    elif  o == '+':
        c = a * b
        main_window.monitor.setText(str(c))

    elif  o == '/':
        if b != 0:
            c = a / b
            main_window.monitor.setText(str(c))
        else:
            main_window.monitor.setText('You can\'t divide any number by ZERO')

    elif o == 'sin':
        c = math.sin(math.radians(b))
        main_window.monitor.setText(str(c))

    elif o == 'cos':
        c = math.cos(math.radians(b))
        main_window.monitor.setText(str(c))

    elif o == 'tan':
        c = math.tan(math.radians(b))
        main_window.monitor.setText(str(c))

    elif o == 'arctan':
        c = 1/math.tan(math.radians(b))
        main_window.monitor.setText(str(c))

    elif o == 'sqrt':
        c = math.sqrt(b)
        main_window.monitor.setText(str(c))

    elif o == 'fact':
        c = math.factorial(b)
        main_window.monitor.setText(str(c))

    elif o == 'log':
        c = math.log10(b)
        main_window.monitor.setText(str(c))

    elif o == 'ln':
        c = math.log(b)
        main_window.monitor.setText(str(c))

    elif o == '^':
        c = math.pow(b,2)
        main_window.monitor.setText(str(c))

    elif o == 'sqrt':
        c = math.sqrt(b)
        main_window.monitor.setText(str(c))


app = QApplication([])
loader = QUiLoader()
main_window = loader.load("mainwindow.ui")
main_window.show()

#Numbers and C

main_window.dotbtn.clicked.connect(dot)
main_window.zerobtn.clicked.connect(zero)
main_window.onebtn.clicked.connect(one)
main_window.twobtn.clicked.connect(two)
main_window.threebtn.clicked.connect(three)
main_window.fourbtn.clicked.connect(four)
main_window.fivebtn.clicked.connect(five)
main_window.sixbtn.clicked.connect(six)
main_window.sevenbtn.clicked.connect(seven)
main_window.eightbtn.clicked.connect(eight)
main_window.ninebtn.clicked.connect(nine)
main_window.clearbtn.clicked.connect(clear)

#Functions

main_window.addbtn.clicked.connect(add)
main_window.subbtn.clicked.connect(sub)
main_window.mulbtn.clicked.connect(mul)
main_window.fracbtn.clicked.connect(frac)
main_window.sinbtn.clicked.connect(sin)
main_window.cosbtn.clicked.connect(cos)
main_window.tanbtn.clicked.connect(tan)
main_window.arctanbtn.clicked.connect(arctan)
main_window.radicalbtn.clicked.connect(sqrt)
main_window.logbtn.clicked.connect(log)
main_window.lnbtn.clicked.connect(ln)
main_window.factorialbtn.clicked.connect(fact)
main_window.powbtn.clicked.connect(pow)
main_window.eqbtn.clicked.connect(eq)

app.exec()
