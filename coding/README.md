# Assessment  
Author: Hao Gu  

## Files  
1. main.py  
   main program  
2. test.py  
   testing program  
3. LOG.md  
   developer log

## Testing  
1. using test.py  
   Pay attention to whether the dependencies are correct  
   ```py
   from main import Light, Thermostat, Camera, DeviceController, SmartHomeHub  
   ```
2. Additional test set  
   ```py  
       def test_singleton():
        hub1 = SmartHomeHub()
        hub2 = SmartHomeHub()
        print(f"hub1 id:\t{id(hub1)}\nhub2 id:\t{id(hub2)}")
        assert hub1 is hub2, "SmartHomeHub is not a singleton!"
        print("SmartHomeHub is a singleton!")  

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
   ```  


you could find the whole packages in github  
>https://github.com/FLumine87/algorithms.git  
https://github.com/FLumine87/algorithms/tree/main/coding  
  

thank reading  
\ o /