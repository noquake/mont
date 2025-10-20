from pathlib import Path # module that helps manage directory movement
import argparse


def get_state(dev_dir="/dev", state_file="orig_state"):
    dev_path = Path(dev_dir)
    state_path = Path.home() / "mont/.state" / state_file

    #  checking if path to directory exists
    state_path.parent.mkdir(parents=True, exist_ok=True)

    # Get all partition devices (e.g., sdb1, sdc1)
    partitions = [partition.name for partition in dev_path.iterdir() if partition.name.startswith("sd")]
    state_path.write_text("\n".join(sorted(partitions)))
    print(f"Baseline device state saved to {state_path}")
    return set(partitions)

def initialize():
    while True:
        inp = input("During installation, mont will get a snapshot of the devices connected to this machine. Are there any current USB connections? [y/n]: ").strip().lower()
        if inp == "y":
            print("Please remove connected devices and retry the installation afterwards.")
            exit()
        elif inp == "n":
            orig_state = Path.home() / "mont/.state/orig_state.txt"

def main():
    parser = argparse.ArgumentParser(
        program = "mont",
        description = "Monitor and mount USB devices to home directory." # this is what is shown upon running the --help subcommand
    )
    subparsers = parser.add_subparsers(dest = "command")
    
    # subcommand: mont init
    subparsers.add_parser("init", help = "Initialize and save baseline device /dev directory state")
    
    # subcommand: mont check
    subparsers.add_parser("check", help = "Compare current device state to baseline")

