import os

def deleteFile(filePath):
  try:
    os.remove(filePath)
    print(f"{filePath} deleted successfully!!")
  except OSError as e:
    print(f"{filePath} failed to delete")
    print(e)


def main():
  fileDelete = input("Enter the file path to delete :")
  deleteFile(fileDelete)

if __name__ == "__main__":
  main()