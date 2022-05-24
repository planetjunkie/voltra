import argparse
import os
import sys
import create_file as CF


parser = argparse.ArgumentParser(description='Voltra: A tool for analyzing and visualizing the output of Voltra.')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.4 Public RC')
parser.add_argument('-c', '--create', action= CF, help='Create a new project structure.')




args = parser.parse_args()

