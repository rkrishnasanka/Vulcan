//sensor pins:
int sensorPin = 0;
int sensorPin2 = 1;
//pwm pins
int peltier = 3;

//variables to keep track of
long desiredTemp;
float actualTemp;
byte PWMOutput;
long Error[15];
long Accumulator;
long PID;
int PTerm;
int ITerm;
int DTerm;
byte Divider;
int peltier_level;

void setup()
{
  Serial.begin(9600);
  PTerm = 3100;
  ITerm = 11;
  DTerm = 1;
  Divider = 0.05;
  desiredTemp = 55;
}

void getError() {
  byte i = 0;
  //bottom of plate

  //top of plate

  String stringa = "A0: ";
  String stringb = stringa + degreesC + "\t";

  String stringc = "A1: ";
  String stringd = stringc + degreesC2 + "\t";

  //Serial.print(stringb + stringd);
  
  actualTemp = (degreesC + degreesC2) * 0.5;

  String stringOne = "Desired Value: ";
  String stringTwo = stringOne + desiredTemp + "\t";

  String stringThree = "Actual Value: ";
  String stringFour = stringThree + actualTemp + "\t";

  Serial.print(stringTwo + stringFour);

  for (i = 9; i > 0; i--)
    Error[i] = Error[i - 1];
  // load new error into top array spot
  Error[0] = desiredTemp - actualTemp;

}

void calculatePID() {
  Accumulator += Error[0];
  PID = Error[0] * PTerm + ITerm * Accumulator + DTerm * (Error[0] - Error[9]);
  PID = PID >> Divider;

  if (PID >= 127)
    PID = 127;
  if (PID <= -126)
    PID = -126;
  PWMOutput = PID + 127;
  peltier_level = map(PWMOutput, 0, 255, 0, 76);

  String stringThree = "|Error|: ";
  float difference = desiredTemp - actualTemp;
  String stringFour = stringThree + abs(difference) + "\t";
  Serial.print(stringFour);

 

}
void loop()
{
  int option;
  if (Serial.available() > 0)
  {
    option = Serial.parseInt();
    desiredTemp = option;
  }
  getError();
  calculatePID();
  analogWrite(peltier, peltier_level);
  String string5 = "PWM Value: ";
  String string6 = string5 + peltier_level + "\t";
  Serial.println(string6);
  delay(1000);                                   //waiting a second
}
