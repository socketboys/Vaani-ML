root_dir = "E:/Vaani-ML/data"
# input_dir = "../../external/"
languages = {
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

AIBharat_TTS = {
    'assamese':'as', 
    'bengali':'bn', 
    'bodo':'brx', 
    'hinglish':'en+hi', 
    'gujrati':'gu', 
    'hindi':'hi', 
    'kannada':'kn', 
    'malyalam':'ml', 
    'manipuri':'mni', 
    'marathi':'mr', 
    'odiya':'or', 'punjabi':'pa',
    'rajasthani':'raj', 
    'tamil':'ta', 
    'telugu':'te'
}
gpu_devices = [0, 1, 2] 