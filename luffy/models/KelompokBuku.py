from sys import api_version
from odoo import api, fields, models


class kelompokbuku(models.Model):
    _name = 'luffy.kelompokbuku'
    _description = 'New Description'

    name = fields.Selection([
        ('novel','Novel'),
        ('komik','Komik'),
        ('cerpen','Cerpen'),
        ('majalah','Majalah'),
        ('self improvement','Self Improvement'),
        ('kamus','Kamus'),
        ('ensiklopedi','Ensiklopedi'),
        ('antologi','Antologi'),
        ('tafsir','Tafsir'),
        ('panduan','Panduan'),
        ('buku ilmiah','Buku Ilmiah')],string='Nama Kelompok Buku')
    
    kode_kelompok = fields.Char(string='Kode Kelompok Buku')

    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if self.name =='novel':
            self.kode_kelompok = '001'
        elif self.name =='komik':
            self.kode_kelompok = '002'
        elif self.name == 'cerpen' :
            self.kode_kelompok = '003'
        elif self.name == 'majalah' :
            self.kode_kelompok = '101'
        elif self.name =='self improvement':
            self.kode_kelompok = '102'
        elif self.name == 'kamus' :
            self.kode_kelompok = '201'
        elif self.name == 'ensiklopedi' :
            self.kode_kelompok = '202'
        elif self.name == 'antologi' :
            self.kode_kelompok = '203'
        elif self.name =='tafsir':
            self.kode_kelompok = '204'
        elif self.name == 'panduan':
            self.kode_kelompok = '205'
        elif self.name =='buku ilmiah':
            self.kode_kelompok = '206'

        
    kode_rak = fields.Char(string='Kode Rak')
    buku_ids = fields.One2many(comodel_name='luffy.buku', 
                               inverse_name='kelompokbuku_id', 
                               string='Daftar Buku')
    
    jml_item = fields.Char(compute= '_compute_jml_item', string='Jumlah Item')

    field_name = fields.Char(compute='_compute_field_name', string='field_name')
    
    @api.depends('buku_ids')
    def _compute_jml_item(self):
        for record in self :
            a = self.env['luffy.buku'].search([('kelompokbuku_id', '=',record.id)]).mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a

    daftar = fields.Char(string='Daftar Isi')
    
    
    
    
    
