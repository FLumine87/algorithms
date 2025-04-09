```mermaid  
graph LR  
A(Requirements)-.abstract.->B[HUB]  
B<--Messages-->C{Controller}  
C--Request-->D[Devices]  
D--Response-->C  
D---E(D1)  
D---F(D2)  
D---G(...)  
```