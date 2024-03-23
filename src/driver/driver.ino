

int leftMotorForward = 11;
int leftMotorReverse = 9;

int rigtMotorForward = 3;
int rightMotorReverse = 5;
int inByte = 0;

unsigned long leftForwardTimer = 0;
unsigned long leftReverseTimer = 0;
unsigned long rightForwardTimer = 0;
unsigned long rightReverseTimer = 0;

unsigned long stopAfter = 100;

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
    Serial.print("ack");
    Serial.println(inByte);

  if (inByte == 49) {
    digitalWrite(leftMotorForward,HIGH);
    leftForwardTimer = millis();
    //Serial.println('ack1');
  }
  
  if (inByte == 50) {
    digitalWrite(leftMotorReverse,HIGH);
    leftReverseTimer = millis();
    //Serial.println('ack2');
  }

  //if (inByte == 51) {
   // digitalWrite(leftMotorForward,LOW);
    //Serial.println('ack3');
 // }

 // if (inByte == '4') {
  //  digitalWrite(leftMotorReverse,LOW);
    //Serial.println('ack4');
  //}
  
  if (inByte == 52) {
    digitalWrite(rigtMotorForward,HIGH);
    rightForwardTimer = millis();
    //Serial.println('ack5');
  }

  if (inByte == 53) {
    digitalWrite(rightMotorReverse,HIGH);
    rightReverseTimer = millis();
    //Serial.println('ack6');
  }

  

   //   if (inByte == 55) {
   // digitalWrite(rigtMotorForward,LOW);
    //Serial.println('ack7');
  }
  unsigned long curentTime = millis();


  if (curentTime - leftForwardTimer > stopAfter){
    digitalWrite(leftMotorForward,LOW);
    leftForwardTimer = millis();
  }

  if (curentTime - leftReverseTimer > stopAfter){
    digitalWrite(leftMotorReverse,LOW);
    leftReverseTimer = millis();
  }

  if (curentTime - rightForwardTimer > stopAfter){
    digitalWrite(rigtMotorForward,LOW);
    rightForwardTimer = millis();
  }

  if (curentTime - rightReverseTimer  > stopAfter){
    digitalWrite(rightMotorReverse, LOW);
    rightReverseTimer = millis();
  }
}
