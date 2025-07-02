document.getElementById("stratForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const data = {
        weather: document.getElementById("weatherType").value,
        fuelLoad: parseFloat(document.getElementById("fuelLoad").value),
        trackType: document.getElementById("trackType").value,
        aggression: parseInt(document.getElementById("aggression").value),
        tire: document.querySelector('input[name="tire"]:checked').value
    }

    console.log("Form submitted");
    console.log(data);

    fetch("http://127.0.0.1:5000/strategy", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })

    .then(res => res.json())

    .then(data => {
        document.getElementById("output").innerHTML = `
            <h2>Recommended Strategy</h2>
            <p><strong>Pit Stops:</strong> ${data.pitStops}</p>
            <p><strong>Tires:</strong> ${data.recommendedTires.join(", ")}</p>
            <p><strong>Notes:</strong> ${data.strategyNotes}</p>
        `;
        console.log("Strategy has been posted.", data);
    })

    .catch(err => {
        document.getElementById("output").innerHTML = "Error getting strategy.";
        console.error(err);
    });

});