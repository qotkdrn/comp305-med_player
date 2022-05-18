from medplayer import Ui_MainWindow
# from PyQt5.QtCore import QObject, pyqtSignal
import urllib.request
import cv2
from cv2 import VideoCapture
import ssl

class mp4play(Ui_MainWindow):
    #https://download.samplelib.com/mp4/sample-15s.mp4
    # finished = pyqtSignal()

    def __init__(self, title, year, url, artist, genre, format):
        # super(QObject, self).__init__()
        self.title = title
        self.year = year 
        self.url = url
        self.artist = artist 
        self.genre = genre
        self.format = format
        self.path = '/Users/alexsbae/Documents/Comp305/comp305proj/'
        ssl._create_default_https_context = ssl._create_unverified_context
        self.filename, header = urllib.request.urlretrieve(self.url, (self.path+self.title))

    def __str__(self):
        return (("Title: {}\nYear: {}\nURL: {} \nArtist: {} \nGenre: {} \nFormat: {} \
                ").format(self.title, self.year, self.url, self.artist, self.genre, self.format))
    
    def playmp4(self):
        cap = VideoCapture(self.filename)
        if(cap.isOpened() == False):
            print("Error opening mp4 video")
        while(cap.isOpened()):
            ret, frame = cap.read()
            if(ret == True):
                cv2.imshow('frame', frame)
                if(cv2.waitKey(25) == ord('q')):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

    def pausemp4(self):
        pass

    def replaymp4(self):
        cap = VideoCapture(self.filename)
        if(cap.isOpened() == False):
            print("Error opening mp4 video")
        while(cap.isOpened()):
            ret, frame = cap.read()
            if(ret == True):
                cv2.imshow('frame', frame)
                if(cv2.waitKey(25) == ord('q')):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
