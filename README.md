# ANI-1 dataset support repository
This repository contains the scripts needed to access the ANI-1 data set.

##### If you use ANI-1 dataset please cite the following two papers: 

Justin S. Smith, Olexandr Isayev, Adrian E. Roitberg. *ANI-1: An extensible neural network potential with DFT accuracy at force field computational cost.* Chemical Science, 2017, DOI: 10.1039/C6SC05720A 

Justin S. Smith, Olexandr Isayev, Adrian E. Roitberg. *ANI-1, A data set of 20 million calculated off-equilibrium conformations for organic molecules.*  Scientific Data, 4, Article number: 170193, DOI: 10.1038/sdata.2017.193 https://www.nature.com/articles/sdata2017193

### Required software
Python3.5 or better
Numpy
H5PY

### Included extraction software
pyanitools.py
	-Contains a class called 
	 "anidataloader" for loading
	 and parsing the ANI-1 data set.

example_data_sampler.py
	-Example of how to sample data
	from the anidataloader class.

### Installation instructions

1) export ANI-1_release/readers/lib/ to PYTHONPATH.

2) Run: example_data_sampler.py to test

### Description
The downloaded file (https://doi.org/10.6084/m9.figshare.c.3846712) can be extracted on a Unix based system with the “tar -xzf ani-1_dataset.tar.gz” command. Once extracted, a folder named “ANI-1_release” is the root directory for all files. The individual data files are separated into 8 HDF5 files (extension .h5) named ani_gdb_s0x.h5 where x is a number between 1 and 8 representing the number of heavy atoms (CNO) in the molecules contained in the file. The README file contains information about the data set and scripts included. The folder named “readers” has a code sample for reading the HDF5 file called “example_data_sampler.py” and “lib/pyanitools.py”, which contains classes for loading and storing data in our in-house format.
File format

The ANI-1 data set is stored in the HDF5 [http://www.hdfgroup.org/HDF5] file format. Two python classes are included with the data set’s compressed archive in the python file: “ANI-1_release/readers/lib/pyanitools.py”. These classes are only tested for python version 3.5 and greater, and requires the h5py library [http://www.h5py.org/]. An example script for reading the data from the HDF5 files is given in: “ANI-1_release/readers/example_data_sampler.py”.

### Data Units
Coordinates: Angstroms
Energies: Hartrees

### Self-interaction atomic energies
H = -0.500607632585
C = -37.8302333826
N = -54.5680045287
O = -75.0362229210

## Related work

### Developing the ANI-1x potential with active learning:
Justin S. Smith, Ben Nebgen, Nicholas Lubbers, Olexandr Isayev, Adrian E. Roitberg. *Less is more: sampling chemical space with active learning*. arXiv, 2018, DOI: [arXiv:1801.09319] (https://arxiv.org/abs/1801.09319)
