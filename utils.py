import pandas as pd

data : pd.DataFrame = pd.read_csv("./WorldCupMatches.csv")
data_2 : pd.DataFrame = pd.read_csv("./WorldCups.csv")
data.drop(range(850,4568), inplace=True)
print(data.shape)

def getHeadToHeadMatches(country1, country2):
    headtohead = data[((data["Home Team Name"] == country1) & (data["Away Team Name"] == country2)) | ((data["Home Team Name"] == country2) & (data["Away Team Name"] == country1))]
    #print(headtohead)
    win_dict = dict()
    win_dict[country1] = 0
    win_dict[country2] = 0
    win_dict["draw"] = 0
    for index,match in headtohead.iterrows():
        if(match["Home Team Name"] == country1 and match["Away Team Name"] == country2):
            goal_diff = int(match["Home Team Goals"]) - int(match["Away Team Goals"])
            if goal_diff > 0:
                win_dict[country1]+=1
            elif goal_diff == 0:
                win_dict["draw"]+=1
            else:
                win_dict[country2]+=1
        elif (match["Home Team Name"] == country2 and match["Away Team Name"] == country1):
            goal_diff = int(match["Home Team Goals"]) - int(match["Away Team Goals"])
            if goal_diff > 0:
                 win_dict[country2]+=1
            elif goal_diff == 0:
                win_dict["draw"]+=1
            else:
                win_dict[country1]+=1
    return {"data" : list(win_dict.values()), "labels" : list(win_dict.keys())}
        
def getAverageGoals():
    average_goals = {}
    years = pd.unique(data["Year"])
    years = years[~pd.isnull(years)]
    for year in years:
        matches = data[data["Year"] == year]
        total_goals = 0
        for index,match in matches.iterrows():
                total_goals += match["Home Team Goals"] + match["Away Team Goals"]
        total_matches = matches.shape[0]
        average_goals[int(year)] = round((total_goals/total_matches),2)
    return [{"Year" : k, "goals" : v} for k,v in average_goals.items()]

def number_of_worldcups():
    worldcups = {}
    finals = data[data["Stage"]=="Final"]
    for index,match in finals.iterrows():
        if match["Home Team Goals"] > match["Away Team Goals"]:
            if match["Home Team Name"] in worldcups.keys():
                worldcups[match["Home Team Name"]] +=1
            else:
                 worldcups[match["Home Team Name"]] =1
        elif match["Home Team Goals"] < match["Away Team Goals"]:
            if match["Away Team Name"] in worldcups.keys():
                worldcups[match["Away Team Name"]] +=1
            else:
                 worldcups[match["Away Team Name"]] =1
        else:
            winner = match["Win conditions"].split(" ")[0]
            if winner in worldcups.keys():
                worldcups[winner] +=1
            else:
                worldcups[winner] = 1
    winners = []
    winners = [{"country" : k, "cups" : v} for k,v in worldcups.items()]
    print(winners)
    return winners
def attendanceInWorldCups():
    result = data_2[["Year","Attendance"]]
    print(result)
    result_dict = [{"Year" : int(val["Year"]), "people" : int(val["Attendance"])} for indx, val in result.iterrows()]
    return result_dict

def popularMatchesByTeam(country):
    matches = data[(data["Away Team Name"] == country) | (data["Home Team Name"] == country)]
    match_data = matches.groupby("Year").sum("Attendance")
    attendance = match_data[["Attendance"]].to_dict()
    result_dict = [ {"Year" : int(k), "people" : int(v)}for k,v in attendance["Attendance"].items()]
    return result_dict

#opularMatchesByTeam("Germany")
#attendanceInWorldCups()