

int leftMotorForward = 9;
int leftMotorReverse = 11;

int rigtMotorForward = 5;
int rightMotorReverse = 3;
int inByte = 0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(leftMotorForward,OUTPUT);
  pinMode(leftMotorReverse,OUTPUT);
  pinMode(rigtMotorForward,OUTPUT);
  pinMode(rightMotorReverse,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0 ) {
    inByte = Serial.read();

    if (inByte == '1') {
      digitalWrite(leftMotorForward,HIGH);
      Serial.print('ack1');
    }
    
    if (inByte == '2') {
      digitalWrite(leftMotorReverse,HIGH);
      Serial.print('ack2');
    }

    if (inByte == '3') {
      digitalWrite(leftMotorForward,LOW);
      Serial.print('ack3');
    }

        if (inByte == '4') {
      digitalWrite(leftMotorReverse,LOW);
      Serial.print('ack4');
    }
    
    if (inByte == '5') {
      digitalWrite(rigtMotorForward,HIGH);
      Serial.print('ack5');
    }

    if (inByte == '6') {
      digitalWrite(leftMotorReverse,HIGH);
      Serial.print('ack6');
    }

        if (inByte == '7') {
      digitalWrite(rigtMotorForward,LOW);
      Serial.print('ack7');
    }

        if (inByte == '8') {
      digitalWrite(rightMotorReverse,LOW);
      Serial.print('ack8');
    }

    
    

  }
  
}
