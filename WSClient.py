import websocket
import threading
from Context import Context


class WSClient:
    def __init__(self, ctx, client_name):
        self.client_name = client_name

        self.url = ctx.url()

        self.ws = websocket.WebSocketApp(
            self.url,
            on_message=self.on_message,  
            on_open=self.on_open,        
            on_error=self.on_error,      
            on_close=self.on_close,      
        )

    def on_message(self, ws, message):
        print(f"\n[reçu] {message}")

    def on_error(self, ws, error):
        print(f"[error] {error}")

    def on_close(self, ws, code, msg):
        print("[déconnecté]")

    def on_open(self, ws):
        print("[connecté]")

        # envoi des messages
        def send_loop():
            while True:
                # Lecture du message 
                msg = input("> ")
                ws.send(f"{self.client_name}: {msg}")

        threading.Thread(target=send_loop).start()

    def connect(self):
        self.ws.run_forever()


if __name__ == "__main__":
    name = input("Ton pseudo : ")
    client = WSClient(Context.dev(), name)
    client.connect()
