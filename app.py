import flask
import pandas as pd
import numpy as np 





app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Definition of routes in our API
@app.route('/', methods=['GET'])
def home():
    return "<h1>Pokemon Dataset Change</h1><p>This is a example API to test the data set of pokemon</p>"

#Get all founders of the dataset
@app.route('/types', methods=['GET'])
def types_pokemon():
    return df.to_json()

#Highest investment of the dataset
# @app.route('/invesment/highest', methods=['GET'])
# def highestInvestment():
#     #call the function, output information in json
#     return objectJson


# @app.route('/investor/{id}', methods=['GET'])
# def highestInvestment():
#     return objectJson

if __name__ == "__main__":
        df_pokemon = pd.read_csv('PokeTypeMatchupData.csv', low_memory=False)
        df = df_pokemon.copy(deep=True)
        df[df.columns] = df.apply(lambda a: a.str.strip('*'))
        df[df.columns] = df.apply(lambda a: a.str.strip('#'))
        types = df.iloc[:,1:]
        types = types.astype("float")
        types.insert(loc=0, column='Pokemon', value=df["Name"])
        df = types
        app.run(port=8080)