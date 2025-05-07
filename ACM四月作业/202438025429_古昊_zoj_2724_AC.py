import heapq

pq = []
while True:
    try:
        command = input().split()
        if command[0] == "GET":
            if not pq:
                print("EMPTY QUEUE!")
            else:
                priority, msg_name, param = heapq.heappop(pq)
                print(f"{msg_name} {param}")
        elif command[0] == "PUT":
            msg_name, param, priority = command[1], int(command[2]), int(command[3])
            heapq.heappush(pq, (priority, msg_name, param))
    except:
        break

# #include<iostream>
# #include<utility>
# #include<queue>
# #include<vector>
# #include<string>

# using std::pair;
# using std::string;
# using std::priority_queue;
# using std::cout;using std::cin;

# typedef pair<string,int> PSI;

# int main(){
#     //std::ios::sync_with_stdio(false);cout.tie(0);cin.tie(0);
#     auto cmp=[](pair<int,PSI> a,pair<int,PSI> b){return a.first>b.first;};
#     priority_queue<pair<int,PSI>,std::vector<pair<int,PSI>>,decltype(cmp)> pq(cmp);
#     int a,b;
#     string m,n;
    
#     auto ot=[&](){
#         if(pq.empty()){
#             cout<<"EMPTY QUEUE!\n";
#             return;
#         }
#         pair<int,PSI> ans=pq.top();
#         cout<<ans.second.first<<' '<<ans.second.second<<'\n';
#         pq.pop();
#     };

#     auto psh=[&](){
#         cin>>n>>a>>b;
#         pq.push(std::make_pair(b,std::make_pair(n,a)));
#     };
    
#     while(cin>>m){
#         if(m=="GET")ot();
#         else psh();
#     }
#     return 0;
# }