root_dir = "./data"
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
gpu_devices = [0, 1, 2] 