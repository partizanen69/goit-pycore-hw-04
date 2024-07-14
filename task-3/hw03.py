import sys
import os
from pathlib import Path
import colorama

colorama.init(autoreset=True)  

try:
  dir_path = sys.argv[1]
except Exception as e:
  print("Script expects directory path as an argument. Nothing given. Exiting")
  sys.exit(1)

if not dir_path.startswith('/'):
  print(f'Please provide absolute path to the directory. Relative path has been given: {dir_path}')
  sys.exit(1)

if not os.path.exists(dir_path) or not os.path.isdir(dir_path):
  print(f"Directory {dir_path} does not exist or it not a directory")
  sys.exit(1)


dir_path = Path(dir_path)

def generate_structure(dir_path: Path, level: int = 1):
  for dir in dir_path.iterdir():
    if dir.is_dir():
      print(colorama.Fore.BLUE + f"{level * '  '}{dir.stem}/")
      generate_structure(dir, level + 1)
    else:
      print(colorama.Fore.GREEN + f"{level * '  '}{dir.stem}")

print(f"{dir_path.stem}/")
generate_structure(dir_path)
