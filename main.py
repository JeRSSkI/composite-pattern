from file import File
from folder import Folder

file1 = File("file1.txt")
file2 = File("file2.txt")

folder = Folder("Documents")
folder.add(file1)
folder.add(file2)

folder.show()
