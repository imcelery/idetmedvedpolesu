//https://www.tinkercad.com/things/hr0R0XUJJn8-neat-trug/editel?sharecode=hSdStL78T2_HkBECKIxWFYbE5YT-M5HCZm2DftLmxOw
int analogPin1 = A0; 
int analogPin2 = A1;
                    
float minVal1 = 0;
float maxVal1 = 675;

float minVal2 = 0;
float maxVal2 = 675;

float maxVert = 180;

#include <Servo.h>

Servo myservo1;
Servo myservo2;

void setup() {


  pinMode(4, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(12, OUTPUT);

  
  myservo1.attach(12);
  myservo2.attach(13);
}

void loop() {
  
  float napor = (analogRead(analogPin1) - minVal1) / maxVal1 * maxVert;
  float temp = (analogRead(analogPin2) - minVal2) / maxVal2;
  
  myservo1.write(napor * (temp));
  myservo2.write(napor * (1 - temp));
  
  if(napor > 0){
    if(temp != 0){
      digitalWrite(4, HIGH);
    }
    else{
      digitalWrite(4, LOW);
    }
    
    if(temp != 1){
      digitalWrite(8, HIGH);
    }
    else{
      digitalWrite(8, LOW);
    }
    digitalWrite(8, LOW);
    digitalWrite(4, LOW);
  }
  
}