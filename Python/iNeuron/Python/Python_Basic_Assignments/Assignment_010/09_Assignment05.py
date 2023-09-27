import os
import shutil
print("------------------------------------_Yogesh Prabhu Nichal_-----------------------------------------\n")
print("""Question-
		5. Create a programme that searches a folder tree for files with a certain file extension (such as .pdf or .jpg).
		Copy these files from whatever location they are in to a new folder.""")

def search_and_copy(source,destination,extensions):
	source = os.path.abspath(source)
	destination = os.path.abspath(destination)
	for foldername, subfolder, filenames in os.walk(source):
		print(f'Folder Name ➞ {foldername}', end='\n\n')
		print(f'Sub Folders ➞ {subfolder}', end='\n\n')
		print(f'Files ➞ {filenames}', end='\n\n')
		for filename in filenames:
			fileName, extension = os.path.splitext(filename)
			if extension in extensions:
				targetFile = foldername + os.path.sep + fileName + extension
				shutil.copy(targetFile, destination)
		print(f'Files copied successfully from {source} to {destination}')

	extensions = ['.pdf', '.jpg', '.ipynb']
	source = 'Dummy Source'
	destination = 'Dummy Destination'
	search_and_copy(source, destination, extensions)


def main():

	print("""Answer-
		The operator for list concatenation is +, while the operator for replication is *.""")

	print("\n-----------------------------------------_Thank You_-----------------------------------------------")


if __name__ == "__main__":
	main()
