import falcon
import json
from pdf_maker import make_pdf
# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class RequireJSON(object):

    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(
                'This API only supports responses encoded as JSON.',
                href='http://docs.examples.com/api/json')

        if req.method in ('POST', 'PUT'):
            if 'application/json' not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType(
                    'This API only supports requests encoded as JSON.',
                    href='http://docs.examples.com/api/json')


class ThingsResource(object):
    # def on_get(self, req, resp):
    #     """Handles GET requests"""
    #     resp.status = falcon.HTTP_200  # This is the default status
    #     resp.body = ('\nTwo things awe me most, the starry sky '
    #                  'above me and the moral law within me.\n'
    #                  '\n'
    #                  '    ~ Immanuel Kant\n\n')
    def on_post(self, req, resp):
       	posted_data = json.loads(req.stream.read())
       	for key in posted_data:
       		print(key)
       		print(posted_data[key])
       	make_pdf(posted_data)
       	# with open('out.pdf', 'r') as file:
       	resp.stream = open('out.pdf', 'r')
       	resp.downloadable_as = 'out.pdf'        
       	resp.status = falcon.HTTP_200
  
# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/users', things)
