import json
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(prog='Tron generator', description='Generates levels (public or private) for Tron game.')
    parser.add_argument('--test_id', metavar='ID', type=int, required=True, help='Test id.')
    parser.add_argument('--test_file', metavar='FILE', type=str, help='Test file name')
    parser.add_argument('--test_description_file', metavar='FILE', type=str, help='Test description file')

    return parser.parse_args()

def write_test(test, file_name):
	if file_name is not None:
		with open(file_name, 'w') as file:
			file.write(json.dumps(test))

def write_test_description(test, file_name):
	if file_name is not None:
		with open(file_name, 'w') as file:
			file.write("\n".join([" ".join(i) for i in test['field']]))
