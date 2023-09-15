//https://www.tinkercad.com/things/lI1ft8vxEOD-fantastic-vihelmo/editel?sharecode=4jEmGCEsUjRdhqbiTNHHpfNDsZcwoVk5SMbWw7z6rFM
int analogPin = A0; 

                    
float minVal = 200;
float maxVal = 400;

float maxVert = 90;

bool lowVlash = false;

bool highVlash = false;

#include <Servo.h>

Servo myservo1;

void setup() {
  Serial.begin(9600);
  pinMode(4, OUTPUT);
  myservo1.attach(12);
}

void loop() {
  
  float vlash = analogRead(analogPin);
  Serial.println(vlash);
  if(minVal > vlash){
    lowVlash = true;
  }
  
  if(maxVal < vlash){
    highVlash = true;
  }
  
  if(lowVlash){
    if((minVal + maxVal)/ 2 <= vlash){
    	lowVlash = false;
    }
  	myservo1.write(maxVert);
  }
  else{
    myservo1.write(0);
  }
  
  if(highVlash){
    if((minVal + maxVal)/ 2 >= vlash){
    	highVlash = false;
    }
  	digitalWrite(4, HIGH);
  }
  else{
    digitalWrite(4, LOW);
  } 
}