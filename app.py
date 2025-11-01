from pathlib import Path # module that helps manage directory movement
import argparse


def get_state(dev_dir="/dev", state_file="orig_state"):
    dev_path = Path(dev_dir)
    orig_state = Path.home() / "mont/.state" / orig_state

    #  checking if path to directory exists
    orig_state.parent.mkdir(parents=True, exist_ok=True)

    # Get all partition devices (e.g., sdb1, sdc1)
    partitions = [partition.name for partition in dev_path.iterdir() if partition.name.startswith("sd")]
    orig_state.write_text("\n".join(sorted(partitions)))
    print(f"Baseline device state saved to {orig_state}")
    return set(partitions)

def initialize():
    while True:
        inp = input("During installation, mont will get a snapshot of the devices connected to this machine. Are there any current USB connections? [y/n]: ").strip().lower()
        if inp == "y":
            print("Please remove connected devices and retry the installation afterwards.")
            exit()
        elif inp == "n":
            orig_state = Path.home() / "mont/.state/orig_state.txt"

def check_and_link(dev_dir="/dev", state_file="current_state"):
    dev_path = Path(dev_dir)
    orig_state = Path.home() / "mont/.state" / orig_state
    current_state = Path.home() / "mont/.state" / current_state
    mount_dir = Path.home() / "mont" 

    try:
        orig_devices = set(orig_state.read_text().splitlines())
    except FileNotFoundError:
        print(f"Error:{orig_state} not found. Run 'mont init' first.")




def main():
    parser = argparse.ArgumentParser(
        program = "mont",
        description = "Monitor and mount USB devices to home directory." # this is what is shown upon running the --help subcommand
    )
    subparsers = parser.add_subparsers(dest = "command")
    
    # subcommand: mont init
    subparsers.add_parser("init", help = "Initialize and save baseline device /dev directory state")
    
    if args.command == "init":
        print("Initializing...")
    
    if args.command == "mount":
        check_and_link()
    
    else:
        check_and_link() 

# TODO: finish check_and_link
# TODO: get_state() needs to be more flexibly/reusable
# TODO: learn how to package the code -> install system wide on MAMMON