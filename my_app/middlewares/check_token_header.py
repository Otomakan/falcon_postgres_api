import falcon, base64
from ..helpers import PwdHelper


class HeaderMiddleware(object):
    def process_response(self, req, resp, resource, req_succeeded):
        
        if not req.path in ['/users/login','/users']:
            print(req.headers)
            # print()
            token = req.get_header('token')
            
            if token is None:
                description = ('Please provide an auth token '
                               'as part of the request.')

                raise falcon.HTTPUnauthorized('Auth token required',
                                              description,
                                              href='http://docs.example.com/auth')

            
            # token = base64.b64decode(token)
            # .decode('utf-8')
            # token = token.hex()
            print("TOKEN IS")
            print(token)
            # print("OR")
            # print(t)
            # user_table = UserTable(session)
            # valid = user_table.check_token(token)
            valid = PwdHelper.verify_token(token)
            
            if not valid:
                description = ('The token is invlaid please provide a valid token')

                raise falcon.HTTPUnauthorized('Auth token required',
                                              description,
                                              href='http://docs.example.com/auth')

