import subprocess
import os
import sys
import tempfile


"""
[Usage]
python3 {thisfile}.py //main:hello-world
"""
def main():
	args = sys.argv

	res = subprocess.check_output(f"bazel query --nohost_deps --noimplicit_deps 'deps({args[1]})' --output graph", shell=True)
	print("[+] created tempfile")
	_, path = tempfile.mkstemp()
	with open(path, 'w+b') as f:
		f.write(res)
	subprocess.check_output(f"xdot {path}", shell=True)

	os.remove(path)
	print("[+] removed tempfile")


if __name__ == "__main__":
	main()
