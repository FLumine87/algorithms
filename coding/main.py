import abc
from datetime import datetime
from collections import defaultdict #Not adopted

# Base Device Class 
class Device(abc.ABC):
    def __init__(self, device_id, name, energy_usage=0,status='off'):
        # Initialize device attributes
        self.__device_id = device_id
        self.__name = name
        self.__status = status      
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
    def set_energy_usage(self,new_usage): 
        if not str(new_usage).isdigit(): # correctness check
            print(f"Error: Invalid energy usage '{new_usage}'. New energy usage must be a number.")
            return -1       #^
        if new_usage == self.__energy_usage:
            print("The %s's energy usage has already been %s." % (self.__name,self.__energy_usage))
            return 0
        self.__energy_usage = new_usage
        print('The new energy usage has been set!!')
        return 1

    def set_name(self,new_name):
        if new_name == self.__name:
            print('The name has been duplicated!')
            return 0
        self.__name = str(new_name)      #^
        print('The new name has been set!!')
        return 1
    
    def set_status(self,new_status):
        if new_status not in ['on', 'off']:#correctness check
            print(f"Error: Invalid status '{new_status}'. Status must be 'on' or 'off'.")
            return -1       #^
        if new_status == self.__status:
            print('The %s has already %s' % (self.__name,self.__status))
            return 0
        self.__status = new_status
        print('The new status has been set!!')
        return 1

    def set_id(self, new_id):       #^
        if new_id == self.__device_id:
            print('The device id has been duplicated!')
            return 0
        self.__device_id = str(new_id)      #^
        print('The new device id has been set!!')
        return 1
    
    def set_schedule(self, command, time):
        if command not in ['on', 'off']:#correctness check
            print(f"Error: Invalid status '{command}'. Status must be 'on' or 'off'.")
            return -1 
        if time==datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
            self.__status=command
            print('The new status has been set!!')
            return 0
        self.__scheduled[0] = command
        self.__scheduled[1] = time
        print(f"The scheduled time: {time} has been set")
        return 1
    
    def do_schedule(self): pass

    # Control methods
    def turn_on(self): return self.set_status('on')

    def turn_off(self): return self.set_status('off')

    def get_energy_usage(self): return self.__energy_usage      #^

    def __str__(self): return 'Device:\t\t\t'+ self.get_name() + '\nID:\t\t\t\t'+ self.get_id() + '\nStatus:\t\t\t' + self.get_status() + '\nEnergy Usage:\t' + str(self.get_energy_usage()) + 'kWh\n\n'      #^

# Subclasses for devices        #^
class Light(Device):
    def __init__(self, device_id, name, brightness=100):
        super().__init__(device_id,name)
        self.__brightness = brightness
        if SmartHomeHub._instance is None: SmartHomeHub()#correctness check
        SmartHomeHub._instance.controller.add_device(self)#add the new device to the dictionary automatically

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
    def __init__(self):self.devices = {}#self.defaultdevice = defaultdict()

    def add_device(self, *device):
        for dv in device: 
            if not isinstance(dv, Device):#correctness check
                print(f"Device:{dv} is not an Instance.")
                continue
            if dv.get_id() in self.devices: pass#print(f"Device:{dv.get_name()} already exists!")
            else: 
                self.devices[dv.get_id()] = dv
                print(f"Device:{dv.get_name()} already set!")

    def remove_device(self, device_id): 
        try:#correctness check
            print(f'{self.devices.pop(device_id).get_name()} has already been deleted' )
        except KeyError:
            print(f"Device with ID {device_id} does not exist.")

    def list_devices(self):
        if self.devices == {}:
            print('No device at all!')
            return -1
        print('all device(s):')
        for i in self.devices.values(): print(i)
        return 0

    def execute_command(self, device_id, command, time = None): 
        if device_id not in self.devices:#correctness check
            print(f"{device_id} does not exist!")
            return -1
        if time is not None: 
            self.devices[device_id].set_schedule(command, time)
            return 1
        self.devices[device_id].set_status(command)
        return 0
    
    def set_device_energy_usage(self, device_id, command):
        if device_id not in self.devices:#correctness check
            print(f"{device_id} does not exist!")
            return -1
        self.devices[device_id].set_energy_usage(command)


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
        if self.controller.devices == {}:
            print('No device at all!')
            return -1
        print("Device's status:")
        for i in self.controller.devices.values():
            print(i.get_name() ,':\t',i.get_status())
        return 0

    def total_energy_usage(self,s=0,ptr = None):
        if ptr is None:
            ptr = iter(self.controller.devices.values())
        try:
            device = next(ptr)
            return self.total_energy_usage(s + device.get_energy_usage(), ptr)
        except StopIteration:
            return s      
        # if ptr is None:ptr = iter(self._instance.controller.devices.values())
        # s = ptr.get_energy_usage + self.total_energy_usage(s,next(ptr))

def test_singleton():
    hub1 = SmartHomeHub()
    hub2 = SmartHomeHub()
    print(f"hub1 id:\t{id(hub1)}\nhub2 id:\t{id(hub2)}")
    assert hub1 is hub2, "SmartHomeHub is not a singleton!"
    print("SmartHomeHub is a singleton!")

# Main Execution 
if __name__ == "__main__":
    hub = SmartHomeHub()

    # Add devices
    hub.controller.add_device(Light('L1', 'Living_Room_Light'), 
    Thermostat('T1', 'Home_Thermostat'), 
    Camera('C1', 'Front_Foor_Cemera'))
    #Error Detection
    hub.controller.add_device('L1')

    # Display devices
    hub.controller.list_devices()

    # Execute commands
    hub.controller.execute_command('L1','on')
    hub.controller.execute_command('T1','off')
    #Error Detection
    hub.controller.execute_command('C2','off')
    hub.controller.execute_command('C1','hello')

    # Schedule tasks
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hub.schedule_task('C1', 'on', current_time)

    # Display status
    hub.display_status()

    # Calculate and print total energy usage
    print(f"Total Energy Usage: {hub.total_energy_usage()} kWh")

    # Remove device
    hub.controller.remove_device('L1')
    hub.controller.remove_device('T1')
    hub.controller.remove_device('C1')
    #Error Detection
    hub.controller.remove_device('C2')

    # Is Singleton
    test_singleton()