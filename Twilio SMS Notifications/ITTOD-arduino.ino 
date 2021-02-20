#include <LiquidCrystal.h>
int trig=10;
int echo=9;



LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int counter=0;
int prev=0;
int currentState1=0;
int previousState1=0;
int currentState2=0;
int previousState2=0;
int outside = 0;
int inside = 0;


void setup() {
  // put your setup code here, to run once:
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
  lcd.begin(16,2);
  lcd.setCursor(0,0);
  lcd.print("Customer");
  lcd.setCursor(0,1);
  lcd.print(" Counter");
  delay(5000);
  lcd.clear();
  lcd.print("In through the ");
  lcd.setCursor(0,1);
  lcd.print("out door");
  delay(5000);
  lcd.clear();

}

void loop() {
  // put your main code here, to run repeatedly:

  lcd.begin(16,2);
 // lcd.setCursor(0,0);
 // lcd.print("IN: ");
  //lcd.setCursor(7,0);
  //lcd.print("OUT: ");
  lcd.setCursor(0,0);
  lcd.print("Total In: ");
  long duration, distance;
  digitalWrite(trig,LOW);
  delayMicroseconds(500);
  digitalWrite(trig, HIGH);
  delay(100);
  digitalWrite(trig, LOW);
  duration = pulseIn(echo, HIGH);
  distance = (duration/2 /29.1);
  if (distance <= 9){
    currentState1=1;
  }
  else{
    currentState1=0;
  }
  delay(1000);
  if(currentState1 !=previousState1){
    if(currentState1==1){
      counter=counter +1;
      prev=counter-1;
    }
    lcd.setCursor(0,0);
    lcd.print("Total Inside: ");
    lcd.setCursor(0,1);
    lcd.print(counter);
   // String submit=String(String(counter)+","+String(prev));
    Serial.println(counter);
    inside=inside+1;
  }
//  lcd.setCursor(4,0);
//  lcd.print(inside);

  if(distance > 9 && distance <=18){
    currentState2=1;
  }
  else{
    currentState2=0;
  }
  delay(100);

  if(currentState2 != previousState2){
    if(currentState2 ==1){
 
      counter=counter-1;
      prev=counter+1;
      
      
    }
    lcd.setCursor(0,0);
    lcd.print("Total In: ");
    lcd.setCursor(0,1);
    lcd.print(counter);
   // String submit=String(String(counter)+","+String(prev));
    Serial.println(counter);
    outside=outside+1;
  }
//  lcd.setCursor(12,0);
//  lcd.print(outside);
  lcd.setCursor(0,0);
  lcd.print("Total In: ");
  lcd.setCursor(0,1);
  lcd.print(counter);
 // String submit=String(counter)+","+String(prev);
  Serial.println(counter);
  if(counter>9 || counter<0){
    lcd.setCursor(0,0);
    lcd.print("Total In: ");
    lcd.setCursor(0,1);
    lcd.print(counter);
  //  String submit=String(String(counter)+","+String(prev));
    Serial.println(counter);
    delay(100);
    lcd.clear();
  }

  
}
