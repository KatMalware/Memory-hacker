from utils import log_change


def write_memory(pid, addr, data):
    """Write raw bytes to memory."""
    with open(f"/proc/{pid}/mem", "rb+", buffering=0) as mem:
        mem.seek(addr)
        mem.write(data)


def replace_all(pid, region_name, start, data, search, replace):
    """Replace every occurrence of search → replace in data."""
    offsets = []
    idx = 0

    while True:
        idx = data.find(search, idx)
        if idx == -1:
            break

        offsets.append(idx)
        idx += len(search)

    for off in offsets:
        abs_addr = start + off
        write_memory(pid, abs_addr, replace)
        log_change(region_name, abs_addr, search, replace)
