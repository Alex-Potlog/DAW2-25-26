import shutil
import sys
import os

def copiaDades(origen, desti):
    if not os.path.exists(origen):
        raise FileNotFoundError
    
    if not os.path.exists(desti):
        os.makedirs(desti)
    
    destinament = os.path.join(desti, "copiaSeguretat")
    
    shutil.copy2(origen, destinament)
    print(f"Creat Arxiu {destinament}")


if __name__ == "__main__":
    copiaDades(sys.argv[1], sys.argv[2])