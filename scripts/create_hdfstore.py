""" Example script to create an HDFStore from the database """

from carsus import init_db
from carsus.io.output import AtomData


# Name of the database file to export
dbname = "path/to/nonempty.db"  # Provide the path to the database
session = init_db(dbname)

# Chianti database version
chianti_short_name = 'chianti_v8.0.X'

# Name of the output file
storename = "/tmp/hdfstore.h5"

print('Initializing AtomData')
ad = AtomData(
        session,
        selected_atoms='H-Zn',
        chianti_ions="H; He",
        chianti_short_name=chianti_short_name
        )

print('Exporting to hdf.')
ad.to_hdf(
        storename,
        store_atom_masses=True,
        store_ionization_energies=True,
        store_levels=True,
        store_lines=True,
        store_macro_atom=True,
        store_collisions=False,
        store_zeta_data=True
        )
