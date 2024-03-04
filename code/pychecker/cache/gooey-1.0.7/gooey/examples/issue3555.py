import subprocess
import gooey
import sys

@gooey.Gooey()
def main():
    parser = gooey.GooeyParser()
    args = parser.parse_args()
    import sys
    print(sys.stdout)
    # startupinfo = subprocess.STARTUPINFO()
    # startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    print('begin')
    # process = subprocess.Popen(["ping", "127.0.0.1", "-n", "5", ],
    #                            shell=True, stdout=subprocess.PIPE,
    #                            stderr=subprocess.STDOUT)
    # print('process waiting')
    # process.communicate()
    # print(sys.stdout.read())
    print('done waiting')
    # if process.returncode != 0:
    #     print("An error occurred :", process.returncode)
    #     exit(1)

if __name__ == '__main__':
    main()