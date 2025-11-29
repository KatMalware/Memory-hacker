import psutil
import re
import logging
from rich.console import Console

console = Console()

# Logging config
logging.basicConfig(
    filename="logs/memory_hacker.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def get_pid_from_name(name):
    """Return PID of process by matching name."""
    for proc in psutil.process_iter(['name', 'cmdline']):
        try:
            if name in " ".join(proc.info['cmdline']):
                return proc.pid
        except:
            continue
    return None


def parse_hex_string(hex_str):
    """Convert '48 65 6C' into b'Hel'"""
    hex_str = hex_str.replace(" ", "")
    return bytes.fromhex(hex_str)


def log_change(region, addr, old, new):
    logging.info(f"[MODIFIED] Region: {region}, Address: {hex(addr)}, "
                 f"Old: {old}, New: {new}")
    console.print(f"[green][+] Modified at {hex(addr)}[/green]")

