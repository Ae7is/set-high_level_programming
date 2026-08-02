#!/usr/bin/python3
print(("{}" * 26).format(*(chr(i) for i in range(97, 123))), end="")
