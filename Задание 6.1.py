from time import sleep


class TrafficLight:
    __color = "grey"

    def running(self):
        while True:
            print("Красный сигнал")
            sleep(7)
            print("Желтый сигнал")
            sleep(2)
            print("Зеленый сигнал")
            sleep(7)
            print("Желтый сигнал")
            sleep(2)


trafficLight = TrafficLight()
trafficLight.running()
