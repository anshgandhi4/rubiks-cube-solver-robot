#include <Arduino.h>
#include "BasicStepperDriver.h"

const int MOTOR_STEPS = 200;
const int RPM = 120;

const int MICROSTEPS = 1;

const int L_DIR = 32;
const int L_STEP = 33;
const int R_DIR = 34;
const int R_STEP = 35;
const int F_DIR = 36;
const int F_STEP = 37;
const int B_DIR = 38;
const int B_STEP = 39;
const int D_DIR = 40;
const int D_STEP = 41;

BasicStepperDriver left(MOTOR_STEPS, L_DIR, L_STEP);
BasicStepperDriver right(MOTOR_STEPS, R_DIR, R_STEP);
BasicStepperDriver front(MOTOR_STEPS, F_DIR, F_STEP);
BasicStepperDriver back(MOTOR_STEPS, B_DIR, B_STEP);
BasicStepperDriver down(MOTOR_STEPS, D_DIR, D_STEP);

void setup() {
  pinMode(L_DIR, OUTPUT);
  pinMode(L_STEP, OUTPUT);
  pinMode(R_DIR, OUTPUT);
  pinMode(R_STEP, OUTPUT);
  pinMode(F_DIR, OUTPUT);
  pinMode(F_STEP, OUTPUT);
  pinMode(B_DIR, OUTPUT);
  pinMode(B_STEP, OUTPUT);
  pinMode(D_DIR, OUTPUT);
  pinMode(D_STEP, OUTPUT);

  left.begin(RPM, MICROSTEPS);
  right.begin(RPM, MICROSTEPS);
  front.begin(RPM, MICROSTEPS);
  back.begin(RPM, MICROSTEPS);
  down.begin(RPM, MICROSTEPS);
}

void rotate(BasicStepperDriver face, double rotation) {
  face.enable();
  face.rotate(rotation);
  face.disable();
}

void loop() {
  for (int i = 0; i < 6; i++) {
    rotate(front, 90);
    rotate(right, 90);
    rotate(front, -90);
    rotate(right, -90);
  }
  delay(4000);
}
