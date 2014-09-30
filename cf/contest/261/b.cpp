#include <iostream>
#include <algorithm>
using namespace std;
int main(){
  int n;
  int beauty[200010];
  int max_diff = 0;
  int set = 0;
  cin>>n;
  for(int i=0; i<n;i++){
    cin>>beauty[i];
  }
  for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
      if(abs(beauty[i]-beauty[j])==max_diff){
	set += 1;
	}
      if(abs(beauty[i]-beauty[j])>max_diff){
	max_diff = abs(beauty[i]-beauty[j]);
	set = 1;
    }
  }
  }
  cout<<max_diff<<' '<<set<<endl;

}
