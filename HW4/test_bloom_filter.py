# Here is a very simple test. Please make sure your code passes the provided tests -- this serves as a check that our grading script will work.
# You are encouraged to add additional tests of your own, but you do not need to submit this file.

from bloom_filter import BloomFilter

bfilter = BloomFilter()
bfilter.add_elem("example_elem")
if bfilter.check_membership("example_elem"):
  print("Found this element in the bloom filter")
else:
  print("Bloom filter did not return True for added element ")
