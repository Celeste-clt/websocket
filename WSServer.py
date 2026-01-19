from websocket_server import WebsocketServer
from Context import Context

class WSServer:
    def __init__(self, ctx):
        self.host = ctx.host
        self.port = ctx.port
        self.server = WebsocketServer(
            host=self.host,
            port=self.port,
            loglevel=1
        )
        self.server.set_fn_new_client(self.on_new_client)
        self.server.set_fn_client_left(self.on_client_left)
        self.server.set_fn_message_received(self.on_message_received)
        self.clients = []

    def on_new_client(self, client, server):
        print(f"[+] Client connecté : {client['id']}")

        self.clients.append(client)

        server.send_message(client, "Bienvenue sur le chat")

    def on_client_left(self, client, server):
        print(f"[-] Client déconnecté : {client['id']}")

        self.clients.remove(client)

    def on_message_received(self, client, server, message):
        # Affiche le message reçu côté serveur**
        print(f"[{client['id']}] {message}")

        # Envoie le message aux  clients**
        for c in self.clients:
            if c != client:
                server.send_message(c, message)

    def start(self):
        print(f"Serveur WS sur ws://{self.host}:{self.port}")
        self.server.run_forever()

    @staticmethod
    def dev():
        return WSServer(Context.dev())

    @staticmethod
    def prod():
        return WSServer(Context.prod())


if __name__ == "__main__":
    server = WSServer.dev()
    server.start()
