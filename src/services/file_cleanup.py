from os import path, remove, chdir
from time import sleep
import glob

cwd = path.dirname(path.realpath(__file__))

chdir(f"{cwd}/../tmp")

while True:
    sleep(3600)
    # sleep(20)
    try:
        files=glob.glob('*.pdf')
        for file in files:
            remove(file)
    except:
        pass
