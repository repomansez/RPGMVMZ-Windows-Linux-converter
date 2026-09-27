import os
import pathlib
import constants
import shutil

def copy_files(gamepath):
    dest_filename = "converted-game"
    shutil.rmtree(dest_filename)
    os.mkdir(dest_filename)
    print("path: " + gamepath)
    
    for dir in constants.rpgm_dirs:
        source = os.path.join(gamepath, dir)
        dest = os.path.join(dest_filename, dir)
        if not os.path.isdir(source):
            print(dest, source)
            print("Skipping missing directory:", dir)
            #time.sleep(1)
            continue
        print("Copying directory:" + dir)
        shutil.copytree(source, dest)


def convert(gamepath):
    game = gamepath
    copy_files(game)