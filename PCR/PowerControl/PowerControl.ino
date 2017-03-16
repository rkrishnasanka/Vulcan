int peltier = 3; //The N-Channel MOSFET is on digital pin 11
int power = 0; //Power level fro 0 to 99% //This is a value from 0 to 255 that actually controls the MOSFET

void setup() {
  Serial.begin(9600);
  Serial.print("Power=");
  Serial.println(power);
}

void loop() {
  char option;

  if (Serial.available() > 0)
  {
    option = Serial.read();
    if (option == 'a')
      power += 5;
    else if (option == 'z')
      power -= 5;

    if (power > 255) power = 255;
    if (power < 0) power = 0;
    Serial.print("Power=");
    Serial.println(power);
  }


  analogWrite(peltier, power); //Write this new value out to the port
  delay(1000);
}
