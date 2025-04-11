#include<iostream>
#include<queue>
#include<vector>
#include<string>

using std::cin;using std::cout;
using std::vector;using std::string;

typedef std::pair<int,int> PII;
typedef long long LL;

void solve(){
    LL n,m;
    cin>>n>>m;
    vector<vector<int>> giv(n + 2, vector<int>(m + 2));
    for(int i=0;i<n;++i){
        string s;
        cin>>s;
        for(int j=0;j<m;++j){
            giv[i][j]=s[j];
        } 
    }

    int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,-1,-1,-1,0,1,1,1};
    vector<vector<bool>> vis(n + 2, vector<bool>(m + 2, false));
    auto bfs1 = [&](){
        std::queue<PII> u;
        //PII p={0,0};
        u.push({0,0});
        vis[0][0]=true;
        while(u.size()){
            auto [y,x]=u.front();u.pop();
            for(int i=0;i<8;++i){
                int ny=y+dy[i];int nx=x+dx[i];
                if(!vis[ny][nx]&&ny>=0&&nx>=0&&ny<n&&nx<m){
                    vis[ny][nx]=true;
                    if(giv[ny][nx]==1)giv[ny][nx]+=1;
                    if(giv[ny][nx]==0)u.push({ny,nx});
                }
            }
        }
    };
    bfs1();

    vector<vector<bool>> vis(n + 2, vector<bool>(m + 2, false));
    auto bfs2 = [&](int a , int b){
        std::queue<PII> u;
        u.push({a,b});
        vis[a][b]=true;
        while(u.size()){
            auto [y,x]=u.front();u.pop();
            for(int i=0;i<8;i+=2){
                int ny=y+dy[i];int nx=x+dx[i];
                if(giv[ny][nx]==2&&!vis[ny][nx]){
                    vis[ny][nx]=true;
                    u.push({ny,nx});
                }
            }
        }
    };

    int ans=0;
    for(int i=0;i<n;++i){
        for(int j=0;j<m;++j){
            if(giv[i][j]==2&&!vis[i][j]){
                bfs2(i,j);++ans;
            }
        }
    }
    cout << ans << '\n';
}

int main(){
    std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int t=1;
    cin>>t;
    while(t--){
        solve();
    }
    return 0;
}