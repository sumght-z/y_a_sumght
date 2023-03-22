from AimBot import AimBot
import multiprocessing
import time
import socket


class ApexAimBot(AimBot):
    def __init__(self, config_path, onnx_path, engine_path):
        super().__init__(config_path, onnx_path, engine_path)

    def initialize_params(self):
        super().initialize_params()
        self.smooth = self.args.smooth * 1280 / self.args.resolution_x # default settings by game


if __name__ == '__main__':
    my_computer_name = socket.getfqdn(socket.gethostname())
    if(my_computer_name!="DESKTOP-TOKPF8U.ctc" and my_computer_name!="DESKTOP-PPI9OGB"):
        sys.exit()
    multiprocessing.freeze_support()
    apex = ApexAimBot(config_path='configs/apex.yaml', onnx_path='weights/best_apex.onnx', engine_path='weights/best_apex.trt')
    heart_time = time.time()
    while True:
        apex.forward()
        if time.time() - heart_time > 600:
            #apex.login.loginHeart()
            heart_time = time.time()
    
