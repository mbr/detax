German income tax calculation
=============================

This is an experimental package, allowing the calculation of income tax rates
in Germany (useful for freelancers, since they usually pay tax once per year
only, resulting in a substantial amount owed).

The package is fairly incomplete, but can be used as a starting point; bug
reports, feedback and pull requests are **very** welcome.


CLI
---

While being usable as a library, the package comes with an optional `CLI`. To
use it, the `click` package must be installed as well:

.. code-block:: python

  $ detax --help
  Usage: detax [OPTIONS] INCOME

  Options:
    -y, --year INTEGER          Tax year
    -c, --church-tax [rk|ev]
    -s, --state TEXT
    -p, --perc / -P, --no-perc  Show total tax percentage
    --help                      Show this message and exit.

An example calculation for Baden-Württemberg:

.. code-block:: python

  $ detax -y 2017 -c rk -s BW 50000
  Steuerjahr: 2017
  Bundesland: BW
  Einkommen: 50000.0 €
  Anz. Kinder: 0
  Steuerklasse: 1
  Kirchensteuer: katholisch, 8.00 %, capped at 3.50 % total income

     12636.00 €    Einkommenssteuer
       694.98 €    Solidaritätszuschlag
      1010.88 €    Kirchensteuer
  -------------
     14341.86 €    Gesamt
  Tax percentage: 28.7%

