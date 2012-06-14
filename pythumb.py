from PIL import Image
import re
import sys
import os

def gen_thumb(_ifile, _ofile, _height, _width):
	im = Image.open( _ifile )
	#im.thumbnail( (_width, _height) )
	im = im.resize( (_width, _height) )
	#im = im.crop( (im.size[0]/2 - 80, im.size[1]/2 - 80, im.size[0]/2 + 80, im.size[1]/2 + 80) )
	im.save( _ofile )

def list_files(_dir, _pattern):
	_imgPattern = re.compile(_pattern, re.IGNORECASE)
	_files = []
	for _name in os.listdir(_dir):
		_match = _imgPattern.search(_name)
		if (_match != None):
			_files.append(_name)
	return _files

in_dir = sys.argv[1]
out_dir = sys.argv[2]
height = int(sys.argv[3])
width = int(sys.argv[4])

if not os.path.isdir(out_dir):
	os.mkdir(out_dir)

large_images = list_files(in_dir, "\.(jpg|png|gif|img)$")
small_images = list_files(out_dir, "\.(jpg|png|gif|img)$")

for _larg_img in large_images:
	if (_larg_img not in small_images):
		_in_file  = in_dir + '//' + _larg_img
		_out_file  = out_dir + '//' + _larg_img
		gen_thumb(_in_file, _out_file, height, width)
for _small_img in small_images:
	if (_small_img not in large_images):
		_delete_file = out_dir + '//' + _small_img
		os.remove(_delete_file)