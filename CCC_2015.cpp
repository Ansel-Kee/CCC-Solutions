#include <bits/stdc++.h>
using namespace std;
/*
int main() {

  int m, d;
  cin >> m >> d;
  if (m == 2 && d == 18) {
    cout << "Special" << endl;
  } else if (m > 2 || m == 2 && d > 18) {
    cout << "After" << endl;
  } else {
    cout << "Before" << endl;
  }
  return 0;
}
*/
/*
int main() {
  string happy = ":-)", sad = ":-(";
  int happy_count = 0, sad_count = 0;

  string s;
  getline(cin, s);
  for (int i = 0; i <= s.size()-3; i++) {
    if (s.substr(i, 3) == happy) {
      happy_count++;
    } else if (s.substr(i, 3) == sad) {
      sad_count++;
    }
  }

  if (happy_count == 0 && sad_count == 0) {
    cout << "none" << endl;
  } else if (happy_count == sad_count) {
    cout << "unsure" << endl;
  } else if (happy_count > sad_count) {
    cout << "happy" << endl;
  } else {
    cout << "sad" << endl;
  }joy
  return 0;
}
*/

int main() {
  string vowels = "aeiou";
  string s; // joy 
  cin >> s;

  string ans;
  for (int i = 0; i < s.size(); i++) {
    ans += s[i];

    if (find(vowels.begin(), vowels.end(), s[i]) == vowels.end()) {
      int d = 30;
      int j;
      // find and add the closest vowel
      for (int k = 0; k < 5; k++) {
        if (abs(vowels[k] - s[i]) < d) {
        //  ascii vowels[k]- ascii s[i]
          d = abs(vowels[k] - s[i]); // d=8, d=5
          j = k;
        }
      }
      ans += vowels[j];
    // next character in the alphabet after s[i] if its a consonant, otherwise take the one after
      if (s[i] == 'z') {
        ans += 'z';
      } else if (find(vowels.begin(), vowels.end(), s[i]+1) == vowels.end()) {
        ans += s[i] + 1;
      } else {
        ans += s[i] + 2;
      }
    }
  }
  cout << ans << endl;
  return 0;
}


/*
int main() {
  char cmd;
  int n, t, m = 0;
  cin >> m;

  vector<int> final(101);
  vector<int> reply(101);
  vector<int> sent(101);
  for (int i = 0; i < m; i++) {
    cin >> cmd >> n;
    if(cmd == 'S')
        {
            final[n] += t - sent[n];
            reply[n] = 1;
        }
        else if(cmd == 'R')
        {
            reply[n] = -1;
            sent[n] = t;
        }
        else {
            t += n - 2;
        }
        t++;
  }
  for(int j = 0; j < 101; ++j)
    {
        if(reply[j] > 0)
            cout<<j<<" "<<final[j]<<endl;
        else if (reply[j] < 0){
            cout<<j<<" "<<reply[j]<<endl;
        }
    }
  return 0;
}
*/

