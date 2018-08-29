import asyncio


class ClientServerProtocol(asyncio.Protocol):

    base = {}

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def save_data(self, data):
        name = data[1]
        metric = float(data[2])
        timestamp = int(data[3])
        if name not in self.base:
            self.base[name] = {timestamp: metric}
        else:
            metrics_by_name = self.base[name]
            metrics_by_name[timestamp] = metric
            self.base[name] = metrics_by_name

    def get_data(self, data):
        name = data[1]
        if name == '*':
            return self.base
        elif name in self.base:
            return {name: self.base[name]}
        else:
            return {}

    def process_data(self, message):
        if not message or len(message) == 0:
            return "error\nwrong command\n\n"

        data = message.split()

        if data[0] == 'put':
            if len(data) != 4:
                return "error\nwrong command\n\n"
            self.save_data(data)
            return 'ok\n\n'
        elif data[0] == 'get':
            if len(data) != 2:
                return "error\nwrong command\n\n"
            result = self.get_data(data)
            res = 'ok\n'
            for key, value in result.items():
                for timestamp, metric in value.items():
                    res += key + ' ' + str(metric) + ' ' + str(timestamp) + '\n'
            res += '\n'
            return res
        else:
            return "error\nwrong command\n\n"


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

def _main():
    run_server('127.0.0.1', 8888)

if __name__ == "__main__":
    _main()
