#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n = 0, id = 0, gra = 0, max_gra = 0, max_id = 0;
    cin >> n;
    vector<int> all(n + 1);
    for (int i = 0; i < n; i++) {
        cin >> id >> gra;
        all[id] += gra;
        if (id > max_id) {
            max_id = id;
        }
    }
    for (int i = 1; i < max_id + 1; i++) {
        if (all[i] > max_gra) {
            max_gra = all[i];
            id = i;
        }
    }
    cout << id << " " << max_gra;
    return 0;
}
