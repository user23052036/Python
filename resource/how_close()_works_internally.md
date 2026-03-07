
# 1. Python parses the arguments

`open()` first interprets the parameters.

Example:

```python
open(filename, mode, buffering, encoding, errors, newline)
```

For your case:

```
filename = "sample.txt"
mode = "w"
```

Mode `"w"` means:

* open for writing
* truncate file if it exists
* create file if it doesn't exist

---

# 2. Python calls the OS to open the file

Python does **not open files itself**.
It asks the operating system.

Internally Python calls the system call equivalent to:

```
open("sample.txt", O_WRONLY | O_CREAT | O_TRUNC)
```

These flags mean:

| Flag     | Meaning                         |
| -------- | ------------------------------- |
| O_WRONLY | write only                      |
| O_CREAT  | create file if it doesn't exist |
| O_TRUNC  | clear file contents             |

This is handled by the OS kernel.

---

# 3. OS creates a file descriptor

If successful, the OS returns a **file descriptor (FD)**.

Example:

```
fd = 3
```

Typical process descriptors:

```
0 → stdin
1 → stdout
2 → stderr
3 → first opened file
```

The OS now keeps an entry in its **open file table**.

This entry contains:

* file location on disk
* current offset
* permissions
* file pointer
* inode reference

---

# 4. Python wraps the descriptor into a file object

Python then builds a **high-level file object** around that descriptor.

Object hierarchy:

```
TextIOWrapper
     ↓
BufferedWriter
     ↓
FileIO
     ↓
OS file descriptor
```

So your variable actually stores something like:

```
<_io.TextIOWrapper name='sample.txt' mode='w'>
```

This layer handles:

* encoding (UTF-8)
* buffering
* newline handling
* high level methods

---

# 5. Buffer allocation

Python allocates a **memory buffer** (usually 8 KB).

So when you do:

```python
f.write("Hello world")
```

the text usually goes first to **memory buffer**, not disk.

Pipeline:

```
Python buffer
      ↓
OS kernel buffer
      ↓
filesystem
      ↓
disk
```

---

# 6. Writing data

When you call:

```python
f.write("Hello world")
```

Steps:

1. Python encodes string → bytes
2. Bytes go to Python buffer
3. When buffer fills or flush occurs
4. Python calls OS `write()` syscall
5. OS stores data in kernel buffer
6. OS eventually writes to disk

Return value `11` = number of characters written.

---

# 7. Closing the file

When you run:

```python
f.close()
```

Python does:

1. flush buffer
2. call OS `close(fd)`
3. OS releases file descriptor
4. remove entry from open file table

If you forget `close()`:

* Python closes automatically when program exits
* but it's **not safe in long-running programs**

---

# 8. Why `with open()` is better

```python
with open("sample.txt","w") as f:
    f.write("Hello")
```

Behind the scenes:

```
__enter__()
   open file
__exit__()
   flush + close
```

Guaranteed cleanup.

---

# Mental model

Think of `open()` like creating a **communication channel with the OS**.

```
Python code
     ↓
Python file object
     ↓
File descriptor
     ↓
Kernel file table
     ↓
Filesystem
     ↓
Disk blocks
```

---

# Interview-level summary

`open()` does three core things:

1. Calls OS `open()` syscall
2. Gets a **file descriptor**
3. Wraps it in a **buffered Python file object**

---

