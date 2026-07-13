#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#include <omp.h>
using namespace std;
namespace {
constexpr int L8=8388608,L9=67108864,L10=536870912,R8=16777217,R9=134217729;
constexpr int MAX_R4=613454687,INHERITED_MAX_R=76583775;
constexpr long long RESIDUAL_COUNT=177844250;
constexpr int SAMPLE_COUNT=512;
constexpr uint64_t RESIDUAL_FNV=0x00369694f2d70526ULL;
constexpr uint64_t FNV_OFFSET=1469598103934665603ULL,FNV_PRIME=1099511628211ULL;
vector<int> uniq(vector<int> v){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());return v;}
vector<int> raw(const vector<int>&s,int R){vector<int>o;o.reserve(3*(s.size()+1));for(int k=0;k<3;k++)o.push_back(k*R);for(int x:s)for(int k=0;k<3;k++)o.push_back(x+k*R);return uniq(move(o));}
vector<int> tr(const vector<int>&v,int L){vector<int>o;o.reserve(v.size());for(int x:v)o.push_back(x+L);return o;}
vector<int> build_s8(){vector<int>H={0,1,2,16,17,18,21,22,23,26,27,28},sc={64,256,2048,8192,32768},Rs={61,303,1597,8195},s;for(int x:H)s.push_back(64+x);s=uniq(move(s));for(int i=0;i<4;i++)s=tr(raw(s,Rs[i]),sc[i+1]);s=tr(raw(s,93476),262144);s=tr(raw(s,230164),1048576);s=tr(raw(s,2097164),L8);return s;}
int v2(int x){if(x<=0)throw invalid_argument("v2");return __builtin_ctz((unsigned)x);}
inline void setb(vector<uint64_t>&b,long long x){if(x>=0&&(uint64_t)(x>>6)<b.size())b[x>>6]|=1ULL<<(x&63);}
inline bool bit(const vector<uint64_t>&b,long long x){return x>=0&&(uint64_t)(x>>6)<b.size()&&((b[x>>6]>>(x&63))&1ULL);}
pair<long long,vector<uint64_t>> load_bits(const string&p){FILE*f=fopen(p.c_str(),"rb");if(!f)throw runtime_error("cannot open "+p);long long low;uint64_t n;if(fread(&low,8,1,f)!=1||fread(&n,8,1,f)!=1)throw runtime_error("bad header");vector<uint64_t>b(n);if(fread(b.data(),8,n,f)!=n)throw runtime_error("truncated bitset");fclose(f);return {low,move(b)};}
long long pop(const vector<uint64_t>&b){long long n=0;for(auto q:b)n+=__builtin_popcountll(q);return n;}
void hash_value(uint64_t&h,int x){string t=to_string(x)+",";for(unsigned char c:t){h^=c;h*=FNV_PRIME;}}
}
int main(int argc,char**argv){try{
 if(argc!=4){cerr<<"usage: sample_depth10_lifted_s9_completion_residual S9_COMPLETIONS_BIN S9_COMPLETION_DIFFERENCES_BIN OUTPUT\n";return 2;}
 auto [clow,completions]=load_bits(argv[1]);auto [dlow,cdiff]=load_bits(argv[2]);
 if(clow!=-115267902LL||pop(completions)!=13923661)throw runtime_error("S9 completion mismatch");
 if(dlow!=0||pop(cdiff)!=71129286)throw runtime_error("S9 completion-difference mismatch");
 vector<uint64_t>lifted((3LL*MAX_R4+64)/64);
 for(size_t w=0;w<cdiff.size();w++){uint64_t q=cdiff[w];while(q){int z=__builtin_ctzll(q);long long d=(long long)w*64+z;for(int m=0;m<=2;m++){setb(lifted,llabs(d+1LL*m*R9));setb(lifted,llabs(d-1LL*m*R9));}q&=q-1;}}
 for(size_t w=0;w<completions.size();w++){uint64_t q=completions[w];while(q){int z=__builtin_ctzll(q);long long c=clow+(long long)w*64+z;for(int layer=0;layer<3;layer++)setb(lifted,llabs(1LL*L10+1LL*layer*R9+c));q&=q-1;}}
 if(pop(lifted)!=354838701)throw runtime_error("lifted support mismatch");
 auto s8=build_s8();vector<int>a8={0};a8.insert(a8.end(),s8.begin(),s8.end());int maxa8=a8.back();vector<uint64_t>d8((maxa8+64LL)/64);
 #pragma omp parallel for schedule(dynamic,4)
 for(int i=0;i<(int)a8.size();i++)for(int j=i+1;j<(int)a8.size();j++){int d=a8[j]-a8[i];__atomic_fetch_or(&d8[d>>6],1ULL<<(d&63),__ATOMIC_RELAXED);}
 auto s9=tr(raw(s8,R8),L9);int maxa9=s9.back();vector<uint64_t>d9((maxa9+64LL)/64);for(int x:s9)setb(d9,x);setb(d9,R8);setb(d9,2LL*R8);
 for(int d=1;d<=maxa8;d++)if(bit(d8,d)){setb(d9,d);setb(d9,1LL*R8+d);setb(d9,llabs(1LL*R8-d));setb(d9,2LL*R8+d);setb(d9,llabs(2LL*R8-d));}
 auto s10=tr(raw(s9,R9),L10);if(s10.size()!=265719||s10.front()!=L10||s10.back()!=920574272)throw runtime_error("S10 mismatch");
 vector<uint64_t>d10((2LL*MAX_R4+64)/64);for(int x:s10)setb(d10,x);setb(d10,R9);setb(d10,2LL*R9);
 for(int d=1;d<=maxa9;d++)if(bit(d9,d)){setb(d10,d);setb(d10,1LL*R9+d);setb(d10,llabs(1LL*R9-d));setb(d10,2LL*R9+d);setb(d10,llabs(2LL*R9-d));}
 vector<long long>targets(SAMPLE_COUNT);for(int j=0;j<SAMPLE_COUNT;j++)targets[j]=((2LL*j+1)*RESIDUAL_COUNT)/(2LL*SAMPLE_COUNT);
 vector<int>samples(SAMPLE_COUNT);long long rank=0;int next=0,first=0,last=0;uint64_t h=FNV_OFFSET;
 for(int R=INHERITED_MAX_R+1;R<=MAX_R4;R++){
   if(v2(R)%2)continue;
   if(bit(d10,R)||bit(d10,2LL*R))continue;
   if(bit(lifted,R)||bit(lifted,2LL*R)||bit(lifted,3LL*R))continue;
   if(!first) first=R;
   last=R;
   hash_value(h,R);
   while(next<SAMPLE_COUNT&&targets[next]==rank){samples[next]=R;next++;}
   rank++;
 }
 if(rank!=RESIDUAL_COUNT||first!=97474324||last!=613454687||h!=RESIDUAL_FNV)throw runtime_error("residual audit mismatch");
 if(next!=SAMPLE_COUNT)throw runtime_error("sample rank mismatch");
 uint64_t sample_hash=FNV_OFFSET;
 for(int R:samples) hash_value(sample_hash,R);
 ofstream out(argv[3]);if(!out)throw runtime_error("cannot write output");
 out<<"index rank separation signed_u abs_u\n";
 for(int j=0;j<SAMPLE_COUNT;j++){long long u=1LL*samples[j]-4LL*R9;out<<j<<" "<<targets[j]<<" "<<samples[j]<<" "<<u<<" "<<llabs(u)<<"\n";}
 cout<<"verified: exact 512-point equal-rank sample of lifted-completion residual\n";
 cout<<"residual_count="<<rank<<"\nfirst_residual="<<first<<"\nlast_residual="<<last<<"\n";
 cout<<"first_sample="<<samples.front()<<"\nlast_sample="<<samples.back()<<"\n";
 cout<<hex<<"sample_separation_fnv64="<<sample_hash<<dec<<"\n";
 return 0;
}catch(const exception&e){cerr<<"error: "<<e.what()<<"\n";return 1;}}
