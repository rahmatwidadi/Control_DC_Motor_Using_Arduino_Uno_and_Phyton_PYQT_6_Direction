//data serial
int inbytes = 1;
byte RXBuf [64];
//int jalan = 0;

// motor satu
int enA = 10;
int in1 = 9;
int in2 = 8;

// motor dua
int enB = 5;
int in3 = 7;
int in4 = 6;

void setup()
{
// set all the motor control pins to outputs
Serial.begin(9600);
pinMode(enA, OUTPUT);
pinMode(enB, OUTPUT);
pinMode(in1, OUTPUT);
pinMode(in2, OUTPUT);
pinMode(in3, OUTPUT);
pinMode(in4, OUTPUT);
}

void stay()
{
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  analogWrite (enA, 0);
  analogWrite (enB, 0);
}

void forward()
{
  //motor 1
  digitalWrite (in1, HIGH);
  digitalWrite (in2,  LOW);
  analogWrite (enA, 100);
  //motor 2
  digitalWrite (in3, HIGH);
  digitalWrite (in4, LOW);
  analogWrite (enB, 100);
}

void reverse()
{
  //motor 1
  digitalWrite (in1,  LOW);
  digitalWrite (in2,  HIGH);
  analogWrite (enA, 100);
  //motor 2
  digitalWrite (in3, LOW);
  digitalWrite (in4, HIGH);
  analogWrite (enB, 100);
}

void turn_forward_left()
{
  //motor 1
  digitalWrite (in1, HIGH);
  digitalWrite (in2,  LOW);
  analogWrite (enA, 120);
  //motor 2
  digitalWrite (in3, HIGH);
  digitalWrite (in4, LOW);
  analogWrite (enB, 0);
}

void turn_forward_right()
{
  //motor 1
  digitalWrite (in1, HIGH);
  digitalWrite (in2,  LOW);
  analogWrite (enA, 0);
  //motor 2
  digitalWrite (in3, HIGH);
  digitalWrite (in4, LOW);
  analogWrite (enB, 120);
}

void turn_reverse_right()
{
  //motor 1
  digitalWrite (in1, LOW);
  digitalWrite (in2,  HIGH);
  analogWrite (enA, 0);
  //motor 2
  digitalWrite (in3, LOW);
  digitalWrite (in4, HIGH);
  analogWrite (enB, 120);
}

void turn_reverse_left()
{
  //motor 1
  digitalWrite (in1,  LOW);
  digitalWrite (in2,  HIGH);
  analogWrite (enA, 120);
  //motor 2
  digitalWrite (in3, LOW);
  digitalWrite (in4, HIGH);
  analogWrite (enB, 0);
}


void loop()
{
  if (Serial.available()) 
  {
    int inbytes = Serial.readBytes(RXBuf,sizeof(RXBuf));
    switch (inbytes) {
      case 1:
        stay();
        break;
      case 2:
        forward();
        break;
      case 3:
        turn_forward_right();
        delay (1000);
        forward();
        break;
      case 4:
        turn_reverse_right();
        delay (1000);
        reverse();
        break;
      case 5:
        reverse();
        break;
      case 6:
        turn_reverse_left();
        delay (1000);
        reverse ();
        break;
      case 7:
        turn_forward_left();
        delay (1000);
        forward ();
        break;
      default:
        stay();
    }
  }
   
}

