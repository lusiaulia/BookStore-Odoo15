from odoo import api, fields, models


class buku(models.Model):
    _name = 'luffy.buku'
    _description = 'New Description'

    name = fields.Char(string='Nama Buku')
    harga_beli = fields.Integer(string='Harga Modal',required = True)
    harga_jual = fields.Integer(string='Harga Jual', required = True)
    kelompokbuku_id = fields.Many2one(comodel_name='luffy.kelompokbuku', 
                                      string='Kelompok Buku',
                                      ondelete = 'cascade')

    penerbit_id = fields.Many2many(comodel_name='luffy.penerbit', string='Penerbit')
    persediaan = fields.Integer(string='Persediaan')
    
