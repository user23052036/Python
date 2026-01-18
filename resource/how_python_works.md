Good — you picked the right tiny example to learn from. I’ll explain exactly what’s happening when you run your two files, how `__pycache__` and `.pyc` files are produced, what “bytecode” is, why people sometimes call Python “interpreted” and sometimes “compiled”, and how to inspect and control the behavior on your machine. I’ll also show the small, practical commands you should run yourself and the smallest changes that will make your experiment produce useful evidence.

Below: concise rules, concrete commands, a short stress test (assumptions / failure modes / tradeoffs), and recommended next steps.

# What happened in your experiment (plain, precise)

1. When you run `import hello` from `import_local.py`, Python:

   * **parses** `hello.py` and converts it to an **AST**,
   * **compiles** the AST to a **code object** (bytecode),
   * **executes** that code object inside the Python runtime (the Python Virtual Machine, PVM).
2. When a module is imported (not executed as the top-level script), CPython writes a compiled bytecode file into `__pycache__` — e.g. `hello.cpython-313.pyc` (the `cpython-313` bit is the implementation + version).
3. The `.pyc` file speeds later imports because Python can skip parsing/AST-creation and load the bytecode directly (subject to freshness checks).
4. Bytecode is **not** machine code. It is a compact, platform-independent representation of instructions for the PVM (a stack-based virtual machine). The PVM itself is implemented in C in CPython and performs the actual machine-level work.

# Evidence you can inspect (I created and compiled a demo)

I wrote `hello.py` and compiled it to `.pyc` in the environment and disassembled the `drugs` function. You can download both files if you want:

* Source: `/mnt/data/py_internals_demo/hello.py`
* Bytecode: `/mnt/data/py_internals_demo/__pycache__/hello.cpython-311.pyc`

(If you run the same steps on your machine you will see a similarly named `.pyc` that includes your Python minor version.)

Example of the disassembly (trimmed): you can see PVM opcodes like `LOAD_GLOBAL`, `FORMAT_VALUE`, `CALL`, `RETURN_VALUE`. This is the bytecode that the PVM executes.

# Exact commands you should run locally to reproduce & inspect

(Use your project directory that contains `hello.py` and `import_local.py`.)

Inspect files:

* `ls -l`
* `ls -l __pycache__`

Compile (force):

* `python -m py_compile hello.py`
  Or compile full tree:
* `python -m compileall -f .`

Find the location for the .pyc that Python will write:

* In Python:

```python
import importlib.util
importlib.util.cache_from_source('hello.py')
```

Disassemble the function (interactive):

```python
import dis
from hello import drugs
dis.dis(drugs)
```

View instructions with readable bytecode:

```python
import dis
d = dis.Bytecode(drugs)
for instr in d:
    print(instr.opname, instr.argrepr)
```

# Controls: how to stop or force `.pyc` creation

* Prevent writing `.pyc`: run Python with the `-B` flag or set environment variable:

  * `python -B import_local.py`
  * `export PYTHONDONTWRITEBYTECODE=1` (Linux/macOS) before running.
* Force recompilation:

  * `python -m compileall -f .`
  * Delete `__pycache__` and re-import.

# Implementation details you must know (short, precise)

* `.pyc` header: contains a magic number (Python version), and either a timestamp or a source hash (PEP 552) used to validate freshness.
* `.pyc` files live in `__pycache__` and include `cpython-XY` in the name, allowing multiple interpreters to coexist.
* `.pyc` files are created **only** when the module is imported (or when you explicitly compile). Running `python hello.py` as the top-level script usually does **not** write `__pycache__` for that module.
* Staleness: CPython checks header info to avoid using outdated `.pyc`; if invalid it recompiles from source.

# Interpreted vs compiled — clarify the confusion

* **Python is both** in the practical sense:

  * Source → *compiled* to bytecode (.pyc / code object).
  * Bytecode → *interpreted* by the Python Virtual Machine (PVM). The PVM executes opcodes one-by-one (or uses C-coded helpers).
* That’s why people say “interpreted”: the bytecode is executed by an interpreter loop rather than being translated to machine code and executed directly. People say “compiled” because the source is compiled to bytecode first.
* Implementations differ:

  * **CPython**: reference implementation; compiles to bytecode; interprets bytecode in a C runtime.
  * **PyPy**: includes a JIT (it compiles hot paths to machine code at runtime).
  * **Jython / IronPython**: compile to JVM/.NET bytecode or use host runtime.
  * **Cython**: transpiles Python-like code to C extension modules (native code).

# How bytecode relates to performance

* Loading `.pyc` saves parse/compile time but does not eliminate interpreter overhead.
* The hot-path speed depends on the interpreter; PyPy (JIT) can be significantly faster for long-running tasks.
* Native extensions (`.so`/`.pyd`) still run machine code — big performance gains when heavy-lifting is done in C.

# Failure modes, edge cases, tradeoffs (ruthless checklist)

* Assumption: `.pyc` always speeds things up. Reality: startup cost saved (parsing), but frequently-file-changed projects may spend extra I/O compiling — tradeoff negligible for production.
* Failure mode: read-only fs — Python may fail to write `.pyc`. It will still run; it just cannot cache.
* Edge case: two different Python minor versions — `__pycache__` keeps separate pyc files so they don’t conflict.
* Edge case: timestamp vs hash validation (PEP 552) — when clocks are wrong, timestamp checking can be unreliable; PEP 552 hash-based pyc fixes many of those issues.
* Security note: `.pyc` files can be redistributed (they reveal code structure and some constants). They’re not a secure obfuscation.
* Tradeoff: disabling `.pyc` reduces disk writes (useful on ephemeral containers) but increases startup cost.

# Smallest set of changes to make your experiment maximally informative

1. Add this line to `import_local.py` to demonstrate top-level vs imported behavior:

```python
# import_local.py
import hello     # generates __pycache__/hello.*.pyc
if __name__ == "__main__":
    print("Top-level execution")
```

2. Re-run as top-level script vs `python -m import_local` and watch whether `.pyc` appears or is used.
3. Use `dis` on `hello.drugs` to inspect the exact opcodes (as I demonstrated above). That directly shows “what the PVM executes”.

# Recommended next steps (learning path)

1. Use `dis` on several small functions — compare comprehension, loops, function calls, and generator bytecodes.
2. Read the CPython eval loop (`Python/ceval.c`) to see how opcodes map to C code.
3. Read PEP 552 (pyc hash-based invalidation) and PEPs about import system to understand header/integ.
4. Try PyPy to see the difference with JIT and profile both.
5. If you want to go deep: clone CPython, add print statements in `ceval.c`, run with gdb, and step through a simple `drugs` call.

# Concrete homework (do these)

1. Run the commands I listed earlier locally and paste the `dis.dis(drugs)` output here.
2. Try `python -B import_local.py` then `python import_local.py` and note presence/absence of `__pycache__`.
3. Use `python -m compileall .` then `python -m py_compile hello.py` and inspect `.pyc` header bytes (use a hex viewer) to see magic number and timestamp/hash.

---

