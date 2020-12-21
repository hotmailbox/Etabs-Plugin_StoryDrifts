# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storyDrift_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(538, 351)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 511, 91))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 20, 279, 53))
        self.widget.setObjectName("widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.reduction_factor_x = QtWidgets.QLineEdit(self.widget)
        self.reduction_factor_x.setObjectName("reduction_factor_x")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.reduction_factor_x)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.reduction_factor_y = QtWidgets.QLineEdit(self.widget)
        self.reduction_factor_y.setObjectName("reduction_factor_y")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.reduction_factor_y)
        self.widget1 = QtWidgets.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(300, 20, 201, 24))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.important_factor = QtWidgets.QLineEdit(self.widget1)
        self.important_factor.setObjectName("important_factor")
        self.horizontalLayout.addWidget(self.important_factor)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 141, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.dd2_sd1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.dd2_sd1.setGeometry(QtCore.QRect(10, 60, 113, 22))
        self.dd2_sd1.setObjectName("dd2_sd1")
        self.dd2_sds = QtWidgets.QLineEdit(self.groupBox_2)
        self.dd2_sds.setGeometry(QtCore.QRect(10, 30, 113, 22))
        self.dd2_sds.setObjectName("dd2_sds")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(170, 110, 141, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.dd3_sd1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.dd3_sd1.setGeometry(QtCore.QRect(10, 60, 113, 22))
        self.dd3_sd1.setObjectName("dd3_sd1")
        self.dd3_sds = QtWidgets.QLineEdit(self.groupBox_3)
        self.dd3_sds.setGeometry(QtCore.QRect(10, 30, 113, 22))
        self.dd3_sds.setObjectName("dd3_sds")
        self.kappa_values = QtWidgets.QComboBox(Form)
        self.kappa_values.setGeometry(QtCore.QRect(400, 220, 73, 22))
        self.kappa_values.setObjectName("kappa_values")
        self.check_button = QtWidgets.QPushButton(Form)
        self.check_button.setGeometry(QtCore.QRect(400, 280, 93, 28))
        self.check_button.setObjectName("check_button")
        self.get_values_button = QtWidgets.QPushButton(Form)
        self.get_values_button.setGeometry(QtCore.QRect(330, 120, 93, 28))
        self.get_values_button.setObjectName("get_values_button")
        self.condition_values = QtWidgets.QComboBox(Form)
        self.condition_values.setGeometry(QtCore.QRect(320, 220, 73, 22))
        self.condition_values.setObjectName("condition_values")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Göreli Kat Ötelenmesi Kontrolü"))
        self.groupBox.setTitle(_translate("Form", "Deprem Parametreleri"))
        self.label_3.setText(_translate("Form", "Taşıyıcı Sistem Davranış Katsayısı, X"))
        self.reduction_factor_x.setPlaceholderText(_translate("Form", "R_X"))
        self.label_4.setText(_translate("Form", "Taşıyıcı Sistem Davranış Katsayısı, Y"))
        self.reduction_factor_y.setPlaceholderText(_translate("Form", "R_Y"))
        self.label_5.setText(_translate("Form", "Bina Önem Katsayısı"))
        self.important_factor.setPlaceholderText(_translate("Form", "I"))
        self.groupBox_2.setTitle(_translate("Form", "DD-2 Parametreleri"))
        self.dd2_sd1.setPlaceholderText(_translate("Form", "Sd1 for DD2"))
        self.dd2_sds.setPlaceholderText(_translate("Form", "Sds for DD2"))
        self.groupBox_3.setTitle(_translate("Form", "DD-3 parametreleri"))
        self.dd3_sd1.setPlaceholderText(_translate("Form", "Sd1 for DD3"))
        self.dd3_sds.setPlaceholderText(_translate("Form", "Sds for DD3"))
        self.check_button.setText(_translate("Form", "Check"))
        self.get_values_button.setText(_translate("Form", "Kaydet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

