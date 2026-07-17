import argparse,os,json
from xtabay import Xtabayxc
ROJO = '\033[31m'
MG = '\033[35m'
AQUA = "\033[96;1m" 
VERDEL = "\033[32;1m" 
WHITEL = "\033[0;1m"  

parse = argparse.ArgumentParser()
parse.add_argument("--file",
                   "-fl",type=str, 
                   help="Ingrese la ruta de inyección",required=True, metavar="FILE DATA")
parse.add_argument("--name","-nm",type=str, help="Ingrese el nombre de salida de la presentación",required=True, metavar="NAME DATA")
args_ = parse.parse_args()


class ParserShow:
    def __init__(self):
        pass

    def lista_execute_pptx_commd(self,file:str, name:str):
        if os.path.isfile(file):
            with open(file,'r') as popen_of:
                valid_archv = file.split("/")
                json_set = json.load(popen_of)
                if "json" in valid_archv[-1].split("."):
                    Xtabayxc().inicie_data_pptx(json_set, name)
                else:
                    print("[!] EXTENSIÓN INVALIDA")
        else:
            print(f"{ROJO}[ERROR] {VERDEL}-> {ROJO}EL ARCHIVO NO EXISTE")

if __name__ == '__main__':
    if args_.file:
        ParserShow().lista_execute_pptx_commd(args_.file,args_.name)