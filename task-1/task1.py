from pathlib import Path
import os

def total_salary(file_path: str):
  current_dir = Path.cwd()
  path_to_file = os.path.join(current_dir, file_path)

  try:
    with open(path_to_file, "r") as fh:
      lines = fh.readlines()
  except Exception as e:
    print(f"Error happened when reading the file {path_to_file}: {e}")
    return 0, 0
  
  lines = list(map(lambda line: line.strip(), lines) )
  lines = list(filter(lambda line: line, lines))

  total = 0

  for line in lines:
    [_, salary] = line.split(',')
    total += float(salary.strip())
  
  avg = total / len(lines)

  return total, avg


total, average = total_salary("task-1/data.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
