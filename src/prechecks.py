from os import listdir, path


def check_rpgm_version(gamepath):
    package_file = path.join(gamepath, "package.json")
    mv_file = path.join(gamepath, "www")
    mz_dir = path.join(gamepath, "js")
    print(package_file, mv_file)
    if not path.isfile(package_file):
        print("Not RPGM directory")
        return "not"
    if path.isfile(mv_file):
        print("RPG MV detectesd")
        return "mv"
    elif path.isdir(mz_dir):
        print("RPG MZ detected.")
        return "mz"


def check_dirs(gamepath, gameoutput):
    print("CHECK SAME: ", gamepath, gameoutput)
    output_empty = len(listdir(gameoutput))
    if gamepath == gameoutput:
        return "same"
    if output_empty != 0:
        return "notempty"


def check(gamepath, gameoutput):
    version_status = check_rpgm_version(gamepath)
    dir_status = check_dirs(gamepath, gameoutput)
    return version_status, dir_status
