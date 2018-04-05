from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests, zipfile, StringIO

class DownloadFiles(object):
	def __init__(self,url):
		self.url = url
	def get_zip_data(self):
		r = requests.get(self.url, stream=True)
		z = zipfile.ZipFile(StringIO.StringIO(r.content))
		z.extractall(path="zipped")
		return z 