#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main() {
    ifstream f("TONGLP.INP");
    ofstream g("TONGLP.OUT");

    int64_t n, count = 0;
    f >> n;

    int64_t i = 1, j = 1;
    while (j * j * j + 1 < n) {
        j++;
    }

    while (true) {
        int64_t k = i * i * i + j * j * j;
        if (k == n) {
            count++;
            g << i << " " << j << endl;
            i++;
            j--;
        } else if (k < n) {
            i++;
        } else {
            j--;
        }

        if (i > j) {
            break;
        }
    }

    g << endl << count << endl;

    f.close();
    g.close();

    return 0;
}
