import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QComboBox
from PyQt5.QtCore import QUrl
from scripts import pipeline_class, pipeline_ai
from config import root_dir

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

        self.audio_name_label = QLabel('Audio File Name:')
        self.audio_name_edit = QLineEdit(self)
        self.audio_name_label.setBuddy(self.audio_name_edit)

        # self.browse_button = QPushButton('Browse', self)
        # self.browse_button.clicked.connect(self.browse_audio_file)

        self.process_button = QPushButton('Process Audio', self)
        self.process_button.clicked.connect(self.process_audio)

        layout = QVBoxLayout()
        layout.addWidget(self.lang_label)
        layout.addWidget(self.lang_combobox)
        layout.addWidget(self.audio_name_label)
        layout.addWidget(self.audio_name_edit)
        # layout.addWidget(self.browse_button)
        layout.addWidget(self.process_button)

        self.setLayout(layout)

    # def browse_audio_file(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     file_name, _ = QFileDialog.getOpenFileName(self, 'Open Audio File', '', 'Audio Files (*.wav *.mp3);;All Files (*)', options=options)
    #     if file_name:
    #         self.audio_name_edit.setText(file_name)

    def process_audio(self):
        selected_language = self.lang_combobox.currentText()
        audio_name = self.audio_name_edit.text()

        languages = [selected_language.lower()]  # Convert to lowercase to match with your seamless list

        try:
            if any(lang in seamless for lang in languages):
                pipeline_class.multi_process(input_dir, audio_name, languages)
            else:
                pipeline_ai.multi_process(input_dir, audio_name, languages)
            
            # Open the directory where the audio files are created
            output_directory = os.path.join(output_dir, audio_name)
            QUrl.fromLocalFile(output_directory).setScheme("file")
            QDesktopServices.openUrl(QUrl.fromLocalFile(output_directory))
        except Exception as e:
            print(f'{e} thrown from pipeline')
            sys.exit(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AudioProcessingApp()
    ex.show()
    sys.exit(app.exec_())
