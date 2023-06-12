import paho.mqtt.client as mqtt # mosquitto.py is deprecated
import time
import signal
import random

# from https://gist.github.com/pyk/e794d774afe4dbefb0958ecc43e7f45d


mqttc = mqtt.Client("py-script")
mqttc.connect("mqtt", 1883, 60)

mqttc.loop_start()

def busy_work(seconds):
    while True:
        mqttc.publish("casa/living/temp",random.randrange(-5, 35, 3))
        time.sleep(seconds)


class Transporter:
    def __init__(self):
        self.stopped = False

    def run(self):
        while not self.stopped:
            busy_work(3)

    def stop(self, signal, frame):
        print("Stop the transporter ...")
        self.stopped = True

def main():
    # Setup transporter
    transporter = Transporter()
    # Setup signal handler
    signal.signal(signal.SIGINT, transporter.stop)
    signal.signal(signal.SIGTERM, transporter.stop)
    transporter.run()


if __name__ == "__main__":
    main()