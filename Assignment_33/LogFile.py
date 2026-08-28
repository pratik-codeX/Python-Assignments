import os
import sys
from pathlib import Path
from datetime import datetime


def Log():
    fobj = None
    date = datetime.now()
    date = date.strftime("%d_%m_%Y_%H_%M_%S.log")
  
    if os.path.isdir("./Marvellous"):
        pass
    else:
        os.mkdir("Marvellous")

    return open(f"./Marvellous/DuplicateRemovalLog_{date}","+a")