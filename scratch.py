from cv2 import VideoCapture
from pygame import mixer
import moviepy
import urllib.request
import ssl
import urllib.parse
import pyglet
import time

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://ncs.io/track/download/9f63f57e-aaf5-48c4-bcb7-cf4c5d329925"
url2 = "https://www.midiworld.com/download/3590"
url3 = "https://bigsoundbank.com/UPLOAD/wav/0253.wav"
mp4file = '/Users/alexsbae/Documents/Comp305/comp305proj/file_example_MP4_1280_10MG.mp4'
filename = urllib.request.urlretrieve(url2, '/Users/alexsbae/Documents/Comp305/comp305proj/url')
mixer.init()
mixer.music.load(filename[0])
mixer.music.play()
print("1")
mixer.music.pause()
# print("1")

mixer.music.unpause()
# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load(filename)
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy(): 
#     pygame.time.Clock().tick(10)
# pygame.event.wait()

# from moviepy.editor import *

 
# clip = VideoFileClip('file_example_MP4_1280_10MG.mp4')
# clip.preview()
 
# pygame.quit()

#########################
# FPS = 60  

# pygame.init()  
# pygame.mixer.quit()  
# clock = pygame.time.Clock()  
# movie = pygame.movie.Movie(mp4file)  
# screen = pygame.display.set_mode(movie.get_size())  
# movie_screen = pygame.Surface(movie.get_size()).convert()  
# movie.set_display(movie_screen)  
# movie.play()  
# playing = True  
# while playing:  
#     for event in pygame.event.get():  
#         if event.type == pygame.QUIT:  
#             movie.stop()  
#             playing = False  
# screen.blit(movie_screen,(0,0))  
# pygame.display.update()  
# clock.tick(FPS)  
# pygame.quit()

####################
# import cv2

# cap = VideoCapture('sample.mp4')
# if(cap.isOpened() == False):
#     print("Error opening mp4 video")
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if(ret == True):
#         cv2.imshow('frame', frame)
#         if(cv2.waitKey(25) == ord('q')):
#             break
#     else:
#         break

# vid_path='sample.mp4' # Name of the video
# window=pyglet.window.Window()
# player = pyglet.media.Player()
# source = pyglet.media.StreamingSource()
# MediaLoad = pyglet.media.load(vid_path)

# player.queue(MediaLoad)
# player.play()

# @window.event
# def on_draw():
#     if player.source and player.source.video_format:
#         player.get_texture().blit(50,50)


# pyglet.app.run()
# cap.release()
# cv2.destroyAllWindows()



        #http://ncs.io/candyland url for tobu:candyland
        #https://ncs.io/candyland
        #https://ncs.io/track/download/9f63f57e-aaf5-48c4-bcb7-cf4c5d329925
        #Tobu - Candyland [NCS Release].mp3