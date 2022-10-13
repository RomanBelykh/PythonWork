import inp
import imp
import exp
import logg

def start():
    if inp.mod() == '1':
        info = inp.exp()
        exp.expp(info)
        logg.log_info(info)
    else:
        info = inp.inpp()
        imp.impo(info)
        logg.log_info(info)