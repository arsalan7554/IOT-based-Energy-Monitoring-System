// Energy Monitor - Arduino Side
// Reads ACS712 output, calculates current, sends via Serial

const int sensorPin = A0;
const float voltageRef = 5.0;
const float sensitivity = 0.185; // 185mV/A for ACS712-5A
const int adcResolution = 1024;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int rawValue = analogRead(sensorPin);
  
  // Convert ADC value to voltage
  float voltage = (rawValue / (float)adcResolution) * voltageRef;
  
  // ACS712 outputs 2.5V at 0A (midpoint)
  float current = (voltage - 2.5) / sensitivity;
  
  // Assume 230V supply (India standard)
  float power = abs(current) * 230.0;
  
  // Send as CSV: timestamp_ms,current,power
  Serial.print(millis());
  Serial.print(",");
  Serial.print(current, 3);
  Serial.print(",");
  Serial.println(power, 3);
  
  delay(500); // 2 readings per second
}
