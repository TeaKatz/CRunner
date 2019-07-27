import os
import subprocess
from subprocess import PIPE
from os.path import join


def run(exe_dir, input=None):
	"""
	Leave input to None if you want to input by hand.
	"""
	if os.path.exists(exe_dir):
		process = subprocess.run(join("./", exe_dir), stdout=PIPE, input=input, encoding="utf-8")
		
		return process.stdout


if __name__ == "__main__":
	# Testing
	print(run("Executables/getCharecter"))
	print(run("Executables/getCharecter", "A"))
	print(run("Executables/getNumber", "15"))
	print(run("Executables/getString", "University"))
	print(run("Executables/getArray", "5 1 2 3 4 5"))