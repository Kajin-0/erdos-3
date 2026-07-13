#include <algorithm>
#include <atomic>
#include <cstdint>
#include <fstream>
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
constexpr int PRIOR_COUNT=1000,EXPECTED_TOTAL=5000,EXPECTED_COUNT=4000;
constexpr int EXPECTED_FIRST=76603913,EXPECTED_LAST=76646105;
constexpr int SCAN_MAX=EXPECTED_LAST;
constexpr long long TRIAL_CAP=3000000;
constexpr uint64_t S10_FNV=0x405b941a1f8b2580ULL;
constexpr uint64_t EXPECTED_WITNESS_FNV=0x2a029f96119035a1ULL;
constexpr long long EXPECTED_TOTAL_TRIALS=363937682,EXPECTED_MAX_TRIALS=774028;
constexpr int EXPECTED_MAX_TRIAL_R=76604127;
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
uint64_t fnv_values(const vector<int>&v){uint64_t h=FNV_OFFSET;for(int x:v){string t=to_string(x)+",";for(unsigned char c:t){h^=c;h*=FNV_PRIME;}}return h;}
struct RNG{uint64_t x=88172645463325252ULL;uint64_t next(){x^=x<<7;x^=x>>9;return x;}};
struct Result{bool found=false; long long a=0,q=0,used=0;};
}
int main(int argc,char**argv){try{
 if(argc>2)throw runtime_error("usage: [OUTPUT_WITNESS_FILE]");
 auto s8=build_s8();vector<int>a8={0};a8.insert(a8.end(),s8.begin(),s8.end());int maxa8=a8.back();
 vector<atomic<uint64_t>>d8a((maxa8+64LL)/64);for(auto&q:d8a)q.store(0);
 #pragma omp parallel for schedule(dynamic,4)
 for(int i=0;i<(int)a8.size();i++)for(int j=i+1;j<(int)a8.size();j++)aset(d8a,a8[j]-a8[i]);
 auto s9=tr(raw(s8,R8),L9);int maxa9=s9.back();vector<uint64_t>d9((maxa9+64LL)/64);
 for(int x:s9)setb(d9,x);setb(d9,R8);setb(d9,2LL*R8);
 for(int d=1;d<=maxa8;d++)if(abit(d8a,d)){setb(d9,d);setb(d9,1LL*R8+d);setb(d9,llabs(1LL*R8-d));setb(d9,2LL*R8+d);setb(d9,llabs(2LL*R8-d));}
 auto s10=tr(raw(s9,R9),L10);if(s10.size()!=265719||s10.front()!=L10||s10.back()!=920574272||fnv_values(s10)!=S10_FNV)throw runtime_error("S10 mismatch");
 vector<int>B={0};B.insert(B.end(),s10.begin(),s10.end());unordered_set<long long>base;base.reserve(B.size()*2);for(int x:B)base.insert(x);
 vector<uint64_t>d10((2LL*SCAN_MAX+64)/64);for(int x:s10)setb(d10,x);setb(d10,R9);setb(d10,2LL*R9);
 for(int d=1;d<=maxa9;d++)if(bit(d9,d)){setb(d10,d);setb(d10,1LL*R9+d);setb(d10,llabs(1LL*R9-d));setb(d10,2LL*R9+d);setb(d10,llabs(2LL*R9-d));}
 vector<int>domain;domain.reserve(EXPECTED_TOTAL);
 for(int R=INHERITED_MAX+1;R<=SCAN_MAX && (int)domain.size()<EXPECTED_TOTAL;R++){if(v2(R)%2)continue;if(bit(d10,R)||bit(d10,2LL*R))continue;domain.push_back(R);}if(domain.size()!=EXPECTED_TOTAL||domain[PRIOR_COUNT]!=EXPECTED_FIRST||domain.back()!=EXPECTED_LAST)throw runtime_error("domain prefix mismatch");
 auto in_candidate=[&](long long z,int R){for(int layer=0;layer<3;layer++){long long b=z-1LL*layer*R;if(b>=0&&base.count(b))return true;}return false;};
 vector<Result> results(EXPECTED_COUNT);atomic<int> failed{-1};
 #pragma omp parallel for schedule(dynamic,1)
 for(int jj=0;jj<EXPECTED_COUNT;jj++){
   int index=PRIOR_COUNT+jj; int R=domain[index]; RNG rng; rng.x^=(uint64_t)R*0x9e3779b97f4a7c15ULL;
   Result res;
   for(long long trial=0;trial<TRIAL_CAP;trial++){
     long long x=B[rng.next()%B.size()]+(rng.next()%3)*1LL*R;
     long long y=B[rng.next()%B.size()]+(rng.next()%3)*1LL*R;
     if(x==y)continue;if(x>y)swap(x,y);long long step=y-x;
     if(in_candidate(x+2*step,R)&&in_candidate(x+3*step,R)){res={true,x,step,trial+1};break;}
   }
   results[jj]=res;if(!res.found)failed.store(jj,memory_order_relaxed);
 }
 if(failed.load()>=0){int jj=failed.load();throw runtime_error("trial cap exhausted at position="+to_string(PRIOR_COUNT+jj+1)+" R="+to_string(domain[PRIOR_COUNT+jj]));}
 string certificate;certificate.reserve(220000);long long total_trials=0,max_trials=0;int max_trial_R=0;
 for(int jj=0;jj<EXPECTED_COUNT;jj++){int R=domain[PRIOR_COUNT+jj];auto r=results[jj];if(!in_candidate(r.a,R)||!in_candidate(r.a+r.q,R)||!in_candidate(r.a+2*r.q,R)||!in_candidate(r.a+3*r.q,R))throw runtime_error("generated point absent");certificate+=to_string(R)+" "+to_string(r.a)+" "+to_string(r.a+r.q)+" "+to_string(r.a+2*r.q)+" "+to_string(r.a+3*r.q)+"\n";total_trials+=r.used;if(r.used>max_trials){max_trials=r.used;max_trial_R=R;}}
 if(fnv_bytes(certificate)!=EXPECTED_WITNESS_FNV)throw runtime_error("generated witness hash mismatch");
 if(total_trials!=EXPECTED_TOTAL_TRIALS||max_trials!=EXPECTED_MAX_TRIALS||max_trial_R!=EXPECTED_MAX_TRIAL_R)throw runtime_error("deterministic trial statistics mismatch");
 if(argc==2){ofstream out(argv[1],ios::binary);if(!out)throw runtime_error("cannot open output");out<<certificate;}
 cout<<"verified: S10 factor-four domain positions 1001-5000\n";
 cout<<"first_R="<<domain[PRIOR_COUNT]<<"\nlast_R="<<domain.back()<<"\nexplicit_witnesses="<<EXPECTED_COUNT<<"\n";
 cout<<"witness_fnv64=2a029f96119035a1\n";
 cout<<"deterministic_total_trials="<<total_trials<<"\nmaximum_trials="<<max_trials<<" at_R="<<max_trial_R<<"\n";
 return 0;
}catch(const exception&e){cerr<<"error: "<<e.what()<<"\n";return 1;}}
