#include<Servo.h>
Servo sm1,s1;
void setup() 
{
  // put your setup code here, to run once:
  
  
  sm1.attach(9);
  s1.attach(10);
  pinMode(11,INPUT);

}

void tata() // function for waving motion of the robots arm
{
  sm1.write(0);
  for(int i=1;i<=3;++i)
   {
    for(int j=666;j<=2000;j+=5)
     {
      s1.writeMicroseconds(j); // writeMicroseconds keyword used for smoother operation of the servo motor
      delayMicroseconds(5000); 
     }
    for(int k=2000;k>=666;k-=5)
     {
      s1.writeMicroseconds(k);
      delayMicroseconds(2500); 
     }
   }
}    

void loop() 
{
  // put your main code here, to run repeatedly:
if(11==HIGH)
tata();
}
