int inByte = '0';
int motorPin = 2; 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(motorPin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  if (Serial.available() > 0){
    inByte = (Serial.read());

    if (inByte == '0') {
      digitalWrite(motorPin,LOW);
    }
    
    if (inByte == '1') {
      digitalWrite(motorPin,HIGH);
    }
  }

}
