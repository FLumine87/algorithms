#include<iostream>
#include<stack>
#include<unordered_map>
#include<utility>
#include<string>
typedef std::pair<int,int> PII;

using std::unordered_map;using std::string;
using std::cout;using std::cin;using std::stack;

unordered_map<char,PII> martix;

void inma(){
    char c;int a,b;
    while(cin>>c>>a>>b){
        PII an={a,b};
        martix[c]=an;
    }
}

void solve(string& s){
    if(s[0]!='('){cout<<0<<'\n';return;}

    auto ct_stck=[&](auto& self,int pos=1)->PII{
        std::pair<PII,PII> ansma;
        if (s[pos] =='('){

        }
        return {};
    };
}

int main(){
    std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int T;cin>>T;
    while(T--){
        inma();
    }
    string s;
    while(cin>>s){
        solve(s);
    }
    return 0;
}

// #include<iostream>
// #include<queue>
// // // #include<cstdio>
//  #include<vector>
// // //#include<cctype>
// #include<string>
// using std::string ;
// using std::vector;
// using std::cout;using std::cin;

// typedef std::pair<int,int> PII;
// typedef long long LL;

// void solve(){
//     vector<vector<int>> giv;
//     LL n,m;
//     cin>>n>>m;
//     for(int i=0;i<n;++i){
//         string s;
//         cin>>s;
//         for(int j=0;j<m;++j){
//             giv[i][j]=s[j];
//         } 
//     }

//     int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,-1,-1,-1,0,1,1,1};
//     vector<vector<bool>> vis(n + 2, vector<bool>(n + 2, false));
//     auto bfs1 = [&](){
//         std::queue<PII> u;
//         //PII p={0,0};
//         u.push({0,0});
//         vis[0][0]=true;
//         while(u.size()){
//             auto [y,x]=u.front();u.pop();
//             for(int i=0;i<8;++i){
//                 int ny=y+dy[i];int nx=x+dx[i];
//                 if(!vis[ny][nx]&&ny>=0&&nx>=0&&ny<n&&nx<m){
//                     vis[ny][nx]=true;
//                     if(giv[ny][nx]==1)giv[ny][nx]+=1;
//                     if(giv[ny][nx]==0)u.push({ny,nx});
//                 }
//             }
//         }
//     };
//     bfs1();

//     vector<vector<bool>> vis(n + 2, vector<bool>(n + 2, false));
//     auto bfs1 = [&](int a , int b){
//         std::queue<PII> u;
//         u.push({a,b});
//         vis[a][b]=true;
//         while(u.size()){
//             auto [y,x]=u.front();u.pop();
//             for(int i=0;i<8;i+=2){
//                 int ny=y+dy[i];int nx=x+dx[i];
//                 if(giv[ny][nx]==2&&!vis[ny][nx]){
//                     vis[ny][nx]=true;
//                     u.push({ny,nx});
//                 }
//             }
//         }
//     };
// }
