import argparse
from typing import List
from scripts import pipeline_class
from config import root_dir

input_dir = f"{root_dir}/input/"

def main():
    parser = argparse.ArgumentParser(description="Process audio input with specified languages and gender.")
    parser.add_argument("--gender", required=True, help="Gender of the speaker")
    parser.add_argument("--lang", nargs="+", required=True, help="List of languages")
    parser.add_argument("--audioname", default="input.mp3", help="Name of the audio file")

    args = parser.parse_args()

    if len(args.lang) == 0:
        parser.error("No languages detected")

    try:
        pipeline_class.multi_process(input_dir, args.audioname, args.lang, args.gender)
    except Exception as e:
        print(f'{e} thrown from pipeline')
        exit(1)

if __name__ == "__main__":
    main()
