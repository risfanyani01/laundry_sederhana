from email.policy import default
from unicodedata import name
from odoo import api, fields, models
from datetime import datetime

class m_transaksi(models.Model):
    _inherit = 'account.move'
    
    costumer_id = fields.Many2one('model.cucian', string='Nama Pelanggan')
    berat_cucian = fields.Float(compute='_compute_berat', string='Berat (Kg)')
    harga_cucian = fields.Float(compute='_compute_harga', string='Harga Perkilo')
    total = fields.Float(compute='_compute_total', string='Total Bayar')
    tanggal_masuk_cucian = fields.Date(compute='_compute_tanggal_masuk', string='Tanggal Masuk')
    tanggal_selesai = fields.Date(string='Tanggal Selesai', default=datetime.today(), readonly=True)
    uang = fields.Float('Jumlah Uang')
    uang_kembali = fields.Float(compute='_compute_uang_kembali', string='Uang Kembali')
    
    @api.depends('costumer_id')
    def _compute_berat(self):
        for record in self:
            record.berat_cucian = record.costumer_id.berat
    
    @api.depends('costumer_id')
    def _compute_harga(self):
        for record in self:
             record.harga_cucian = record.costumer_id.harga
    
    @api.depends('costumer_id')
    def _compute_tanggal_masuk(self):
        for record in self:
            record.tanggal_masuk_cucian = record.costumer_id.tanggal_masuk

    @api.depends('berat_cucian', 'harga_cucian')
    def _compute_total(self):
        for record in self:
            record.total = record.berat_cucian * record.harga_cucian
    
    @api.depends('total', 'uang')
    def _compute_uang_kembali(self):
        for record in self:
            record.uang_kembali = record.uang - record.total