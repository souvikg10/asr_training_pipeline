from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from get_config import GetConfigurationData
if __name__ == '__main__':
    # Running as standalone python application
   config_path = GetConfigurationData(configPath="config.json")

   config_data = config_path.get_config()

   print(config_data['url'])