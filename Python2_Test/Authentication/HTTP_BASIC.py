# from flask import Flask, render_template
# 
# from flask_basicauth import BasicAuth
# 
# 
# app = Flask(__name__)
# 
# app.config['BASIC_AUTH_USERNAME'] = 'john'
# app.config['BASIC_AUTH_PASSWORD'] = 'matrix'
# 
# basic_auth = BasicAuth(app)
# 
# @app.route('/secret')
# @basic_auth.required
# def secret_view():
#     return render_template('secret.html')
# 
# 
# if __name__ == '__main__':
#     app.run(debug=True, port=65010)



# from functools import wraps
# 
# from flask import request, Response
# from flask import Flask, render_template
# 
# 
# app = Flask(__name__)
# 
# 
# def check_auth(username, password):
#     """This function is called to check if a username /
#     password combination is valid.
#     """
#     return username == 'admin' and password == 'secret'
# 
# def authenticate():
#     """Sends a 401 response that enables basic auth"""
#     return Response(
#     'Could not verify your access level for that URL.\n'
#     'You have to login with proper credentials', 401,
#     {'WWW-Authenticate': 'Basic realm="Login Required"'})
# 
# def requires_auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         auth = request.authorization
#                
#         if not auth or not check_auth(auth.username, auth.password):            
#             return authenticate()
#                 
#         return f(*args, **kwargs)
#     return decorated
# 
# 
# @app.route('/secret-page')
# @requires_auth
# def secret_page():
#     return render_template('secret_page.html')


import base64

myUser = 'nfv2'
myPass = '4321'
authString = base64.encodestring('%s:%s' % (myUser, myPass))
headers = {'Authorization':"Basic %s" % authString}



print authString

##########################################
decoded_text = base64.b64decode(headers['Authorization'].split()[1])


id = decoded_text.split(':')[0]
pw = decoded_text.split(':')[1]

print id ,pw


# from flask import Flask
# from flask_restful import Resource, Api
# 
# 
# app = Flask(__name__)
# api = Api(app)
# 
# if __name__ == '__main__':
#     app.run(debug=True)
# 
# 
# USER_DATA = {
#     "admin": "SuperSecretPwd"
# }
# 
# 
# def verify(username, password):
#     if not (username and password):
#         return False
#     return USER_DATA.get(username) == password


# if __name__ == '__main__':
#     app.run(debug=True, port=65010)





# import urllib2, base64 
# request = urllib2.Request("http://api.foursquare.com/v1/user") 
# base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
# request.add_header("Authorization", "Basic %s" % base64string) 
# result = urllib2.urlopen(request)


