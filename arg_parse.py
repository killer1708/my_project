import argparse

class ArgParse(object):
        
	def cl_arguments(self):
		parser = argparse.ArgumentParser()
		parser.add_argument("--input1", action="store", required=True, help="input filename")
		parser.add_argument("--input2", action="store", help="output file, last n lines or first n lines")
		parser.add_argument("--input3", action="store", help="flag")
		args = parser.parse_args()
		f_arg = args.input1
		s_arg = args.input2
		t_arg = args.input3
		return f_arg, s_arg, t_arg
	
