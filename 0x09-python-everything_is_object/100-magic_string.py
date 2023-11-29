#!/usr/bin/python3

def magic_string():
    s = "BestSchool"
    for i in range(len(s)):
        s += ", " + s
        return s
