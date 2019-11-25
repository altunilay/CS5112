# TODO: Your name, Cornell NetID
# TODO: Your Partner's name, Cornell NetID

# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1
from cs5112_hash import cs5112_hash2
from cs5112_hash import cs5112_hash3

# Implementation of a basic bloom filter. Uses exactly three hash functions.
class BloomFilter:
  def __init__(self, size=10):
    # DO NOT EDIT THIS CONSTRUCTOR
    self.size = size
    self.array = FixedSizeArray(size)
    for i in range(0, size):
      self.array.set(i, False)

  # To add an element to the bloom filter, use each of the k=3 hash functions we provided and compute
  # the positions that we are setting in the fixed size array using modulo operation.
  def add_elem(self, elem):
    #TODO: YOUR CODE HERE, delete the line below and implement accordingly
    raise NotImplementedError

  # Returns False if the given element was definitely not added to the filter. 
  # Returns True if it's possible that the element was added to the filter.
  def check_membership(self, elem):
    #TODO: YOUR CODE HERE, delete the line below and implement accordingly
    raise NotImplementedError
