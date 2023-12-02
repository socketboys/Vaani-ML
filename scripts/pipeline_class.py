import logging
import warnings
import sys
import os
from re import search
import typer
import scipy
import torch
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from transformers import VitsModel, AutoTokenizer
from whisper import load_model, load_audio
from whisper.utils import get_writer
import ssl
from config import root_dir


class Pipeline:
    def __init__(self,output_path,audio_path,language):
        self.output_path = output_path
        self.audio_path = audio_path
        self.language = language
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.translated = list()
        self.languages = {
            "hindi": {
                "translate": "hi_IN",
                "tts": "facebook/mms-tts-hin"
            },
            "marathi": {
                "translate": "mr_IN",
                "tts": "facebook/mms-tts-mar"
            },
            "bengali": {
                "translate": "bn_IN",
                "tts": "facebook/mms-tts-ben"
            },
            "tamil": {
                "translate": "ta_IN",
                "tts": "facebook/mms-tts-tam"
            },
            "telugu": {
                "translate": "te_IN",
                "tts": "facebook/mms-tts-tel"
            },
            "kannada": {
                "translate": "kn_IN",
                "tts": "facebook/mms-tts-kan"
            }
        }
        
    