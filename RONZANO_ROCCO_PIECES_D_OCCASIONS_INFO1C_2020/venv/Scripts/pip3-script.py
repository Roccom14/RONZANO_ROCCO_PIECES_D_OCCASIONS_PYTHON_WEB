#!C:\Users\rocco\Documents\GitHub\RONZANO_ROCCO_PIECES_D_OCCASIONS_PYTHON_WEB\RONZANO_ROCCO_PIECES_D_OCCASIONS_INFO1C_2020\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==19.0.3','console_scripts','pip3'
__requires__ = 'pip==19.0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip==19.0.3', 'console_scripts', 'pip3')()
    )
