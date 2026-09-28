from pathlib import Path
import os
import tarfile
import urllib.request


############ TODO: a lot
def get_nwjs(version, gameoutput):
    nwjs_fulldir = f"nwjs-sdk-v{version}-linux-x64"
    nwjs_tarball = f"{nwjs_fulldir}.tar.gz"
    download_link = f"https://dl.nwjs.io/v{version}/{nwjs_tarball}"
    print(version, nwjs_fulldir, download_link, nwjs_tarball)

    if os.path.exists(nwjs_tarball):
        print("NWJS already downloaded")
        print("Extracting nwjs")
        extract_nwjs(nwjs_tarball, gameoutput)
    else:
        request = urllib.request.Request(  # NWJS doesnt like python scripts downloading their shit so lets trick them into thinking we're firefox hehehehehe
            download_link, headers={"User-Agent": "Mozilla/5.0"}
        )

        print("Downloading nwjs")
        with urllib.request.urlopen(request) as response, open(nwjs_tarball, "wb") as file:
            file.write(response.read())
        print("Extracting nwjs")
        extract_nwjs(nwjs_tarball, gameoutput)


def extract_nwjs(nwjs_tarball, gameoutput):
    extract_dir = gameoutput
    print("Fulldir: " + nwjs_tarball)
    with tarfile.open(nwjs_tarball) as file:

        def strip_top_directory(member, path):
            parts = Path(member.name).parts

            if len(parts) <= 1:
                return None

            member.name = str(Path(*parts[1:]))
            return member

        file.extractall(extract_dir, filter=strip_top_directory)
        file.close()
