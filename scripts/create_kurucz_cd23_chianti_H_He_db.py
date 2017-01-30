""" Example script to create a database """

from carsus import init_db
from carsus.io.nist import NISTWeightsCompIngester, NISTIonizationEnergiesIngester
from carsus.io.kurucz import GFALLIngester
from carsus.io.chianti_ import ChiantiIngester

def create_test_db(db_fname, gfall_fname):
    """
    Create a database

    Parameters
    ----------
    db_fname : str
        Filename for the database
    gfall_fname : str
        Filename for the GFALL file
    """

    session = init_db(db_fname)
    session.commit()

    # Ingest atomic weights
    weightscomp_ingester = NISTWeightsCompIngester(session)
    weightscomp_ingester.ingest()
    session.commit()

    # Ingest ionization energies
    ioniz_energies_ingester = NISTIonizationEnergiesIngester(session, spectra="h-zn")
    ioniz_energies_ingester.ingest(ionization_energies=True, ground_levels=True)
    session.commit()

    # Ingest kurucz levels and lines
    gfall_ingester = GFALLIngester(session, gfall_fname, ions='H-Zn')
    gfall_ingester.ingest(levels=True, lines=True)
    session.commit()

    # Ingest chianti levels, lines and electron collisions
    # H I, He I-II
    chianti_ingester = ChiantiIngester(session, ions='H-He')
    chianti_ingester.ingest(levels=True, lines=True, collisions=True)
    session.commit()

    session.close()


if __name__ == "__main__":
    db_fname = "path/to/empty.db"  # Provide the path to the database
    gfall_fname = "path/to/gfall.dat"  # Provide the path to the gfall file
    create_test_db(db_fname=db_fname, gfall_fname=gfall_fname)
