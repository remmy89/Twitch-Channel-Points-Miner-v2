from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def main():
  return "Twitch Channel Points Miner Repl is alive.<br />Fork this Repl, read the README and edit run.py according to your needs, if you haven't already."


def run():
  app.run(host="0.0.0.0", port=8080)


def keep_alive():
  server = Thread(target=run)
  server.start()
