""" Example script to create an HDFStore from the database """

from carsus import init_db
from carsus.io.output import AtomData


dbname = "path/to/nonempty.db"  # Provide the path to the database
session = init_db(dbname)
ad = AtomData(session, selected_atoms='H-Zn', chianti_ions="H; He")
storename = "path/to/hdfstore.h5"
ad.to_hdf(storename, store_atom_masses=True, store_ionization_energies=True,
	store_levels=True, store_lines=True, store_macro_atom=True, store_collisions=False,
	store_zeta_data=True)
