# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PycharmProjects/DPricer/DPricer/presentation/Designer-Files/CourbeTaux.ui'
#
# Created: Fri Oct 17 18:14:01 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CourbeTaux(object):
    def setupUi(self, CourbeTaux):
        CourbeTaux.setObjectName(_fromUtf8("CourbeTaux"))
        CourbeTaux.resize(674, 550)
        CourbeTaux.setMaximumSize(QtCore.QSize(1678976, 123456))
        CourbeTaux.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(CourbeTaux)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox = QtGui.QGroupBox(CourbeTaux)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(430, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(750, 16777215))
        self.groupBox.setSizeIncrement(QtCore.QSize(1, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.dateEditFilter = QtGui.QDateEdit(self.groupBox)
        self.dateEditFilter.setMaximumSize(QtCore.QSize(250, 16777215))
        self.dateEditFilter.setDate(QtCore.QDate(2014, 10, 1))
        self.dateEditFilter.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1785, 9, 14), QtCore.QTime(0, 0, 0)))
        self.dateEditFilter.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.dateEditFilter.setCalendarPopup(True)
        self.dateEditFilter.setCurrentSectionIndex(0)
        self.dateEditFilter.setObjectName(_fromUtf8("dateEditFilter"))
        self.horizontalLayout.addWidget(self.dateEditFilter)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.labelTransaction = QtGui.QLabel(self.groupBox)
        self.labelTransaction.setObjectName(_fromUtf8("labelTransaction"))
        self.horizontalLayout.addWidget(self.labelTransaction)
        self.lineEditTransaction = QtGui.QLineEdit(self.groupBox)
        self.lineEditTransaction.setMaximumSize(QtCore.QSize(115, 16777215))
        self.lineEditTransaction.setReadOnly(True)
        self.lineEditTransaction.setObjectName(_fromUtf8("lineEditTransaction"))
        self.horizontalLayout.addWidget(self.lineEditTransaction)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableWidgetCourbe = QtGui.QTableWidget(self.groupBox)
        self.tableWidgetCourbe.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetCourbe.sizePolicy().hasHeightForWidth())
        self.tableWidgetCourbe.setSizePolicy(sizePolicy)
        self.tableWidgetCourbe.setMinimumSize(QtCore.QSize(400, 0))
        self.tableWidgetCourbe.setMaximumSize(QtCore.QSize(5000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidgetCourbe.setFont(font)
        self.tableWidgetCourbe.setMidLineWidth(0)
        self.tableWidgetCourbe.setEditTriggers(QtGui.QAbstractItemView.EditKeyPressed)
        self.tableWidgetCourbe.setDragDropOverwriteMode(False)
        self.tableWidgetCourbe.setAlternatingRowColors(True)
        self.tableWidgetCourbe.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetCourbe.setShowGrid(False)
        self.tableWidgetCourbe.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidgetCourbe.setWordWrap(False)
        self.tableWidgetCourbe.setRowCount(0)
        self.tableWidgetCourbe.setObjectName(_fromUtf8("tableWidgetCourbe"))
        self.tableWidgetCourbe.setColumnCount(5)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetCourbe.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetCourbe.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetCourbe.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetCourbe.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetCourbe.setHorizontalHeaderItem(4, item)
        self.tableWidgetCourbe.horizontalHeader().setVisible(True)
        self.tableWidgetCourbe.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetCourbe.verticalHeader().setVisible(True)
        self.tableWidgetCourbe.verticalHeader().setDefaultSectionSize(22)
        self.tableWidgetCourbe.verticalHeader().setMinimumSectionSize(16)
        self.tableWidgetCourbe.verticalHeader().setSortIndicatorShown(True)
        self.tableWidgetCourbe.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableWidgetCourbe)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(CourbeTaux)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.saisirMaturitLabel = QtGui.QLabel(self.groupBox_2)
        self.saisirMaturitLabel.setObjectName(_fromUtf8("saisirMaturitLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.saisirMaturitLabel)
        self.maturiteLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.maturiteLineEdit.setMinimumSize(QtCore.QSize(40, 0))
        self.maturiteLineEdit.setObjectName(_fromUtf8("maturiteLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.maturiteLineEdit)
        self.tauxDActualisationLabel = QtGui.QLabel(self.groupBox_2)
        self.tauxDActualisationLabel.setObjectName(_fromUtf8("tauxDActualisationLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.tauxDActualisationLabel)
        self.tauxLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.tauxLineEdit.setMinimumSize(QtCore.QSize(40, 0))
        self.tauxLineEdit.setReadOnly(True)
        self.tauxLineEdit.setObjectName(_fromUtf8("tauxLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.tauxLineEdit)
        self.interpolationSplineLabel = QtGui.QLabel(self.groupBox_2)
        self.interpolationSplineLabel.setObjectName(_fromUtf8("interpolationSplineLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.interpolationSplineLabel)
        self.splineCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.splineCheckBox.setObjectName(_fromUtf8("splineCheckBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.splineCheckBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.line_2 = QtGui.QFrame(self.groupBox_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.saisirMaturitLabel.setBuddy(self.maturiteLineEdit)

        self.retranslateUi(CourbeTaux)
        QtCore.QMetaObject.connectSlotsByName(CourbeTaux)

    def retranslateUi(self, CourbeTaux):
        CourbeTaux.setWindowTitle(_translate("CourbeTaux", "Courbe de taux", None))
        self.groupBox.setTitle(_translate("CourbeTaux", "Taux BAM", None))
        self.label.setText(_translate("CourbeTaux", "Date d\'évaluation :", None))
        self.dateEditFilter.setDisplayFormat(_translate("CourbeTaux", "dd/MM/yyyy", None))
        self.labelTransaction.setText(_translate("CourbeTaux", "Date de Transaction :", None))
        item = self.tableWidgetCourbe.horizontalHeaderItem(0)
        item.setText(_translate("CourbeTaux", "Maturite résiduelle", None))
        item = self.tableWidgetCourbe.horizontalHeaderItem(1)
        item.setText(_translate("CourbeTaux", "TMP", None))
        item = self.tableWidgetCourbe.horizontalHeaderItem(2)
        item.setText(_translate("CourbeTaux", "Date Valeur", None))
        item = self.tableWidgetCourbe.horizontalHeaderItem(3)
        item.setText(_translate("CourbeTaux", "Date Echeance", None))
        item = self.tableWidgetCourbe.horizontalHeaderItem(4)
        item.setText(_translate("CourbeTaux", "Transactions", None))
        self.saisirMaturitLabel.setText(_translate("CourbeTaux", "Saisir &maturité", None))
        self.maturiteLineEdit.setPlaceholderText(_translate("CourbeTaux", "jours", None))
        self.tauxDActualisationLabel.setText(_translate("CourbeTaux", "Taux d\'actualisation", None))
        self.interpolationSplineLabel.setText(_translate("CourbeTaux", "Interpolation Spline", None))

