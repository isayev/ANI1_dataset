import pyanitools as pya

# Set the HDF5 file containing the data
hdf5file = '../ani_gdb_s01.h5'

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
