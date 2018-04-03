from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests

class DownloadFiles(object):
	def __init__(self,url):
		self.url = url
