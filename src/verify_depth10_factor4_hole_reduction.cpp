#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#include <omp.h>
using namespace std; namespace {
constexpr int L8=8388608,L9=67108864,L10=536870912,R8=16777217,R9=134217729;constexpr uint64_t FNV_OFFSET=1469598103934665603ULL,FNV_PRIME=1099511628211ULL,EXPECTED=0xf728ae4689a0fe2aULL;
vector<int> uniq(vector<int>v){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());return v;}vector<int> raw(const vector<int>&s,int R){vector<int>o;o.reserve(3*(s.size()+1));for(int k=0;k<3;k++)o.push_back(k*R);for(int x:s)for(int k=0;k<3;k++)o.push_back(x+k*R);return uniq(move(o));}vector<int> tr(const vector<int>&v,int L){vector<int>o;o.reserve(v.size());for(int x:v)o.push_back(x+L);return o;}vector<int> s8(){vector<int>H={0,1,2,16,17,18,21,22,23,26,27,28},sc={64,256,2048,8192,32768},Rs={61,303,1597,8195},s;for(int x:H)s.push_back(64+x);s=uniq(move(s));for(int i=0;i<4;i++)s=tr(raw(s,Rs[i]),sc[i+1]);s=tr(raw(s,93476),262144);s=tr(raw(s,230164),1048576);s=tr(raw(s,2097164),L8);return s;}
inline bool bit(const vector<uint64_t>&a,long long x){return x>=0&&(uint64_t)(x>>6)<a.size()&&((a[x>>6]>>(x&63))&1ULL);}inline void aset(vector<uint64_t>&a,long long x){__atomic_fetch_or(&a[x>>6],1ULL<<(x&63),__ATOMIC_RELAXED);}long long pop(const vector<uint64_t>&a){long long c=0;for(auto q:a)c+=__builtin_popcountll(q);return c;}vector<int> readl(const string&p){FILE*f=fopen(p.c_str(),"r");if(!f)throw runtime_error("open");vector<int>v;int x;while(fscanf(f,"%d",&x)==1)v.push_back(x);fclose(f);return v;}void writel(const string&p,const vector<int>&v){FILE*f=fopen(p.c_str(),"w");if(!f)throw runtime_error("write");for(int x:v)fprintf(f,"%d\n",x);fclose(f);}uint64_t hashv(const vector<int>&v){uint64_t h=FNV_OFFSET;for(int x:v){string t=to_string(x)+",";for(unsigned char b:t){h^=b;h*=FNV_PRIME;}}return h;}
}
int main(int argc,char**argv){if(argc!=3){cerr<<"usage INPUT OUTPUT\n";return 2;}auto rs=readl(argv[1]);if(rs.size()!=2520||rs.front()!=97474324||rs.back()!=613340173)throw runtime_error("input mismatch");auto a=s8();auto b=tr(raw(a,R8),L9);auto s=tr(raw(b,R9),L10);vector<int>B={0};B.insert(B.end(),s.begin(),s.end());int M=B.back();vector<uint64_t>present(((uint64_t)M+64)/64),h1(((uint64_t)M+64)/64),h2(((uint64_t)M+64)/64);for(int x:B)present[x>>6]|=1ULL<<(x&63);
#pragma omp parallel for schedule(dynamic,4)
for(int i=0;i<(int)B.size();i++){int x=B[i];for(int j=i+1;j<(int)B.size();j++){int z=B[j],span=z-x;if(span%3)continue;int d=span/3;if(bit(present,1LL*x+d))aset(h2,1LL*x+2*d);if(bit(present,1LL*x+2*d))aset(h1,1LL*x+d);}}
if(pop(h1)!=2447725||pop(h2)!=2412779)throw runtime_error("hole support mismatch");vector<int>rem;for(int R:rs){bool ok=false;for(int x:B){for(int k=1;k<=2;k++){long long h=1LL*x+k*1LL*R;if(h<=M&&(bit(h1,h)||bit(h2,h))){ok=true;break;}}if(ok)break;}if(!ok)rem.push_back(R);}if(rem.size()!=1866||rem.front()!=97530521||rem.back()!=613340173||hashv(rem)!=EXPECTED)throw runtime_error("hole residual mismatch");writel(argv[2],rem);cout<<"verified: missing-interior reduction\nh1=2447725\nh2=2412779\ncovered=654\nremaining=1866\nresidual_fnv64=f728ae4689a0fe2a\n";}
