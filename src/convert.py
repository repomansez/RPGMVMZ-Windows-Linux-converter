import os
import urllib
from getnwjs import download_helper
from shutil import copyfile, copytree

import constants


def copy_dirs(gamepath, gameoutput, version):
    dest_filename = gameoutput
    if os.path.isdir(dest_filename):
        # shutil.rmtree(dest_filename)
        # os.mkdir(dest_filename)
        print("NWJS found")
    else:
        os.mkdir(dest_filename)
    print("path: " + gamepath)

    for dir in constants.rpgm_dirs:
        if(version == "MZ"):
            source = os.path.join(gamepath, dir)
            dest = os.path.join(dest_filename, dir)
        else:
            source = os.path.join(gamepath, "www", dir)
            dest = os.path.join(dest_filename, "www", dir)
            
        if not os.path.isdir(source):
            print(dest, source)
            print("Skipping missing directory:", dir)
            # time.sleep(1)
            continue
        print("Copying directory:" + dir)
        copytree(source, dest)

def get_scripts(gameoutput, version):
    print("hi")
    for url in constants.script_links:
        filename = os.path.basename(url)
        output_path = os.path.join(gameoutput, filename)
        print("Downloading file: ", filename)
        download_helper(url, filename)
        copyfile(filename, output_path)
        
    # for url in constants.script_links:
    #     filename = os.path.basename(url)
    #     if ( version == "MZ"):
    #         output_path = os.path.join(gameoutput, filename)
    #     else:
    #         output_path = os.path.join(gameoutput, "www", filename)
    #     print("Downloading script: ", filename)
    #     request = urllib.request.Request(  # NWJS doesnt like python scripts downloading their shit so lets trick them into thinking we're firefox hehehehehe
    #         url, headers={"User-Agent": "Mozilla/5.0"}
    #         )

    #     with urllib.request.urlopen(request) as response, open(output_path, "wb") as file:
    #         file.write(response.read())
    #         #copyfile(script, gameoutput)
    
    
def copy_files(gamepath, gameoutput, version):
    dest_filename = gameoutput
    for file in constants.rpgm_files:
        if (version == "MZ") or (file == "package.json"):
            source = os.path.join(gamepath, file)
            dest = os.path.join(dest_filename, file)          
        else:
            source = os.path.join(gamepath, "www", file)
            dest = os.path.join(dest_filename, "www", file)
        if not os.path.isfile(source):
            print("Missing file: ", source)
            continue
        print("Copying file: ", file)
        copyfile(source, dest)


def convert(gamepath, gameoutput, version):
    game = gamepath
    copy_dirs(game, gameoutput, version)
    copy_files(game, gameoutput, version)
    get_scripts(gameoutput, version)