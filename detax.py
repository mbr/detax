# coding: utf8
from datetime import date
from math import floor

import click


class TaxData(object):
    def __init__(self, year):
        self.year = year
        self.income = 0
        self.children = []
        self.tax_class = 1

    def calc_tax(self):
        if self.children:
            raise NotImplementedError

        if self.year not in (2015, 2016, 2017):
            raise NotImplementedError

        if self.tax_class != 1:
            raise NotImplementedError

        taxes = []

        # Grundfreibetrag
        if self.income <= 8652:
            taxes.append((0, 'Grundfreibetrag'))
        elif self.income <= 13669:
            y = (self.income - 8652) / 10000.0
            t = floor((993.62 * y + 1400) * y)
            taxes.append((t, 'Einkommenssteuer'))
        elif self.income <= 53665:
            z = (self.income - 13669) / 10000.0
            t = floor((225.4 * z + 2397) * z + 952.48)
            taxes.append((t, 'Einkommenssteuer'))
        elif self.income <= 254446:
            t = floor(0.42 * self.income - 8394.14)
            taxes.append((t, 'Einkommenssteuer'))
        else:
            t = floor(0.45 * self.income - 16027.52)
            taxes.append((t, 'Einkommenssteuer'))

        if self.tax_class == 1:
            if taxes[0][0] > 972:
                # Solidaritätszuschlag
                soli = round(taxes[0][0] * 0.055, 2)
                taxes.append((soli, 'Solidaritätszuschlag'))
        else:
            raise NotImplementedError

        return taxes


@click.command()
@click.argument('income', type=float)
@click.option('--year', '-y', type=int, help='Tax year')
def cli(income, year):
    if year is None:
        year = date.today().year

    d = TaxData(year)
    d.income = income

    tax = d.calc_tax()

    print(tax)
    print('Total: {:.2f} EUR'.format(sum(e[0] for e in tax)))


if __name__ == '__main__':
    cli()
