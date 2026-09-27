import pathlib
import os
import tarfile
import urllib.request
import shutil

############ TODO: a lot
def get_nwjs(version):
    nwjs_fulldir = f"nwjs-sdk-v{version}-linux-x64"
    nwjs_tarball = f"{nwjs_fulldir}.tar.gz"
    download_link = f"https://dl.nwjs.io/v{version}/{nwjs_tarball}"
    print(version, nwjs_fulldir, download_link, nwjs_tarball)

    if os.path.exists(nwjs_tarball):
        print("NWJS already downloaded")
        print("Extracting nwjs")
        shutil.rmtree("nwjs-extracted")
        extract_nwjs(nwjs_tarball)
    else:
        request = urllib.request.Request( # NWJS doesnt like python scripts downloading their shit so lets trick them into thinking we're firefox hehehehehe
            download_link,
            headers={"User-Agent": "Mozilla/5.0"}
        )
    
        print("Downloading nwjs")
        with urllib.request.urlopen(request) as response:
            with open(nwjs_tarball, "wb") as file:
                file.write(response.read())
        print("Extracting nwjs")
        extract_nwjs(nwjs_tarball)

def extract_nwjs(nwjs_tarball):
    print("Fulldir: " + nwjs_tarball)
    file = tarfile.open(nwjs_tarball)  # noqa: SIM115
    file.extractall('nwjs-extracted')
    file.close()