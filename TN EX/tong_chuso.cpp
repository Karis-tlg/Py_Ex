#include <iostream>
#include <string>
#include <string.h>
#include <math.h>
using namespace std;

int main(){
	// Chuyen kieu string ve int
	string s = "12345";
	int l1 = s.length();
	int num1 = 0;
	for(int i = l1 - 1; i >= 0; --i){
		num1 += (int)(s[i] - '0');
	}
	cout << "num1 = " << num1 << 'n';
	return 0;
	}
