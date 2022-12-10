from flask import Flask,jsonify,request
from flask_cors import CORS
from utils import number_of_worldcups,getAverageGoals,popularMatchesByTeam,getHeadToHeadMatches,attendanceInWorldCups,goalsScorePerWorldCup
app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/getbarchart')
def bardata():
    print(request.args.get("country1"),request.args.get("country2"))
    return getHeadToHeadMatches(request.args.get("country1"),request.args.get("country2"))

@app.route("/getpiechart")
def piedata():
    return jsonify(number_of_worldcups())

@app.route("/getlinechart")
def linechart():
    return jsonify(getAverageGoals())

@app.route("/getcolumnchart")
def columnchart():
    print(request.args.get("country"))
    return popularMatchesByTeam(request.args.get("country"))

@app.route("/getbarchart2")
def barchart2():
    return jsonify(attendanceInWorldCups())

@app.route("/getGoalData")
def getGoalData():
    return jsonify(goalsScorePerWorldCup())

if __name__ == "main":
    app.run(debug=True)