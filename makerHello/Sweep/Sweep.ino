

/*
Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
                // twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
char s;
void setup()
{
  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  pinMode(13,OUTPUT);
   digitalWrite(13,HIGH);
  delay(1000);
  digitalWrite(13,LOW);
 //  myservo.write(175); 
}

void loop()
{
  if(Serial.available()>0)   s = Serial.read();

  if(s == '1')
  {

  for(pos = 120; pos>=30; pos-=1)     // goes from 180 degrees to 0 degrees
  {
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
    for(pos = 30; pos <= 120; pos += 1) // goes from 0 degrees to 180 degrees
  {                                  // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
   digitalWrite(13,HIGH);
   delay(1000);
   digitalWrite(13,LOW);
  }
  s = '0';
}
