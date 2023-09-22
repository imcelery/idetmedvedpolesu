#include <vector>
#include <algorithm>
class Solution {
public:
    int getPower(int x, int i) {
        if (x == 1) {
            return i;
        }
        if (x % 2 == 0) {
            return getPower(x / 2, i + 1);
        } else {
            return getPower(x * 3 + 1, i + 1);
        }
    }

    int getKth(int lo, int hi, int k) {
        std::vector<std::vector<int>> a(hi - lo + 1);

        for (int i = 0; i < hi - lo + 1; i++) {
            a[i].resize(2);
            a[i][0] = getPower(i + lo, 0);
            a[i][1] = i + lo;
        }
        std::sort(begin(a), end(a));
        return a[k - 1][1];
    }
};