#include <SoftwareSerial.h>
#include "winsen_ze25o3.h"

WinsenZE25O3 sensor{2};

void setup() {
  Serial.begin(9600);
  Serial.println("ppb");
}

void loop() {
  int ppb = sensor.readPPB();

  if (ppb > 0) {
    Serial.println(ppb);
    delay(1000);
  }
}
