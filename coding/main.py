import abc
from datetime import datetime
from collections import defaultdict

# Base Device Class (Template)
class Device(abc.ABC):
    def __init__(self, device_id, name, energy_usage=0,status='off'):
        # Initialize device attributes
        self.__device_id = device_id
        self.__name = name
        self.__status = status      #^
        self.__energy_usage = energy_usage
        self.__scheduled = [None, None]     #the first position is scheduled time, and the second one is operation.

    # Getter methods
    def get_id(self): return self.__device_id

    def get_name(self): return self.__name

    def get_status(self): return self.__status
    
    def get_energy_usage(self): return self.__energy_usage      #^
    
    def get_schedule_status(self): return self.__scheduled[0]

    def get_schedule_time(self): return self.__scheduled[1]

    # Setting methods       #^
    def set_energy_usage(self,new_usage): self.__energy_usage = new_usage

    def set_name(self,new_name):
        if new_name == self.__name:
            print('The name has been duplicated!')
            return
        self.__name = new_name      #^
        print('The new name has been set!!')
    
    def set_status(self,new_status): #原则上这个函数可以被复用，若真被复用，可体现
        if new_status not in ['on', 'off']:#!= 'on' or new_status != 'off':
            return -1 #这里是否需要采用断言，我还没有想好       #^
        if new_status == self.__status:
            print('The %s has already %s' % (self.__name,self.__status))
            return
        self.__status = new_status
        print('The new status has been set!!')
        return

    def set_id(self, new_id):       #^
        assert False,'the device id can not change'
    
    def set_schedule(self, command, time):
        self.__scheduled[0] = command
        self.__scheduled[1] = time
    
    def do_schedule(self): pass

    # Control methods
    def turn_on(self): return self.set_status('on')

    def turn_off(self): return self.set_status('off')

    def get_energy_usage(self): return self.__energy_usage      #^

    def __str__(self): return 'Device:\t\t'+ self.get_name() + '\nID:\t\t'+ self.get_id() + '\nStatus:\t\t' + self.get_status() + '\nEnergy Usage:\t' + str(self.get_energy_usage()) + 'kWh\n\n'      #^

# Subclasses for devices        #^
class Light(Device):
    def __init__(self, device_id, name, brightness=100):
        super().__init__(device_id,name)
        self.__brightness = brightness
        if SmartHomeHub._instance is None: SmartHomeHub()
        SmartHomeHub._instance.controller.add_device(self)


class Thermostat(Device):
    def __init__(self, device_id, name, temperature=22):
        super().__init__(device_id,name)
        self.__temperature = temperature
        if SmartHomeHub._instance is None: SmartHomeHub()
        SmartHomeHub._instance.controller.add_device(self)

class Camera(Device):
    def __init__(self, device_id, name, resolution='1080p'):
        super().__init__(device_id,name)
        self.__resolution = resolution
        if SmartHomeHub._instance is None: SmartHomeHub()
        SmartHomeHub._instance.controller.add_device(self)

# Device Controller
class DeviceController:
    def __init__(self): self.devices = {}

    def add_device(self, *device):
        #print('\n')
        for dv in device: 
            if dv.get_id() in self.devices: pass#print(f"Device:{dv.get_name()} already exists!")
            else: 
                self.devices[dv.get_id()] = dv
                print(f"Device:{dv.get_name()} already set!")
        #print('\n')

    def remove_device(self, device_id): 
        try:
            print(f'{self.devices.pop(device_id)} has already been deleted' )
        except KeyError:
            print(f"Device with ID {device_id} does not exist.")

    def list_devices(self):
        print('all device(s):')
        for i in self.devices.values(): print(i.get_name())

    def execute_command(self, device_id, command, time = None): #####
        if time is not None: 
            self.devices[device_id].set_schedule(command, time)
            return
        self.devices[device_id].set_status(command)

# Smart Home Hub (Singleton)
class SmartHomeHub:
    _instance = None

    def __new__(cls):       #^104
        if cls._instance is None:
            cls._instance = super(SmartHomeHub, cls).__new__(cls)
            cls._instance.controller = DeviceController()
        return cls._instance

    def schedule_task(self, device_id, command, time = None): self.controller.execute_command(device_id,command, time)

    def display_status(self):
        print("Device's status:")
        for i in self.controller.devices.values():
            print(i.get_name() ,'\t',i.get_status())
            #if i.get_schedule_status is not None: print('Will be ',i.get_schedule_status,':\t',i.get_schedule_time)

    def total_energy_usage(self,s=0,ptr = None):
        if ptr is None:
            ptr = iter(self.controller.devices.values())
        try:
            device = next(ptr)  # 从迭代器中获取设备对象
            return self.total_energy_usage(s + device.get_energy_usage(), ptr)
        except StopIteration:
            return s      
        # if ptr is None:ptr = iter(self._instance.controller.devices.values())
        # s = ptr.get_energy_usage + self.total_energy_usage(s,next(ptr))

# Main Execution (Template)
if __name__ == "__main__":
    hub = SmartHomeHub()

    Living_Room_Light = Light('L1', 'Living_Room_Light') 
    Home_Thermostat = Thermostat('T1', 'Home_Thermostat')
    Front_Foor_Cemera = Camera('C1', 'Front_Foor_Cemera')
    # Add devices
    hub.controller.add_device(Living_Room_Light)
    hub.controller.add_device(Home_Thermostat)
    hub.controller.add_device(Front_Foor_Cemera)

    # Display devices
    hub.display_status()

    # Execute commands
    hub.controller.execute_command('L1','on')
    hub.controller.execute_command('T1','off')

    # Schedule tasks
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hub.schedule_task('C1', 'on', current_time)

    # Calculate and print total energy usage
    print(f"Total Energy Usage: {hub.total_energy_usage()} kWh")