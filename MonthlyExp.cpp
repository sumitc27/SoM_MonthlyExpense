#include <bits/stdc++.h>
using namespace std;

int main (){
     int mess,cant,rel,onli,city;
     cin>>mess>>cant>>rel>>onli>>city;
     int exp=600;
     int cantfac=25,cityfac=150;
     if(mess==0){mess=2500;cantfac=60;}
     if(rel==1){cityfac=200;cantfac+=20;}
     cout<<exp+abs(mess-1)+(cant*cantfac*5)+(onli*100)+(city*cityfac);
}