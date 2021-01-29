#include <SoftwareSerial.h>
#include "winsen_ze25o3.h"

WinsenZE25O3 sensor{2};

void setup() {
  Serial.begin(9600);
}

void loop() {
  int ppb = sensor.readPPB();
  int analogVal = analogRead(A0);

  if (ppb > 0) {
    Serial.print(ppb);
    Serial.print(",");
    Serial.print(analogVal);
    Serial.print(",");
    Serial.println(estimateIndoorNO2PPB(analogVal));
    delay(1000);
  }
}

double estimateIndoorNO2PPB(int analogVal) {
  // based on fitted model for predicting outdoor NO2 and indoor/outdoor ratio from
  // https://link.springer.com/article/10.1007/s10653-019-00441-0?shared-article-renderer
  return ((7.51826819982211 * analogVal - 636.9571501802109) * 0.73) / 1.88;
}
