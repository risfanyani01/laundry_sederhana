from email.policy import default
import string
from odoo import api, fields, models, _
import time
from datetime import datetime

class m_cucian(models.Model):
    _name = "model.cucian"
    _description = "Daftar Cucian"
    _order = 'id desc'

    def func_proses(self):
        if self.status == 'belum':
            self.status = 'proses'

    def func_selesai(self):
        if self.status == 'proses':
            self.status = 'selesai'

    def func_diambil(self):
        if self.status == 'selesai':
            self.status = 'diambil'

    name = fields.Many2one('res.partner', string='Costumer')
    petugas_id = fields.Many2one('hr.employee', string='Petugas', required=True)
    jenis_cucian_id = fields.Many2one('jenis.cucian', string='Jenis Cucian')
    berat = fields.Float('Berat Cucian')
    harga = fields.Float('Harga Perkilo')
    tanggal_masuk = fields.Date(string='Tanggal Masuk', default=datetime.today())
    status = fields.Selection([
        ('belum', 'Belum di Proses'),
        ('proses', 'Sedang di Proses'),
        ('selesai', 'Sudah Selesai'),
        ('diambil', 'Sudah Diambil'),
    ], string='status', default="belum")
    cucian_tambahan_ids = fields.One2many('cucian.tambahan', 'cucian_tambahan_id')
    # total_bayar = fields.Float(compute='_compute_total_bayar', string='Total Bayar')

    _sql_constraints = [
        ("kode_unique", "unique(kode_cucian)", "Kode Cucian Tidak Boleh Sama"),
    ]

    # name = fields.Char(string='Kode Cucian', readonly=True)
    
    # # def name_get(self):
    # #     return [(r.id, r.name + '# '+r.jenis_cucian_id.name) for r in self]

    # @api.model
    # def create(self, vals):
    #     vals['name'] = self.env['ir.sequence'].next_by_code('model.cucian')
    #     return super(m_cucian, self).create(vals)

    @api.onchange('jenis_cucian_id')
    def _onchange_jenis_cucian(self):
        for i in self:
            if i.jenis_cucian_id:
                i.harga = i.jenis_cucian_id.harga
    
    # @api.depends('berat', 'harga')
    # def _compute_total_bayar(self):
    #     for i in self:
    #         i.total_bayar = i.berat * i.harga

class jenis_cucian(models.Model):
    _name = 'jenis.cucian'
    _description = 'Jenis Cucian'

    name = fields.Char('Jenis Cucian')
    harga = fields.Float('Harga Perkilo')

    _sql_constraints = [
        ('unique_id', 'unique(nama_jenis_cucian)', 'Jenis Cucian duplicate, mohon cek kembali !'),
    ]

class cucian_tambahan(models.Model):
    _name = 'cucian.tambahan'
    _description = 'Cucian Tambahan'

    cucian_tambahan_id = fields.Many2one('model.cucian')
    cucian_tambahan = fields.Char('Cucian Tambahan')
    harga_tambahan = fields.Float('Harga')
    kuantitas = fields.Integer('Kuantitas')