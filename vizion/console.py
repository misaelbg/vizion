#!/usr/bin/python
import argparse

from lib import Detect
from lib.utils import Enums
from yaspin import yaspin
from colorama import colorama_text, Fore
from pyfiglet import Figlet


def main():
    """automatically reset stdout"""
    with colorama_text():
        logo = Figlet(font='standard')
        print(Fore.BLUE + logo.renderText('VIZION'))
        print(Fore.GREEN + '"Artificial intelligence for computer vision!!"\n')

    parser = argparse.ArgumentParser(
        description="Object detection and recognition")
    parser.add_argument(
        "--image", help="Image object detection and classification")
    parser.add_argument(
        "--video", help="Video object detection and classification")
    parser.add_argument(
        "--detect", help="Label to detect in file")
    parser.add_argument(
        "--model", help="Pre trained model")

    args = parser.parse_args()

    if args.image:
        file_type = Enums.DETECT_FILE_TYPE_IMAGE
    elif args.video:
        file_type = Enums.DETECT_FILE_TYPE_VIDEO
    else:
        raise argparse.ArgumentTypeError('Input file type as required')

    if args.detect:
        detector = None
        input_file = args.image or args.video

        with yaspin(text="Object detection", color="cyan") as spinner:
            try:
                detector = Detect(args.model, file_type)
                spinner.write("✅ Starting object detection")

                results = detector.run(input_file)
                spinner.write("✅ Running detection in file [{}]".format(input_file))

                if not results:
                    raise Exception('No results for label ' + args.detect)

                spinner.ok("✅ Success:")
            except Exception as error:
                spinner.fail("💥 Failed:")
                print(Fore.RED, '--> Error:', str(error))
                exit

if __name__ == "__main__":
    main()
