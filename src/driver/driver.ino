

int motorLeftForward = 2;
int leftMotorReverse = 3;

int rigtMotorForward = 4;
int rightMotorReverse = 5;



void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(motorLeftForward,OUTPUT);
  pinMode(leftMotorReverse,OUTPUT);
  pinMode(rigtMotorForward,OUTPUT);
  pinMode(rightMotorReverse,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0 ) {
    inByte = Serial.read();

    Serial.Print("I received: ");
    Serial.println(inByte, DEC);
  }
  
}
