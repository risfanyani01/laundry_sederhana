from odoo import api, fields, models

class m_pelanggan(models.Model):
    _inherit = 'res.partner'

    cucian_id = fields.Many2one('model.cucian', string='Cucian')
    jenis_kelamin = fields.Selection([
        ('l', 'Laki-Laki'),
        ('p', 'Perempuan')
    ], string='jenis_kelamin')   
