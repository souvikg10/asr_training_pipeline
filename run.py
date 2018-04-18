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
   features = fc.feature_combination(mfcc_features=mfcc_features,text_features=text_features)
   
   while epoch < config_data['epochs']:
      feature_by_batch = np.array_split(features,config_data['Batch_size'])
      size = feature_by_batch.shape
      training_split = size * (1- config_data['validation_split'])
      testing_split = size * (config_data['validation_split'])
      training_data = np.array_split(feature_by_batch,training_split)

      ## training the data
      ## training_alogrithm.fit(training_data)

      test_data = np.array_split(feature_by_batch,testing_split)

      ## Validation of the data
      ## training.algorithm.validate(test_data)

      performance = 0.8

   persisted_path = config_data['model_path']

   ## Persist the model
   ## training.algorithm.persist(persisted_path)


   
