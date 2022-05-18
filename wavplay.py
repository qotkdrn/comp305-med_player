from medplayer import Ui_MainWindow
import pygame
import urllib.request
import ssl

class wavplay(Ui_MainWindow):

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
    
    def playwav(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)
        pygame.event.wait()

    def pausewav(self):
        pass
        # if self.but_pause.isChecked():
        #     pygame.mixer.music.pause
        # else:
        #     pygame.mixer.music.unpause

    def replaywav(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)
        pygame.event.wait()
