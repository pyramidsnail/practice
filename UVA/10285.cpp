#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;
int grid[110][110];
int longest[110][110];
int r,c;

int dfs(int x, int y){//depth first search
  int max_length=0;

  if(longest[x][y])
    return longest[x][y];
  else{
    if(x>=1 && grid[x][y]>grid[x-1][y])
      if(dfs(x-1,y)>max_length)
	max_length=dfs(x-1,y);
      
    if(y>=1 && grid[x][y]>grid[x][y-1])
      if(dfs(x,y-1)>max_length)
	max_length=dfs(x,y-1);
    if(x<r-1 && grid[x+1][y]>grid[x][y])
      if(dfs(x+1,y)>max_length)
	max_length=dfs(x+1,y);
    if(y<c-1 && grid[x][y+1]>max_length)
      if(dfs(x,y+1)>max_length)
	max_length=dfs(x,y+1);
    longest[x][y]=max_length+1;
    return longest[x][y];

  }
  
}

int main(){
  int n;
  cin>>n;
  while(n--){
    string case_name;
    cin>>case_name>>r>>c;
    memset(grid, 0, sizeof(grid));
    memset(longest,0,sizeof(longest));
    for(int i=0;i<r;i++){
      for(int j=0; j<c;j++){ 
	cin>> grid[i][j];
      }
    }
    int ans = 0;
    for(int i=0; i<r;i++){
      for(int j=0; j<c; j++){
	if(longest[i][j])
	  ans = max(ans, longest[i][j]);
	else
	  ans = max(ans, dfs(i,j));
      }
    }
    
    cout<<case_name<<': '<<ans<<endl;
    //printf("%s: %d\n",case_name,ans); 
  }
  return 0;
}
