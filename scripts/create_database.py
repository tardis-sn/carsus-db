""" Example script to create a database """

from carsus import init_db
from carsus.io.nist import (
        NISTWeightsCompIngester,
        NISTIonizationEnergiesIngester
        )
from carsus.io.kurucz import GFALLIngester
from carsus.io.chianti_ import ChiantiIngester
from carsus.io.zeta import KnoxLongZetaIngester


def create_base_db(db_fname, zeta_fname):
    """
    Create a database

    Parameters
    ----------
    db_fname : str
        Filename for the database
    zeta_fname : str
        Filename for the Zeta file
    """

    session = init_db(db_fname)
    session.commit()

    # Ingest atomic weights
    weightscomp_ingester = NISTWeightsCompIngester(session)
    weightscomp_ingester.ingest()
    session.commit()

    # Ingest ionization energies
    ioniz_energies_ingester = NISTIonizationEnergiesIngester(
            session,
            spectra="h-zn"
            )
    ioniz_energies_ingester.ingest(
            ionization_energies=True,
            ground_levels=True
            )
    session.commit()

    zeta_ingester = KnoxLongZetaIngester(session, zeta_fname)
    zeta_ingester.ingest()
    session.commit()

    return session


def add_kurucz(session, gfall_fname):
    # Ingest kurucz levels and lines
    gfall_ingester = GFALLIngester(session, gfall_fname, ions='H-Zn')
    gfall_ingester.ingest(levels=True, lines=True)
    session.commit()


def add_chianti(session, ions='H-He', collisions=True):
    # Ingest chianti levels, lines and electron collisions
    # H I, He I-II
    chianti_ingester = ChiantiIngester(session, ions=ions)
    chianti_ingester.ingest(levels=True, lines=True, collisions=collisions)
    session.commit()
