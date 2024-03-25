from fastapi import FastAPI, HTTPException, Query
from typing import Optional  # Ensure this line is present

import requests

# Create FastAPI instance
app = FastAPI()

# Define API endpoint and headers
url = "https://api.core.ac.uk/v3/search/journals"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer agQj23dyn5qRpEVY14PhuWvxGbUDHo0N"
}

# Define route to handle GET requests
@app.get("/search/")
async def search_journals(query: str = Query(None, min_length=1), limit: Optional[int] = 10, offset: Optional[int] = 0):
    # Make sure query parameter is provided
    if query is None:
        raise HTTPException(status_code=422, detail="Query parameter is required")

    # Define search parameters
    search_params = {
        "q": query,
        "limit": limit,
        "offset": offset
    }

    # Send POST request to Core API
    response = requests.post(url, json=search_params, headers=headers)

    # Check response status
    if response.status_code == 200:
        # Return response data
        return response.json()
    else:
        # Raise HTTPException with error status code
        raise HTTPException(status_code=response.status_code, detail="Error occurred during search")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
