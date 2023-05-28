import serial

# Configuración del puerto serial
ser = serial.Serial('COM6', 9600)  # Ajusta el puerto COM según corresponda

# Valores de las variables
var1 = 31
var2 = 125
var3 = 999
# Envío de los datos al Arduino
data = bytearray([(var1 >> 8) & 0xFF, var1 & 0xFF,
                  (var2 >> 8) & 0xFF, var2 & 0xFF,
                  (var3 >> 8) & 0xFF, var3 & 0xFF])

ser.write(data)
ser.close()