# test_import.py
import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_cleaner import SolarDataCleaner
from src.featuring import SolarFeatureGenerator


print("Import successful! Class definition:", 
      SolarDataCleaner.__doc__)

print ("Import successful! Class definition:", 
       SolarFeatureGenerator.__doc__)