from django.template.response import TemplateResponse

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

class NotificationsMiddleware(MiddlewareMixin):
    def process_template_response(self, request, response):
        # if not ('notification_count' in response.context_data):
        response.context_data['notification'] = "I AM HERE"
        # context = {
        #     "notification": "YYYYYYYY"
        # }
        # response = TemplateResponse(request, '../registration/templates/base.html', context)
        print('here')
        return response

    def process_request(self, req):
        # req.dept = "OS"
        # print('nowwww')
        return None