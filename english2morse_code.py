#! /usr/bin/env python

import argparse

# A-Z , 0-9, space
english = "abcdefghijklmnopqrstuvwxyz0123456789 "

# A-Z , 0-9, space
international_morse_code = [
    ".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
    "-----",
    ".----",
    "..---",
    "...--",
    "....-",
    ".....",
    "-....",
    "--...",
    "---..",
    "----.",
    "/",
]


class Eng2Morse(object):
    """
    Translate English characters to Morse Code.
    """

    xlator__ = dict(zip((ord(c) for c in english), international_morse_code))

    def __getitem__(self, x):
        xlated = self.xlator__.get(x)
        return xlated


def main(args):
    user_message = args.infile.read().lower()
    translated = user_message.translate(Eng2Morse())
    print(translated)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Translate English to Morse Code")
    parser.add_argument(
        "infile",
        type=argparse.FileType("r"),
        help="File to read English message from.  Use `-` for STDIN.",
    )
    args = parser.parse_args()
    main(args)
