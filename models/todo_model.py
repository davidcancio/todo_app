# -*- coding: utf-8 -*-
from odoo import models, fields
class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-do Task'
    _description = 'To-do Task'
    name = fields.Char('Description', required=True)
    id_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)