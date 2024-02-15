#Server.PY #
import socket
import ssl
from datetime import datetime
import pickle
import subprocess
import platform
class Server():
    def __init__(self, name, port, connection, priority):
        self.name = name
        self.port = port
        self.connection = connection.lower()
        self.priority = priority.lower()
        self.history = []
        self.alert = False

    def check_connection(self):
        msg = ""
        success = False
        now = datetime.now()
        try:
            if self.connection == "plain":
                socket.create_connection((self.name, self.port), timeout=10)
                msg = f"{self.name} is Up on port {self.port} with connection type {self.connection}"
                success = True
                self.alert = False
            elif self.connecion == "ssl":
                ssl.wrap_socket(socket.create_connection((self.name, self.port), timeout=10))
                msg = f"{self.name} is Up on port {self.port} with {self.connection}"
                success = True
                self.alert = False
            else:
                if self.ping():
                    msg = f"{self.name} is up. On port {self.port} with {self.connection}"
                    success = True
                    self.alert = False
        except socket.timeout:
            msg = f"server: {self.name} timeout. On port {self.port}"
        except (ConnectionRefusedError, ConnectionResetError) as e:
            msg = f"server: {self.name} {e}"
        except Exception as e:
            msg = f"No Clue??: {e}"

