# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleCostum/mLoundry(http.Controller):
#     @http.route('/module_costum/m_loundry/module_costum/m_loundry/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_costum/m_loundry/module_costum/m_loundry/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_costum/m_loundry.listing', {
#             'root': '/module_costum/m_loundry/module_costum/m_loundry',
#             'objects': http.request.env['module_costum/m_loundry.module_costum/m_loundry'].search([]),
#         })

#     @http.route('/module_costum/m_loundry/module_costum/m_loundry/objects/<model("module_costum/m_loundry.module_costum/m_loundry"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_costum/m_loundry.object', {
#             'object': obj
#         })
