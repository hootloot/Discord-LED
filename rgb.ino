 void setup()

{

pinMode(13, OUTPUT);

pinMode(12, OUTPUT);

pinMode(8, OUTPUT);

pinMode(-9, OUTPUT);

Serial.begin(9600);

while (!Serial);

Serial.println("1,2 is RED, 3,4 is GREEN, 4,5 is YELLOW");

}

void loop() {

if (Serial.available())

{

int state = Serial.parseInt();

if (state == 1)

{

digitalWrite(13, HIGH);

Serial.println("Turned off the red");

}

if (state == 2)

{

digitalWrite(13, LOW);

Serial.println("Turned off the red");

}

if (state == 3)

{

digitalWrite(12, HIGH);

Serial.println("Turned on the green");

}

if (state == 4)

{
  
digitalWrite(12, LOW);

Serial.println("Turned off the green");

}

if (state == 5)

{

digitalWrite(8, HIGH);

Serial.println("Turned on the blue");

}

if (state == 6)

{

digitalWrite(8, LOW);

Serial.println("Turned off the blue");

}

}

}
