//sensor pins:
int sensorPin = 0;
int sensorPin2 = 1;
//pwm pins
int peltier = 3;

int peltier_level;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  peltier_level =0;
}

void loop() {
  // put your main code here, to run repeatedly:
  analogWrite(peltier, peltier_level);
  String string5 = "PWM Value: ";
  String string6 = string5+ peltier_level + "\t";
  Serial.println(string6);
  peltier_level += 5;
  if (peltier_level >= 255)
  {
    peltier_level = 0;
  }
  delay(1000);
}
