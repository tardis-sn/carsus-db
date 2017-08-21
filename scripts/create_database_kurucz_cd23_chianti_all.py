""" Example script to create a database """

from create_database import (
        create_base_db,
        add_chianti,
        add_kurucz
        )


if __name__ == "__main__":
    # Provide the path to the database
    db_fname = "sqlite:///../databases/kurucz_cd23_chianti_all.db"

    # Provide the path to the zeta file
    zeta_fname = "../zeta/knox_long_recombination_zeta.dat"

    # Provide the path to the gfall file
    gfall_fname = "../gfall/gfall_old.dat"

    session = create_base_db(
            db_fname,
            zeta_fname
            )

    add_kurucz(session, gfall_fname)

    add_chianti(session, ions='H-Zn')

    session.close()
