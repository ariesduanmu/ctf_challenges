* disassemble main

```
define hook-stop
> x/1i $eip
> x/8wx $esp
> end
```
* si(debug step by step)

* save input in to a file, such as:
```
python -c "print 'A' * 80" > /tmp/input_file
```
* then as input in debug
```
r < /tmp/input_file
```

* get registors information
```
info registers
```

* interrupt 3-trap to debugger `\xcc`

* turn on the `core dump`
```
ulimit -c unilimited
echo "/tmp/core.%t" > /proc/sys/kernal/core_pattern
```
