import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/Sv443/api/jokeapi-v2'

mcp = FastMCP('jokeapi-v2')

@mcp.tool()
def get_joke(type: Annotated[Union[str, None], Field(description='Will make JokeAPI only serve jokes with this joke type. Leave empty to randomly select a type. ')] = None,
             format: Annotated[Union[str, None], Field(description='The file format the joke should be served with ')] = None,
             contains: Annotated[Union[str, None], Field(description='If specified, only jokes that contain this string will be served. Value needs to be percent-encoded. ')] = None,
             idRange: Annotated[Union[str, None], Field(description='A single ID or range of IDs to serve jokes from ')] = None,
             blacklistFlags: Annotated[Union[str, None], Field(description='A single or comma-separated list of blacklist flags ')] = None,
             safe_mode: Annotated[Union[str, None], Field(description='A value-less parameter, that, if present, will tell JokeAPI to try its hardest not to serve any offensive jokes. By default, every joke that has one or more flags set to true is considered unsafe, in addition to a few more hand-picked ones. ')] = None) -> dict: 
    '''This is the endpoint you need to call to get a joke.'''
    url = 'https://jokeapi-v2.p.rapidapi.com/joke/Any'
    headers = {'x-rapidapi-host': 'jokeapi-v2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'type': type,
        'format': format,
        'contains': contains,
        'idRange': idRange,
        'blacklistFlags': blacklistFlags,
        'safe-mode': safe_mode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def info(format: Annotated[Union[str, None], Field(description='The file format the joke should be served with ')] = None) -> dict: 
    '''This endpoint provides some information on JokeAPI'''
    url = 'https://jokeapi-v2.p.rapidapi.com/info'
    headers = {'x-rapidapi-host': 'jokeapi-v2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'format': format,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def submit_joke() -> dict: 
    '''This endpoint is used to submit a joke to be reviewed and added to JokeAPI's official jokes.'''
    url = 'https://jokeapi-v2.p.rapidapi.com/submit'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'jokeapi-v2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.put(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def categories(format: Annotated[Union[str, None], Field(description='The file format the joke should be served with. More info: https://sv443.net/jokeapi/v2/#response-formats')] = None) -> dict: 
    '''This endpoint returns a list / an array of all available joke categories'''
    url = 'https://jokeapi-v2.p.rapidapi.com/categories'
    headers = {'x-rapidapi-host': 'jokeapi-v2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'format': format,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def ping(format: Annotated[Union[str, None], Field(description='The file format the joke should be served with. More info: https://sv443.net/jokeapi/v2/#response-formats')] = None) -> dict: 
    '''This endpoint is intended for external uptime monitoring but you can also use it if you want to.'''
    url = 'https://jokeapi-v2.p.rapidapi.com/ping'
    headers = {'x-rapidapi-host': 'jokeapi-v2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'format': format,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def flags(format: Annotated[Union[str, None], Field(description='The file format the joke should be served with. More info: https://sv443.net/jokeapi/v2/#response-formats')] = None) -> dict: 
    '''This endpoint returns a list / an array of all available blacklist flags'''
    url = 'https://jokeapi-v2.p.rapidapi.com/flags'
    headers = {'x-rapidapi-host': 'jokeapi-v2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'format': format,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def formats(format: Annotated[Union[str, None], Field(description='The file format the joke should be served with. More info: https://sv443.net/jokeapi/v2/#response-formats')] = None) -> dict: 
    '''This endpoint returns a list / an array of all available response formats'''
    url = 'https://jokeapi-v2.p.rapidapi.com/formats'
    headers = {'x-rapidapi-host': 'jokeapi-v2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'format': format,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
