import subprocess
import sys

from .util import Conf
from .util import read_json

c = Conf()

def rm_venv(fp) :
    """ remove virtualenv with pyenv if specified in the config file """
    j = read_json(fp)
    if j[c.rm_venv] :
        cmd = ['pyenv' , 'virtualenv-delete' , '-f']
        cmd += [j[c.pkg] + '.' + j[c.py_ver]]

        subprocess.run(cmd)

if __name__ == '__main__' :
    conf_fn = sys.argv[1]
    rm_venv(conf_fn)