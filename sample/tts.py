import subprocess

lang ='bn'
text = "তবুও আমার রোদ এক ভোরে জ্বলে উঠল,আমার কপালে সমস্ত বিজয়ী জাঁকজমক;কিন্তু বাইরে, অ্যালাক, সে কেবল এক ঘন্টা আমার ছিল,অঞ্চলের মেঘ এখন তাকে আমার কাছ থেকে মুছে ফেলেছে"

str = f'tts --text "{text}"     --config_path  models/v1/{lang}/fastpitch/config.json\
    --model_path models/v1/{lang}/fastpitch/best_model.pth \
    --out_path data/audio/output.wav \
    --speaker_idx "female" \
    --vocoder_path models/v1/{lang}/hifigan/best_model.pth \
    --vocoder_config_path models/v1/{lang}/hifigan/config.json'

subprocess.run(str)