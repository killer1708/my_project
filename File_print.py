class FileOperation(object):


	def append(self, f, f2):
		with open(f,'rb+') as file:
			print 'Text is append.'
			content=file.readlines()
			a=content.__len__()
			n=int(a/2)
			content.insert(n,'This izz rajat\n')
			with open(f2,'w') as f1:
				content = "".join(content)
				f1.write(str(content))

	def First_N_Lines(self, f, n):
		with open(f,'r') as file:			
			print 'First ',n,'lines from file',f 
			try:
				for lines in (file.readlines()[:n]):
					print(lines)
			except Exception as er:
			   	print er
			
	def Last_N_Lines(self, f, n):
		with open(f,'r') as file:
			print 'Last ',n,'lines from file',f
			try:
				for lines in (file.readlines()[-n:]):  
					print(lines)
			except Exception as error:
				  print error
			
	def Read_File(self, f):
		try:
			with open(f,'r') as file:
				content=file.read()
				print content
		except Exception as e:
			  print e


