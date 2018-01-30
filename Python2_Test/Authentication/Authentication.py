CLIENT_ID = "p-jcoLKBynTLew"
CLIENT_SECRET = "gko_LXELoV07ZBNUXrvWZfzE3aI"
REDIRECT_URI = "http://localhost:65010/reddit_callback"

from flask import Flask
app = Flask(__name__)

from flask import abort, request
@app.route('/reddit_callback')
def reddit_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    state = request.args.get('state', '')
    if not is_valid_state(state):
        # Uh-oh, this request wasn't started by us!
        abort(403)
    code = request.args.get('code')
    # We'll change this next line in just a moment
    return "got a code! %s" % code


@app.route('/')
def homepage():
    text = '<a href="%s">Authenticate with reddit</a>'
    return text % make_authorization_url()

def make_authorization_url():
    # Generate a random string for the state parameter
    # Save it for use later to prevent xsrf attacks
    from uuid import uuid4
    state = str(uuid4())
    save_created_state(state)
    params = {"client_id": CLIENT_ID,
              "response_type": "code",
              "state": state,
              "redirect_uri": REDIRECT_URI,
              "duration": "temporary",
              "scope": "identity"}
    import urllib
    url = "https://ssl.reddit.com/api/v1/authorize?" + urllib.urlencode(params)
    return url

# Left as an exercise to the reader.
# You may want to store valid states in a database or memcache,
# or perhaps cryptographically sign them and verify upon retrieval.
def save_created_state(state):
    pass
def is_valid_state(state):
    return True


if __name__ == '__main__':
    app.run(debug=True, port=65010)
    
    
    
# # Authentication with HTTP Basic ( CLIENT -> SERVER )
#     from http.client import HTTPSConnection
# from base64 import b64encode
# #This sets up the https connection
# c = HTTPSConnection("www.google.com")
# #we need to base 64 encode it 
# #and then decode it to acsii as python 3 stores it as a byte string
# userAndPass = b64encode(b"username:password").decode("ascii")
# headers = { 'Authorization' : 'Basic %s' %  userAndPass }
# #then connect
# c.request('GET', '/', headers=headers)
# #get the response back
# res = c.getresponse()
# # at this point you could check the status etc
# # this gets the page text
# data = res.read() 
