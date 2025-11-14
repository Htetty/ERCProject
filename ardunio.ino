#include <Servo.h>

Servo myServo;

void setup() {
  Serial.begin(9600);
  myServo.attach(9);
  myServo.write(90);
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();

    if (c == '0') {
      myServo.write(0);
    }
    if (c == '1') {
      myServo.write(90);
    }
    if (c == '2') {
      myServo.write(180);
    }
  }
}
