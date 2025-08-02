from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI()

# Create and mount the MCP server directly to your FastAPI app
mcp = FastApiMCP(app)
mcp.mount_http()

# @app.get("/")
# async def root():
#     return {"message": "MCP is super cool"}