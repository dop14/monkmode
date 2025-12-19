# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'small_focus_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(200, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(200, 200))
        Form.setMaximumSize(QSize(300, 287))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.smallFrame = QFrame(Form)
        self.smallFrame.setObjectName(u"smallFrame")
        self.smallFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.smallFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.smallFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.back_to_main_btn = QPushButton(self.smallFrame)
        self.back_to_main_btn.setObjectName(u"back_to_main_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.back_to_main_btn.sizePolicy().hasHeightForWidth())
        self.back_to_main_btn.setSizePolicy(sizePolicy1)
        self.back_to_main_btn.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(9)
        self.back_to_main_btn.setFont(font)
        self.back_to_main_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.back_to_main_btn.setStyleSheet(u"padding: 3px 0px 3px 0px;")
        self.back_to_main_btn.setIconSize(QSize(12, 12))

        self.verticalLayout.addWidget(self.back_to_main_btn)

        self.image_layout = QVBoxLayout()
        self.image_layout.setObjectName(u"image_layout")

        self.verticalLayout.addLayout(self.image_layout)

        self.time_label = QLabel(self.smallFrame)
        self.time_label.setObjectName(u"time_label")
        sizePolicy1.setHeightForWidth(self.time_label.sizePolicy().hasHeightForWidth())
        self.time_label.setSizePolicy(sizePolicy1)
        self.time_label.setMaximumSize(QSize(300, 220))
        font1 = QFont()
        font1.setPointSize(36)
        self.time_label.setFont(font1)

        self.verticalLayout.addWidget(self.time_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.session_label = QLabel(self.smallFrame)
        self.session_label.setObjectName(u"session_label")

        self.verticalLayout.addWidget(self.session_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.small_pause_btn = QPushButton(self.smallFrame)
        self.small_pause_btn.setObjectName(u"small_pause_btn")
        sizePolicy1.setHeightForWidth(self.small_pause_btn.sizePolicy().hasHeightForWidth())
        self.small_pause_btn.setSizePolicy(sizePolicy1)
        self.small_pause_btn.setMinimumSize(QSize(60, 0))
        self.small_pause_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.small_pause_btn.setStyleSheet(u"padding: 3px 0px 3px  0px;")

        self.horizontalLayout.addWidget(self.small_pause_btn)

        self.small_resume_btn = QPushButton(self.smallFrame)
        self.small_resume_btn.setObjectName(u"small_resume_btn")
        sizePolicy1.setHeightForWidth(self.small_resume_btn.sizePolicy().hasHeightForWidth())
        self.small_resume_btn.setSizePolicy(sizePolicy1)
        self.small_resume_btn.setMinimumSize(QSize(60, 0))
        self.small_resume_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.small_resume_btn.setStyleSheet(u"padding: 3px 0px 3px  0px;")

        self.horizontalLayout.addWidget(self.small_resume_btn)

        self.small_stop_btn = QPushButton(self.smallFrame)
        self.small_stop_btn.setObjectName(u"small_stop_btn")
        sizePolicy1.setHeightForWidth(self.small_stop_btn.sizePolicy().hasHeightForWidth())
        self.small_stop_btn.setSizePolicy(sizePolicy1)
        self.small_stop_btn.setMinimumSize(QSize(60, 0))
        self.small_stop_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.small_stop_btn.setStyleSheet(u"padding: 3px 0px 3px  0px;")

        self.horizontalLayout.addWidget(self.small_stop_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.smallFrame)


        self.retranslateUi(Form)

        self.back_to_main_btn.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.back_to_main_btn.setText("")
        self.time_label.setText(QCoreApplication.translate("Form", u"time", None))
        self.session_label.setText("")
        self.small_pause_btn.setText("")
        self.small_resume_btn.setText("")
        self.small_stop_btn.setText("")
    # retranslateUi

