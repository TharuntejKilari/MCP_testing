from fastmcp import FastMCP

mcp = FastMCP('Restaurant')

@mcp.tool
def menu():
    """The food items provided by restaurant"""
    food = ['Biryani', 'Kebab', 'Pizza', 'Ice cream']

    return food

@mcp.tool
def locations():
    """The locations where restaurant is available"""
    locations = ['Hyderabad', 'Bangalore', 'Mumbai', 'Chennai']
    return locations

if __name__ == '__main__':
    mcp.run(transport = 'streamable-http', port = 5001, host = '0.0.0.0')