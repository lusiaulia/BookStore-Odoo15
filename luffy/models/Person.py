from odoo import api, fields, models


class person(models.Model):
    _name = 'luffy.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    panggilan = fields.Char(string='Nama Panggilan')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Date(string='Tanggal Lahir')

class Kasir(models.Model):
    _name = 'luffy.kasir'
    _inherit = 'luffy.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID Kasir')


class AdminTokoOnline(models.Model):
    _name = 'luffy.admintokoonline'
    _inherit = 'luffy.person'
    _description = 'New Description'

    id_admintokoonline = fields.Char(string='ID Admin Toko Online')


class CleaningService(models.Model):
    _name = 'luffy.cleaningservice'
    _inherit = 'luffy.person'
    _description = 'New Description'

    id_cleaningservice = fields.Char(string='ID Cleaning Service')
