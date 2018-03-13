from arg_parse import ArgParse
from FILE import FileOperation
from remote_mach import SSH

def obj():
	oper = FileOperation()
	return oper

def inputs():
	arg = ArgParse()
	f_arg = arg.cl_arguments()[0]
	s_arg = arg.cl_arguments()[1]
	t_arg = arg.cl_arguments()[2]
	return f_arg, s_arg, t_arg

def read_operation(f_arg, s_arg, t_arg, operation):
		if(f_arg!=None and s_arg==None and t_arg==None):
			operation.Read_File(f_arg)

def append_operation(f_arg, s_arg, t_arg, operation):
	if(f_arg!=None and s_arg!=None and t_arg==None):
		if(s_arg.isalnum()):
			operation.append(f_arg, s_arg)
		
def f_l_operation(f_arg, s_arg, t_arg, operation):
	if(f_arg!=None and s_arg!=None and t_arg!=None):
		if(s_arg.isdigit()):
			if(t_arg == "f"):
				operation.First_N_Lines(f_arg, int(s_arg))
			elif(t_arg == "l"):
				operation.Last_N_Lines(f_arg, int(s_arg))
			else:
				print "ERROR:Choose from l and f onloperation"
		else:
			print "Error:s_arg is not digit"
	elif(f_arg!=None and s_arg==None and t_arg!=None):
		print "ERROR:All 3 inputs are required."


def main():
	operation = obj()
	argu = inputs()
	read_operation(argu[0], argu[1], argu[2], operation)
	append_operation(argu[0], argu[1], argu[2], operation)
	f_l_operation(argu[0], argu[1], argu[2], operation)
	remote_machine = SSH()
	remote_machine.access_file(argu[0])
	remote_machine.close_Connection()

if __name__=="__main__":
	main()
