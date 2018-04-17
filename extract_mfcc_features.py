from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests, zipfile, StringIO
import re
import librosa
import numpy as np

def extractMFCCfeatures(extracted_wav_files,number_mfcc_features):
	mfcc_features = np.array([])
	for files in extracted_wav_files:
		y, sr = librosa.load(path="zipped/"+files)
		mfcc_features = np.append(mfcc_features,librosa.feature.mfcc(y=y, sr=sr,n_mfcc=number_mfcc_features))
	return mfcc_features