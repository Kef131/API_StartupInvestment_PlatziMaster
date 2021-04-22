import flask
import pandas as pd

app = flask.Flask(__name__)
app.config["DEBUG"] = True


#load dataset with pandas
# prework - clean informacion - define information ( optional)
# functions of what we wanna do
# statistics etc
# hacer funciones que definan los datos que vamos a mostrar

# Definition of routes in our API
#
@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

#Get all founders of the dataset
@app.route('/statuses', methods=['GET'])
def statuses():
    return print(companies['status'].value_counts())

#Highest investment of the dataset
# @app.route('/invesment/highest', methods=['GET'])
# def highestInvestment():
#     #call the function, output information in json
#     return objectJson




# @app.route('/investor/{id}', methods=['GET'])
# def highestInvestment():
#
#     return objectJson
#

if __name__ == "__main__":
    companies = pd.read_csv('DataSet_StartupInvestment/objects.csv', low_memory=False)
    app.run(port=8080)