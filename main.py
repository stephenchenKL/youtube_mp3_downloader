from pytube import YouTube
import os
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(480, 140))
        self.setWindowTitle("Youtube mp3 convertor")

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Youtube URL:')
        self.line = QLineEdit(self)

        self.line.move(120, 20)
        self.line.resize(320, 32)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('Download', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(120,32)
        pybutton.move(10, 60)

    def clickMethod(self):
        print('Processing ' + self.line.text())
        yt = YouTube(self.line.text(), use_oauth=True, allow_oauth_cache=True)
        yt.streams.get_audio_only()
        video = yt.streams.filter(only_audio=True).first()
        destination = '.'
        # download the file
        out_file = video.download(output_path=destination)
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # result of success
        print(yt.title + " has been successfully downloaded.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )



# url input from user
yt = YouTube(
    str("https://www.youtube.com/watch?v=wMQQN4LZaDs"))

# extract only audio
print("extract only audio")
yt.streams.get_audio_only()
video = yt.streams.filter(only_audio=True).first()

# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")