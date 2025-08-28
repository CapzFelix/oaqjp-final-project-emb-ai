import socket

def open_port(port):
    try:
        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Allow reusing the address
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind the socket to the specified port
        server_socket.bind(('0.0.0.0', port))
        # Start listening for connections
        server_socket.listen(5)
        print(f"Port {port} is now open and listening...")
        return server_socket
    except Exception as e:
        print(f"Error opening port {port}: {e}")
        return None

# Example: Close the socket to stop the port
def close_port(server_socket):
    try:
        if server_socket:
            server_socket.close()
            print("Port has been closed successfully.")
        else:
            print("No socket to close.")
    except Exception as e:
        print(f"Error closing the port: {e}")

# Main execution
if __name__ == "__main__":
    port = 5000  # Specify the port to open
    server_socket = open_port(port)

    # Simulate some operations (e.g., waiting for connections)
    input("Press Enter to close the port...")

    # Close the port
    close_port(server_socket)