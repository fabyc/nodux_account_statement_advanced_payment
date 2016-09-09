# This file is part of the sale_payment module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .statement import *

def register():
    Pool.register(
        Line,
        module='nodux_account_statement_advanced_payment', type_='model')
