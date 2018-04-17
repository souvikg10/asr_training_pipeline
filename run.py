from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from get_config import GetConfigurationData
from download_file import DownloadFiles
from extract_wav import ExtractFiles
import numpy
import extract_mfcc_features as emfc
import extract_text_features as etf 
import feature_combination as fc 

if __name__ == '__main__':
    # Running as standalone python application
   config_path = GetConfigurationData(configPath="config.json")
   config_data = config_path.get_config()

   download_file = DownloadFiles(url = config_data['URL'])
   zipfile = download_file.get_zip_data()

   extract_wav = ExtractFiles(zipfile=zipfile)
   extracted_files = extract_wav.get_wav_files(duration=config_data['Duration'])

   mfcc_features = emfc.extractMFCCfeatures(extracted_wav_files=extracted_files,number_mfcc_features=config_data['NumberMFCC'])
   
   text_features = etf.extract_text_features(zipfile=zipfile)
   
   feature_by_batch = fc.feature_combination(batchsize=config_data['Batch_size'],mfcc_features=mfcc_features,text_features=text_features)



   
