# To run backend server, type the following into your TERMINAL:
# cd \Users\gwant\OneDrive\Documents\VSCode\race-strat-planner\back-end
# - then type -
# python app.py

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/strategy', methods=['POST'])
def strategy():
    data = request.json
    weather = data.get("weatherType", "Dry")
    fuel = data.get("fuelLoad", 100)
    aggression = data.get("aggression", 5)
    tire = data.get("tire", "Medium")
    track = data.get("trackType", "Permanent Circuit")

    if fuel > 100 or aggression >= 8:
        pit_stops = 3
    elif fuel > 80 or aggression >= 5:
        pit_stops = 2
    else:
        pit_stops = 1

    if weather == "Rain":
        tires = ["Intermediates"]
        note = "Start on Intermediates due to rain. Adjust based on weather updates."
    elif weather == "Mixed":
        tires = ["Soft", "Medium"]
        note = "Start on Softs for early dry laps, then Mediums as track evolves."
    else: 
        if tire == "Soft":
            tires = ["Soft", "Medium"]
        elif tire == "Hard":
            tires = ["Hard", "Medium"]
        else:
            tires = ["Medium", "Hard"]

        note = f"Start on {tires[0]}, pit around lap {int(50 / pit_stops)} for {tires[1]}."

    if track == "Street":
        note += " Street circuits tend to have more safety cars — consider early pit windows."
    elif track == "Permanent Circuit":
        note += " Expect consistent grip — plan pit stops based on lap degradation."

    return jsonify({
        "pit_stops": pit_stops,
        "recommendedTires": tires,
        "strategyNotes": note
    })

if __name__ == "__main__":
    app.run(debug=True)