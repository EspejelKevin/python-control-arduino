byte rele1 = 2;
byte rele2 = 3;

void setup() {
  pinMode(rele1, OUTPUT);
  pinMode(rele2, OUTPUT);
  Serial.begin(9600);
  digitalWrite(rele1, HIGH);
}

void loop() {
  if(Serial.available()){
    char senial = Serial.read();
    if(senial == '1'){
      digitalWrite(rele1, LOW);
    }
    else if(senial == '2'){
      digitalWrite(rele1, HIGH);
    }
  }
}
