import requests


def download_file(url, filename, output_dir):
    with requests.get(url, stream=True) as r:
        if r.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        else:
            print("empty file downloaded")
