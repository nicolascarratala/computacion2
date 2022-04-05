# COMPUTING II
## parallelism, concurrency

This is a project for the computing II course of Universidad de Mendoza.

## Notes:

```sh
--------------------------------------------------------------
user
--------------------------------------------------------------
aplications
--------------------------------------------------------------
Operative system (utilities, compilers, editors)
--------------------------------------------------------------
syscall (system call interface) - POSIX.1 - (API)
open(), read(), write(), fork()...
--------------------------------------------------------------
nucleus or kernel (I/O, memory, network, disk, ...)
drivers
--------------------------------------------------------------
hardware
--------------------------------------------------------------
```

Parallel and concurrency programming
IPC - inter process communication
- pipes, fifos, sockets unix, shm, ...
- sockets inet
- distributed process -> celery+redis
- docker

python3

```sh
--------------
Process: 
Priorities:

              |Tiempo real (RT)|                           |Ususario|
+-----------------------------------------------+------------------------+
0                                               100                      139
                                                0                        39 PRIority
                                                -20                      +19 NIce


Process creation: -> clonación

- fork()
- subprocess
- system
- pool
- multiprocessing
- threading

Process Table:

PID (process id), open files, memory ...
    -> memory map

+----------------------------+
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
+----------------------------+
|                            |
|                            |
|                            |
|                            |
|                            |
+----------------------------+

+----------------------------+
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
+----------------------------+
|                            |
|                            |
|                            |
|                            |
|                            |
+----------------------------+

daemon process (daemon)


```
