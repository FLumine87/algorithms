tree_count = {}
while True:
    try:
        tree = input()
        if tree:
            tree_count[tree] = tree_count.get(tree, 0) + 1
        else:
            break
    except:
        break

total_trees = sum(tree_count.values())
sorted_trees = sorted(tree_count.keys())
for tree in sorted_trees:
    percentage = (tree_count[tree] / total_trees) * 100
    print(f"{tree} {percentage:.4f}")

# #include<iostream>
# // #include<cstdio>
# // #include<vector>
# //#include<cctype>
# #include<string>
# #include<sstream>
# // using std::string ;
# // using std::vector;
# // #include<queue>
# #include<unordered_map>
# #include<map>

# using std::cin;using std::cout;using std::unordered_map;using std::string;

# std::map<string,int> zidian;

# int main(){
#     std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#     string a;int s=0;
#     while(std::getline(cin,a)){
#         if (a.empty()) break;
#         zidian[a]++;
#         ++s;
#     }

#     for (const auto& e:zidian ){
#         printf("%s %.4f\n",e.first.c_str(),(e.second*100.0)/s);
#     }
#     return 0;
# }