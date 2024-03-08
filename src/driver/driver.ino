

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

    if (inByte == '1') {
      digitalWrite(motorLeftForward,HiGH);
    }
    
    if (inByte == '2') {
      digitalWrite(leftMotorReverse,HIGH);
    }

    if (inByte == '3') {
      digitalWrite(leftMotorReverse,LOW);
    }

        if (inByte == '4') {
      digitalWrite(motorLeftForward,HiGH);
    }
    
    if (inByte == '5') {
      digitalWrite(leftMotorReverse,HIGH);
    }

    if (inByte == '6') {
      digitalWrite(leftMotorReverse,LOW);
    }

        if (inByte == '7') {
      digitalWrite(leftMotorReverse,LOW);
    }

        if (inByte == '8') {
      digitalWrite(leftMotorReverse,LOW);
    }
    
    

  }
  
}
