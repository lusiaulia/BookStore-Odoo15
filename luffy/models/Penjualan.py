from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError


class Penjualan(models.Model):
    _name = 'luffy.penjualan'
    _description = 'Penjualan'

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    tgl_penjualan = fields.Datetime(
        string='Tanggal Transaksi',
        default=fields.Datetime.now())
    total_bayar = fields.Integer(
        string='Total Pembayaran',
        compute='_compute_totalbayar')
    detailpenjualan_ids = fields.One2many(
        comodel_name='luffy.detailpenjualan',
        inverse_name='penjualan_id',
        string='Detail Penjualan')
    
    def unlink(self):
        if self.detailpenjualan_ids:
            penjualan = []
            for line in self:
                penjualan = self.env['luffy.detailpenjualan'].search(
                    [('penjualan_id', '=', line.id)])
                print(penjualan)

            for ob in penjualan:
                print(ob.buku_id.name + ' ' + str(ob.qty))
                ob.buku_id.persediaan += ob.qty

        line = super(Penjualan, self).unlink()

    def write(self, vals):
      for line in self:
          data_asli = self.env['luffy.detailpenjualan'].search([('penjualan_id', '=', line.id)])
          print(data_asli)

          for data in data_asli:
              print(str(data.buku_id.name) + " " + str(data.qty) + ' ' + str(data.buku_id.persediaan))
              data.buku_id.persediaan += data.qty
      
      line = super(Penjualan, self).write(vals)
      
      for line in self:
          data_setelah_edit = self.env['luffy.detailpenjualan'].search([('penjualan_id', '=', line.id)])
          print(data_asli)
          print(data_setelah_edit)

          for data_baru in data_setelah_edit:
              if data_baru in data_asli:
                  print(data_baru.buku_id.name + " " + str(data_baru.qty) + ' ' + str(data_baru.buku_id.persediaan))
                  data_baru.buku_id.persediaan -= data_baru.qty
              else:
                  pass

      return line

    _sql_constraints = [
        ('no_nota_unik','unique (name)','Nomor Nota tidak boleh sama !!')
    ]

    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for line in self:
            result = sum(self.env['luffy.detailpenjualan'].search(
                [('penjualan_id', '=', line.id)]).mapped('subtotal'))
            line.total_bayar = result


class DetailPenjualan(models.Model):
    _name = 'luffy.detailpenjualan'
    _description = 'Detail'

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(
        comodel_name='luffy.penjualan',
        string='Detail Penjualan')
    buku_id = fields.Many2one(
        comodel_name='luffy.buku',
        string='List Buku')
    harga_satuan = fields.Integer(
        string='Harga Satuan',
        onchange='_onchange_buku_id')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.qty * line.harga_satuan

    @api.model
    def create(self, vals):
        line = super(DetailPenjualan, self).create(vals)
        if line.qty:
            # Mendapatkan data berdasarkan ID pada buku_id
            self.env['luffy.buku'].search(
                [('id', '=', line.buku_id.id)]
            ).write({'persediaan': line.buku_id.persediaan - line.qty})

        return line

    @api.onchange('buku_id')
    def _onchange_buku_id(self):
        if self.buku_id.harga_jual:
            self.harga_satuan = self.buku_id.harga_jual

    @api.constrains('qty')
    def check_quantity(self):
        for rec in self :
            if rec.qty < 1:
                raise ValidationError("Hei hei jangan lupa pilih mau beli berapa Buku {} nya ><..".format(rec.buku_id.name))
            elif (rec.buku_id.persediaan < rec.qty):
                raise ValidationError(
                    'Persediaan Buku {} tidak mencukupi, hanya tersedia {}'. format(rec.buku_id.name, rec.buku_id.persediaan))