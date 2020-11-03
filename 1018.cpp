#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <map>
 
using namespace std;
 
int main()
{
    int N = 0, i = 0;
    map<char,int> map1, map2;
    int res1[3] = {0}, res2[3] = {0};//0 赢 1平局 2输
    char ch1 = 0, ch2 = 0, maxch = 0;
    int maxx = 0;
    map<char,int>::iterator it;
 
    /* 读取数据，并进行处理 */
    cin >> N;
    for(i = 0; i < N; i++)
    {
        cin >> ch1 >> ch2;
        if (ch1 == ch2) //平手
        {
            res1[1]++;
            res2[1]++;
        }
        else if ((ch1 == 'C' && ch2 == 'J') //甲赢
                 || (ch1 == 'J' && ch2 == 'B')
                 || (ch1 == 'B' && ch2 == 'C'))
        {
            res1[0]++;
            res2[2]++;
            map1[ch1]++;
        }
        else
        {
            res1[2]++;
            res2[0]++;
            map2[ch2]++;
        }
    }
 
    /* 输出数据  */
    cout << res1[0] << " " << res1[1] << " " << res1[2] << endl;
    cout << res2[0] << " " << res2[1] << " " << res2[2] << endl;
 
    /* 找到甲获胜次数最多的手势 */
    maxch = 'B';
    for(it = map1.begin(); it != map1.end(); it++)
    {
        if (it->second > maxx)
        {
            maxch = it->first;
            maxx = it->second;
        }
    }
    cout << maxch << " ";
 
    /* 找到已获胜次数最多的手势 */
    maxch = 'B';
    maxx = 0; //防止甲的结果影响乙
    for(it = map2.begin(); it != map2.end(); it++)
    {
        if (it->second > maxx)
        {
            maxch = it->first;
            maxx = it->second;
        }
    }
    cout << maxch << endl;
 
    return 0;
}
