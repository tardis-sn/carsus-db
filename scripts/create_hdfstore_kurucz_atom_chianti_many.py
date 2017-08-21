""" Example script to create an HDFStore from the database """

from carsus import init_db
from carsus.io.output import AtomData
from carsus.model import DataSource


# Name of the database file to export
dbname = "sqlite:///../databases/kurucz_cd23_chianti_all.db"

# Name of the output file
storename = "../hdfstores/kurucz_atom_chianti_many.h5"

chianti_ions = 'H-He; Si II; Ca II; Mg II; S II'

session = init_db(dbname)

# Chianti database version
chianti_short_name = (
            session.
            query(DataSource.short_name).
            filter(DataSource.short_name.like('chianti%'))
            ).one()[0]


print('Initializing AtomData')
ad = AtomData(
        session,
        selected_atoms='H-Zn',
        chianti_ions=chianti_ions,
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
        store_collisions=True,
        store_zeta_data=True
        )
