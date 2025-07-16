/*
  Barometric Altitude Estimation

  Reads pressure from the LPS22HB sensor on the Arduino Nano 33 BLE Sense,
  calculates altitude using the barometric formula, and prints it over Serial.

  Hardware:
  - Arduino Nano 33 BLE Sense

  Author: Aarav Sangar
*/

#include <Arduino_LPS22HB.h>

void setup()
{
    Serial.begin(9600);
    while (!Serial)
        ;

    if (!BARO.begin())
    {
        Serial.println("Failed to initialize pressure sensor!");
        while (1)
            ;
    }
}

void loop()
{
    float pressure = BARO.readPressure(); // Pressure in kPa
    float altitude = 44330 * (1 - pow(pressure / 101.325, 1.0 / 5.255));

    Serial.print("Altitude according to kPa is = ");
    Serial.print(altitude);
    Serial.println(" m");

    delay(1000);
}
