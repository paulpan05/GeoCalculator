import sys
import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python36\tcl\tk8.6'

buildOptions = {"include_files": [r'C:\Program Files\Python36\DLLs\tcl86t.dll',
                                  r'C:\Program Files\Python36\DLLs\tk86t.dll',
                                  r'1494497497_globe-01.ico',
                                  r'Geography.png',
                                  r'mapkey.txt',
                                  r'timekey.txt',
                                  r'earth-png-25606.png']
                }

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable(r'GeoCalculator.pyw', base=base, icon=r'1494497497_globe-01.ico')
]


setup(name='GeoCaculator',
      version='1.0',
      description='GeoCalculator: A Useful Travel Companion',
      options=dict(build_exe=buildOptions),
      executables=executables
      )
