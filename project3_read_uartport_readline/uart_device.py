import serial
import threading
import signal
import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())

client_list: list = []

COMPORT = ''
for p in ports:
    print(p)
    if not str(p).count("CP210"):
        continue
    COMPORT = p.device

print(COMPORT)

exit_event = threading.Event()


class device_port:
    __rpt = False

    def __init__(self, port="/dev/ttyUSB0", baud_rate=9600):
        try:
            self.ser = serial.Serial(port, baud_rate)
            t = threading.Thread(target=self.read)  # 建立執行緒
            self.status = True
            t.start()  # 執行
        except Exception as ex:
            print("open serial port error " + str(ex))
            exit()

    def read(self, rpt=True):
        self.__rpt = rpt
        while self.__rpt:
            data = self.ser.readline()
            __str = data.decode('utf-8')
            print(__str)
            # 分析字串切入點


def signal_handler(signum, frame):
    exit_event.set()


def start():
    signal.signal(signal.SIGINT, signal_handler)
    ser = device_port('/dev/ttyUSB0', 38400)


if __name__ != '__main__':
    pass
# Press the green button in the gutter to run the script.
else:
    start()
