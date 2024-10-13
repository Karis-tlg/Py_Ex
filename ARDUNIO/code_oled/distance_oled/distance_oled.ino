#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// Định nghĩa kích thước OLED
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

// Địa chỉ I2C của màn hình OLED
#define OLED_RESET    -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Định nghĩa chân kết nối HC-SR04
const int trigPin = 8;
const int echoPin = 9;

long duration;
int distance;

void setup() {
  // Thiết lập chân của HC-SR04
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Khởi động màn hình OLED
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("Khởi động OLED thất bại"));
    for (;;);
  }
  
  // Xóa màn hình
  display.clearDisplay();
  display.display();

  // Khởi động Serial
  Serial.begin(9600);

  // Hiển thị thông điệp chào mừng
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0, 10);
  display.print("Khoang cach tu HC-SR04");
  display.display();
  delay(2000);
}

void loop() {
  // Tính toán khoảng cách
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;

  // Xóa màn hình và hiển thị khoảng cách
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(0, 20);
  display.print("Distance:");
  display.setCursor(0, 40);
  display.print(distance);
  display.print(" cm");
  display.display();

  delay(500); // Cập nhật mỗi 500ms
}
