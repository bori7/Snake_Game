import sys
import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:/Users/MOSES/AppData/Local/Programs/Python/Python35-32/tcl/tcl8.6"
os.environ['TK_LIBRARY'] = "C:/Users/MOSES/AppData/Local/Programs/Python/Python35-32/tcl/tk8.6"


include_files = ['autorun.inf']
base = None

if sys.platform == "win32":
    base = "WIN32GUI"

executables = [cx_Freeze.Executable("BORI_SNAKE.py")]

cx_Freeze.setup(name="BORI_SNAKE",
                options={"build_exe":{"packages":["pygame"],
                         "include_files":["snakehead.png","snahead.png","snakeappl2.jfif","snahead22.png",
                                          "snakeappl2py.jpg","ssnakeapp1py.jpg"]}},
                description = "Bori's pygame game. LOL!!!",
                executables = [cx_Freeze.Executable("BORI_SNAKE.py",base = base)]
                )