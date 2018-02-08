from datetime import date

import click

from . import TaxData


@click.command()
@click.argument('income', type=float)
@click.option('--year', '-y', type=int, help='Tax year')
@click.option('-c', '--church-tax', type=click.Choice(['rk', 'ev']))
@click.option('-s', '--state', default='BW')
@click.option(
    '-p/-P',
    '--perc/--no-perc',
    default=True,
    help='Show total tax percentage')
def cli(income, year, church_tax, state, perc):
    if year is None:
        year = date.today().year

    d = TaxData(year)
    d.income = income
    d.church_tax = church_tax
    d.state = state

    click.echo(d)
    click.echo()

    tax = d.calc_tax()

    tpl = '{:>11.2f} €    {}'

    for amount, title in tax:
        click.echo(tpl.format(amount, title))
    click.echo('-------------')

    total = sum(e[0] for e in tax)
    click.echo(tpl.format(total, 'Gesamt'))

    if perc:
        click.echo('Tax percentage: {:.1f}%'.format(total * 100.0 / income))


if __name__ == '__main__':
    cli()
