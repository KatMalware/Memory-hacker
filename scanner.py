def get_memory_regions(pid):
    """Return writable memory regions from /proc/<pid>/maps."""
    regions = []

    with open(f"/proc/{pid}/maps", "r") as f:
        for line in f:
            parts = line.split()

            address = parts[0]
            perms = parts[1]

            if "rw" not in perms:
                continue

            start, end = address.split("-")
            regions.append((int(start, 16), int(end, 16), parts[-1]))

    return regions


def read_region(pid, start, end):
    """Read a memory region."""
    with open(f"/proc/{pid}/mem", "rb", buffering=0) as mem:
        mem.seek(start)
        return mem.read(end - start)
