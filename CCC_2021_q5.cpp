#include <iostream>
#include <vector>
#include <map>
#include <bits/stdc++.h>
using namespace std;


int main(){
    int m, n, k;
    cin>>m>>n>>k;
    map<vector<char>, int> moves;
    
    for (int i=0;i<k;i++){
        char direction, pos;        
        cin>>direction>>pos;
        vector<char> move{direction, pos};

        if (moves.find(move) == moves.end()){
            moves[move] = 1;
        }
        else{
            moves[move]++;
            cout<<moves[move]<<endl;
        }
    }

    map<vector<char>, int>::iterator i;
    map<char, int> ans {{'R', 0}, {'C', 0}};
    for (i = moves.begin(); i != moves.end(); ++i) {
        if (i->second%2 == 1){
            ans[i->first[0]]++;
        }
    }

    cout<<ans['R']*n + ans['C']*m - ans['R']*ans['C']*2<<endl;
    return 0;
}
