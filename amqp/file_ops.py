import os

import requests


def clean_residual_files(filename, extension):
    os.remove(f"/data/input/{filename}.{extension}")
    os.remove(f"/data/input/{filename}.srt")


def download_file(url, filename) -> str:
    with requests.get(url, stream=True) as r:
        if r.status_code == 200 and r.headers.get('Content-Length') != 0 and check_mime_type(
                r.headers.get('Content-Type')):
            with open(filename + get_extension(r.headers.get('Content-Type')), 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return get_extension(r.headers.get('Content-Type'))
        else:
            print("empty file downloaded")
            return ""


def check_mime_type(mime: str) -> bool:
    if (
            mime == "audio/mpeg" or mime == "audio/wav" or mime == "audio/webm" or mime == "audio/ogg" or mime == "audio/flac"
            or mime == "audio/aac" or mime == "audio/mp4" or mime == "audio/x-ms-wma" or mime == "audio/x-wav" or
            mime == "audio/x-aiff" or mime == "audio/x-matroska" or mime == "audio/x-pn-realaudio"):
        return True
    else:
        return False


def get_extension(mime: str) -> str:
    if mime == "audio/mpeg":
        return "mpeg"
    if mime == "audio/wav" or mime == "audio/x-wav":
        return "wav"
    if mime == "audio/mp4":
        return "mp4"
    return "wav"
