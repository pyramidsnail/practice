#include <iostream>
#include <string.h>
using namespace std;

int main(){
  int n;
  cin>>n;
  for(int i=0; i<n; i++){
    int m,c;
    cin>>m>>c;
    int price[20][21];
    memset(price, 0, sizeof(price));
    
    for(int j=0; j<c; j++){
      int k;
      cin>>k;
      price[j][0]=k;
      for(int x=1; x<=k; x++){
	cin>>price[j][k];
      }
      
    }
    // try every possible combination, using DP
    int max = 0;
    for(int m=0; m<c; m++){
      for(int n=1; n<price[m][0]; n++){
	
	
      }
    }


  }
  return 0;
  
}
