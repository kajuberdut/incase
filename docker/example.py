from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse, HTMLResponse
from incase.middleware import JSONCaseTranslatorMiddleware, camelJsonResponse

app = FastAPI(default_response_class=camelJsonResponse)

app.add_middleware(JSONCaseTranslatorMiddleware, handle_response=False)


@app.get("/")
def read_root():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>JSON Submission Form</title>
    <script>
        function submitJSON() {
            // Retrieve the JSON input from the text box
            var jsonInput = document.getElementById("jsonInput").value;

            // Create a request to the server
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "http://localhost:8000/json", true);
            xhr.setRequestHeader("Content-Type", "application/json");

            // Define what happens on successful data submission
            xhr.onload = function () {
                if (xhr.status === 200) {
                    // Parse the response and display it
                    var response = JSON.parse(xhr.responseText);
                    document.getElementById("response").textContent = JSON.stringify(response, null, 2);
                } else {
                    console.error("Error in request: " + xhr.status);
                }
            };

            // Handle any errors that occur during the request
            xhr.onerror = function () {
                console.error("Request error...");
            };

            // Send the JSON data
            xhr.send(JSON.stringify({ data: jsonInput }));
        }
    </script>
</head>
<body>
    <h1>JSON Submission Form</h1>
    <textarea id="jsonInput" rows="10" cols="50" placeholder="Enter JSON here"></textarea>
    <br>
    <button onclick="submitJSON()">Submit</button>
    <pre id="response"></pre>
</body>
</html>
""")

@app.get("/json")
async def kenobi():
    return {"hello_there": "general kenobi"}

@app.post("/json")
async def receive_data(request: Request):
    json_data = await request.json()
    print(f"/ got: {json_data}")
    # Generating an actual JSONResponse to avoid default_response_class
    return JSONResponse({"Received": json_data})
