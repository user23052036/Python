
# **Linux Command Basics – Quick Manual**

## **1. Test Network Connectivity**

```bash
ping google.com
```

Sends network packets to verify internet connection.

---

## **2. View Network Interfaces**

**Old command (deprecated):**

```bash
ifconfig
```

**Modern command:**

```bash
ip a
```

Shows interface names, IP addresses, MAC address, etc.

---

## **3. Show Current Date & Time**

```bash
date
```

---

## **4. Exit Terminal / Program**

```bash
exit
```

---

## **5. Print Working Directory**

```bash
pwd
```

Displays your current location in the filesystem.

---

## **6. Change Directory**

```bash
cd <directory_path>
```

Supports:

* **Absolute path**: `/home/user/Documents`
* **Relative path**: `Documents/Projects`

---

## **7. Create Empty File**

```bash
touch file_name
```

---

## **8. Move Backward in Directories**

```bash
cd ..
```

Moves one level up.

```bash
cd ../..
```

Moves two levels up.

---

## **9. List Files and Directories**

```bash
ls
```

List contents of any directory:

```bash
ls /path/to/directory
```

`/` at the beginning refers to the **root directory**.

---

## **10. Detailed Listing + Hidden Files**

```bash
ls -l -a
```

* `-l` → long format
* `-a` → includes hidden files (starting with `.`)

---

## **11. File Types in Linux**

Linux treats **everything as a file**:

* **Regular files**
* **Directories**
* **Device files** (`/dev/sda`, etc.)

Check file type:

```bash
file <name>
```

---

## **12. Understanding File Permissions**

Example:
`drwxr-xr-x`

| Symbol  | Meaning                               |
| ------- | ------------------------------------- |
| **d**   | Directory (regular file would be `-`) |
| **rwx** | Owner → read, write, execute          |
| **r-x** | Group → read, execute                 |
| **r-x** | Others → read, execute                |

---

## **13. View File Contents (No Editing)**

```bash
less <file>
```

Example:

```bash
less /bin/ls
```

---

## **14. Locate Python Executable**

### **which**

```bash
which python3
```

Shows the exact binary that runs when you type `python3`
(only checks `$PATH`).

### **whereis**

```bash
whereis python3
```

Shows all locations:
binary, config, libraries, man pages.

---

## **15. Open a Path Graphically**

```bash
open <path>
```

---

## **16. Terminal Emulator vs True TTY**

### **Terminal Emulator**

* Runs inside GUI
* Examples: Parrot Terminal, GNOME Terminal
* More comfortable

### **True TTY**

* TeleType Terminal
* Full-screen console without GUI
* Connected directly to kernel
* More raw and powerful

---

### ✅ `touch file1`

Creates a file literally named **file1** (no extension).

### ✅ `touch file1.txt`

Creates a file named **file1.txt** with a `.txt` extension.

---

### ✔ Extensions in Linux are optional

Linux **does not require** extensions.
`file1` and `file1.txt` are both valid files. The OS treats them the same way—just names.

---

### ✔ When are they the same?

Only if **you already have a file named exactly `file1.txt`**, then:

```bash
touch file1
```

won’t affect it.

---
