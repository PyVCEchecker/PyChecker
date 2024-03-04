import argparse
from gooey import Gooey
from gooey import GooeyParser

@Gooey
def initOptParser():
    defaultFolderPath = "./TEST"
    archivePath = "./Archives"

    parser = argparse.ArgumentParser(description="Copy files to specified location")
    parser.add_argument('files', metavar='file', type=str, nargs='+',
                         help='file(s) or directory that you wish to copy' )
    # parser.add_argument('-p', '--path', metavar='path',dest='path',  type=str,
    #                     help='Path which will be considered as root of all projects. Default is currently : ' + defaultFolderPath,
    #                     default=defaultFolderPath)
    # parser.add_argument('projectName', metavar='projectName', type=str,
    #                     help='The project you wish to retrieve/add files to/from.')
    # parser.add_argument('-v', '--version', metavar='versionName', type=str,
    #                     help='The name of the directory which will be created during an update. By default, this will be : DATE_TIME.')
    # parser.add_argument('-o', '--overwrite',
    #                     help='Overwrites the files in the current version of specified project. (no new directory creation)', action="store_true")
    # parser.add_argument('-m', '--message', metavar='logMessage', type=str, help='Use to specify a log message which will be put in a .txt file. (default : commit.txt)')
    # parser.add_argument('-g', '--get', dest='method', action='store_const', help='Retrieve files from project (last version by default)')
    # parser.add_argument('-l', '--lock', action="store_true",
    #                     help='Locks the current project. Can be overriden/ignored on demand. (Will ask other users if they want to pull files)'+
    #                         'Unlocked when next push from the locking user is made')
    # parser.add_argument('user', metavar='userName', type=str, help='Specify your name.')
    # parser.add_argument('-a', '--archive', metavar='archivePath', type=str, help='Use to specify a directory which will be used as an archive. Current default is : ' + archivePath)
    # parser.add_argument('-s', '--store', metavar="destPath", help='Use to specify where you want the files retrieved from the project to be copied.')

    args = parser.parse_args()
    args.method() # Either get() or push(). For now i'm using two factice functions who just print their name.
    return (args)

if __name__ == '__main__':
  initOptParser()
