# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clipboard_history.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QSizePolicy, QWidget)

class Ui_SimpleClipboardHistory(object):
    def setupUi(self, SimpleClipboardHistory):
        if not SimpleClipboardHistory.objectName():
            SimpleClipboardHistory.setObjectName(u"SimpleClipboardHistory")
        SimpleClipboardHistory.resize(300, 393)
        SimpleClipboardHistory.setMinimumSize(QSize(0, 0))
        SimpleClipboardHistory.setMaximumSize(QSize(16777215, 16777215))
        SimpleClipboardHistory.setStyleSheet(u"/* \u4e3b\u7a97\u53e3\u6837\u5f0f - \u6539\u8fdb\u7684\u4e9a\u514b\u529b\u6bdb\u73bb\u7483\u6548\u679c */\n"
"SimpleClipboardHistory {\n"
"    background: rgba(245, 245, 245, 0.85);  /* \u63d0\u9ad8\u4e0d\u900f\u660e\u5ea6 */\n"
"    border-radius: 12px;\n"
"    border: 1px solid rgba(255, 255, 255, 0.6);\n"
"    padding: 0;\n"
"    backdrop-filter: blur(15px);\n"
"    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"/* \u6807\u9898\u680f\u6837\u5f0f */\n"
"QWidget#header {\n"
"    height: 40px;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border-top-left-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"    padding-left: 15px;\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.08);\n"
"}\n"
"\n"
"/* \u6807\u9898\u6587\u672c */\n"
"QLabel#title_label {\n"
"    font-family: \"Segoe UI\", \"Microsoft YaHei\", sans-serif;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    color: #333333;  /* \u6539\u4e3a\u6df1\u8272\u6587\u5b57 */\n"
"    text-shadow: 0 1px 1px rgba(255, 255, 255, "
                        "0.8);\n"
"}\n"
"\n"
"/* \u641c\u7d22\u6846 - \u6539\u8fdb\u7684\u53ef\u8bfb\u6027 */\n"
"QLineEdit#search_box {\n"
"    border: 1px solid rgba(0, 0, 0, 0.1);\n"
"    border-radius: 18px;\n"
"    padding: 8px 15px 8px 35px;\n"
"    margin: 12px;\n"
"    font-size: 13px;\n"
"    background: rgba(255, 255, 255, 0.7) url(:/icons/search.svg) no-repeat 12px center;\n"
"    color: #333333;  /* \u6df1\u8272\u6587\u5b57 */\n"
"    selection-background-color: #0078D4;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QLineEdit#search_box::placeholder {\n"
"    color: rgba(0, 0, 0, 0.4);  /* \u66f4\u660e\u663e\u7684\u5360\u4f4d\u7b26 */\n"
"}\n"
"\n"
"QLineEdit#search_box:focus {\n"
"    border: 1px solid #0078D4;\n"
"    background-color: rgba(255, 255, 255, 0.9);\n"
"}\n"
"\n"
"/* \u5386\u53f2\u5217\u8868 - \u63d0\u9ad8\u5bf9\u6bd4\u5ea6 */\n"
"QListWidget#history_list {\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.08);\n"
"    border-radius: 8px;\n"
"    padding: 0;\n"
"    outl"
                        "ine: none;\n"
"    font-size: 13px;\n"
"    margin: 12px;\n"
"    color: #333333;  /* \u6df1\u8272\u6587\u5b57 */\n"
"}\n"
"\n"
"/* \u5217\u8868\u9879 */\n"
"QListWidget#history_list::item {\n"
"    height: 40px;\n"
"    padding: 8px 15px;\n"
"    background: transparent;\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.05);\n"
"    color: #333333;  /* \u6df1\u8272\u6587\u5b57 */\n"
"}\n"
"\n"
"/* \u60ac\u505c\u6548\u679c */\n"
"QListWidget#history_list::item:hover {\n"
"    background: rgba(0, 0, 0, 0.05);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u9009\u4e2d\u6548\u679c */\n"
"QListWidget#history_list::item:selected {\n"
"    background: #0078D4;\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"/* ================= \u5782\u76f4\u6eda\u52a8\u6761 ================= */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgba(0, 0, 0, 0.05);  /* \u975e\u5e38\u6de1\u7684\u80cc\u666f */\n"
"    width: 10px;  /* \u6eda\u52a8\u6761\u5bbd\u5ea6 */\n"
"    margin: 2px;\n"
"   "
                        " border-radius: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgba(0, 0, 0, 0.2);  /* \u534a\u900f\u660e\u7070\u8272 */\n"
"    min-height: 30px;  /* \u6700\u5c0f\u9ad8\u5ea6 */\n"
"    border-radius: 5px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgba(0, 0, 0, 0.3);  /* \u60ac\u505c\u65f6\u52a0\u6df1 */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;  /* \u9690\u85cf\u4e0a\u4e0b\u7bad\u5934\u533a\u57df */\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;  /* \u6eda\u52a8\u6761\u80cc\u666f\u4ee5\u5916\u7684\u533a\u57df\u900f\u660e */\n"
"}\n"
"\n"
"/* ================= \u6c34\u5e73\u6eda\u52a8\u6761 ================= */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgba(0, 0, 0, 0.05);\n"
"    height: 10px;  /* \u6eda\u52a8\u6761\u9ad8\u5ea6 */\n"
"    margin: 2px;\n"
"    border"
                        "-radius: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(0, 0, 0, 0.2);\n"
"    min-width: 30px;  /* \u6700\u5c0f\u5bbd\u5ea6 */\n"
"    border-radius: 5px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 0px;  /* \u9690\u85cf\u5de6\u53f3\u7bad\u5934\u533a\u57df */\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"/* ================= \u6eda\u52a8\u6761\u89d2\u90e8 ================= */\n"
"QScrollCorner {\n"
"    background: rgba(0, 0, 0, 0.05);  /* \u4e0e\u6eda\u52a8\u6761\u80cc\u666f\u4e00\u81f4 */\n"
"}\n"
"\n"
"/* ================= \u786e\u8ba4\u6309\u94ae\u548c\u5220\u9664 ================= */\n"
"\n"
"/* ===== \u529f\u80fd\u6309\u94ae ===== */\n"
"QPushButton#toggle_btn {\n"
"    background-color: #4CAF50;\n"
"  "
                        "  border: none;\n"
"    color: white;\n"
"    padding: 10px;\n"
"    margin: 6px;\n"
"    border-radius: 5px;\n"
"    min-height: 36px;\n"
"}\n"
"\n"
"QPushButton#toggle_btn:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton#toggle_btn:pressed {\n"
"    background-color: #3d8b40;\n"
"}\n"
"\n"
"QPushButton#btn_delete {\n"
"    background-color: #ef5350;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px;\n"
"    margin: 6px;\n"
"    border-radius: 5px;\n"
"    min-height: 36px;\n"
"}\n"
"\n"
"QPushButton#btn_delete:hover {\n"
"    background-color: #e53935;\n"
"}\n"
"\n"
"QPushButton#btn_delete:pressed {\n"
"    background-color: #d32f2f;\n"
"}\n"
"\n"
"\n"
"\n"
"/* \u786e\u4fdd\u80cc\u666f\u900f\u660e */\n"
"QListWidget {\n"
"    background: transparent;\n"
"    outline: none;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background: white;\n"
"    border-radius: 5px;\n"
"    margin: 3px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background: #f0f7ff;\n"
"}\n"
"\n"
"\n"
"/"
                        "* \u7cfb\u7edf\u6258\u76d8\u83dc\u5355\u6837\u5f0f */\n"
"QMenu {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #d0d0d0;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 5px 20px 5px 10px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background: #e0e0e0;\n"
"    margin: 3px 0;\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u7a97\u53e3\u6837\u5f0f */\n"
"SettingsWindow {\n"
"    background-color: #f9f9f9;\n"
"    border: 1px solid #ddd;\n"
"}\n"
"\n"
"SettingsWindow QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: #5c9dff;\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"SettingsWindow QSpinBox {\n"
"    padding: 5px;\n"
"}\n"
"\n"
"SettingsWindow QCheckBox {\n"
"    spacing: 5px;\n"
"}")
        self.centralwidget = QWidget(SimpleClipboardHistory)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.search_box = QLineEdit(self.centralwidget)
        self.search_box.setObjectName(u"search_box")
        self.search_box.setStyleSheet(u"")

        self.gridLayout.addWidget(self.search_box, 0, 0, 1, 1)

        self.history_list = QListWidget(self.centralwidget)
        self.history_list.setObjectName(u"history_list")

        self.gridLayout.addWidget(self.history_list, 1, 0, 1, 1)

        SimpleClipboardHistory.setCentralWidget(self.centralwidget)

        self.retranslateUi(SimpleClipboardHistory)

        QMetaObject.connectSlotsByName(SimpleClipboardHistory)
    # setupUi

    def retranslateUi(self, SimpleClipboardHistory):
        SimpleClipboardHistory.setWindowTitle(QCoreApplication.translate("SimpleClipboardHistory", u"\u526a\u8d34\u677f\u5386\u53f2\u8bb0\u5f55", None))
        self.search_box.setPlaceholderText(QCoreApplication.translate("SimpleClipboardHistory", u"\u641c\u7d22\u526a\u8d34\u677f\u5386\u53f2...", None))
    # retranslateUi

