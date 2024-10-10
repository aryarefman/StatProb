# interpreter dan compiler
# compiler lebih cepat jika dibandingkan dengan interpreter
import time
start_time = time.time()
print("Hello")
print("World")
print("Hello World")

print("Halo guys")
a = 10 # ini adalah comment juga
# ini adalah comment
"""tanda kutip tiga digunakan untuk comment multiline"""
print(a)
print(time.time() - start_time, "detik")
# kita bisa mengcompile python ke
# yang namanya bytecode
# cara mengcompile, buka terminal lalu tuliskan
# python -m py_compile Main.py