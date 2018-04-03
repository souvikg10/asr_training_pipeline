from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import logging
import re


class GetConfigurationData(object):
	def __init__(self,configPath):
		self.configPath = configPath

	def get_config(self):
		
		with open(self.configPath) as json_data_file:
			data = json.load(json_data_file)
    		return data