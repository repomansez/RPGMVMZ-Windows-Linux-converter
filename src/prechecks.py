import os
import pathlib

def check_rpgm_version(gamepath):
    package_file = os.path.join(gamepath, "package.json")
    mv_file = os.path.join(gamepath, "www")
    mz_dir = os.path.join(gamepath, "js")
    print(package_file, mv_file)
    if not os.path.isfile(package_file):
        print("Not RPGM directory")
        return "not"
    if os.path.isfile(mv_file):
        print("RPG MV detectesd")
        return "mv"
    elif os.path.isdir(mz_dir):
        print("RPG MZ detected.")
        return "mz"

def check_dirs(gamepath, gameoutput):
    print("CHECK SAME: ", gamepath, gameoutput)
    output_empty = len(os.listdir(gameoutput))
    if gamepath == gameoutput:
        return "same"
    if output_empty != 0:
        return "notempty"
def check(gamepath, gameoutput):
    version_status = check_rpgm_version(gamepath)
    dir_status = check_dirs(gamepath, gameoutput)
    return version_status, dir_status
    