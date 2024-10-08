#include <Servo.h>

const int trigPin = 7;
const int echoPin = 6;
const int servoPin = 9;

Servo myServo;

long duration;
int distance;

int openAngle = 90;  
int closeAngle = 0;   

unsigned long objectRemovedTime = 0;
bool objectDetected = false;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  myServo.attach(servoPin);
  myServo.write(closeAngle); 

  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  
  distance = duration * 0.034 / 2;
  
  Serial.print("Distance: ");
  Serial.println(distance);
  
  if (distance <= 30) {
    myServo.write(openAngle);  
    objectDetected = true;     
  } else if (objectDetected) {
    objectRemovedTime = millis(); 
    objectDetected = false;       
  }

  if (!objectDetected && (millis() - objectRemovedTime >= 1000)) {
    myServo.write(closeAngle); 
  }

  delay(500);
}
