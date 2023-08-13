from odoo import api, fields, models


class penerbit(models.Model):
    _name = 'luffy.penerbit'
    _description = 'New Description'

    name = fields.Char(string='Nama Penerbit')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    buku_id = fields.Many2many(comodel_name='luffy.buku', string='Buku')
    
    
    



