from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np
def extract_text_features(zipfile):
	text_features = np.array([])
	for filename in zipfile.namelist():
		if filename.endswith(".lab"):
			labelled_file = zipfile.read(filename,'rb')
			text_features = np.append(text_features,labelled_file)
	return text_features

	