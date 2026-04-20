import xmlrpc.client

# Connect to server
client = xmlrpc.client.ServerProxy("http://localhost:8282/")

print("Connected to Server")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", client.add(a, b))
print("Subtraction:", client.subtract(a, b))
print("Multiplication:", client.multiply(a, b))
print("Division:", client.divide(a, b))
