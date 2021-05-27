import sys
import os

print(sys.path)
dir_path = os.path.dirname("D:\\tuz\\manya\\Lesson1\\Task1\\")
sys.path.insert(0, os.path.split(dir_path)[0])

print(sys.path)