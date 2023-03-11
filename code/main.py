import sys
import random
from PyQt5 import QtMultimediaWidgets, QtMultimedia, QtCore
from PyQt5.QtWidgets import *
import threading


    
class show_dialog(QMainWindow): 
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Дополнительное окно')
        self.resize(200, 150)

        self.count = 0
        while True:
            self.count += 1
            x = random.randint(0, QApplication.desktop().screenGeometry().width() - self.width())
            y = random.randint(0, QApplication.desktop().screenGeometry().height() - self.height())
            self.setGeometry(x,y,200,150)
            reply = QMessageBox.question(self, 'Message', f"Счет {self.count}",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)



            

        


class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Title')    
        self.resize(400, 300)
        self.move(0, 0)
        self.ledText = QLineEdit('text', self)

        self.btnUpdate = QPushButton('update window', self)
        self.btnUpdate.clicked.connect(self.ev_btn_click)


    
        

    def video_player(self):
        movie_file = QtCore.QUrl.fromLocalFile('bad_gapple.mp4')
        vid_media = QtMultimedia.QMediaContent(movie_file)

        # create video widget
        self.videoWidget = QtMultimediaWidgets.QVideoWidget()
        self.videoWidget.setMinimumSize(QApplication.desktop().screenGeometry().width(),QApplication.desktop().screenGeometry().height())

        # create media player object   (video widget goes in media player)
        self.mediaPlayer = QtMultimedia.QMediaPlayer(None, QtMultimedia.QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        # playlist
        self.playlist = QtMultimedia.QMediaPlaylist()
        self.playlist.setCurrentIndex(0)
        self.playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
        self.playlist.addMedia(vid_media)
        # add content to media player
        self.mediaPlayer.setPlaylist(self.playlist)
        self.mediaPlayer.play()
        self.setCentralWidget(self.videoWidget)

    def ev_btn_click(self):
        res = QMessageBox.information(self, 'Боже чел', 'Ты зачем нажал?')
        if res == 1024:
            pass
        resqt = QMessageBox.question(self, 'Выбор - дело человека', 'Выберите' , QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if resqt == QMessageBox.Yes:
            resqt = QMessageBox.information(self, 'Ваш выбор это OSU', 'Наберите 100 очков!')
            
            thread2 = threading.Thread(target=self.video_player())
            show_dialog()
            
            
            
            
            
            
            
            
            
            

    


if __name__  == "__main__":  
    app = QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())
