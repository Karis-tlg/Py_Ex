#include <bits/stdc++.h>
using namespace std;

// Hàm tìm độ dài của chuỗi con tăng dần dài nhất
int LIS_length(vector<int>& books) {
    vector<int> lis;
    for (int book : books) {
        auto it = lower_bound(lis.begin(), lis.end(), book);
        if (it == lis.end()) {
            lis.push_back(book);
        } else {
            *it = book;
        }
    }
    return lis.size();
}

int main() {
    // Mở file để đọc dữ liệu đầu vào
    ifstream infile("THUVIEN.INP");
    ofstream outfile("THUVIEN.OUT");

    int N;
    infile >> N;
    vector<int> books(N);
    for (int i = 0; i < N; ++i) {
        infile >> books[i];
    }

    // Tìm độ dài của chuỗi con tăng dần dài nhất
    int lis_length = LIS_length(books);

    // Số lần chuyển sách tối thiểu
    int min_moves = N - lis_length;

    // Ghi kết quả ra file
    outfile << min_moves << endl;

    // Đóng file
    infile.close();
    outfile.close();

    return 0;
}
