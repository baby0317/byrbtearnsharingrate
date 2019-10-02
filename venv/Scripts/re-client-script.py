#!D:\pycharm\PycharmProjects\untitled\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 're-client==0.0.6.post5','console_scripts','re-client'
__requires__ = 're-client==0.0.6.post5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('re-client==0.0.6.post5', 'console_scripts', 're-client')()
    )
