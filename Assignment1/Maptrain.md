```
flowchart TD 
    A(CH<sub>4</sub>,H<sub>2</sub>S) -->B1[脱硫]; 
    E("Fe(OH)<sub>3</sub>") -->B1[脱硫] 
    B1[脱硫] --> C(CH<sub>4</sub>); 
    B1[脱硫] --> D(Fe<sub>2</sub>S<sub>3</sub>,H<sub>2</sub>O);
    D(Fe<sub>2</sub>S<sub>3</sub>,H<sub>2</sub>O) --> E("Fe(OH)<sub>3</sub>"); 
    F(O<sub>2</sub>) --> D(Fe<sub>2</sub>S<sub>3</sub>,H<sub>2</sub>O); 
    D(Fe<sub>2</sub>S<sub>3</sub>,H<sub>2</sub>O) --> G("S(硫)"); 
    H("H<sub>2</sub>O(g)") --> B2[一次转化]; 
    C(CH<sub>4</sub>) --> B2[一次转化]; 
    O(KHCO<sub>3</sub>) --> Q(CO<sub>2</<sub>);
    N(N<sub>2</sub>,H<sub>2</sub>) --> B4[合成]; 
    B4[合成] --> R(N<sub>2</sub>,H<sub>2</sub>,NH<sub>3</sub>) 
    R(N<sub>2</sub>,H<sub>2</sub>,NH<sub>3</sub>) --> S(NH<sub>3</sub>)
```
