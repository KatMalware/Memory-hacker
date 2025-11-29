import argparse
from scanner import get_memory_regions, read_region
from writer import replace_all
from utils import get_pid_from_name, parse_hex_string
from rich.console import Console

console = Console()


def main():
    parser = argparse.ArgumentParser(description="Advanced Memory Hacker")

    parser.add_argument("--pid", type=int, help="Target PID")
    parser.add_argument("--process", type=str, help="Process name")

    parser.add_argument("--search", type=str, help="ASCII search string")
    parser.add_argument("--replace", type=str, help="ASCII replacement")

    parser.add_argument("--search-hex", type=str, help="HEX search bytes")
    parser.add_argument("--replace-hex", type=str, help="HEX replacement bytes")

    args = parser.parse_args()

    # Determine PID
    pid = args.pid or get_pid_from_name(args.process)

    if not pid:
        console.print("[red]Error: PID not provided or process not found[/red]")
        return

    console.print(f"[cyan]Target PID: {pid}[/cyan]")

    # Determine search method
    if args.search:
        search = args.search.encode()
    elif args.search_hex:
        search = parse_hex_string(args.search_hex)
    else:
        console.print("[red]No search pattern provided[/red]")
        return

    if args.replace:
        replace = args.replace.encode()
    elif args.replace_hex:
        replace = parse_hex_string(args.replace_hex)
    else:
        replace = None  # allow search-only mode

    # Scan regions
    regions = get_memory_regions(pid)
    console.print(f"[yellow]Found {len(regions)} writable regions[/yellow]")

    for start, end, region_name in regions:
        data = read_region(pid, start, end)

        if search not in data:
            continue

        console.print(f"[green]Match found in region: {region_name}[/green]")

        if replace:
            replace = replace.ljust(len(search), b'\x00')
            replace_all(pid, region_name, start, data, search, replace)
        else:
            console.print("[blue]Search-only mode[/blue]")

    console.print("[bold green]Done.[/bold green]")


if __name__ == "__main__":
    main()
