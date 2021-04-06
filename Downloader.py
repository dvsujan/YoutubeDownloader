from PyQt5 import QtCore, QtGui, QtWidgets 
from pytube import YouTube
from youtubesearchpython import VideosSearch
from youtubesearchpython import Video
import requests
import sys 
import pytube

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowTitle("Youtube Downloader")
        Dialog.resize(1126, 623)
        self.FILENAME = ""
        Dialog.setStyleSheet("background-color:#282828;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1131, 71))
        self.label.setStyleSheet("background-color:#FF0000")
        self.label.setText("")
        self.label.setObjectName("label")
        self.LinkInput = QtWidgets.QLineEdit(Dialog)
        self.LinkInput.setGeometry(QtCore.QRect(280, 210, 301, 41))
        self.LinkInput.setStyleSheet("background-color:white;\n"
"color: rgb(34, 34, 34);\n"
"border-radius:20px;")
        self.LinkInput.setObjectName("LinkInput")
        self.ThumbNailView = QtWidgets.QLabel(Dialog)
        self.ThumbNailView.setGeometry(QtCore.QRect(660, 170, 421, 241))
        self.ThumbNailView.setStyleSheet("background-color:#282829")
        self.ThumbNailView.setText("")
        self.ThumbNailView.setObjectName("ThumbNailView")
        self.LocationInput = QtWidgets.QLineEdit(Dialog)
        self.LocationInput.setGeometry(QtCore.QRect(280, 320, 301, 41))
        self.LocationInput.setStyleSheet("background-color:white;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px; ")
        self.LocationInput.setObjectName("LocationInput")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 131, 31))
        self.label_3.setStyleSheet("font: 75 16pt \"SansSerif\"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 320, 221, 31))
        self.label_4.setStyleSheet("font: 75 16pt \"SansSerif\"")
        self.label_4.setObjectName("label_4")
        self.DownloadButton = QtWidgets.QPushButton(Dialog)
        self.DownloadButton.setGeometry(QtCore.QRect(450, 510, 211, 51))
        self.DownloadButton.setStyleSheet("color: rgb(253, 253, 253);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(72, 72, 72);\n"
"")
        self.DownloadButton.setObjectName("DownloadButton")
        self.FileSelector = QtWidgets.QPushButton(Dialog)
        self.FileSelector.setGeometry(QtCore.QRect(590, 320, 51, 41))
        self.FileSelector.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.FileSelector.setObjectName("FileSelector")
        self.DownloadInfo = QtWidgets.QLabel(Dialog)
        self.DownloadInfo.setGeometry(QtCore.QRect(40, 570, 101, 16))
        self.DownloadInfo.setObjectName("DownloadInfo")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.DownloadButton.clicked.connect(self.on_download_btn_clicked)
        self.FileSelector.clicked.connect(self.openFileDialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Enter Link"))
        self.label_4.setText(_translate("Dialog", "Enter File location"))
        self.DownloadButton.setText(_translate("Dialog", "Download"))
        self.FileSelector.setText(_translate("Dialog", "..."))
        self.DownloadInfo.setText(_translate("Dialog", " "))

    def openFileDialog(self):
            try: 
                self.FILENAME = str(QtWidgets.QFileDialog.getExistingDirectory(Dialog,"Select location to save the video"))
                self.LocationInput.setText(self.FILENAME)
            except Exception as e:
                self.DownloadInfo.setText("ERROR")
    
    def on_download_btn_clicked(self):
        try:
            videoLink = self.LinkInput.text() 
            videoInfo = Video.getInfo(videoLink)
            Title = videoInfo['title']
            ThumbNail = videoInfo['thumbnails'][3]['url']
            image = QtGui.QImage() 
            image.loadFromData(requests.get(ThumbNail).content) 
            self.ThumbNailView.setPixmap(QtGui.QPixmap(image))
            self.DownloadInfo.setText("Downloading")     
            print(self.FILENAME) 
            yt = YouTube(videoLink) 
            yt.streams.filter(progressive = True,file_extension = "mp4").first().download(output_path = str(self.FILENAME),filename = str(Title))
        
        except Exception as e:
                self.DownloadInfo.setText("ERROR") 
                return 
        
        self.DownloadInfo.setText("compleated")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('logo.png'))
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())