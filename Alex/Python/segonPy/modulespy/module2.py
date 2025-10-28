import shutil
import sys
import os

def recarregaCopia(origen, desti):
    if not os.path.exists(origen):
        raise FileNotFoundError
    
    if not os.path.exists(desti):
        raise FileNotFoundError
    
    shutil.copy2(origen, desti)
    print(f"Creat Arxiu {desti}")


if __name__ == "__main__":
    recarregaCopia(sys.argv[1], sys.argv[2])