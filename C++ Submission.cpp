#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int m, n;
    cin >> m >> n;

    vector<int> tt(n), zz(n), yy(n);

    // Input 
    for (int i = 0; i < n; ++i) {
        cin >> tt[i] >> zz[i] >> yy[i];
    }

    // Setting the boundaries for binary search
    int left = 0;
    int right = (m / *min_element(zz.begin(), zz.end())) * *max_element(yy.begin(), yy.end());
    right += *max_element(tt.begin(), tt.end()) * m;

    // Initializing the answer in case the balloons to be inflated is zero
    int ans = 0;
    vector<int> res(n);

    // Function to check if it's possible to inflate all balloons within this many minutes
    auto check = [&](int minutes) -> pair<bool, vector<int>> {
        int done = 0;
        vector<int> worked(n);
        for (int i = 0; i < n; ++i) {
            int this_ = 0;
            if (minutes / tt[i] > zz[i]) {
                this_ += (minutes / ((zz[i] * tt[i]) + yy[i])) * zz[i];
                int minus = (minutes / ((zz[i] * tt[i]) + yy[i])) * ((zz[i] * tt[i]) + yy[i]);
                int left_min = minutes - minus;
                this_ += left_min / tt[i];
            } else {
                this_ += minutes / tt[i];
            }
            done += this_;
            worked[i] = this_;
            if (done >= m) {
                return {true, worked};
            }
        }
        return {false, {}};
    };

    // Binary search from max minutes to minimum minutes to check the minimum required minutes to perform the task
    while (left <= right && m > 0) {
        int mid = (left + right) / 2;
        if (check(mid).first == true) {
            ans = mid;
            res = check(mid).second;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    cout << ans << endl;
    for (int x : res) {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}
