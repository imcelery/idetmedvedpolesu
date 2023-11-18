#include <iostream>
#include <vector>
using namespace std;
vector<vector<int>> vv;
vector<vector<long long>> vd;
vector<pair<int, int>> rebra;
int n;
long long vpered(int x, int old) {
    if (!vd[x][old]) {
        long long s = 1;
        for (int i = 0; i < n; i++) {
            if (vv[x][i] && i != old) {
                s += vpered(i, x);
            }
        }
        vd[x][old] = s;
        return s;
    } else {
        return vd[x][old];
    }
}
int main() {
    int m, a, b, q;
    cin >> n >> m;
    vv.resize(n);
    vd.resize(n);
    for (int i = 0; i < n; i++) {
        vv[i].resize(n);
        vd[i].resize(n);
    }
    for (int i = 0 ; i < m; i++) {
        cin >> a >> b;
        vv[a - 1][b - 1] = 1;
        vv[b - 1][a - 1] = 1;
        rebra.push_back(pair {a - 1, b - 1});
    }
    cin >> q;
    for (int i = 0; i < q; i++) {
        cin >> a;
        long long s = vpered(rebra[a - 1].first, rebra[a - 1].second) * vpered(rebra[a - 1].second, rebra[a - 1].first);
        cout << s << endl;
    }
}
