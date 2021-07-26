#include <iostream>
#include <vector>
#include <typeinfo>
#include <string>
#include <deque>
#include <bits/stdc++.h>
#include <fstream>
using namespace std;

int r, c, q;
int input;
int posx, posy;
unordered_set<int> beat;

vector<vector<int>> levels;
vector<vector<int>> types;
deque<deque<vector<int>>> junctions;
vector<vector<int>> seen;
vector<int> ans;

int search(int x, int y, int level, vector<vector<int>> levels, int r, int c){
	posx = x-1;
	posy = y-1;
	if (levels[posy][posx] > level){
		return 0;
	}
	while (true){
		beat.insert(types[posy][posx]);
		
		vector<int> temp{posx, posy};
		seen.push_back(temp);

		deque<vector<int>> options;
	
		if (0 <= posx-1 and posx-1 < c){
			if (levels[posx-1][posy] <= level){
				vector <int> nxt{posx-1, posy};
				options.push_back(nxt);
			}
		}
		
		if (posx < c and 0 <= posy-1 and posy-1 < r){
			if (levels[posx][posy-1] <= level){
				vector <int> nxt{posx, posy-1};
				options.push_back(nxt);
			}
		}
		
		if (posx+1 < c and 0 <= posy and posy<r){
			if (levels[posx+1][posy] <= level){
				vector<int> nxt{posx+1, posy};
				options.push_back(nxt);
			}
		}
		if (posx < c and posy+1 < r){
			if (levels[posx][posy+1] <= level){
				vector<int> nxt{posx, posy+1};
				options.push_back(nxt);
			}
		}
		if (!options.empty()){
			vector<int> temp;
			temp = options.front();
			options.pop_front();
			posx = temp[0];
			posy = temp[1];
			if (options.size() > 0){
				junctions.push_back(options);
			}
		}

		if (find(seen.begin(), seen.end(), temp) != seen.end()){
			if (junctions.empty()){
				return beat.size();
			}

			if (!junctions.empty()){
				vector<int> temp;
				options = junctions.front();
				junctions.pop_front();
				temp = options.front();
				options.pop_front();
				posx = temp[0];
				posy = temp[1];
				
				if (options.size()>0){
					junctions.push_back(options);
				}
			}
		}
	}
	return 0;
}

int main() {
	fstream f;
 /* f = open('D:\\Computing\\Python\\NOI\\pokemonmaster\\input\\5.12.in', )*/
	cin>>r>>c>>q;
	levels.resize(r);
	for (int i=0; i<r; i++){
		for (int j=0; j<c; j++){
			int input;
			cin>>input;
			levels[i].push_back(input);
		}
	}

	types.resize(r);
	for (int i=0; i<r; i++){
		for (int j=0; j<c; j++){
			int input;
			cin>>input;
			types[i].push_back(input);
		}
	}

	for (int i=0; i<q; i++){
		int t, x, y, z;
		
		cin>>t>>x>>y>>z;
		if (t==1){
			types[y-1][x-1] = z;

		} 
		else if (t==2){
			ans.push_back(search(x, y, z, levels, c, r));
		} 
	}
	
	for (int i=0; i<ans.size(); i++){
		cout<<ans[i]<<endl;
	}
	return 0;
}

