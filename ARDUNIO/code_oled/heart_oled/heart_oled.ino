#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

String text = "I Love You 3000";  // Chuỗi cần hiển thị
int textPosX;                     // Vị trí X khởi tạo
int textPosY = SCREEN_HEIGHT / 2; // Vị trí Y giữa màn hình
int textWidth = text.length() * 6; // Chiều rộng của chuỗi (mỗi ký tự ~6 pixel)

bool showHeart = false;           // Cờ để xác định khi nào cần hiển thị trái tim
int heartSize = 1;                // Kích thước ban đầu của trái tim
int maxHeartSize = 30;            // Kích thước tối đa của trái tim

void setup() {
  // Khởi tạo màn hình OLED với SSD1306_SWITCHCAPVCC
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;);
  }
  display.clearDisplay();
  display.setTextSize(1);         // Kích thước chữ
  display.setTextColor(SSD1306_WHITE);
  display.display();

  // Tính toán vị trí X khởi tạo: màn hình rộng - chiều dài chuỗi
  textPosX = SCREEN_WIDTH - textWidth;
}

void loop() {
  if (!showHeart) {
    display.clearDisplay();  // Xóa màn hình mỗi lần lặp

    // Vẽ chuỗi chữ "I Love You 3000" trên một dòng cố định
    display.setCursor(textPosX, textPosY);
    display.print(text);

    display.display();

    // Dịch chuyển chuỗi từ phải sang trái
    textPosX -= 2;

    // Khi chuỗi ra hoàn toàn khỏi màn hình, reset vị trí ban đầu và hiển thị trái tim
    if (textPosX < -textWidth) {
      showHeart = true;  // Đặt cờ để hiển thị trái tim sau khi chuỗi kết thúc
    }
  } else {
    display.clearDisplay();  // Xóa màn hình

    // Tạo hiệu ứng phóng to cho trái tim
    drawHeart(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, heartSize);  // Vẽ trái tim với kích thước tăng dần
    display.display();
    
    // Tăng kích thước trái tim dần dần để tạo hiệu ứng phóng to
    heartSize += 2;

    // Nếu đạt kích thước tối đa, giữ trái tim hiển thị trong một lúc rồi kết thúc
    if (heartSize > maxHeartSize) {
      delay(2000);  // Hiển thị trái tim trong 2 giây
      heartSize = 1;  // Reset kích thước về nhỏ lại để chạy lại hiệu ứng (nếu cần)
    }

    delay(100);  // Điều chỉnh tốc độ phóng to
  }

  delay(50);  // Tốc độ di chuyển
}

// Hàm để vẽ hình trái tim mềm mại
void drawHeart(int x, int y, int size) {
  int radius = size / 2;

  // Vẽ hai nửa đường tròn trên cùng để tạo hình trái tim
  display.fillCircle(x - radius, y - radius / 2, radius, SSD1306_WHITE);
  display.fillCircle(x + radius, y - radius / 2, radius, SSD1306_WHITE);

  // Vẽ tam giác bên dưới để hoàn thành hình trái tim
  display.fillTriangle(x - size, y, x + size, y, x, y + size, SSD1306_WHITE);
}
