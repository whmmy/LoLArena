"""Tiny CLI shim so `python -m lola` routes to src/cli.py."""

from .cli import main

if __name__ == "__main__":
    main()
