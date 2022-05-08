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

void rotate(BasicStepperDriver face, double rotation) {
  face.enable();
  face.rotate(rotation);
  face.disable();
}

void execute_simple(String str, int rotation) {
  char face_letters [] = {'L', 'R', 'F', 'B', 'D'};
  BasicStepperDriver face_drivers [] = {left, right, front, back , down};

  for (int i = 0; i < 5; i++) {
    if (str.charAt(0) == face_letters[i]) {
      rotate(face_drivers[i], rotation * -90);
      return;
    }
  }
}

void execute(String str) {
  if (str.length() == 1) {
    execute_simple(str, 1);
  } else if (str.charAt(1) == '2') {
    execute_simple(str, 2);
  } else if (str.charAt(1) == '\'') {
    execute_simple(str, -1);
  }
}

void execute_moves(String str) {
  int i = 0;
  while (i < str.length()) {
    if (str.charAt(i) == ' ') {
      i++;
      continue;
    }
    
    String temp = "";
    while (str.charAt(i) != ' ' && i != str.length()) {
      temp += str.charAt(i);
      i++;
    }
    execute(temp);
  }
}

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

void loop() {
  execute_moves("R D R' D R D2 R'");
  delay(200);
}
