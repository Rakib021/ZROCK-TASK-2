def readFile(file_path):
  try:
    with open(file_path, 'r') as file:
      contents = file.read()
      print(contents)
  except FileNotFoundError as e:
    print(f"{file_path} not found")
    print(e)
  
  finally:
    try:
      file.close()
      print("file is closed")
    except UnboundLocalError:
      pass
def main():
  filePath =input("Enter the file path directory :")
  readFile(filePath)
  
if __name__ == "__main__":
  main()