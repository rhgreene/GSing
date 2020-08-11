import unittest
import gsing.waves
import inspect
import re
import json
import os
from collections import defaultdict
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
from .definitions import TEST_RESOURCE_LOCATION

class WaveShapeTest(unittest.TestCase):
   def setUp(self):
      self.x = np.linspace(0, np.pi * 2.0, 201)
      self.wave_frequency = 1.0
      self.y = defaultdict(list)
      self.test_file_dir = 'wave_shape_test'

# No judging me here please. I understand that this is totally unreadable
# but I think list comprehension is one of Python's weak points.
# I'm discovering all classes whose names match the pattern ".+Wave"
# and instantiating them in a list.
      self.waves = { 
         wave[1](velocity=self.wave_frequency) for wave in inspect.getmembers(
            gsing.waves, predicate=inspect.isclass
         ) 
         if re.search(r".+Wave", wave[0])
      }

      last = 0
      for current in self.x:
         for wave in self.waves:
            wave.increment(current - last)
            self.y[wave.__class__.__name__].append(wave.get_sample())
         last = current

   def test_wave_shape(self):
      for wave in self.waves:
         with self.subTest(name='test_' + wave.__class__.__name__ + '_shape'):
            with open(os.path.join(TEST_RESOURCE_LOCATION, self.test_file_dir, wave.__class__.__name__ + '.json')) as json_y:
               y = json.load(json_y)
               self.assertEqual(y, self.y[wave.__class__.__name__])


# Run with `python -m test.wave_shape_test` to write test data
if __name__ == "__main__":
   manual_test = WaveShapeTest()
   manual_test.setUp()
   fig, ax = plt.subplots(len(manual_test.waves), 1, constrained_layout=True)
   for i, wave in enumerate(manual_test.waves):
      ax[i].set_title(wave.__class__.__name__)
      ax[i].plot(manual_test.x, manual_test.y[wave.__class__.__name__], lw=2)

   print("Please review the waves in the provided graphs")
   plt.show()
   write_tests = input("Would you like to write the test values used for unittesting? (Y/n)\n")
   if write_tests in ["Y", "y"]:
      with open(os.path.join(TEST_RESOURCE_LOCATION, manual_test.test_file_dir, 'x.json'), 'w+') as resource_file:
         json.dump(manual_test.x.tolist(), resource_file)
      for wave in manual_test.waves:
         with open(os.path.join(TEST_RESOURCE_LOCATION, manual_test.test_file_dir, wave.__class__.__name__ + '.json'), 'w+') as resource_file:
            json.dump(manual_test.y[wave.__class__.__name__], resource_file)
   else:
      print("No files written")
      exit(0)
