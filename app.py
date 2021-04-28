import flask
from StartupController import StartupController

app = flask.Flask(__name__)
app.config["DEBUG"] = True
startupData = StartupController()

# Definition of routes in our API
@app.route('/', methods=['GET'])
def home():
    return "<h1>Startup Enviroment Dataset</h1><p>This is a example API to get information about the startups, VC, " \
           "fundings, and so on </p> "


# Get all the data of the companies
@app.route('/companies', methods=['GET'])
def all_companies():
    return startupData.all_companies_name()


# All of the possible statuses of the companies
@app.route('/statuses', methods=['GET'])
def all_statuses():
    return startupData.all_statuses()


if __name__ == "__main__":
    app.run(port=8080)
