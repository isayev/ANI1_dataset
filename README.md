This repository contains the files and scripts needed to access the ANI-1 data set. Data used in the training of machine learned potentials:

Original ANI-1 potential paper where this data set was first used.

Justin S. Smith, Olexandr Isayev, Adrian E. Roitberg. *ANI-1: An extensible neural network potential with DFT accuracy at force field computational cost.* Chemical Science, 2017, DOI: 10.1039/C6SC05720A 

## Required software
Python3.5 or better
Numpy
H5PY

## Included extraction software
pyanitools.py
	-Contains a class called 
	 "anidataloader" for loading
	 and parsing the ANI-1 data set.

example_data_sampler.py
	-Example of how to sample data
	from the anidataloader class.

## Installation instructions

1) export ANI-1_release/readers/lib/ to PYTHONPATH.

2) Run: example_data_sampler.py to test


## Data Units
Coordinates: Angstroms
Energies: Hartrees

## Self-interaction atomic energies
H=-0.500607632585
C=-37.8302333826
N=-54.5680045287
O=-75.0362229210
