from medplayer import Ui_MainWindow
# from PyQt5.QtCore import QObject, pyqtSignal
import pygame
import urllib.request
import ssl

class mp3play(Ui_MainWindow):

    # finished = pyqtSignal()
    # pauseSignal = pyqtSignal()

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
    
    # def play(self):
    #     import threading
    #     thread = threading.Thread(target = self.playmp3(),args=(),daemon = True)
    #     thread.start()

    
    def playmp3(self):
        print("Playing mp3 file...")
        pygame.mixer.init()
        pygame.mixer.music.load(self.filename)
        pygame.mixer.music.play()
        while(pygame.mixer.music.get_busy()):
            pygame.time.Clock().tick(10)

        # if(self.pause == True):
        #     pygame.mixer.music.play()
        # else:
        #     pygame.mixer.music.pause()
        # count = 0
        # while(self.pause == True):
        #     if(self.pause == True and count == 0):
        #         pygame.mixer.music.play()
        #         count += 1
        #     elif(self.pause == False):
        #         pygame.mixer.init()
        #         pygame.mixer.music.load(self.filename)
        #         pygame.mixer.music.pause()

        # while(self.pause):
            # while (pygame.mixer.music.get_busy()): 
            #     pygame.time.Clock().tick(10)

    def pausemp3(self):
        print("Paused...")
        self.pause = False
        # print(self.pause)
        # pygame.mixer.music.pause()
        print("paused?")


    def unpausemp3(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()
        
    def replaymp3(self):
        print("Replaying mp3 file...")
        pygame.mixer.init()
        pygame.mixer.music.load(self.filename)
        pygame.mixer.music.play()
        while(pygame.mixer.music.get_busy()):
            pygame.time.Clock().tick(10)

        # pygame.mixer.init()
        # pygame.mixer.music.load(self.filename)
        # pygame.mixer.music.rewind()
        
        # pygame.mixer.init()
        # pygame.mixer.music.unload()
        # pygame.mixer.music.load(self.filename)
        # pygame.mixer.music.play()
        # while pygame.mixer.music.get_busy(): 
        #     pygame.time.Clock().tick(10)
        # pygame.event.wait()
        # pygame.mixer.init()
        # pygame.mixer.music.load(self.filename)
        # pygame.mixer.music.play()
        # while pygame.mixer.music.get_busy(): 
        #     pygame.time.Clock().tick(10)
        # pygame.event.wait()
        # pygame.mixer.music.rewind()
        # self.playmp3()
        # self.Ui_MainWindow.play()