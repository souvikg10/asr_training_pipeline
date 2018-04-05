from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests, zipfile, StringIO
import re
import librosa
class ExtractFiles(object):
	def __init__(self,zipfile):
		self.zipfile = zipfile
		
	def get_wav_files(self,duration):
		extracted_files = []
		for filename in self.zipfile.namelist():
			if filename.endswith(".wav"):
				audio_file = self.zipfile.read(filename,'rb')
				d = librosa.get_duration(filename="zipped/"+filename)
				if d > duration:
					extracted_files.append(filename)
		return extracted_files

		
