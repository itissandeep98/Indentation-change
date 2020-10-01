#program to change indentation of 4 spaces to a single tab
import os
def change_indent_to_tabs(filename):
	"""
	Simple function to convert the 4 space indentation to single tab for python  files
	It does the operation in the same file

	"""
	try:
		file=open(filename,'r')
		file1=open('temp.py','w')
		for i in file:
		    s=i
		    s.replace('    ','	')
		    file1.write(s)
		file1.close()
		file.close()
		os.remove(filename)
		os.rename('temp.py',filename)
	except FileNotFoundError :
		print("No file of such name")

if __name__ == '__main__':
	filename=input('enter filename: ')
	change_indent_to_tabs(filename)