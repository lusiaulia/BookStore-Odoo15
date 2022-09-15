# -*- coding: utf-8 -*-
# from odoo import http


# class Luffy(http.Controller):
#     @http.route('/luffy/luffy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/luffy/luffy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('luffy.listing', {
#             'root': '/luffy/luffy',
#             'objects': http.request.env['luffy.luffy'].search([]),
#         })

#     @http.route('/luffy/luffy/objects/<model("luffy.luffy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('luffy.object', {
#             'object': obj
#         })
