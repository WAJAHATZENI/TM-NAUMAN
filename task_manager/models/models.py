
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Task(models.Model):
    _name = 'task.task'
    _description = 'Task Management'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    deadline = fields.Date(string='Deadline')
    completed = fields.Selection([('completed', 'COMPLETED'), ('draft', 'DRAFT')],string='Completed')
    days_left = fields.Integer(string='Days Left', compute='_compute_days_left', store=True)

    @api.depends('deadline')
    def _compute_days_left(self):
        today = fields.Date.today()

        for task in self:
            if task.deadline:
                if task.deadline >= today:
                    if task.deadline:
                        task.days_left = (task.deadline - today).days
                    else:
                        task.days_left = 0
                else:
                    raise ValidationError('Deadline should be greater than current date')



    def mark_as_completed(self):
        # self.write({'completed': True})
        self.completed = 'completed'

