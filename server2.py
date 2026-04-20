
from xmlrpc.server import SimpleXMLRPCServer

# Create server
server = SimpleXMLRPCServer(("localhost", 8282))
print("Server started on port 8000...")

# Functions to expose
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Register functions
server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")

# Keep server running
server.serve_forever()
