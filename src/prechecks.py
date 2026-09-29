from os import listdir, path
import json


def check_rpgm_version(gamepath):
    package_file = path.join(gamepath, "package.json")
    mv_file = path.join(gamepath, "www", "package.json")
    print("MV FILE: ", mv_file)
    mz_dir = path.join(gamepath, "js")
    print(package_file, mv_file)
    if not path.isfile(package_file):
        print("Not RPGM directory")
        return "not"
    if path.isfile(mv_file):
        print("RPG MV detectesd")
        return "MV"
    elif path.isdir(mz_dir):
        print("RPG MZ detected.")
        return "MZ"


def check_dirs(gamepath, gameoutput):
    print("CHECK SAME: ", gamepath, gameoutput)
    output_empty = len(listdir(gameoutput))
    if gamepath == gameoutput:
        return "same"
    if output_empty != 0:
        return "notempty"

def check_empty_json_name(gamepath):
    json_file = path.join(gamepath, "package.json")
    with open(json_file, "r+") as packagejson:
        data = json.load(packagejson)
        print(data)
        if "name" not in data or data["name"] is None or data["name"] == "":
            print("JSON DATA NAME: ", data["name"])
            data["name"] = "whydodevsleavethisnullsmh"
            packagejson.seek(0)
            json.dump(data, packagejson, indent=4)
            packagejson.truncate()
        else:
            print("DATA CONDITION FAILED!!!!!!")


def check(gamepath, gameoutput):
    version_status = check_rpgm_version(gamepath)
    check_empty_json_name(gamepath)
    dir_status = check_dirs(gamepath, gameoutput)
    return version_status, dir_status
