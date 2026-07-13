#include <algorithm>
#include <atomic>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>
#include <omp.h>
using namespace std;
namespace {
constexpr int L8=8388608,L9=67108864,L10=536870912,R8=16777217,R9=134217729;
constexpr int INHERITED_MAX=76583775;
constexpr int EXPECTED_FIRST=76583927,EXPECTED_LAST=76587052,EXPECTED_COUNT=100;
constexpr uint64_t EXPECTED_FNV=0x1a61bdf6a331636dULL;
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
uint64_t fnv_bytes(const string&s){uint64_t h=FNV_OFFSET;for(unsigned char c:s){h^=c;h*=FNV_PRIME;}return h;}
struct Row{int R;long long a,b,c,d;};
vector<Row> read_rows(const string&p,string&bytes){FILE*f=fopen(p.c_str(),"rb");if(!f)throw runtime_error("cannot open witness file");fseek(f,0,SEEK_END);long n=ftell(f);rewind(f);bytes.resize(n);if(n&&fread(bytes.data(),1,n,f)!=(size_t)n)throw runtime_error("read error");fclose(f);vector<Row>rows;size_t pos=0;while(pos<bytes.size()){size_t e=bytes.find('\n',pos);if(e==string::npos)e=bytes.size();string line=bytes.substr(pos,e-pos);if(!line.empty()){Row r;if(sscanf(line.c_str(),"%d %lld %lld %lld %lld",&r.R,&r.a,&r.b,&r.c,&r.d)!=5)throw runtime_error("bad row");rows.push_back(r);}pos=e+1;}return rows;}
}
int main(int argc,char**argv){try{if(argc!=2)throw runtime_error("usage: WITNESS_FILE");string bytes;auto rows=read_rows(argv[1],bytes);if(rows.size()!=EXPECTED_COUNT||rows.front().R!=EXPECTED_FIRST||rows.back().R!=EXPECTED_LAST||fnv_bytes(bytes)!=EXPECTED_FNV)throw runtime_error("witness file mismatch");
auto s8=build_s8();vector<int>a8={0};a8.insert(a8.end(),s8.begin(),s8.end());int maxa8=a8.back();vector<atomic<uint64_t>>d8a((maxa8+64LL)/64);for(auto&q:d8a)q.store(0);
#pragma omp parallel for schedule(dynamic,4)
for(int i=0;i<(int)a8.size();i++)for(int j=i+1;j<(int)a8.size();j++)aset(d8a,a8[j]-a8[i]);
auto s9=tr(raw(s8,R8),L9);int maxa9=s9.back();vector<uint64_t>d9((maxa9+64LL)/64);for(int x:s9)setb(d9,x);setb(d9,R8);setb(d9,2LL*R8);for(int d=1;d<=maxa8;d++)if(abit(d8a,d)){setb(d9,d);setb(d9,1LL*R8+d);setb(d9,llabs(1LL*R8-d));setb(d9,2LL*R8+d);setb(d9,llabs(2LL*R8-d));}
auto s10=tr(raw(s9,R9),L10);vector<int>B={0};B.insert(B.end(),s10.begin(),s10.end());vector<uint64_t>d10((2LL*EXPECTED_LAST+64)/64);for(int x:s10)setb(d10,x);setb(d10,R9);setb(d10,2LL*R9);for(int d=1;d<=maxa9;d++)if(bit(d9,d)){setb(d10,d);setb(d10,1LL*R9+d);setb(d10,llabs(1LL*R9-d));setb(d10,2LL*R9+d);setb(d10,llabs(2LL*R9-d));}
vector<int>domain;for(int R=INHERITED_MAX+1;R<=EXPECTED_LAST;R++){if(v2(R)%2)continue;if(bit(d10,R)||bit(d10,2LL*R))continue;domain.push_back(R);}if(domain.size()!=EXPECTED_COUNT)throw runtime_error("domain count mismatch");for(size_t i=0;i<rows.size();i++)if(rows[i].R!=domain[i])throw runtime_error("witness keys are not first 100 domain values");
unordered_set<long long>base;base.reserve(B.size()*2);for(int x:B)base.insert(x);auto in_candidate=[&](long long z,int R){for(int layer=0;layer<3;layer++){long long b=z-1LL*layer*R;if(b>=0&&base.count(b))return true;}return false;};
for(const auto&r:rows){long long q=r.b-r.a;if(q<=0||r.c-r.b!=q||r.d-r.c!=q)throw runtime_error("non-AP row");if(!in_candidate(r.a,r.R)||!in_candidate(r.b,r.R)||!in_candidate(r.c,r.R)||!in_candidate(r.d,r.R))throw runtime_error("witness point absent");}
cout<<"verified: first 100 genuinely new S10 factor-four candidates\n";cout<<"first_R="<<EXPECTED_FIRST<<"\nlast_R="<<EXPECTED_LAST<<"\nexplicit_witnesses=100\nwitness_fnv64=1a61bdf6a331636d\n";return 0;}catch(const exception&e){cerr<<"error: "<<e.what()<<"\n";return 1;}}
