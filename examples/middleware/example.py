from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse, HTMLResponse
from incase.middleware import JSONCaseTranslatorMiddleware, CamelJsonResponse

app = FastAPI(default_response_class=CamelJsonResponse)

app.add_middleware(JSONCaseTranslatorMiddleware, handle_response=False)


@app.get("/")
def read_root():
    return HTMLResponse("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>JSON Submission Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        h1 {
            color: #333;
        }

        textarea {
            width: 80%;
            max-width: 500px;
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            resize: vertical;
        }

        button {
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background-color: #0056b3;
        }

        pre {
            width: 80%;
            max-width: 500px;
            background-color: #fff;
            border: 1px solid #ddd;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
    </style>
    <script>
        function submitJSON() {
            var jsonInput = document.getElementById("jsonInput").value;
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "http://localhost:8000/json", true);
            xhr.setRequestHeader("Content-Type", "application/json");

            xhr.onload = function () {
                if (xhr.status === 200) {
                    var response = JSON.parse(xhr.responseText);
                    document.getElementById("response").textContent = JSON.stringify(response, null, 2);
                } else {
                    console.error("Error in request: " + xhr.status);
                }
            };

            xhr.onerror = function () {
                console.error("Request error...");
            };

            xhr.send(jsonInput);
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
