from odoo import models, api

class GradeReport(models.AbstractModel):
    _name = 'report.student_test.grade_report_template'
    _description = 'Grade Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        grades = self.env['student_test.grade'].browse(docids)
        return {
            'grades': grades,
        }
