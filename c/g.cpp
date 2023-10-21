#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <stack>
using namespace std;
int main() {
    int n, a, c, j;
    c = 1;
    cin >> n;
    vector<int> o;
    stack<int> v1;
    queue<int> v;
    for (int i = 0; i < n; i++) {
        cin >> a;
        v.push(a);
    }
    while (true) {
        while (v.front() != c) {
            if (v1.size() > 0) {
                if (v.front() > v1.top()) {
                    cout << 0;
                    return 0;
                }
            }
            o.push_back(1);
            v1.push(v.front());
            v.pop();
            if (v.size() == 0) {
                break;
            }
        }
        o.push_back(1);
        o.push_back(2);
        v.pop();
        c++;
        if (0 < v1.size()) {
            while (c == v1.top()) {
                o.push_back(2);
                c++;
                v1.pop();
                if (v1.size() == 0) {
                    break;
                }
            }
        }
        if (v.size() == 0) {
            if (c <= n) {
                cout << 0;
                return 0;
            } else {
                int t, k;
                k = 0;
                t = 1;
                vector<int> oo;
                for (int i = 0; i < o.size(); i++) {
                    if (o[i] == t) {
                        k++;
                    } else {
                        oo.push_back(k);
                        t = o[i];
                        k = 1;
                    }
                }
                oo.push_back(k);
                cout << oo.size() << endl;

                for (int i = 0; i < oo.size(); i++) {
                    if (i % 2 == 0) {
                        t = 1;
                    } else {
                        t = 2;
                    }
                    cout << t << " " << oo[i] << endl;
                }
                return 0;
            }
        }
    }
}
