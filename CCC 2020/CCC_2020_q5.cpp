#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <math.h>
#include <deque>
using namespace std;

deque<vector<int>> coords(int n, int M, int N){
    deque<vector<int>> fact;
    for (int i=1; i<ceil(sqrt(n))+1; i++){
        if (!(n%i)){
            int b = n/i;
            if (i <= M && b <= N){
                vector<int> temp{i-1, b-1};
                if (find(fact.begin(), fact.end(), temp) == fact.end()){
                    fact.push_back(temp);
                }
            }
            
            if (b <= M and i <= N){
                vector<int> temp{b-1, i-1};
                if (find(fact.begin(), fact.end(), temp) == fact.end()){
                    fact.push_back(temp);
                }
            }
        }
    }
    
    return fact;
}

string escape(int m, int n, vector<vector<int>> grid){
    vector<int> pos{0, 0};
    vector<vector<int>> seen;
    deque<deque<vector<int>>> junctions;
    map<int, deque<vector<int>>> factors;

    if (grid[0][0] == m*n){
        return "yes";
    }

    while (true){
        int num = grid[pos[0]][pos[1]];
        deque<vector<int>> options;

        if (factors.find(num) == factors.end()){
            options = coords(num, m, n);
            factors[num] = options;
        }
        else{
            options = factors[num];
        }
        
        seen.push_back(pos);

        if (!options.empty()){
            pos = options.front();
            options.pop_front();
            
            if (junctions.empty() && pos[0] == 0 && pos[1] == 0){
                return "no";
            }
            
            if (!options.empty()){
                junctions.push_back(options);
            }
        }

        if (find(seen.begin(), seen.end(), pos) != seen.end()){
            if (junctions.empty()){
                return "no";
            }
            if (!options.empty() &&  !junctions.empty()){
                options = junctions.front();
                junctions.pop_front();
                pos = options.front();
                options.pop_front();
                if (!options.empty()){
                    junctions.push_back(options);
                }
            }
        }

        if (pos[0] == m-1 && pos[1] == n-1){
            return "yes";
        }
    }
}

int main(){
    int M, N;
    vector<vector<int>> grid;
    
    cin>>M>>N;
    grid.resize(M);
    
    for (int i=0; i<M; i++){
        grid[i].resize(N);
        for (int j=0; j<N; j++){
            cin>>grid[i][j];
        }
    }
    
    cout<<escape(M, N, grid)<<endl;
    return 0;
}
