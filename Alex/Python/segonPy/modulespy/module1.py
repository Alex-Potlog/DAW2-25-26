import sys

def proba(name):
    if name != "":
        print(name)
    else:
        print("Fallo");
        
if __name__ == "__main__":
    proba(sys.argv[1])