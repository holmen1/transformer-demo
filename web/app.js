

// App data


// SHOW ERROR WHEN THERE IS AN ISSUE WITH GEOLOCATION SERVICE
function showError(error) {
    notificationElement.style.display = "block";
    notificationElement.innerHTML = `<p> ${error.message} </p>`;
}

function summarizeText() {
    let text = document.getElementById("text_to_summarize").value;

    const data = { "text": "Amazon Elastic Compute Cloud is a part of Amazon.com cloud-computing platform. it allows users to rent virtual machines on which to run their own computer applications." };
    let tmp = JSON.stringify(data);

    const url = new URL("https://salty-depths-48137.herokuapp.com/ping")

    fetch('https://salty-depths-48137.herokuapp.com/ping', {
        method: 'GET',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
        },
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });

    fetch('localhost:8000/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });




    let summarized = text;

    document.getElementById("summary").value = summarized;
}

