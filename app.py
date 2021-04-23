import flask
import pandas as pd

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Definition of routes in our API
@app.route('/', methods=['GET'])
def home():
    return "<h1>Pokemon Dataset</h1><p>This is a example API to test the data set of pokemon</p>"

#Get all founders of the dataset
@app.route('/names', methods=['GET'])
def statuses():
    return pokemon['Name'].value_counts()

#Highest investment of the dataset
# @app.route('/invesment/highest', methods=['GET'])
# def highestInvestment():
#     #call the function, output information in json
#     return objectJson


# @app.route('/investor/{id}', methods=['GET'])
# def highestInvestment():
#     return objectJson

if __name__ == "__main__":
    pokemon = pd.read_csv('PokeTypeMatchupData.csv', low_memory=False)
    app.run(port=8080)