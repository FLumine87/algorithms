dictionary = {}
while True:
    line = input()
    if line == "":
        break
    english_word, foreign_word = line.split()
    dictionary[foreign_word] = english_word

while True:
    try:
        foreign_word = input()
        print(dictionary.get(foreign_word, "eh"))
    except:
        break

# #include<iostream>
# #include<string>
# #include<sstream>
# #include<unordered_map>

# using std::cin;using std::cout;using std::unordered_map;using std::string;

# unordered_map<string,string> zidian;

# int main(){
#     std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#     string a;
#     while(std::getline(cin,a)){
# if (a.empty()) break;
#         string p1,p2;
#         std::istringstream iss(a);
#         iss >>p1>>p2;
#         zidian[p2]=p1;
#     }

#     while(cin>>a){
#         auto it = zidian.find(a);
#         if(it==zidian.end())cout<<"eh\n";
#         else cout<<it->second<<'\n';
#     }
#     return 0;
# }