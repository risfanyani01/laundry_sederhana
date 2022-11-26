from email.policy import default
from time import time
from odoo import api, fields, models
import time
from datetime import datetime

class m_karyawan(models.Model):
    _inherit = 'hr.employee'

    name = fields.Char('Kode Karyawan')
    jenis_kelamin = fields.Selection([
        ('l', 'Laki-Laki'),
        ('p', 'Perempuan')
    ], string='Jenis Kelamin')
    tanggal_lahir = fields.Date('Tanggal Lahir')
    tanggal_bergabung = fields.Date(string='Tanggal Bergabung', default=datetime.today())
    usia = fields.Integer('Usia')
    alamat = fields.Text('Alamat')
    ref = fields.Char(string='Kode Karyawan', readonly=True)
 
    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hr.employee')
        return super(m_karyawan, self).create(vals)
