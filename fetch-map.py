import requests
import datetime
import argparse
from os import path, getcwd, chdir, _exit

URL_TEMPLATE = 'https://www.poelab.com/wp-content/labfiles/{:s}-{:s}-{:s}-{:s}.json'

parser = argparse.ArgumentParser(description='fetches a path of exile lab compass file from poelab.com')
parser.add_argument('-date', help='the date of the lab to fetch a compass file for (format: yyyy-mm-dd, default: today\'s date)')
parser.add_argument('-lab', default='uber', help='the lab tier (default: uber)')
parser.add_argument('-format', default='{:s}-{:s}-{:s}-{:s}.json', help='python string format for the file\'s name (default: {:s}-{:s}-{:s}-{:s}.json)')
parser.add_argument('-dir', help='the directory in which the lab file would be saved in (default: current working directory)')

def fetch_json(lab, date, file_name_format):
	try:
		print('fetching lab file for {:s} lab on {:s}-{:s}-{:s}'.format(lab, *date))
	except IndexError:
		print('failed to retrieve lab compass file, the date is invalid')
		return

	res = requests.get(URL_TEMPLATE.format(lab, *date))
	
	if res.status_code == 200:
		map_file_name = path.join(getcwd(), file_name_format.format(lab, *date))
		with open(map_file_name, 'w') as map_file:
			map_file.write(res.text)
		print('file saved to {:s}'.format(map_file_name))
	else:
		print('failed to retrieve lab compass file, does the lab compass file exist or is the date/lab name correct? (HTTP {:d})'.format(res.status_code))


if __name__ == '__main__':
	print('--- PoE Lab compass fetcher ---')

	args = parser.parse_args()
	
	if args.date is None:
		args.date = datetime.datetime.now().strftime('%Y-%m-%d')
	
	if args.dir is not None:
		if path.isdir(args.dir):
			chdir(args.dir)
		else:
			print('the directory {:s} does not exist'.format(args.dir))
			input('Press enter to continue...')
			_exit(1)
			
	args.date = tuple(args.date.split('-'))			
	fetch_json(args.lab, args.date, args.format)
	input('Press enter to continue...')
	
