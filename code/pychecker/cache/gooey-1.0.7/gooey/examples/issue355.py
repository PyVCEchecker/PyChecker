import subprocess
import gooey
import sys

# @gooey.Gooey()
# def main():
#     parser = gooey.GooeyParser()
#     args = parser.parse_args()
#
#     # startupinfo = subprocess.STARTUPINFO()
#     # startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
#
#     process = subprocess.Popen(
#         ["ping", "127.0.0.1", "-n", "5", ],
#         # startupinfo=startupinfo
#     )
#     process.wait()
#     if process.returncode != 0:
#         print("An error occurred :", process.returncode)
#         exit(1)
#
# if __name__ == '__main__':
#     main()


import subprocess
import gooey

@gooey.Gooey()
def main():
    parser = gooey.GooeyParser()
    args = parser.parse_args()

    process = subprocess.Popen(["ping", "127.0.0.1", "-n", "5", ])
    process.wait()
    if process.returncode != 0:
        print("An error occurred :", process.returncode)
        exit(1)

if __name__ == '__main__':
    main()