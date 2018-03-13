import paramiko


class SSH(object):

	client = None

	def __init__(self):
		self.client = paramiko.SSHClient()
		self.client.load_system_host_keys()
		self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.client.connect('192.168.102.56', username='msys', password='master#123')

	def access_file(self, f_name):
		sftp = self.client.open_sftp()
		sftp.get('/home/rajat/'+f_name, '/home/msys/doc1.txt')
		sftp.close()
			
	def close_Connection(self):
		if(self.client != None):
			self.client.close()


   
