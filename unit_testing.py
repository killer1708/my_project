import unittest
import os
from FILE import FileOperation

class TestFile(unittest.TestCase):

	def setUp(self):
		self.fc_obj = FileOperation()
		self.fname = "doc1.txt"
		f = open(self.fname, 'w')
		f.write('rajat' + '\n' + 'kumar' + '\n' + 'punjab' + '\n' + 'patiala' + '\n' + 'himachal' + '\n')
		f.close()
			
	def test_Read_File(self):
		expected = "rajat\nkumar\npunjab\npatiala\nhimachal\n"
		result = self.fc_obj.Read_File(self.fname)
		self.assertEqual(result, expected)
    
	def test_First_N_Lines(self):
		expected = ['rajat\n', 'kumar\n']
		result = self.fc_obj.First_N_Lines(self.fname, 2)
		self.assertEqual(result, expected)
	
	def test_Last_N_Lines(self):
		expected = ['punjab\n', 'patiala\n', 'himachal\n']
		result = self.fc_obj.Last_N_Lines(self.fname, 3)
		self.assertEqual(result, expected)

	def test_append(self):
		expected =['rajat\n', 'kumar\n', 'This izz rajat\n', 'punjab\n', 'patiala\n', 'himachal\n']
		output_file = "doc3.txt"
		result = self.fc_obj.append(self.fname, output_file)
		f1 = open(output_file, 'r')
		l = f1.readlines()
		f1.close()
		self.assertEqual(expected, l)

	def tearDown(self):
	 	try:
	 		os.remove(self.fname) 
	 		os.path.isfile(self.fname)
	 	except OSError as ose:
	 		print(ose)

        
if __name__ == "__main__":
	unittest.main()