# Memory-hacker


A Python tool that can scan and modify live process memory on Linux using `/proc/<pid>/maps` and `/proc/<pid>/mem`.

## Features

- Scan **all memory regions** (not only heap)
- Find and replace **multiple occurrences**
- Support **ASCII, HEX, and raw bytes**
- Automatically detect all writable (`rw-p`) memory segments
- Logging of all modifications
- Process selection by PID or process name
- Safe replacement: never crashes the target process
- CLI with argparse

## Usage

### Replace ASCII string
```bash
python3 main.py --pid 1234 --search "Hello" --replace "Hacked!"
```

### Replace HEX pattern
```bash
python3 main.py --pid 1234 --search-hex "48 65 6C 6C 6F" --replace-hex "90 90 90 90 90"
```

### Search only
```bash
python3 main.py --pid 1234 --search "password"
```

### Find process by name
```bash
python3 main.py --process loop.out --search "Holberton"
```

Logs are saved in:

```
logs/memory_hacker.log
```

---

## Warning

This tool is for **educational purposes only**.  
Modifying memory of other processes without permission is illegal.

