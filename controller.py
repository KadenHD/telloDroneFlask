import time 
from djitellopy import tello

""" Controller  """
def telloControler(new_direction):
    drone = None 
    try: 
        drone = tello.Tello()
        drone.connect()
    except RuntimeError: 
        print ('Failed to initialize the drone.\n' )
        print ('Please, check your Wi-Fi SSID.\n')
        return

    droneCooldown = 3

    if (new_direction == "Takeoff") :
        print("Takeoff")
        drone.takeoff()
        time.sleep(droneCooldown)
    elif (new_direction == "Land") :
        print("Land")
        drone.land() 
        time.sleep(droneCooldown)
    elif (new_direction == "Forward") :
        print("Forward")
        drone.move_forward(60)
        time.sleep(droneCooldown)
    elif (new_direction == "Left") :
        print("Left")
        drone.move_left(60)
        time.sleep(droneCooldown)
    elif (new_direction == "Right") :
        print("Right")
        drone.move_right(60)
        time.sleep(droneCooldown)
    elif (new_direction == "Backward") :
        print("Backward")
        drone.move_back(60)
        time.sleep(droneCooldown)
    elif (new_direction == "Clockwise") :
        print("Clockwise")
        drone.rotate_clockwise(360)
        time.sleep(droneCooldown)  
    elif (new_direction == "Flip") :
        print("Flip")
        drone.flip('f')
        time.sleep(droneCooldown)
""" /Controller  """