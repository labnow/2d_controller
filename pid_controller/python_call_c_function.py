from ctypes import *
import pathlib

# cc -fPIC -shared -o example_c.so example_c.c

pwd = pathlib.Path(__file__).parent.resolve()
pwd2 = pwd.parent.resolve()
print(pwd2)
# so_file = "/home/gang/Documents/dspace_vecu/example_c.so"
so_file = pwd / "pid.so"

example_lib = cdll.LoadLibrary(so_file)

# func.restype = c_double


example_lib.lateral.restype = c_float
lib_return = example_lib.lateral()
print(type(lib_return), lib_return)
