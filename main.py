#!/usr/bin/python
# Import module support
import os, sys, hone
sys.path.insert(0, os.path.abspath(".."))
from utils import support,csv_utils,json_utils

# Now you can call defined function that module as follows
support.print_func("Zara")

Hone = hone.Hone()
result = Hone.convert('./data/example_b.csv')
print result