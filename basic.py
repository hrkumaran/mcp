from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI()

# Create and mount the MCP server directly to your FastAPI app
mcp = FastApiMCP(app)
mcp.mount_http()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
    
# @app.get("/")
# async def root():
#     return {"message": "MCP is super cool"}