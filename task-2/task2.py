from pathlib import Path
import os
from pprint import pprint

def get_cats_info(file_path: str):
  current_dir = Path.cwd()
  path_to_file = os.path.join(current_dir, file_path)

  try:
    with open(path_to_file, "r") as fh:
      lines = fh.readlines()
  except Exception as e:
    print(f"Error happened when reading the file {path_to_file}: {e}")
    return None
  
  lines = list(map(lambda line: line.strip(), lines) )
  lines = list(filter(lambda line: line, lines))

  result = []
  for line in lines:
    [id, name, age] = line.split(',')
    result.append({
      id: id,
      name: name,
      age: age,
    })
  
  return result

cats_info = get_cats_info("task-2/cats.txt")
pprint(cats_info)
