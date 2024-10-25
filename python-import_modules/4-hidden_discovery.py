#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # List all names from hidden_4, filter out names that start with '__'
    names = [name for name in dir(hidden_4) if not name.startswith("__")]

    # Sort names alphabetically and print each one on a new line
    for name in sorted(names):
        print(name)
