#include <algorithm>
#include <array>
#include <atomic>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>
#include <omp.h>
using namespace std;
namespace {
constexpr int L8=8388608,L9=67108864,L10=536870912,R8=16777217,R9=134217729;
constexpr int MAX_R4=613454687,CUTOFF=76583775;
constexpr long long NEW_COUNT=314986450;
constexpr int FIRST_INDEX=384,COUNT=128;
constexpr uint64_t EXPECTED_FNV=0x69c322f3b61e1419ULL;
constexpr uint64_t FNV_OFFSET=1469598103934665603ULL,FNV_PRIME=1099511628211ULL;
vector<int> uniq(vector<int>v){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());return v;}
vector<int> raw(const vector<int>&s,int R){vector<int>o;o.reserve(3*(s.size()+1));for(int k=0;k<3;k++)o.push_back(k*R);for(int x:s)for(int k=0;k<3;k++)o.push_back(x+k*R);return uniq(move(o));}
vector<int> tr(const vector<int>&v,int L){vector<int>o;o.reserve(v.size());for(int x:v)o.push_back(x+L);return o;}
vector<int> build_s8(){vector<int>H={0,1,2,16,17,18,21,22,23,26,27,28},sc={64,256,2048,8192,32768},Rs={61,303,1597,8195},s;for(int x:H)s.push_back(64+x);s=uniq(move(s));for(int i=0;i<4;i++)s=tr(raw(s,Rs[i]),sc[i+1]);s=tr(raw(s,93476),262144);s=tr(raw(s,230164),1048576);s=tr(raw(s,2097164),L8);return s;}
inline void aset(vector<atomic<uint64_t>>&b,long long x){if(x>0&&(uint64_t)(x>>6)<b.size())b[x>>6].fetch_or(1ULL<<(x&63),memory_order_relaxed);}
inline bool abit(const vector<atomic<uint64_t>>&b,long long x){return x>0&&(uint64_t)(x>>6)<b.size()&&((b[x>>6].load(memory_order_relaxed)>>(x&63))&1ULL);}
inline void setb(vector<uint64_t>&b,long long x){if(x>0&&(uint64_t)(x>>6)<b.size())b[x>>6]|=1ULL<<(x&63);}
inline bool bit(const vector<uint64_t>&b,long long x){return x>0&&(uint64_t)(x>>6)<b.size()&&((b[x>>6]>>(x&63))&1ULL);}
int v2(int x){if(x<=0)throw invalid_argument("v2");return __builtin_ctz((unsigned)x);}
uint64_t fnv(const string&s){uint64_t h=FNV_OFFSET;for(unsigned char c:s){h^=c;h*=FNV_PRIME;}return h;}
array<int,4> pw(const string&s){if(s.size()!=4)throw runtime_error("bad word");return{s[0]-'0',s[1]-'0',s[2]-'0',s[3]-'0'};}
struct Row{int local,global;long long rank;int R;long long a,q;string lam,mu;};
}
int main(int argc,char**argv){try{
 if(argc!=2)throw runtime_error("usage: DATA_FILE");ifstream in(argv[1],ios::binary);if(!in)throw runtime_error("cannot open data");ostringstream ss;ss<<in.rdbuf();string bytes=ss.str();if(fnv(bytes)!=EXPECTED_FNV)throw runtime_error("data hash mismatch");istringstream ls(bytes);vector<Row>rows;Row r;while(ls>>r.local>>r.global>>r.rank>>r.R>>r.a>>r.q>>r.lam>>r.mu)rows.push_back(r);if(rows.size()!=COUNT)throw runtime_error("row count mismatch");
 auto s8=build_s8();vector<int>a8={0};a8.insert(a8.end(),s8.begin(),s8.end());int maxa8=a8.back();vector<atomic<uint64_t>>d8a((maxa8+64LL)/64);for(auto&q:d8a)q.store(0);
 #pragma omp parallel for schedule(dynamic,4)
 for(int i=0;i<(int)a8.size();i++)for(int j=i+1;j<(int)a8.size();j++)aset(d8a,a8[j]-a8[i]);
 auto s9=tr(raw(s8,R8),L9);vector<int>B9={0};B9.insert(B9.end(),s9.begin(),s9.end());unordered_set<long long>base9;base9.reserve(B9.size()*2);for(int x:B9)base9.insert(x);int maxa9=s9.back();vector<uint64_t>d9((maxa9+64LL)/64);for(int x:s9)setb(d9,x);setb(d9,R8);setb(d9,2LL*R8);for(int d=1;d<=maxa8;d++)if(abit(d8a,d)){setb(d9,d);setb(d9,1LL*R8+d);setb(d9,llabs(1LL*R8-d));setb(d9,2LL*R8+d);setb(d9,llabs(2LL*R8-d));}
 auto s10=tr(raw(s9,R9),L10);vector<int>B10={0};B10.insert(B10.end(),s10.begin(),s10.end());unordered_set<long long>base10;base10.reserve(B10.size()*2);for(int x:B10)base10.insert(x);vector<uint64_t>d10((2LL*MAX_R4+64)/64);for(int x:s10)setb(d10,x);setb(d10,R9);setb(d10,2LL*R9);for(int d=1;d<=maxa9;d++)if(bit(d9,d)){setb(d10,d);setb(d10,1LL*R9+d);setb(d10,llabs(1LL*R9-d));setb(d10,2LL*R9+d);setb(d10,llabs(2LL*R9-d));}
 vector<long long>targets(512);for(int j=0;j<512;j++)targets[j]=((2LL*j+1)*NEW_COUNT)/(2LL*512);vector<int>sample(512);long long rank=0;int ti=0;for(int T=CUTOFF+1;T<=MAX_R4;T++){if(v2(T)%2)continue;if(bit(d10,T)||bit(d10,2LL*T))continue;if(ti<512&&rank==targets[ti])sample[ti++]=T;rank++;}if(rank!=NEW_COUNT||ti!=512)throw runtime_error("domain mismatch");
 auto layer=[&](long long z,int sep,const unordered_set<long long>&set){int f=-1;for(int l=0;l<3;l++)if(set.count(z-1LL*l*sep)){if(f!=-1)throw runtime_error("layer overlap");f=l;}return f;};
 map<string,int>patterns;long long max_abs_A=0;for(int j=0;j<COUNT;j++){const Row&x=rows[j];int g=FIRST_INDEX+j;if(x.local!=j||x.global!=g||x.rank!=targets[g]||x.R!=sample[g]||x.q<=0)throw runtime_error("key mismatch");auto lam=pw(x.lam),mu=pw(x.mu);array<long long,4>anc{};for(int i=0;i<4;i++){long long z=x.a+i*x.q;int l=layer(z,x.R,base10);if(l!=lam[i])throw runtime_error("outer layer mismatch");long long b=z-1LL*l*x.R;if(b==0)throw runtime_error("root witness");long long y=b-L10;int m=layer(y,R9,base9);if(m!=mu[i])throw runtime_error("parent layer mismatch");anc[i]=y-1LL*m*R9;if(!base9.count(anc[i]))throw runtime_error("ancestor absent");}
 string key=x.lam+"/"+x.mu;patterns[key]++;long long A;if((x.lam=="0011"||x.lam=="1122")&&x.mu=="0202")A=1LL*x.R-4LL*R9;else if(x.lam=="0112"&&x.mu=="2020")A=4LL*R9-x.R;else throw runtime_error("outside k=4 rectangle channel");long long d=anc[1]-anc[0];if(anc[2]!=anc[0]+2*d-A||anc[3]!=anc[0]+3*d-A)throw runtime_error("rectangle descent mismatch");max_abs_A=max(max_abs_A,llabs(A));}
 map<string,int>expected={{"0011/0202",49},{"1122/0202",37},{"0112/2020",42}};if(patterns!=expected||max_abs_A!=76122367)throw runtime_error("profile mismatch");
 cout<<"verified: top-quartile 128 equal-rank samples\n";cout<<"raw_pair_0011_0202=49\nraw_pair_1122_0202=37\nraw_pair_0112_2020=42\n";cout<<"canonical_outer_0011=86\ncanonical_outer_0112=42\ncanonical_parent_0202=128\n";cout<<"max_abs_effective_separation=76122367\n";cout<<"data_fnv64=69c322f3b61e1419\n";return 0;
}catch(const exception&e){cerr<<"error: "<<e.what()<<"\n";return 1;}}
