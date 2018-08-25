import socket
import time

class Client(object):

    def __init__(self, ip, port, timeout=None):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.sock = socket.create_connection((ip, port))

    def put(self, key, value, timestamp=None):
        if not timestamp:
            timestamp = int(time.time())
        self.sock.sendall(("put" + " " + key + " " + str(value) + " " + \
                           str(timestamp) + "\n").encode("utf8"))
        return self.sock.recv(1024).decode("utf8")

    def get(self, key):
        self.sock.sendall(("get" + " " + key + "\n").encode("utf8"))
        res = self.sock.recv(1024).decode("utf8").split('\n')

        metrics = {}
        if len(res) == 0 or res[0] != "ok":
            raise ClientError('')
        if res[0] == "ok" and len(res) == 1:
            return metrics

        for metric in res[1:-2]:
            metric_array = metric.split(" ")
            t = (int(metric_array[2]), float(metric_array[1]))
            if metric_array[0] in metrics:
                metrics[metric_array[0]].append(t)
            else:
                metrics[metric_array[0]] = [t]

        for k in metrics:
            sorted(metrics[k], key=lambda tup: tup[0])

        return metrics


class ClientError(Exception):

    def __init__(self, message):
        super(ClientError, self).__init__(message)
