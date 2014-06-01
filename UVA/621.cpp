#include <iostream>
#include <string>
using namespace std;

int main(){
  int n;
  cin>>n;
  for(int i=0; i<n; i++){
    string s;
    cin>>s;
    if(s=="1"||s=="4"||s=="78"){
      cout<<"+"<<endl;
    }
    if(s.length()>2){
    if(s.substr(s.length()-2)=="35"){
      cout<<"-"<<endl;
    }

    if(s.substr(0,1)=="9" && s.substr(s.length()-1)=="4"){
      cout<<"*"<<endl;
    }
    }
    if(s.length()>4){
    if(s.substr(0,3)=="190"){
      cout<<"?"<<endl;
    }
    }
    
  }

  return 0;
}
