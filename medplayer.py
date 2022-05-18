from PyQt5 import QtCore, QtGui, QtWidgets
import multiprocessing
# from PyQt5.QtCore import QThread

# class Worker(QObject):
#     finished = pyqtSignal()

#     def __init__(self,title,year,url,artist,genre,format):
#         super(QObject, self).__init__()
#         self.title = title
#         self.year = year 
#         self.url = url 
#         self.artist = artist 
#         self.genre = genre 
#         self.format = format

#     def wavPlay(self):
#         from wavplay import wavplay
#         self.wav = wavplay(self.title, self.year, self.url, self.artist, self.genre, self.format)
#         print(self.wav)
#         self.wav.playwav()

#     def mp3Play(self):
#         from mp3play import mp3play
#         self.mp3 = mp3play(self.title, self.year, self.url, self.artist, self.genre, self.format)
#         print(self.mp3)
#         self.mp3.playmp3()
    
#     def mp4Play(self):
#         from mp4play import mp4play
#         self.mp4 = mp4play(self.title, self.year, self.url, self.artist, self.genre, self.format)
#         print(self.mp4)
#         self.mp4.playmp4()

# url2 = "https://www.midiworld.com/download/3590"
# url3 = "https://bigsoundbank.com/UPLOAD/wav/0253.wav"
# mp4file = '/Users/alexsbae/Documents/Comp305/comp305proj/file_example_MP4_1280_10MG.mp4'
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(558, 254)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lab_med_player = QtWidgets.QLabel(self.centralwidget)
        self.lab_med_player.setGeometry(QtCore.QRect(10, 0, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lab_med_player.setFont(font)
        self.lab_med_player.setObjectName("lab_med_player")
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 20, 651, 16))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.inp_title = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_title.setGeometry(QtCore.QRect(90, 40, 261, 21))
        self.inp_title.setAccessibleName("")
        self.inp_title.setObjectName("inp_title")
        # self.inp_title.textChanged.connect(self.getTitle)

        self.inp_year = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_year.setGeometry(QtCore.QRect(440, 40, 101, 21))
        self.inp_year.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.inp_year.setObjectName("inp_year")
        # self.inp_year.textChanged.connect(self.getYear)

        self.inp_url = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_url.setGeometry(QtCore.QRect(90, 100, 451, 21))
        self.inp_url.setObjectName("inp_url")
        # self.inp_url.textChanged.connect(self.getUrl)

        self.inp_artist = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_artist.setGeometry(QtCore.QRect(90, 70, 261, 21))
        self.inp_artist.setObjectName("inp_artist")
        # self.inp_artist.textChanged.connect(self.getArtist)

        self.inp_genre = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_genre.setGeometry(QtCore.QRect(440, 70, 101, 21))
        self.inp_genre.setObjectName("inp_genre")
        # self.inp_genre.textChanged.connect(self.getGenre)

        self.lab_title = QtWidgets.QLabel(self.centralwidget)
        self.lab_title.setGeometry(QtCore.QRect(10, 40, 81, 16))
        self.lab_title.setAutoFillBackground(False)
        self.lab_title.setObjectName("lab_title")

        self.lab_year = QtWidgets.QLabel(self.centralwidget)
        self.lab_year.setGeometry(QtCore.QRect(360, 40, 71, 20))
        self.lab_year.setObjectName("lab_year")

        self.lab_artist = QtWidgets.QLabel(self.centralwidget)
        self.lab_artist.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.lab_artist.setObjectName("lab_artist")

        self.lab_genre = QtWidgets.QLabel(self.centralwidget)
        self.lab_genre.setGeometry(QtCore.QRect(360, 70, 81, 16))
        self.lab_genre.setObjectName("lab_genre")

        self.lab_url = QtWidgets.QLabel(self.centralwidget)
        self.lab_url.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.lab_url.setObjectName("lab_url")

        self.but_play = QtWidgets.QPushButton(self.centralwidget)
        self.but_play.setGeometry(QtCore.QRect(10, 160, 113, 32))
        self.but_play.setObjectName("but_play")
        self.but_play.clicked.connect(self.play)

        self.but_pause = QtWidgets.QPushButton(self.centralwidget)
        self.but_pause.setGeometry(QtCore.QRect(120, 160, 113, 32))
        self.but_pause.setObjectName("but_pause")
        # self.but_pause.setCheckable(True)
        # self.but_pause.toggle()
        self.but_pause.clicked.connect(self.pause)

        self.but_replay = QtWidgets.QPushButton(self.centralwidget)
        self.but_replay.setGeometry(QtCore.QRect(230, 160, 113, 32))
        self.but_replay.setObjectName("but_replay")
        self.but_replay.clicked.connect(self.replay)

        self.but_load = QtWidgets.QPushButton(self.centralwidget)
        self.but_load.setGeometry(QtCore.QRect(430, 130, 113, 32))
        self.but_load.setObjectName("but_load")
        self.but_load.clicked.connect(self.load)

        self.formatMenu = QtWidgets.QComboBox(self.centralwidget)
        self.formatMenu.setGeometry(QtCore.QRect(330, 130, 101, 31))
        self.formatMenu.setObjectName("format")
        self.formatMenu.addItem("")
        self.formatMenu.addItem("")
        self.formatMenu.addItem("")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    # def play(self):
    #     self.playthread = QThread()
    #     if(self.format == ".wav"):
    #         from wavplay import wavplay
    #         self.worker = wavplay(self.title, self.year, self.url, self.artist, self.genre, self.format)
    #         self.worker.moveToThread(self.playthread)
    #         self.playthread.started.connect(self.worker.playwav)
    #     if(self.format == ".mp3"):
    #         from mp3play import mp3play
    #         self.worker = mp3play(self.title, self.year, self.url, self.artist, self.genre, self.format, self.playthread)
    #         self.worker.moveToThread(self.playthread)
    #         self.playthread.started.connect(self.worker.playmp3)   
    #         # self.playthread.pauseSignal.connect(self.worker.pausemp3)  
    #         self.worker.pauseSignal.connect(self.worker.pausemp3)  
    #     if(self.format == ".mp4"):
    #         from mp4play import mp4play
    #         self.worker = mp4play(self.title, self.year, self.url, self.artist, self.genre, self.format)
    #         self.worker.moveToThread(self.playthread)
    #         self.playthread.started.connect(self.worker.playmp4)
        
    #     self.worker.finished.connect(self.playthread.quit)
    #     self.worker.finished.connect(self.worker.deleteLater)
    #     self.playthread.finished.connect(self.playthread.deleteLater)

    #     self.playthread.start() 

    #     self.but_play.setEnabled(False)
    #     self.playthread.finished.connect(
    #         lambda: self.but_play.setEnabled(True)
    #     )

    # def play(self):
        # # from threading import Thread
        # import threading
        # if(self.format == ".mp3"):
        #     from mp3play import mp3play
        #     self.mp3 = mp3play(self.title, self.year, self.url, self.artist, self.genre, self.format)
        #     self.thread = threading.Thread(target = self.mp3.playmp3, args=(),daemon = True)
        #     self.thread.start()
        # if(self.format == ".wav"):
        #     from wavplay import wavplay
        #     self.wav = wavplay(self.title, self.year, self.url, self.artist, self.genre, self.format)
        #     self.thread = threading.Thread(target = self.wav.playwav, args=(),daemon = True)
        #     self.thread.start()
        # if(self.format == ".mp4"):
        #     from mp4play import mp4play
        #     self.mp4 = mp4play(self.title, self.year, self.url, self.artist, self.genre, self.format)
        #     self.thread = threading.Thread(target = self.mp4.playmp4, args=(),daemon = True)
        #     self.thread.start()

    def play(self):
        # from threading import Thread
        if(self.format == ".mp3"):
            from mp3play import mp3play
            self.mp3 = mp3play(self.title, self.year, self.url, self.artist, self.genre, self.format)
            print(self.mp3)
            self.thread = multiprocessing.Process(target = self.mp3.playmp3, args=(),daemon = True)
            self.thread.start()
        if(self.format == ".wav"):
            from wavplay import wavplay
            self.wav = wavplay(self.title, self.year, self.url, self.artist, self.genre, self.format)
            print(self.wav)
            self.thread = multiprocessing.Process(target = self.wav.playwav, args=(),daemon = True)
            self.thread.start()
        if(self.format == ".mp4"):
            from mp4play import mp4play
            self.mp4 = mp4play(self.title, self.year, self.url, self.artist, self.genre, self.format)
            print(self.mp4)
            self.thread = multiprocessing.Process(target = self.mp4.playmp4, args=(),daemon = True)
            self.thread.start()

    def pause(self):
        pass
        # self.worker.pauseSignal.emit()
        # self.worker.stop()
        # self.playthread.stop()
        # self.worker.pausemp3()
        # self.worker.pauseSignal.emit()
        # if(self.format == ".mp3"):
        #     if self.but_pause.isChecked():
        #         self.worker.pausemp3()
        #     else:
        #         self.worker.unpausemp3()
        # if(self.format == ".wav"):
        #     if self.but_pause.isChecked():
        #     # from wavplay import wavplay
        #         self.wav.pausewav()
        # if(self.format == ".mp4"):
        #     if self.but_pause.isChecked():
        #     # from mp4play import mp4play
        #         self.mp4.pausemp4()

    def replay(self):
        self.thread.terminate()    
        if(self.format == ".mp3"):
            from mp3play import mp3play
            self.mp3 = mp3play(self.title, self.year, self.url, self.artist, self.genre, self.format)
            self.thread = multiprocessing.Process(target = self.mp3.replaymp3, args=(),daemon = True)
            self.thread.start()
        if(self.format == ".wav"):
            from wavplay import wavplay
            self.wav = wavplay(self.title, self.year, self.url, self.artist, self.genre, self.format)
            print(self.wav)
            self.thread = multiprocessing.Process(target = self.wav.replaywav, args=(),daemon = True)
            self.thread.start()
        if(self.format == ".mp4"):
            from mp4play import mp4play
            self.mp4 = mp4play(self.title, self.year, self.url, self.artist, self.genre, self.format)
            print(self.mp4)
            self.thread = multiprocessing.Process(target = self.mp4.replaymp4, args=(),daemon = True)
            self.thread.start()
        
        # self.worker.finished = 1
        # self.playthread.started.connect(self.worker.replaymp3)
        # self.playthread.start()
        # self.worker.replaymp3()
        # self.playthread.terminate()
        # self.playthread = QThread()
        # if(self.format == ".wav"):
        #     from wavplay import wavplay
        #     self.worker = wavplay(self.title, self.year, self.url, self.artist, self.genre, self.format)
        #     self.worker.moveToThread(self.playthread)
        #     self.playthread.started.connect(self.worker.replaywav)
        # if(self.format == ".mp3"):
        #     from mp3play import mp3play
        #     self.worker = mp3play(self.title, self.year, self.url, self.artist, self.genre, self.format)
        #     self.worker.moveToThread(self.playthread)
        #     self.playthread.started.connect(self.worker.replaymp3)        
        # if(self.format == ".mp4"):
        #     from mp4play import mp4play
        #     self.worker = mp4play(self.title, self.year, self.url, self.artist, self.genre, self.format)
        #     self.worker.moveToThread(self.playthread)
        #     self.playthread.started.connect(self.worker.replaymp4)
        # self.worker.finished.connect(self.playthread.quit)
        # self.worker.finished.connect(self.worker.deleteLater)
        # self.playthread.finished.connect(self.playthread.deleteLater)
        # self.playthread.start()
        # self.thread.terminate()
        # import multiprocessing
        # if(self.format == ".mp3"):
        #     # from mp3play import mp3play
        #     # self.mp3 = mp3play(self.title, self.year, self.url, self.artist, self.genre, self.format)
        #     # self.mp3.replaymp3()
        #     self.thread = multiprocessing.Process(target = self.mp3.replaymp3, args=(),daemon = True)
        #     self.thread.start()
        # if(self.format == ".wav"):
        #     from wavplay import wavplay
        #     self.wav = wavplay(self.title, self.year, self.url, self.artist, self.genre, self.format)
        #     # self.wav.replaywav()
        #     self.thread = multiprocessing.Process(target = self.wav.replaywav, args=(),daemon = True)
        #     self.thread.start()
        # if(self.format == ".mp4"):
        #     from mp4play import mp4play
        #     self.mp4 = mp4play(self.title, self.year, self.url, self.artist, self.genre, self.format)
        #     # self.mp4.replaymp4()
        #     self.thread = multiprocessing.Process(target = self.mp4.replaymp4, args=(),daemon = True)
        #     self.thread.start()

    def load(self):
        self.title = self.inp_title.text()
        self.year = self.inp_year.text()
        self.artist = self.inp_artist.text()
        self.genre = self.inp_genre.text()
        self.url = self.inp_url.text()
        self.format = self.formatMenu.currentText()
        print("Media file has been loaded.")

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lab_med_player.setText(_translate("MainWindow", "Media Player"))
        self.lab_title.setText(_translate("MainWindow", "Input Title:"))
        self.lab_year.setText(_translate("MainWindow", "Input Year:"))
        self.lab_artist.setText(_translate("MainWindow", "Input Artist:"))
        self.lab_genre.setText(_translate("MainWindow", "Input Genre:"))
        self.lab_url.setText(_translate("MainWindow", "Input URL:"))
        self.but_play.setText(_translate("MainWindow", "Play"))
        self.but_pause.setText(_translate("MainWindow", "Pause"))
        self.but_replay.setText(_translate("MainWindow", "Replay"))
        self.but_load.setText(_translate("MainWindow", "Load"))
        self.formatMenu.setItemText(0, _translate("MainWindow", ".wav"))
        self.formatMenu.setItemText(1, _translate("MainWindow", ".mp3"))
        self.formatMenu.setItemText(2, _translate("MainWindow", ".mp4"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
