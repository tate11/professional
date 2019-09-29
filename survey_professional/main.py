import logging

from odoo import fields, http, SUPERUSER_ID, _
from odoo.http import request
from odoo.addons.survey_conditional_questions.controllers.main import SurveyConditional as SurveyController 


_logger = logging.getLogger(__name__)


# code from survey_action
# inherit from survey_conditional_questions instead of survey
class SurveyController2(SurveyController):

    @http.route()
    def fill_survey(self, survey, token, prev=None, **post):

        user_input = request.env['survey.user_input'].sudo().search([('token', '=', token)], limit=1)

        if user_input and user_input.state[:3] == 'new':

            user_input.state = 'new'
        
        if user_input and user_input.state == 'done':
        
            action = survey.server_action_id
            user = survey.company_id.user_tech_id
            if action and user:
                url = action.with_context(active_id=user_input.id, active_model='survey.user_input', website_id=request.website.id).sudo(user).run()
                return request.redirect(url)

        return super(SurveyController2, self).fill_survey(survey, token, prev, **post)

