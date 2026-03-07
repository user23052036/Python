**POSIX write semantics** refers to the behavior defined by the **POSIX** for the system call **`write()`** used to write data to files or devices.

The Portable Operating System Interface (POSIX) is a family of standards developed to ensure compatibility among operating systems. Managed by the Austin Group—a collaboration between the IEEE Computer Society, The Open Group, and ISO/IEC—it defines common APIs, command-line shells, and utilities so that software can run on diverse Unix and Unix-like systems without modification.



**In short:**

When a program calls `write()`, the function **returns the number of bytes actually written** to the file descriptor.

### Key rules

1. **Return value = bytes written**

   * If successful, it returns how many bytes were written.

2. **Partial writes are allowed**

   * The OS may write **less than requested**.

   Example:

   ```text
   requested: 100 bytes
   written:   60 bytes
   return:    60
   ```

3. **Errors return -1**

   * If something fails (disk full, permission issue).

### Why this design exists

Operating systems deal with:

* pipes
* sockets
* disks
* network buffers

These resources may not always accept all data at once, so the API must report **exactly how much was written**.

### Why Python’s `write()` returns `11`

Python's file object ultimately relies on the underlying **POSIX `write()` behavior**, so it returns the **number of characters written**.

`"Hello world"` → **11 characters → return 11**.
