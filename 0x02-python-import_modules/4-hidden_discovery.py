#!/usr/bin/python3
import hidden_4
for name in sorted(hidden_4.__dict__):
    if not name.startswith("__"):
        print(name)
