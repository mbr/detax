#!/usr/bin/python3

from math import floor


class TaxData(object):
    def __init__(self, year):
        self.year = year
        self.income = 0
        self.children = []
        self.tax_class = 1
        self.state = 'BW'
        self.church_tax = False

    @property
    def num_children(self):
        return len(self.children)

    @property
    def church_tax_rate(self):
        if self.state in ('BW', 'BY'):
            return 0.08
        else:
            return 0.09

    @property
    def church_tax_cap(self):
        if self.state != 'BW':
            raise NotImplementedError

        if self.church_tax == 'rk':
            return 0.035
        elif self.church_tax == 'ev':
            return 0.025

        return 0

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

                # 20% Differenz Freigrenze zu Bemessungsgrundlage (= ESt)
                sdiff = round((taxes[0][0] - 972) * 0.20, 2)
                taxes.append((min(soli, sdiff), 'Solidaritätszuschlag'))
        else:
            raise NotImplementedError

        if self.church_tax:
            church_tax_real = round(taxes[0][0] * self.church_tax_rate, 2)
            taxes.append((church_tax_real, "Kirchensteuer"))

        return taxes

    def __str__(self):
        if self.church_tax:
            longname = ('katholisch'
                        if self.church_tax == 'rk' else 'evangelisch')
            ctax = '{}, {:>2.02f} %'.format(longname,
                                            self.church_tax_rate * 100)
        else:
            ctax = 'no'

        if self.church_tax_cap:
            ctax += ', capped at {:.02f} % total income'.format(
                self.church_tax_cap * 100)

        return ('Steuerjahr: {s.year}\n'
                'Bundesland: {s.state}\n'
                'Einkommen: {s.income} €\n'
                'Anz. Kinder: {s.num_children}\n'
                'Steuerklasse: {s.tax_class}\n'
                'Kirchensteuer: {}'.format(ctax, s=self))
