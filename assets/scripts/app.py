import sys
import math
import pywinstyles
import assets.scripts.variables as vary

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        vary.main_window = self
        self.setGeometry(vary.x, vary.y, vary.width, vary.height)
        self.setWindowTitle('Dimension Calculator')
        self.setWindowIcon(QIcon('assets/images/icon.ico'))
        self.setMinimumSize(949, 554)

        self.settingTwoDimWidgets()

    def settingTwoDimWidgets(self):
        self.twoDimList = QListWidget()
        self.twoDimList.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.twoDimList.addItems(['Square', 'Rectangle', 'Circle', 'Triangle'])
        self.twoDimList.setCurrentRow(0)
        self.twoDimList.currentRowChanged.connect(
            lambda: self.twoDimStack.setCurrentIndex(self.twoDimList.currentRow())
        )

        # Square
        self.square_img = QPixmap('assets/images/square.png')

        self.topic_one = QLabel('Square')
        self.topic_one.setObjectName('topic')

        self.lbl_one = QLabel('Area: a<sup>2</sup>')
        self.lbl_one.setObjectName('topic_1')

        self.lbl_two = QLabel('Enter side length(a): ')
        self.entry_one = QLineEdit()
        self.entry_one.setValidator(QIntValidator(1, 99999, self))
        self.entry_one.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_one.setPlaceholderText('0 cm')

        self.lbl_three = QLabel('Area: 0 cm<sup>2</sup>')

        self.btn_1 = QPushButton('Calculate Area')
        self.btn_1.clicked.connect(lambda: self.calcSquarePeriArea(self.entry_one.text(), 0))

        self.lbl_four = QLabel('Perimeter: 4a')
        self.lbl_four.setObjectName('topic_1')

        self.lbl_five = QLabel('Enter side length(a): ')
        self.entry_two = QLineEdit()
        self.entry_two.setValidator(QIntValidator(1, 99999, self))
        self.entry_two.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_two.setPlaceholderText('0 cm')

        self.btn_2 = QPushButton('Calculate Perimeter')
        self.btn_2.clicked.connect(lambda: self.calcSquarePeriArea(self.entry_two.text(), 1))

        self.lbl_six = QLabel('Perimeter: 0 cm')

        self.btn_clear_1 = QPushButton('Clear')
        self.btn_clear_1.clicked.connect(self.clearBtnAction)

        self.square_lbl = QLabel()
        self.square_lbl.setPixmap(self.square_img)

        self.squareLay = QGridLayout()
        self.squareLay.addWidget(self.topic_one, 0, 0, 1, 2)
        self.squareLay.addWidget(self.square_lbl, 0, 2, 7, 1)
        self.squareLay.addWidget(self.lbl_one, 1, 0, 1, 2)
        self.squareLay.addWidget(self.lbl_two, 2, 0)
        self.squareLay.addWidget(self.entry_one, 2, 1)
        self.squareLay.addWidget(self.lbl_three, 3, 0, 1, 2)
        self.squareLay.addWidget(self.btn_1, 4, 0, 1, 2)
        self.squareLay.addWidget(self.lbl_four, 5, 0, 1, 2)
        self.squareLay.addWidget(self.lbl_five, 6, 0)
        self.squareLay.addWidget(self.entry_two, 6, 1)
        self.squareLay.addWidget(self.lbl_six, 7, 0, 1, 2)
        self.squareLay.addWidget(self.btn_2, 8, 0, 1, 2)
        self.squareLay.addWidget(self.btn_clear_1, 8, 2)

        self.squareWdj = QWidget()
        self.squareWdj.setLayout(self.squareLay)

        # Rectangle
        self.rectangle_img = QPixmap('assets/images/rectangle.png')

        self.topic_two = QLabel('Rectangle')
        self.topic_two.setObjectName('topic')

        self.lbl_seven = QLabel('Area: wl')
        self.lbl_seven.setObjectName('topic_1')

        self.lbl_eight = QLabel('Enter the length(l): ')
        self.entry_three = QLineEdit()
        self.entry_three.setValidator(QIntValidator(1, 99999, self))
        self.entry_three.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_three.setPlaceholderText('0 cm')

        self.lbl_nine = QLabel('Enter the width(w): ')
        self.entry_four = QLineEdit()
        self.entry_four.setValidator(QIntValidator(1, 99999, self))
        self.entry_four.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_four.setPlaceholderText('0 cm')

        self.btn_3 = QPushButton('Calculate Area')
        self.btn_3.clicked.connect(lambda: self.calcRectanglePeriArea(0))

        self.lbl_ten = QLabel('Area: 0 cm<sup>2</sup>')

        self.lbl_11 = QLabel('Perimeter: 2(w + l)')
        self.lbl_11.setObjectName('topic_1')

        self.lbl_12 = QLabel('Enter the length(l): ')
        self.entry_five = QLineEdit()
        self.entry_five.setValidator(QIntValidator(1, 99999, self))
        self.entry_five.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_five.setPlaceholderText('0 cm')

        self.lbl_13 = QLabel('Enter the width(w): ')
        self.entry_six = QLineEdit()
        self.entry_six.setValidator(QIntValidator(1, 99999, self))
        self.entry_six.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_six.setPlaceholderText('0 cm')

        self.btn_4 = QPushButton('Calculate Perimeter')
        self.btn_4.clicked.connect(lambda: self.calcRectanglePeriArea(1))

        self.lbl_14 = QLabel('Perimeter: 0 cm')

        self.btn_clear_2 = QPushButton('Clear')
        self.btn_clear_2.clicked.connect(self.clearBtnAction)

        self.rectangle_lbl = QLabel()
        self.rectangle_lbl.setPixmap(self.rectangle_img)

        self.rectangleLay = QGridLayout()
        self.rectangleLay.addWidget(self.topic_two, 0, 0, 1, 2)
        self.rectangleLay.addWidget(self.rectangle_lbl, 0, 2, 10, 1)
        self.rectangleLay.addWidget(self.lbl_seven, 1, 0, 1, 2)
        self.rectangleLay.addWidget(self.lbl_eight, 2, 0)
        self.rectangleLay.addWidget(self.entry_three, 2, 1)
        self.rectangleLay.addWidget(self.lbl_nine, 3, 0)
        self.rectangleLay.addWidget(self.entry_four, 3, 1)
        self.rectangleLay.addWidget(self.lbl_ten, 4, 0, 1, 2)
        self.rectangleLay.addWidget(self.btn_3, 5, 0, 1, 2)
        self.rectangleLay.addWidget(self.lbl_11, 6, 0, 1, 2)
        self.rectangleLay.addWidget(self.lbl_12, 7, 0)
        self.rectangleLay.addWidget(self.entry_five, 7, 1)
        self.rectangleLay.addWidget(self.lbl_13, 8, 0)
        self.rectangleLay.addWidget(self.entry_six, 8, 1)
        self.rectangleLay.addWidget(self.lbl_14, 9, 0, 1, 2)
        self.rectangleLay.addWidget(self.btn_4, 10, 0, 1, 2)
        self.rectangleLay.addWidget(self.btn_clear_2, 10, 2)

        self.rectangleWdj = QWidget()
        self.rectangleWdj.setLayout(self.rectangleLay)

        # Circle
        self.circle_img = QPixmap('assets/images/circle.png')

        self.topic_three = QLabel('Circle')
        self.topic_three.setObjectName('topic')

        self.lbl_15 = QLabel('Area: \u03c0r<sup>2</sup>')
        self.lbl_15.setObjectName('topic_1')

        self.lbl_16 = QLabel('Enter the radius(r): ')
        self.entry_seven = QLineEdit()
        self.entry_seven.setValidator(QIntValidator(1, 99999, self))
        self.entry_seven.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_seven.setPlaceholderText('0 cm')

        self.lbl_17 = QLabel('Area: 0 cm<sup>2</sup>')

        self.btn_5 = QPushButton('Calculate Area')
        self.btn_5.clicked.connect(lambda: self.calcCirclePeriArea(self.entry_seven.text(), 0))

        self.lbl_18 = QLabel('Perimeter: 2\u03c0r')
        self.lbl_18.setObjectName('topic_1')

        self.lbl_19 = QLabel('Enter the radius(r): ')
        self.entry_eight = QLineEdit()
        self.entry_eight.setValidator(QIntValidator(1, 99999, self))
        self.entry_eight.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_eight.setPlaceholderText('0 cm')

        self.btn_6 = QPushButton('Calculate Perimeter')
        self.btn_6.clicked.connect(lambda: self.calcCirclePeriArea(self.entry_eight.text(), 1))

        self.lbl_20 = QLabel('Perimeter: 0 cm')

        self.btn_clear_3 = QPushButton('Clear')
        self.btn_clear_3.clicked.connect(self.clearBtnAction)

        self.circle_lbl = QLabel()
        self.circle_lbl.setPixmap(self.circle_img)

        self.circleLay = QGridLayout()
        self.circleLay.addWidget(self.topic_three, 0, 0, 1, 2)
        self.circleLay.addWidget(self.circle_lbl, 0, 2, 7, 1)
        self.circleLay.addWidget(self.lbl_15, 1, 0, 1, 2)
        self.circleLay.addWidget(self.lbl_16, 2, 0)
        self.circleLay.addWidget(self.entry_seven, 2, 1)
        self.circleLay.addWidget(self.lbl_17, 3, 0, 1, 2)
        self.circleLay.addWidget(self.btn_5, 4, 0, 1, 2)
        self.circleLay.addWidget(self.lbl_18, 5, 0, 1, 2)
        self.circleLay.addWidget(self.lbl_19, 6, 0)
        self.circleLay.addWidget(self.entry_eight, 6, 1)
        self.circleLay.addWidget(self.lbl_20, 7, 0, 1, 2)
        self.circleLay.addWidget(self.btn_6, 8, 0, 1, 2)
        self.circleLay.addWidget(self.btn_clear_3, 8, 2)

        self.circleWdj = QWidget()
        self.circleWdj.setLayout(self.circleLay)

        # Triangle
        self.triangle_img = QPixmap('assets/images/triangle.png')

        self.topic_four = QLabel('Triangle')
        self.topic_four.setObjectName('topic')

        self.lbl_21 = QLabel('Area: <sup>1</sup>/<sub>2</sub>bh')
        self.lbl_21.setObjectName('topic_1')

        self.lbl_22 = QLabel('Enter the base length(b): ')
        self.entry_nine = QLineEdit()
        self.entry_nine.setValidator(QIntValidator(1, 99999, self))
        self.entry_nine.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_nine.setPlaceholderText('0 cm')

        self.lbl_23 = QLabel('Enter the height(h): ')
        self.entry_ten = QLineEdit()
        self.entry_ten.setValidator(QIntValidator(1, 99999, self))
        self.entry_ten.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_ten.setPlaceholderText('0 cm')

        self.btn_7 = QPushButton('Calculate Area')
        self.btn_7.clicked.connect(lambda: self.calcTrianglePeriArea(0))

        self.lbl_24 = QLabel('Area: 0 cm<sup>2</sup>')

        self.lbl_25 = QLabel('Perimeter: a + b + c')
        self.lbl_25.setObjectName('topic_1')

        self.lbl_26 = QLabel('Enter the length(a): ')
        self.entry_11 = QLineEdit()
        self.entry_11.setValidator(QIntValidator(1, 99999, self))
        self.entry_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_11.setPlaceholderText('0 cm')

        self.lbl_27 = QLabel('Enter the length(b): ')
        self.entry_12 = QLineEdit()
        self.entry_12.setValidator(QIntValidator(1, 99999, self))
        self.entry_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_12.setPlaceholderText('0 cm')

        self.lbl_28 = QLabel('Enter the length(c): ')
        self.entry_13 = QLineEdit()
        self.entry_13.setValidator(QIntValidator(1, 99999, self))
        self.entry_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_13.setPlaceholderText('0 cm')

        self.btn_8 = QPushButton('Calculate Perimeter')
        self.btn_8.clicked.connect(lambda: self.calcTrianglePeriArea(1))

        self.lbl_29 = QLabel('Perimeter: 0 cm')

        self.btn_clear_4 = QPushButton('Clear')
        self.btn_clear_4.clicked.connect(self.clearBtnAction)

        self.triangle_lbl = QLabel()
        self.triangle_lbl.setPixmap(self.triangle_img)

        self.triangleLay = QGridLayout()
        self.triangleLay.addWidget(self.topic_four, 0, 0, 1, 2)
        self.triangleLay.addWidget(self.triangle_lbl, 0, 2, 10, 1)
        self.triangleLay.addWidget(self.lbl_21, 1, 0, 1, 2)
        self.triangleLay.addWidget(self.lbl_22, 2, 0)
        self.triangleLay.addWidget(self.entry_nine, 2, 1)
        self.triangleLay.addWidget(self.lbl_23, 3, 0)
        self.triangleLay.addWidget(self.entry_ten, 3, 1)
        self.triangleLay.addWidget(self.lbl_24, 4, 0, 1, 2)
        self.triangleLay.addWidget(self.btn_7, 5, 0, 1, 2)
        self.triangleLay.addWidget(self.lbl_25, 6, 0, 1, 2)
        self.triangleLay.addWidget(self.lbl_26, 7, 0)
        self.triangleLay.addWidget(self.entry_11, 7, 1)
        self.triangleLay.addWidget(self.lbl_27, 8, 0)
        self.triangleLay.addWidget(self.entry_12, 8, 1)
        self.triangleLay.addWidget(self.lbl_28, 9, 0)
        self.triangleLay.addWidget(self.entry_13, 9, 1)
        self.triangleLay.addWidget(self.lbl_29, 10, 0, 1, 2)
        self.triangleLay.addWidget(self.btn_8, 11, 0, 1, 2)
        self.triangleLay.addWidget(self.btn_clear_4, 11, 2)

        self.triangleWdj = QWidget()
        self.triangleWdj.setLayout(self.triangleLay)

        self.twoDimWdj = QWidget()

        self.twoDimStack = QStackedLayout(self.twoDimWdj)
        self.twoDimStack.addWidget(self.squareWdj)
        self.twoDimStack.addWidget(self.rectangleWdj)
        self.twoDimStack.addWidget(self.circleWdj)
        self.twoDimStack.addWidget(self.triangleWdj)
        self.twoDimStack.setCurrentIndex(0)

        self.twoDimWdj.setLayout(self.twoDimStack)

        self.twoDimLayout = QHBoxLayout()
        self.twoDimLayout.addWidget(self.twoDimList)
        self.twoDimLayout.addWidget(self.twoDimWdj)

        self.twoDimWidget = QWidget()
        self.twoDimWidget.setLayout(self.twoDimLayout)

        self.settingThreeDimSettings()

    def settingThreeDimSettings(self):
        self.threeDimList = QListWidget()
        self.threeDimList.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.threeDimList.addItems(['Cube', 'Cuboid', 'Sphere', 'Cone', 'Pyramid'])
        self.threeDimList.setCurrentRow(0)
        self.threeDimList.currentRowChanged.connect(
            lambda: self.threeDimStack.setCurrentIndex(self.threeDimList.currentRow())
        )

        # Cube
        self.cube_img = QPixmap('assets/images/cube.png')

        self.topic_five = QLabel('Cube')
        self.topic_five.setObjectName('topic')

        self.lbl_30 = QLabel('Area: 6a<sup>2</sup>')
        self.lbl_30.setObjectName('topic_1')

        self.lbl_31 = QLabel('Enter side length(a): ')
        self.entry_14 = QLineEdit()
        self.entry_14.setValidator(QIntValidator(1, 99999, self))
        self.entry_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_14.setPlaceholderText('0 cm')

        self.lbl_32 = QLabel('Area: 0 cm<sup>2</sup>')

        self.btn_9 = QPushButton('Calculate Area')
        self.btn_9.clicked.connect(lambda: self.calcCubeVolArea(self.entry_14.text(), 0))

        self.lbl_33 = QLabel('Volume: a<sup>3</sup> ')
        self.lbl_33.setObjectName('topic_1')

        self.lbl_34 = QLabel('Enter side length(a): ')
        self.entry_15 = QLineEdit()
        self.entry_15.setValidator(QIntValidator(1, 99999, self))
        self.entry_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_15.setPlaceholderText('0 cm')

        self.btn_10 = QPushButton('Calculate Volume')
        self.btn_10.clicked.connect(lambda: self.calcCubeVolArea(self.entry_15.text(), 1))

        self.lbl_35 = QLabel('Volume: 0 cm<sup>3</sup>')

        self.btn_clear_5 = QPushButton('Clear')
        self.btn_clear_5.clicked.connect(self.clearBtnAction)

        self.cube_lbl = QLabel()
        self.cube_lbl.setPixmap(self.cube_img)

        self.cubeLay = QGridLayout()
        self.cubeLay.addWidget(self.topic_five, 0, 0, 1, 2)
        self.cubeLay.addWidget(self.cube_lbl, 0, 2, 7, 1)
        self.cubeLay.addWidget(self.lbl_30, 1, 0, 1, 2)
        self.cubeLay.addWidget(self.lbl_31, 2, 0)
        self.cubeLay.addWidget(self.entry_14, 2, 1)
        self.cubeLay.addWidget(self.lbl_32, 3, 0, 1, 2)
        self.cubeLay.addWidget(self.btn_9, 4, 0, 1, 2)
        self.cubeLay.addWidget(self.lbl_33, 5, 0, 1, 2)
        self.cubeLay.addWidget(self.lbl_34, 6, 0)
        self.cubeLay.addWidget(self.entry_15, 6, 1)
        self.cubeLay.addWidget(self.lbl_35, 7, 0, 1, 2)
        self.cubeLay.addWidget(self.btn_10, 8, 0, 1, 2)
        self.cubeLay.addWidget(self.btn_clear_5, 8, 2)

        self.cubeWdj = QWidget()
        self.cubeWdj.setLayout(self.cubeLay)

        # Cuboid
        self.cuboid_img = QPixmap('assets/images/cuboid.png')

        self.topic_six = QLabel('Cuboid')
        self.topic_six.setObjectName('topic')

        self.lbl_36 = QLabel('Area: 2(lb + bh + lh)')
        self.lbl_36.setObjectName('topic_1')

        self.lbl_37 = QLabel('Enter the length(l): ')
        self.entry_16 = QLineEdit()
        self.entry_16.setValidator(QIntValidator(1, 99999, self))
        self.entry_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_16.setPlaceholderText('0 cm')

        self.lbl_38 = QLabel('Enter the breadth(b): ')
        self.entry_17 = QLineEdit()
        self.entry_17.setValidator(QIntValidator(1, 99999, self))
        self.entry_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_17.setPlaceholderText('0 cm')

        self.lbl_39 = QLabel('Enter the height(h): ')
        self.entry_18 = QLineEdit()
        self.entry_18.setValidator(QIntValidator(1, 99999, self))
        self.entry_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_18.setPlaceholderText('0 cm')

        self.lbl_40 = QLabel('Area: 0 cm<sup>2</sup>')

        self.btn_11 = QPushButton('Calculate Area')
        self.btn_11.clicked.connect(lambda: self.calcCuboidValArea(0))

        self.lbl_41 = QLabel('Volume: lbh')
        self.lbl_41.setObjectName('topic_1')

        self.lbl_42 = QLabel('Enter the length(l): ')
        self.entry_19 = QLineEdit()
        self.entry_19.setValidator(QIntValidator(1, 99999, self))
        self.entry_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_19.setPlaceholderText('0 cm')

        self.lbl_43 = QLabel('Enter the breadth(b): ')
        self.entry_20 = QLineEdit()
        self.entry_20.setValidator(QIntValidator(1, 99999, self))
        self.entry_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_20.setPlaceholderText('0 cm')

        self.lbl_44 = QLabel('Enter the height(h): ')
        self.entry_21 = QLineEdit()
        self.entry_21.setValidator(QIntValidator(1, 99999, self))
        self.entry_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_21.setPlaceholderText('0 cm')

        self.btn_12 = QPushButton('Calculate Volume')
        self.btn_12.clicked.connect(lambda: self.calcCuboidValArea(1))

        self.lbl_45 = QLabel('Volume: 0 cm<sup>3</sup>')

        self.btn_clear_6 = QPushButton('Clear')
        self.btn_clear_6.clicked.connect(self.clearBtnAction)

        self.cuboid_lbl = QLabel()
        self.cuboid_lbl.setPixmap(self.cuboid_img)

        self.cuboidLay = QGridLayout()
        self.cuboidLay.addWidget(self.topic_six, 0, 0, 1, 2)
        self.cuboidLay.addWidget(self.cuboid_lbl, 0, 2, 11, 1)
        self.cuboidLay.addWidget(self.lbl_36, 1, 0, 1, 2)
        self.cuboidLay.addWidget(self.lbl_37, 2, 0)
        self.cuboidLay.addWidget(self.entry_16, 2, 1)
        self.cuboidLay.addWidget(self.lbl_38, 3, 0)
        self.cuboidLay.addWidget(self.entry_17, 3, 1)
        self.cuboidLay.addWidget(self.lbl_39, 4, 0)
        self.cuboidLay.addWidget(self.entry_18, 4, 1)
        self.cuboidLay.addWidget(self.lbl_40, 5, 0, 1, 2)
        self.cuboidLay.addWidget(self.btn_11, 6, 0, 1, 2)
        self.cuboidLay.addWidget(self.lbl_41, 7, 0, 1, 2)
        self.cuboidLay.addWidget(self.lbl_42, 8, 0)
        self.cuboidLay.addWidget(self.entry_19, 8, 1)
        self.cuboidLay.addWidget(self.lbl_43, 9, 0)
        self.cuboidLay.addWidget(self.entry_20, 9, 1)
        self.cuboidLay.addWidget(self.lbl_44, 10, 0)
        self.cuboidLay.addWidget(self.entry_21, 10, 1)
        self.cuboidLay.addWidget(self.lbl_45, 11, 0, 1, 2)
        self.cuboidLay.addWidget(self.btn_12, 12, 0, 1, 2)
        self.cuboidLay.addWidget(self.btn_clear_6, 12, 2)

        self.cuboidWdj = QWidget()
        self.cuboidWdj.setLayout(self.cuboidLay)

        # Sphere
        self.sphere_img = QPixmap('assets/images/sphere.png')

        self.topic_seven = QLabel('Sphere')
        self.topic_seven.setObjectName('topic')

        self.lbl_46 = QLabel('Area: 4\u03c0r<sup>2</sup>')
        self.lbl_46.setObjectName('topic_1')

        self.lbl_47 = QLabel('Enter the radius(r): ')
        self.entry_22 = QLineEdit()
        self.entry_22.setValidator(QIntValidator(1, 99999, self))
        self.entry_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_22.setPlaceholderText('0 cm')

        self.lbl_48 = QLabel('Area: 0 cm<sup>2</sup>')

        self.btn_13 = QPushButton('Calculate Area')
        self.btn_13.clicked.connect(lambda: self.calcSphereVolArea(self.entry_22.text(), 0))

        self.lbl_49 = QLabel('Volume: <sup>4</sup>/<sub>3</sub>\u03c0r<sup>3</sup>')
        self.lbl_49.setObjectName('topic_1')

        self.lbl_50 = QLabel('Enter the radius(r): ')
        self.entry_23 = QLineEdit()
        self.entry_23.setValidator(QIntValidator(1, 99999, self))
        self.entry_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_23.setPlaceholderText('0 cm')

        self.btn_14 = QPushButton('Calculate Volume')
        self.btn_14.clicked.connect(lambda: self.calcSphereVolArea(self.entry_23.text(), 1))

        self.lbl_51 = QLabel('Volume: 0 cm<sup>3</sup>')

        self.btn_clear_7 = QPushButton('Clear')
        self.btn_clear_7.clicked.connect(self.clearBtnAction)

        self.sphere_lbl = QLabel()
        self.sphere_lbl.setPixmap(self.sphere_img)

        self.sphereLay = QGridLayout()
        self.sphereLay.addWidget(self.topic_seven, 0, 0, 1, 2)
        self.sphereLay.addWidget(self.sphere_lbl, 0, 2, 8, 1)
        self.sphereLay.addWidget(self.lbl_46, 1, 0, 1, 2)
        self.sphereLay.addWidget(self.lbl_47, 2, 0)
        self.sphereLay.addWidget(self.entry_22, 2, 1)
        self.sphereLay.addWidget(self.lbl_48, 3, 0, 1, 2)
        self.sphereLay.addWidget(self.btn_13, 4, 0, 1, 2)
        self.sphereLay.addWidget(self.lbl_49, 5, 0, 1, 2)
        self.sphereLay.addWidget(self.lbl_50, 6, 0)
        self.sphereLay.addWidget(self.entry_23, 6, 1)
        self.sphereLay.addWidget(self.lbl_51, 7, 0, 1, 2)
        self.sphereLay.addWidget(self.btn_14, 8, 0, 1, 2)
        self.sphereLay.addWidget(self.btn_clear_7, 8, 2)

        self.sphereWdj = QWidget()
        self.sphereWdj.setLayout(self.sphereLay)

        # Cone
        self.cone_img = QPixmap('assets/images/cone.png')

        self.topic_eight = QLabel('Cone')
        self.topic_eight.setObjectName('topic')

        self.lbl_52 = QLabel('Area: \u03c0r<sup>2</sup> + \u03c0rl')
        self.lbl_52.setObjectName('topic_1')

        self.lbl_53 = QLabel('Enter the radius(r): ')
        self.entry_24 = QLineEdit()
        self.entry_24.setValidator(QIntValidator(1, 99999, self))
        self.entry_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_24.setPlaceholderText('0 cm')

        self.lbl_54 = QLabel('Enter the length(l): ')
        self.entry_25 = QLineEdit()
        self.entry_25.setValidator(QIntValidator(1, 99999, self))
        self.entry_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_25.setPlaceholderText('0 cm')

        self.lbl_55 = QLabel('Area: 0 cm<sup>2</sup>')

        self.btn_15 = QPushButton('Calculate Area')
        self.btn_15.clicked.connect(lambda: self.calcConeValArea(0))

        self.lbl_56 = QLabel('Volume: <sup>1</sup>/<sub>3</sub>\u03c0r<sup>2</sup>h')
        self.lbl_56.setObjectName('topic_1')

        self.lbl_57 = QLabel('Enter the radius(r): ')
        self.entry_26 = QLineEdit()
        self.entry_26.setValidator(QIntValidator(1, 99999, self))
        self.entry_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_26.setPlaceholderText('0 cm')

        self.lbl_58 = QLabel('Enter the height(h): ')
        self.entry_27 = QLineEdit()
        self.entry_27.setValidator(QIntValidator(1, 99999, self))
        self.entry_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_27.setPlaceholderText('0 cm')

        self.btn_16 = QPushButton('Calculate Volume')
        self.btn_16.clicked.connect(lambda: self.calcConeValArea(1))

        self.lbl_59 = QLabel('Volume: 0 cm<sup>3</sup>')

        self.btn_clear_8 = QPushButton('Clear')
        self.btn_clear_8.clicked.connect(self.clearBtnAction)

        self.cone_lbl = QLabel()
        self.cone_lbl.setPixmap(self.cone_img)

        self.coneLay = QGridLayout()
        self.coneLay.addWidget(self.topic_eight, 0, 0, 1, 2)
        self.coneLay.addWidget(self.cone_lbl, 0, 2, 10, 1)
        self.coneLay.addWidget(self.lbl_52, 1, 0, 1, 2)
        self.coneLay.addWidget(self.lbl_53, 2, 0)
        self.coneLay.addWidget(self.entry_24, 2, 1)
        self.coneLay.addWidget(self.lbl_54, 3, 0)
        self.coneLay.addWidget(self.entry_25, 3, 1)
        self.coneLay.addWidget(self.lbl_55, 4, 0, 1, 2)
        self.coneLay.addWidget(self.btn_15, 5, 0, 1, 2)
        self.coneLay.addWidget(self.lbl_56, 6, 0, 1, 2)
        self.coneLay.addWidget(self.lbl_57, 7, 0)
        self.coneLay.addWidget(self.entry_26, 7, 1)
        self.coneLay.addWidget(self.lbl_58, 8, 0)
        self.coneLay.addWidget(self.entry_27, 8, 1)
        self.coneLay.addWidget(self.lbl_59, 9, 0, 1, 2)
        self.coneLay.addWidget(self.btn_16, 10, 0, 1, 2)
        self.coneLay.addWidget(self.btn_clear_8, 10, 2)

        self.coneWdj = QWidget()
        self.coneWdj.setLayout(self.coneLay)

        # Pyramid
        self.pyramid_img = QPixmap('assets/images/pyramid.png')

        self.topic_nine = QLabel('Pyramid')
        self.topic_nine.setObjectName('topic')

        self.lbl_60 = QLabel('Area: lw + l\u221a((<sup>w</sup>/<sub>2</sub>)<sup>2</sup> + h<sup>2</sup>) + w\u221a((<sup>l</sup>/<sub>2</sub>)<sup>2</sup> + h<sup>2</sup>)')
        self.lbl_60.setObjectName('topic_1')

        self.lbl_61 = QLabel('Enter the length(l): ')
        self.entry_28 = QLineEdit()
        self.entry_28.setValidator(QIntValidator(1, 99999, self))
        self.entry_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_28.setPlaceholderText('0 cm')

        self.lbl_62 = QLabel('Enter the width(w): ')
        self.entry_29 = QLineEdit()
        self.entry_29.setValidator(QIntValidator(1, 99999, self))
        self.entry_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_29.setPlaceholderText('0 cm')

        self.lbl_63 = QLabel('Enter the height(h): ')
        self.entry_30 = QLineEdit()
        self.entry_30.setValidator(QIntValidator(1, 99999, self))
        self.entry_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_30.setPlaceholderText('0 cm')

        self.lbl_64 = QLabel('Area: 0 cm<sup>2</sup>')

        self.btn_16 = QPushButton('Calculate Area')
        self.btn_16.clicked.connect(lambda: self.calcPyramidValArea(0))

        self.lbl_65 = QLabel('Volume: <sup>1</sup>/<sub>3</sub>lwh')
        self.lbl_65.setObjectName('topic_1')

        self.lbl_66 = QLabel('Enter the length(l): ')
        self.entry_31 = QLineEdit()
        self.entry_31.setValidator(QIntValidator(1, 99999, self))
        self.entry_31.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_31.setPlaceholderText('0 cm')

        self.lbl_67 = QLabel('Enter the width(w): ')
        self.entry_32 = QLineEdit()
        self.entry_32.setValidator(QIntValidator(1, 99999, self))
        self.entry_32.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_32.setPlaceholderText('0 cm')

        self.lbl_68 = QLabel('Enter the height(h): ')
        self.entry_33 = QLineEdit()
        self.entry_33.setValidator(QIntValidator(1, 99999, self))
        self.entry_33.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_33.setPlaceholderText('0 cm')

        self.btn_17 = QPushButton('Calculate Volume')
        self.btn_17.clicked.connect(lambda: self.calcPyramidValArea(1))

        self.lbl_69 = QLabel('Volume: 0 cm<sup>3</sup>')

        self.btn_clear_9 = QPushButton('Clear')
        self.btn_clear_9.clicked.connect(self.clearBtnAction)

        self.pyramid_lbl = QLabel()
        self.pyramid_lbl.setPixmap(self.pyramid_img)

        self.pyramidLay = QGridLayout()
        self.pyramidLay.addWidget(self.topic_nine, 0, 0, 1, 2)
        self.pyramidLay.addWidget(self.pyramid_lbl, 0, 2, 11, 1)
        self.pyramidLay.addWidget(self.lbl_60, 1, 0, 1, 2)
        self.pyramidLay.addWidget(self.lbl_61, 2, 0)
        self.pyramidLay.addWidget(self.entry_28, 2, 1)
        self.pyramidLay.addWidget(self.lbl_62, 3, 0)
        self.pyramidLay.addWidget(self.entry_29, 3, 1)
        self.pyramidLay.addWidget(self.lbl_63, 4, 0)
        self.pyramidLay.addWidget(self.entry_30, 4, 1)
        self.pyramidLay.addWidget(self.lbl_64, 5, 0, 1, 2)
        self.pyramidLay.addWidget(self.btn_16, 6, 0, 1, 2)
        self.pyramidLay.addWidget(self.lbl_65, 7, 0, 1, 2)
        self.pyramidLay.addWidget(self.lbl_66, 8, 0)
        self.pyramidLay.addWidget(self.entry_31, 8, 1)
        self.pyramidLay.addWidget(self.lbl_67, 9, 0)
        self.pyramidLay.addWidget(self.entry_32, 9, 1)
        self.pyramidLay.addWidget(self.lbl_68, 10, 0)
        self.pyramidLay.addWidget(self.entry_33, 10, 1)
        self.pyramidLay.addWidget(self.lbl_69, 11, 0, 1, 2)
        self.pyramidLay.addWidget(self.btn_17, 12, 0, 1, 2)
        self.pyramidLay.addWidget(self.btn_clear_9, 12, 2)

        self.pyramidWdj = QWidget()
        self.pyramidWdj.setLayout(self.pyramidLay)

        self.threeDimWdj = QWidget()

        self.threeDimStack = QStackedLayout(self.threeDimWdj)
        self.threeDimStack.addWidget(self.cubeWdj)
        self.threeDimStack.addWidget(self.cuboidWdj)
        self.threeDimStack.addWidget(self.sphereWdj)
        self.threeDimStack.addWidget(self.coneWdj)
        self.threeDimStack.addWidget(self.pyramidWdj)
        self.threeDimStack.setCurrentIndex(0)

        self.threeDimWdj.setLayout(self.threeDimStack)

        self.threeDimLayout = QHBoxLayout()
        self.threeDimLayout.addWidget(self.threeDimList)
        self.threeDimLayout.addWidget(self.threeDimWdj)

        self.threeDimWidget = QWidget()
        self.threeDimWidget.setLayout(self.threeDimLayout)

        self.settingWidgets()

    def settingWidgets(self):
        self.tabWidget = QTabWidget()
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.addTab(self.twoDimWidget, '2D Objects')
        self.tabWidget.addTab(self.threeDimWidget, '3D Objects')

        self.setCentralWidget(self.tabWidget)

    def clearBtnAction(self):
        array_1 = [
            self.entry_one, self.entry_two, self.entry_three, self.entry_four, self.entry_six, self.entry_seven,
            self.entry_eight, self.entry_nine, self.entry_ten, self.entry_11, self.entry_12, self.entry_13,
            self.entry_14, self.entry_15, self.entry_16, self.entry_17, self.entry_18, self.entry_19, self.entry_20,
            self.entry_21, self.entry_22, self.entry_23, self.entry_24, self.entry_25, self.entry_26, self.entry_27,
            self.entry_28, self.entry_29, self.entry_30, self.entry_31, self.entry_32, self.entry_33
        ]

        array_2 = [
            self.lbl_three, self.lbl_ten, self.lbl_17, self.lbl_24, self.lbl_32, self.lbl_40, self.lbl_48, self.lbl_55,
            self.lbl_64
        ]

        array_3 = [
            self.lbl_six, self.lbl_14, self.lbl_20, self.lbl_29
        ]

        array_4 = [
            self.lbl_35, self.lbl_45, self.lbl_51, self.lbl_59, self.lbl_69
        ]

        for i in array_1:
            i.clear()
        for i in array_2:
            i.setText(f'Area: 0 cm<sup>2</sup>')
        for i in array_3:
            i.setText(f'Perimeter: 0 cm')
        for i in array_4:
            i.setText(f'Volume: 0 cm<sup>3</sup>')

    def calcPyramidValArea(self, event):
        length_1 = self.entry_28.text()
        breadth_1 = self.entry_29.text()
        height_1 = self.entry_30.text()
        length_2 = self.entry_31.text()
        breadth_2 = self.entry_32.text()
        height_2 = self.entry_33.text()
        if (not (length_1 == '' or breadth_1 == '' or height_1 == '')) and event == 0:
            l_1 = int(length_1)
            b_1 = int(breadth_1)
            h_1 = int(height_1)
            self.lbl_64.setText(f'Area: {round((l_1 * b_1) + (l_1 * math.sqrt((b_1 / 2)**2 + h_1**2)) + (b_1 * math.sqrt((l_1 / 2)**2 + h_1**2)), 2)} cm<sup>2</sup>')
        if (not (length_2 == '' or breadth_2 == '' or height_2 == '')) and event == 1:
            l_2 = int(length_2)
            b_2 = int(breadth_2)
            h_2 = int(height_2)
            self.lbl_69.setText(f'Volume: {round((1/3) * l_2 * b_2 * h_2, 2)} cm<sup>3</sup>')

    def calcConeValArea(self, event):
        radius_1 = self.entry_24.text()
        height_1 = self.entry_25.text()
        radius_2 = self.entry_26.text()
        height_2 = self.entry_27.text()
        if (not (radius_1 == '' or height_1 == '')) and event == 0:
            r_1 = int(radius_1)
            h_1 = int(height_1)
            self.lbl_55.setText(f'Area: {round((math.pi * r_1**2) + (math.pi * r_1 * h_1), 2)} cm<sup>2</sup>')
        if (not (radius_2 == '' or height_2 == '')) and event == 1:
            r_2 = int(radius_2)
            h_2 = int(height_2)
            self.lbl_59.setText(f'Volume: {round((1/3) * math.pi * r_2**2 * h_2, 2)} cm<sup>3</sup>')

    def calcSphereVolArea(self, text, event):
        if not text == '':
            r = int(text)
            if event == 0:
                self.lbl_48.setText(f'Area: {round(4 * math.pi * r**2, 2)} cm<sup>2</sup>')
            elif event == 1:
                self.lbl_51.setText(f'Volume: {round((4/3) * math.pi * r**3, 2)} cm<sup>3</sup>')

    def calcCuboidValArea(self, event):
        length_1 = self.entry_16.text()
        breadth_1 = self.entry_17.text()
        height_1 = self.entry_18.text()
        length_2 = self.entry_19.text()
        breadth_2 = self.entry_20.text()
        height_2 = self.entry_21.text()
        if (not (length_1 == '' or breadth_1 == '' or height_1 == '')) and event == 0:
            l_1 = int(length_1)
            b_1 = int(breadth_1)
            h_1 = int(height_1)
            self.lbl_40.setText(f'Area: {2 * (l_1 * b_1 + l_1 * h_1 + h_1 * b_1)} cm<sup>2</sup>')
        if (not (length_2 == '' or breadth_2 == '' or height_2 == '')) and event == 1:
            l_2 = int(length_2)
            b_2 = int(breadth_2)
            h_2 = int(height_2)
            self.lbl_45.setText(f'Volume: {l_2 * b_2 * h_2} cm<sup>3</sup>')

    def calcCubeVolArea(self, text, event):
        if not text == '':
            a = int(text)
            if event == 0:
                self.lbl_32.setText(f'Area: {a**2 * 6} cm<sup>2</sup>')
            elif event == 1:
                self.lbl_35.setText(f'Volume: {a**3} cm<sup>3</sup>')

    def calcTrianglePeriArea(self, event):
        base_1 = self.entry_nine.text()
        height = self.entry_ten.text()
        a_side = self.entry_11.text()
        b_side = self.entry_12.text()
        c_side = self.entry_13.text()
        if (not (base_1 == '' or height == '')) and event == 0:
            b_1 = int(base_1)
            h = int(height)
            self.lbl_24.setText(f'Area: {1/2 * b_1 * h} cm<sup>2</sup>')
        if (not (a_side == '' or b_side == '' or c_side == '')) and event == 1:
            a = int(a_side)
            b = int(b_side)
            c = int(c_side)
            self.lbl_29.setText(f'Perimeter: {a + b + c} cm')

    def calcCirclePeriArea(self, text, event):
        if not text == '':
            r = int(text)
            if event == 0:
                self.lbl_17.setText(f'Area: {round(math.pi * r**2, 2)} cm<sup>2</sup>')
            elif event == 1:
                self.lbl_20.setText(f'Perimeter: {round(2 * math.pi * r, 2)} cm')

    def calcRectanglePeriArea(self, event):
        width_1 = self.entry_three.text()
        length_1 = self.entry_four.text()
        width_2 = self.entry_five.text()
        length_2 = self.entry_six.text()
        if (not (width_1 == '' or length_1 == '')) and event == 0:
            w_1 = int(width_1)
            l_1 = int(length_1)
            self.lbl_ten.setText(f'Area: {w_1 * l_1} cm<sup>2</sup>')
        if (not (width_2 == '' or length_2 == '')) and event == 1:
            w_2 = int(width_2)
            l_2 = int(length_2)
            self.lbl_14.setText(f'Perimeter: {(w_2 * 2) + (l_2 * 2)} cm')

    def calcSquarePeriArea(self, text, event):
        if not text == '':
            a = int(text)
            if event == 0:
                self.lbl_three.setText(f'Area: {a * a} cm<sup>2</sup>')
            elif event == 1:
                self.lbl_six.setText(f'Perimeter: {a * 4} cm')

    def resizeEvent(self, event):
        vary.width = self.width()
        vary.height = self.height()
        text = f'{vary.width}\n{vary.height}'
        file = open('assets/data/winfo.txt', 'w')
        file.write(text)


def main():
    app = QApplication(sys.argv)
    styleSheet = open(f'assets/styles/theme.qss', 'r').read()
    app.setStyleSheet(styleSheet)
    window = MainWindow()
    pywinstyles.apply_style(window, 'dark')
    window.show()
    app.exec()
