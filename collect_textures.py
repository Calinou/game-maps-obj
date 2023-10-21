#!/usr/bin/env python3

import argparse
import os
import platform
import shutil


def main() -> None:
    # Enable ANSI escape code support on Windows 10 and later (for colored console output).
    # <https://bugs.python.org/issue29059>
    if platform.system().lower() == "windows":
        from ctypes import byref, c_int, windll  # type: ignore

        stdout_handle = windll.kernel32.GetStdHandle(c_int(-11))
        mode = c_int(0)
        windll.kernel32.GetConsoleMode(c_int(stdout_handle), byref(mode))
        mode = c_int(mode.value | 4)
        windll.kernel32.SetConsoleMode(c_int(stdout_handle), mode)

    parser = argparse.ArgumentParser(
        description="Collects textures referenced by a OBJ material file (.mtl) to copy into the specified path.",
    )
    parser.add_argument("mtl", help="path to .mtl file")  # Positional argument.
    parser.add_argument(
        "-i",
        "--input",
        help="input folder path (path to Sauerbraten/Red Eclipse/Tesseract installation folder)",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="output folder path (will be created recursively if it doesn't exist)",
        required=True,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="print a message for every detected material texture",
    )

    args = parser.parse_args()

    files_to_copy = []
    header_length = len("map_Kd ")
    with open(args.mtl, encoding="utf-8") as file:
        for line in file.readlines():
            if line.startswith("map_Kd"):
                file_to_copy = line[header_length:].strip("\n")
                files_to_copy.append(file_to_copy)
                os.makedirs(
                    os.path.join(args.output, os.path.dirname(file_to_copy)),
                    exist_ok=True,
                )

                input_file = os.path.join(args.input, file_to_copy)
                output_file = os.path.join(args.output, file_to_copy)

                shutil.copyfile(input_file, output_file)
                if args.verbose:
                    print(
                        f"Copying \x1b[4m{input_file}\x1b[0m to \x1b[96;4m{output_file}\x1b[0m..."
                    )


if __name__ == "__main__":
    main()
