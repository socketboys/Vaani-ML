import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QComboBox
from PyQt5.QtCore import QUrl
from scripts import pipeline_class, pipeline_ai
from config import root_dir,languages
from pytube import YouTube
from ffmpeg import audio_extraction, mute, add_audio_track

input_dir = f"{root_dir}/input/"
output_dir = f"{root_dir}/audio/"
seamless = ["hindi", "bengali", "telugu"]



class AudioProcessingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Audio Processing App')

        self.lang_label = QLabel('Select Language:')
        self.lang_combobox = QComboBox(self)
        self.lang_combobox.addItems(['Hindi', 'Bengali', 'Telugu'])  

        self.audio_name_label = QLabel('Youtube Link:')
        self.audio_name_edit = QLineEdit(self)
        self.audio_name_label.setBuddy(self.audio_name_edit)

        self.process_button = QPushButton('Process Audio', self)
        self.process_button.clicked.connect(self.process_audio)

        # self.browse_button = QPushButton('Browse', self)
        # self.browse_button.clicked.connect(self.browse_audio_file)

        layout = QVBoxLayout()
        layout.addWidget(self.lang_label)
        layout.addWidget(self.lang_combobox)
        layout.addWidget(self.audio_name_label)
        layout.addWidget(self.audio_name_edit)
        # layout.addWidget(self.browse_button)
        layout.addWidget(self.process_button)

        self.setLayout(layout)

    def youtube_video_download(self, link):
        yt = YouTube(link)
        ys = yt.streams.get_highest_resolution()
        title = yt.title
        ys.download(f"{root_dir}/video/")
        
        path = f"{root_dir}/video/"+title
        # os.rename(path, path.strip())
        return title
        


    # def browse_audio_file(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     file_name, _ = QFileDialog.getOpenFileName(self, 'Open Audio File', '', 'Audio Files (*.wav *.mp3);;All Files (*)', options=options)
    #     if file_name:
    #         self.audio_name_edit.setText(file_name)

    def process_audio(self):
        selected_language = self.lang_combobox.currentText()
        # audio_name = self.audio_name_edit.text()
        link = self.audio_name_edit.text()
        input_video = self.youtube_video_download(link)
        audio_extraction(f"data/video/{input_video}.mp4", f"data/input/{input_video}.mp3")
        mute(f"data/video/{input_video}.mp4", f"data/video/{input_video}_muted.mp4")





        langs = [selected_language.lower()]  # Convert to lowercase to match with your seamless list

        try:
            if any(lang in seamless for lang in langs):
                pipeline_class.multi_process(input_dir, f"{input_video}.mp3", langs)
            else:
                pipeline_ai.multi_process(input_dir, f"{input_video}.mp3", langs)
            lang = langs[0]
            lang= languages[lang]["tts"]
            file = input_video
            file_name = f"{root_dir}/audio/" + file + "_" + lang[:-1] + ".wav"
            print(file_name)
            
        #     # Open the directory where the audio files are created
        #     output_directory = os.path.join(output_dir, audio_name)
        #     QUrl.fromLocalFile(output_directory).setScheme("file")
            # QDesktopServices.openUrl(QUrl.fromLocalFile(output_directory))
            
            add_audio_track(f"data/video/{input_video}_muted.mp4",file_name)
        except Exception as e:
            print(f'{e} thrown from pipeline')
            sys.exit(1)

    # def browse_audio_file(self):
    #     fname = QFileDialog.getOpenFileName(self, 'Open Audio File', '', 'Audio Files (*.wav *.mp3);;All Files (*)')
    #     if fname[0]: 
    #         self.audio_name_edit.setText(fname[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AudioProcessingApp()
    ex.show()
    sys.exit(app.exec_())
