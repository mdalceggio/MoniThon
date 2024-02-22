import socket
import ssl
from datetime import datetime
import pickle
import subprocess
import platform
from gmail import email_alert
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
                msg = f"{self.name} is up. On port {self.port} with {self.connection}"
                success = True
                self.alert = False
            elif self.connection == "ssl":
                ssl.wrap_socket(socket.create_connection((self.name, self.port), timeout=10))
                msg = f"{self.name} is up. On port {self.port} with {self.connection}"
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
        if success == False and self.alert == False:
            # Send Alert
            self.alert = True
            email_alert(self.name, f"{msg}\n{now}", "mdalceggio@gmail.com")
            self.create_history(msg, success, now)
    def ping(self):
        try:
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system(
            ).lower() == "windows" else 'c', self.name), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
            return False
if __name__ == "__main__":
    try:
        servers = pickle.load(open("servers.pickle", "rb"))
    except:
        servers = [
            Server("reddit87.com", 80, "plain", "high"),
            Server("msn.com", 443, "ssl", "high"),
            Server("smtp.gmail.com", 465, "ssl", "high"),
            Server("yahoo.com", 80, "plain", "high"),
        ]
    for server in servers:
        server.check_connection()
        print(len(server.history))
        #print(server.history[-1])
        print(server.history)
        print(server.alert)
        print(server.name)
        

    pickle.dump(servers, open("servers.pickle", "wb"))