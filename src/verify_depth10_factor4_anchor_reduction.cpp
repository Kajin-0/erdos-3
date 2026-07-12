#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#include <omp.h>
using namespace std;
namespace {
constexpr int L8=8388608,L9=67108864,L10=536870912,R8=16777217,R9=134217729;
constexpr int MAXR=613454687, INHERITED_MAX=76583775;
constexpr uint64_t EXPECTED_FNV=0x5092d3a9e6133767ULL;
constexpr uint64_t FNV_OFFSET=1469598103934665603ULL,FNV_PRIME=1099511628211ULL;
vector<int> uniq(vector<int>v){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());return v;}
vector<int> raw(const vector<int>&s,int R){vector<int>o;o.reserve(3*(s.size()+1));for(int k=0;k<3;k++)o.push_back(k*R);for(int x:s)for(int k=0;k<3;k++)o.push_back(x+k*R);return uniq(move(o));}
vector<int> tr(const vector<int>&v,int L){vector<int>o;o.reserve(v.size());for(int x:v)o.push_back(x+L);return o;}
vector<int> s8(){vector<int>H={0,1,2,16,17,18,21,22,23,26,27,28},sc={64,256,2048,8192,32768},Rs={61,303,1597,8195},s;for(int x:H)s.push_back(64+x);s=uniq(move(s));for(int i=0;i<4;i++)s=tr(raw(s,Rs[i]),sc[i+1]);s=tr(raw(s,93476),262144);s=tr(raw(s,230164),1048576);s=tr(raw(s,2097164),L8);return s;}
int v2(int x){return __builtin_ctz((unsigned)x);}inline void setbit(vector<uint64_t>&b,long long x){if(x>=0&&(uint64_t)(x>>6)<b.size())b[x>>6]|=1ULL<<(x&63);}inline bool bit(const vector<uint64_t>&b,long long x){return x>=0&&(uint64_t)(x>>6)<b.size()&&((b[x>>6]>>(x&63))&1ULL);}inline void clearbit(vector<uint64_t>&b,int x){__atomic_fetch_and(&b[x>>6],~(1ULL<<(x&63)),__ATOMIC_RELAXED);}long long pop(const vector<uint64_t>&b){long long c=0;for(auto q:b)c+=__builtin_popcountll(q);return c;}
pair<long long,vector<uint64_t>> loadbits(const string&p){FILE*f=fopen(p.c_str(),"rb");if(!f)throw runtime_error("open "+p);long long low;uint64_t n;if(fread(&low,8,1,f)!=1||fread(&n,8,1,f)!=1)throw runtime_error("header");vector<uint64_t>v(n);if(fread(v.data(),8,n,f)!=n)throw runtime_error("truncated");fclose(f);return {low,move(v)};}
void write_list(const string&p,const vector<int>&v){FILE*f=fopen(p.c_str(),"w");if(!f)throw runtime_error("write");for(int x:v)fprintf(f,"%d\n",x);fclose(f);}uint64_t hash_list(const vector<int>&v){uint64_t h=FNV_OFFSET;for(int x:v){string t=to_string(x)+",";for(unsigned char b:t){h^=b;h*=FNV_PRIME;}}return h;}
}
int main(int argc,char**argv){if(argc!=4){cerr<<"usage: COMPLETIONS SUPPORT OUTPUT\n";return 2;}auto [dlow,D9]=loadbits(argv[2]);auto [clow,C9]=loadbits(argv[1]);if(dlow!=0||pop(D9)!=71129286||clow!=-115267902||pop(C9)!=13923661)throw runtime_error("S9 bitset mismatch");
 const long long LIMIT=3LL*MAXR;vector<uint64_t>lift((LIMIT+64)/64);for(size_t w=0;w<D9.size();w++){uint64_t q=D9[w];while(q){int b=__builtin_ctzll(q);long long d=(long long)w*64+b;for(int m=0;m<=2;m++){setbit(lift,llabs(d+1LL*m*R9));setbit(lift,llabs(d-1LL*m*R9));}q&=q-1;}}for(size_t w=0;w<C9.size();w++){uint64_t q=C9[w];while(q){int b=__builtin_ctzll(q);long long z=clow+(long long)w*64+b;for(int i=0;i<3;i++)setbit(lift,llabs(1LL*L10+i*1LL*R9+z));q&=q-1;}}if(pop(lift)!=354838701)throw runtime_error("lift support mismatch");
 auto a=s8();auto b=tr(raw(a,R8),L9);auto s10=tr(raw(b,R9),L10);vector<int>a8={0};a8.insert(a8.end(),a.begin(),a.end());int m8=a8.back();vector<uint64_t>d8((m8+64LL)/64);
#pragma omp parallel for schedule(dynamic,4)
 for(int i=0;i<(int)a8.size();i++)for(int j=i+1;j<(int)a8.size();j++){int d=a8[j]-a8[i];__atomic_fetch_or(&d8[d>>6],1ULL<<(d&63),__ATOMIC_RELAXED);}int m9=b.back();vector<uint64_t>d9((m9+64LL)/64);for(int x:b)setbit(d9,x);setbit(d9,R8);setbit(d9,2LL*R8);for(int d=1;d<=m8;d++)if(bit(d8,d)){setbit(d9,d);setbit(d9,1LL*R8+d);setbit(d9,llabs(1LL*R8-d));setbit(d9,2LL*R8+d);setbit(d9,llabs(2LL*R8-d));}
 vector<uint64_t>d10((2LL*MAXR+64)/64);for(int x:s10)setbit(d10,x);setbit(d10,R9);setbit(d10,2LL*R9);for(int d=1;d<=m9;d++)if(bit(d9,d)){setbit(d10,d);setbit(d10,1LL*R9+d);setbit(d10,llabs(1LL*R9-d));setbit(d10,2LL*R9+d);setbit(d10,llabs(2LL*R9-d));}
 vector<uint64_t>target((MAXR+64LL)/64);long long sponsor=0,disjoint=0,initial=0;for(int R=1;R<=MAXR;R++)if(v2(R)%2==0){sponsor++;if(!bit(d10,R)&&!bit(d10,2LL*R)){disjoint++;if(R>INHERITED_MAX&&!(bit(lift,R)||bit(lift,2LL*R)||bit(lift,3LL*R))){setbit(target,R);initial++;}}}if(sponsor!=408969792||disjoint!=348012826||initial!=177844250)throw runtime_error("initial domain mismatch");
 vector<int>thirds;for(int x:s10)if(x%3==0)thirds.push_back(x/3);if(thirds.size()!=88572)throw runtime_error("third count");
#pragma omp parallel for schedule(dynamic,1)
 for(int i=0;i<(int)thirds.size();i++){int d=thirds[i];for(int s:s10){long long diff=1LL*s-d;if(diff<=0)continue;if(diff<=MAXR&&bit(target,diff))clearbit(target,(int)diff);if((diff&1)==0){long long R=diff/2;if(R>0&&R<=MAXR&&bit(target,R))clearbit(target,(int)R);}}}
 vector<int>rem;for(int R=1;R<=MAXR;R++)if(bit(target,R))rem.push_back(R);if(rem.size()!=2520||rem.front()!=97474324||rem.back()!=613340173||hash_list(rem)!=EXPECTED_FNV)throw runtime_error("anchor residual mismatch");write_list(argv[3],rem);cout<<"verified: depth-ten anchor reduction\ninitial_new=177844250\nanchor_covered=177841730\nremaining=2520\nresidual_fnv64=5092d3a9e6133767\n";}
