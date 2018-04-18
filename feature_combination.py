from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np 

def feature_combination(batchsize, mfcc_features,text_features):
	features = np.concatenate((mfcc_features,text_features))
	
	return features
