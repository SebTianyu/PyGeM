"""
Utilities for reading and writing different CAD files.
"""
import os

class FileHandler(object):
	"""
	A base class for file handling.

	:cvar string infile: name of the input file to be processed.
	:cvar string outfile: name of the output file where to write in.
	:cvar string extension: extension of the input/output files. It is specific for each
		subclass.
	"""
	def __init__(self):
		self.infile = None
		self.outfile = None
		self.extension = None


	def parse(self, infile):
		"""
		Abstract method to parse a specific file.

		Not implemented, it has to be implemented in subclasses.
		"""
		raise NotImplementedError("Subclass must implement abstract method " \
			+ self.__class__.__name__ + ".parse")


	def write(self, mesh_points, outfile):
		"""
		Abstract method to write a specific file.

		Not implemented, it has to be implemented in subclasses.
		"""
		raise NotImplementedError("Subclass must implement abstract method " \
			+ self.__class__.__name__ + ".write")


	def _check_extension(self, filename):
		"""
		This private method checks if the given `filename` has the proper `extension` set
		in the child class. If not it raises a ValueError.

		:param string filename: file to check.
		"""
		__, file_ext = os.path.splitext(filename)
		if not file_ext == self.extension:
			raise ValueError('The input file does not have the proper extension. \
				It is %s, instead of %s.' % (file_ext, self.extension))


	def _check_filename_type(self, filename):
		"""
		This private method checks if `filename` is a string. If not it raises a TypeError.

		:param string filename: file to check.
		"""
		if not isinstance(filename, basestring):
			raise TypeError('The given filename (%s) must be a string' % filename)


	def _check_infile_instantiation(self, infile):
		"""
		This private method checks if the input file `infile` is instantiated. If not it means
		that nobody called the parse method, i.e. `self.infile` is None. If the check fails
		it raises a RuntimeError.

		:param string infile: file to check.
		"""
		if not infile:
			raise RuntimeError("You can not write a file without having parsed one.")
