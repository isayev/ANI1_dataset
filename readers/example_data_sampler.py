import lib.pyanitools as pya
import os

# Set the HDF5 file containing the testdata
hdf5file = os.path.join(os.path.dirname(__file__), './../benchmark/ani1_gdb10_ts.h5')

# Construct the data loader class
adl = pya.anidataloader(hdf5file)

# Print the species of the data set one by one
for data in adl:

    # Extract the data
    P = data['path']
    X = data['coordinates']
    E = data['energies']
    S = data['species']
    sm = data['smiles']

    # Print the data
    print("Path:   ", P)
    print("  Smiles:      ","".join(sm))
    print("  Symbols:     ", S)
    print("  Coordinates: ", X)
    print("  Energies:    ", E, "\n")

# Closes the H5 data file
adl.cleanup()
