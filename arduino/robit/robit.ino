// Includes
#include "BasicStepperDriver.h"

// Motor Constants
const int MOTOR_STEPS = 200;
const int MICROSTEPS = 16;
const int RPM = 190;
const int MOVE_DELAY_MS = 20;
const int D_RPM = 160;
const int D_MOVE_DELAY_MS = 25;

// Pins
const int L_ENABLE = 23;
const int L_DIR = 24;
const int L_STEP = 25;
const int R_ENABLE = 29;
const int R_DIR = 30;
const int R_STEP = 31;
const int F_ENABLE = 37;
const int F_DIR = 38;
const int F_STEP = 39;
const int B_ENABLE = 45;
const int B_DIR = 46;
const int B_STEP = 47;
const int D_ENABLE = 51;
const int D_DIR = 52;
const int D_STEP = 53;

// Miscellaneous
String solution = "";

// Stepper Motors
BasicStepperDriver left(MOTOR_STEPS, L_DIR, L_STEP, L_ENABLE);
BasicStepperDriver right(MOTOR_STEPS, R_DIR, R_STEP, R_ENABLE);
BasicStepperDriver front(MOTOR_STEPS, F_DIR, F_STEP, F_ENABLE);
BasicStepperDriver back(MOTOR_STEPS, B_DIR, B_STEP, B_ENABLE);
BasicStepperDriver down(MOTOR_STEPS, D_DIR, D_STEP, D_ENABLE);

/**
  Disables all stepper motors
*/
void disable_all() {
  left.disable();
  right.disable();
  front.disable();
  back.disable();
  down.disable();
}

/**
  Enables all stepper motors
*/
void enable_all() {
  left.enable();
  right.enable();
  front.enable();
  back.enable();
  down.enable();
}

/**
  Rotates specified stepper motor by specified number of quarter-turns
  @param face_letter Letter representing face
  @param face Stepper motor
  @param rotation Number of quarter-turns
*/
void rotate(char face_letter, BasicStepperDriver face, double rotation) {
  face.enable();
  face.rotate(rotation);
  if (face_letter == 'D') {
    delay(D_MOVE_DELAY_MS);
  } else {
    delay(MOVE_DELAY_MS);
  }
  face.disable();
}

/**
  Executes specified face by specified number of quarter-turns
  @param str Cube notation string
  @param rotation Number of quarter-turns
*/
void execute_simple(String str, int rotation) {
  if (str.charAt(0) == 'U') {
    execute_moves("R L F2 B2 R' L'");
    execute_simple("D", rotation);
    execute_moves("R L F2 B2 R' L'");
    return;
  }

  char face_letters [] = {'L', 'R', 'F', 'B', 'D'};
  BasicStepperDriver face_drivers [] = {left, right, front, back, down};

  for (int i = 0; i < 5; i++) {
    if (str.charAt(0) == face_letters[i]) {
      rotate(str.charAt(0), face_drivers[i], rotation * -90);
      return;
    }
  }
}

/**
  Executes move for single cube notation term (e.g. "D2", "F'", and "L")
  @param str Cube notation string
*/
void execute(String str) {
  if (str.length() == 1) {
    execute_simple(str, 1);
  } else if (str.charAt(1) == '2') {
    execute_simple(str, 2);
  } else if (str.charAt(1) == '\'') {
    execute_simple(str, -1);
  }
}

/**
  Executes entire cube notation string (e.g. "F D F' D'")
  @param str Cube notation string
*/
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
  // Initialize Serial
  Serial.begin(115200);
  Serial.setTimeout(1);

  // Set Pin Modes
  pinMode(L_DIR, OUTPUT);
  pinMode(L_STEP, OUTPUT);
  pinMode(L_ENABLE, OUTPUT);
  pinMode(R_DIR, OUTPUT);
  pinMode(R_STEP, OUTPUT);
  pinMode(R_ENABLE, OUTPUT);
  pinMode(F_DIR, OUTPUT);
  pinMode(F_STEP, OUTPUT);
  pinMode(F_ENABLE, OUTPUT);
  pinMode(B_DIR, OUTPUT);
  pinMode(B_STEP, OUTPUT);
  pinMode(B_ENABLE, OUTPUT);
  pinMode(D_DIR, OUTPUT);
  pinMode(D_STEP, OUTPUT);
  pinMode(D_ENABLE, OUTPUT);

  // Initialize Stepper Motors
  left.begin(RPM, MICROSTEPS);
  right.begin(RPM, MICROSTEPS);
  front.begin(RPM, MICROSTEPS);
  back.begin(RPM, MICROSTEPS);
  down.begin(D_RPM, MICROSTEPS);
  left.setEnableActiveState(LOW);
  right.setEnableActiveState(LOW);
  front.setEnableActiveState(LOW);
  back.setEnableActiveState(LOW);
  down.setEnableActiveState(LOW);

  disable_all();
}

void loop() {
  while (Serial.available() > 0) {
    char character = Serial.read();

    if (character != '\n') {
      solution += character;
    } else {
      Serial.println("Solution Received: " + solution);
      long time = millis();
      execute_moves(solution);
      Serial.println("Solved In: " + String(millis() - time) + " ms");
      solution = "";
    }
  }
}
