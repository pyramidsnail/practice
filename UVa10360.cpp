#include <iostream>
#include <algorithm>

int max(int a[], int n){
    int max_num=0;
    for(int i=0; i<n; i++){
        if(a[i]>max_num)
            max_num=a[i];
    }
    return max_num;
}
int min(int a[], int n){
    int min_num=0;
    for(int i=0; i<n; i++){
        if(a[i]<min_num)
            min_num=a[i];

    }
    return min_num;
}
int main()
{
    int sce=0;
    std::cin >> sce;
    for(int ii=0;ii<sce; ii++){
        int d=0, n1=0;
        std::cin>>d>>n1;
        int x[20000], y[20000], sized[20000];
        int maxList[3]={0,0,0};
        for(int j=0; j<n1; j++){
            std::cin>>x[j]>>y[j]>>sized[j];
        }
        int pos[1026][1026];
        //std::memset(pos, 0, sizeof(pos));
        for(int o=0;o<1026;o++)
            for(int p=0; p<1026;p++)
                pos[o][p] = 0;
        for(int m=0;m<n1;m++){
//            pos[x[m]][y[m]] += sized[m];
//            for(int n=1;n<=d;n++){
//                if(x[m]+n<=1025)
//                    pos[x[m]+n][y[m]] += sized[m];
//                if(x[m]-n>=1)
//                    pos[x[m]-n][y[m]] += sized[m];
//                if(y[m]+n<=1025)
//                    pos[x[m]][y[m]+n] += sized[m];
//                if(y[m]-n>=1)
//                    pos[x[m]][y[m]-n] += sized[m];
//                if(x[m]-n>=1&&y[m]-n>=1)
//                    pos[x[m]-n][y[m]-n] += sized[m];
//                if(x[m]+n<=1025&&y[m]-n>=1)
//                    pos[x[m]+n][y[m]-n] += sized[m];
//                if(x[m]+n<=1025&&y[m]+n<=1025)
//                    pos[x[m]+n][y[m]+n] += sized[m];
//                if(x[m]-n>=1&&y[m]+n<=1025)
//                    pos[x[m]-n][y[m]+n] += sized[m];
//            }
            for(int inx=x[m]-d;inx<=x[m]+d;inx++){
                for(int iny=y[m]-d;iny<=y[m]+d;iny++){
                    if(inx>=1&&inx<=1025&&iny>=1&&iny<=1025)
                        pos[inx][iny] +=sized[m];
                }
                }
        }
        for(int x1=1; x1<1026;x1++){
            for(int y1=1; y1<1026; y1++){
            if(pos[x1][y1]>maxList[2]){
                maxList[0]=x1;
                maxList[1]=y1;
                maxList[2]=pos[x1][y1];
            }
            }
        }
//    for(int m=min(x,n1); m<=max(x,n1); m++){
//        for(int n=min(y,n1); n<=max(y,n1); n++){
//            int total = 0;
//            for(int r=0; r<n; r++){
//                if(abs(x[r]-m)<=d && abs(y[r]-n)<=d)
//                    total += sized[r];
//
//            }
//            if(total>maxList[2]){
//                maxList[0]=m;
//                maxList[1]=n;
//                maxList[2]=total;
//            }
//        }
//    }
    std::cout<<maxList[0]<<" "<<maxList[1]<<" "<<maxList[2]<<std::endl;
    }

    return 0;
}
