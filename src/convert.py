import os
import pathlib
import constants
import shutil

def copy_dirs(gamepath, gameoutput):
    dest_filename = gameoutput
    if os.path.isdir(dest_filename):
        #shutil.rmtree(dest_filename)
        #os.mkdir(dest_filename)
        print("NWJS found")
    else:
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

def copy_files(gamepath, gameoutput):
    dest_filename = gameoutput
    for file in constants.rpgm_files:
        source = os.path.join(gamepath, file)
        dest = os.path.join(dest_filename, file)
        if not os.path.isfile(source):
            print("Missing file: ", source)
            continue
        print("Copying file: ", file)
        shutil.copyfile(source, dest)

def convert(gamepath, gameoutput):
    game = gamepath
    copy_dirs(game, gameoutput)
    copy_files(game, gameoutput)