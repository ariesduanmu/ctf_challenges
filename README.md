# ctf_challenges
All kinds of ctf challenges


### gdb skills

#### BoF overwrite offset

`pattern create <pattern length>`

in 32bits: it is easy just `pattern offset <eip>`

in 64bits: `pattern offset <x/xg $rsp>`

#### get rop chain by tools

> r2 `r2 <file>` -> `/R pop rdi`

### get function address

`readelf -s <file> | grep <function>`

### find "/bin/sh" in file

> `break main`
> `run`
> `print system`
> `print __libc_start_main`
> `find <__libc_start_main address>, +2200000, "/bin/sh"`
