#include <SoftwareSerial.h>
#include "winsen_ze25o3.h"

WinsenZE25O3 sensor{2};

void setup() {
  Serial.begin(9600);
  Serial.println("ppb,analogVal");
}

void loop() {
  int ppb = sensor.readPPB();
  int analogVal = analogRead(A0);

  if (ppb > 0) {
    Serial.print(ppb);
    Serial.print(",");
    Serial.println(analogVal);
    delay(1000);
  }
}
