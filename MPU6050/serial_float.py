import serial

# Open serial port
ser = serial.Serial('COM6', 57600)

while True:
    # Read a line of data from the serial port
    line = ser.readline().decode().strip()
    if ';' in line:
        # Split the line into accelerometer and gyroscope values
        acc_str, gyro_str = line.split(';')
        acc_values = [float(x) for x in acc_str.split(',')]
        gyro_values = [float(x) for x in gyro_str.split(',')]

        # Print the sensor data
        print("Accelerometer:", acc_values)
        print("Gyroscope:", gyro_values)

# Close serial port
ser.close()