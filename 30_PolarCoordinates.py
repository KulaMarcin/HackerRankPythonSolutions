from cmath import phase
from pip._vendor.distlib.compat import raw_input

complex_number = raw_input()
print(abs(complex(complex_number)))
print(phase((complex(complex_number))))