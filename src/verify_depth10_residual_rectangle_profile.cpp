#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>
#include <omp.h>
using namespace std;
namespace {
constexpr int L8=8388608,L9=67108864,L10=536870912,R8=16777217,R9=134217729;
constexpr long long CAP=5000000;
constexpr int EXPECTED_FOUND=284,EXPECTED_FIRST_FOUND_INDEX=228;
constexpr long long EXPECTED_TOTAL_TRIALS=29552689,EXPECTED_MAX_TRIALS=1066649;
constexpr int EXPECTED_WORST_INDEX=478,EXPECTED_WORST_T=592613709;
constexpr uint64_t EXPECTED_SUCCESS_FNV=0xa391c1771f01d79bULL;
constexpr uint64_t FNV_OFFSET=1469598103934665603ULL,FNV_PRIME=1099511628211ULL;
vector<int> uniq(vector<int>v){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());return v;}
vector<int> raw(const vector<int>&s,int R){vector<int>o;o.reserve(3*(s.size()+1));for(int k=0;k<3;k++)o.push_back(k*R);for(int x:s)for(int k=0;k<3;k++)o.push_back(x+k*R);return uniq(move(o));}
vector<int> tr(const vector<int>&v,int L){vector<int>o;o.reserve(v.size());for(int x:v)o.push_back(x+L);return o;}
vector<int> build_s8(){vector<int>H={0,1,2,16,17,18,21,22,23,26,27,28},sc={64,256,2048,8192,32768},Rs={61,303,1597,8195},s;for(int x:H)s.push_back(64+x);s=uniq(move(s));for(int i=0;i<4;i++)s=tr(raw(s,Rs[i]),sc[i+1]);s=tr(raw(s,93476),262144);s=tr(raw(s,230164),1048576);s=tr(raw(s,2097164),L8);return s;}
struct RNG{uint64_t x;uint64_t next(){x^=x<<7;x^=x>>9;return x;}};
struct Row{int idx;long long rank;int T;long long su,U;};
struct Hit{bool ok=false;int x=0,d=0,z=0,w=0;long long used=0;};
void hash_bytes(uint64_t&h,const string&s){for(unsigned char c:s){h^=c;h*=FNV_PRIME;}}
}
int main(int argc,char**argv){try{
 if(argc!=3)throw runtime_error("usage: verify_depth10_residual_rectangle_profile SAMPLE_FILE OUTPUT_WITNESSES");
 auto s8=build_s8();auto s9=tr(raw(s8,R8),L9);vector<int>B9={0};B9.insert(B9.end(),s9.begin(),s9.end());unordered_set<int>p9;p9.reserve(B9.size()*2);for(int x:B9)p9.insert(x);
 auto s10=tr(raw(s9,R9),L10);unordered_set<long long>base10;base10.reserve((s10.size()+1)*2);base10.insert(0);for(int x:s10)base10.insert(x);
 ifstream in(argv[1]);if(!in)throw runtime_error("cannot open sample");string line;getline(in,line);vector<Row>rows;while(getline(in,line)){istringstream ss(line);Row r;long long au;if(!(ss>>r.idx>>r.rank>>r.T>>r.su>>au))throw runtime_error("bad sample row");r.U=au;rows.push_back(r);}if(rows.size()!=512)throw runtime_error("sample count mismatch");
 vector<Hit>hits(rows.size());
 #pragma omp parallel for schedule(dynamic,1)
 for(int i=0;i<(int)rows.size();i++){
   RNG rng{88172645463325252ULL ^ ((uint64_t)rows[i].U*0x9e3779b97f4a7c15ULL)};Hit h;
   for(long long t=0;t<CAP;t++){
     int a=B9[rng.next()%B9.size()],b=B9[rng.next()%B9.size()];if(a==b)continue;if(a>b)swap(a,b);int d=b-a;long long z=1LL*a+2LL*d-rows[i].U,w=z+d;if(z<0||w<0||z>INT32_MAX||w>INT32_MAX)continue;if(p9.count((int)z)&&p9.count((int)w)){h={true,a,d,(int)z,(int)w,t+1};break;}
   }
   hits[i]=h;
 }
 auto in_candidate=[&](long long q,int T){for(int layer=0;layer<3;layer++)if(base10.count(q-1LL*layer*T))return true;return false;};
 ofstream out(argv[2]);if(!out)throw runtime_error("cannot open output");
 int found=0,first_found=-1;long long total=0,maxused=0;int worst=-1;uint64_t cert=FNV_OFFSET;
 for(int i=0;i<(int)rows.size();i++){
   auto&r=rows[i];auto&h=hits[i];
   if(!h.ok)continue;
   if(first_found<0) first_found=i;
   found++;
   total+=h.used;
   if(h.used>maxused){maxused=h.used;worst=i;}
   if(!p9.count(h.x)||!p9.count(h.x+h.d)||!p9.count(h.z)||!p9.count(h.w)||h.z!=h.x+2*h.d-r.U||h.w!=h.z+h.d)throw runtime_error("ancestor rectangle mismatch");
   long long p0,p1,p2,p3;
   string channel;
   if(r.su>0){channel="0011/0202";p0=1LL*L10+h.x;p1=1LL*L10+h.x+h.d+2LL*R9;p2=1LL*L10+h.z+r.T;p3=1LL*L10+h.w+2LL*R9+r.T;}
   else {channel="0112/2020";p0=1LL*L10+h.x+2LL*R9;p1=1LL*L10+h.x+h.d+r.T;p2=1LL*L10+h.z+2LL*R9+r.T;p3=1LL*L10+h.w+2LL*r.T;}
   if(p1-p0<=0||p2-p1!=p1-p0||p3-p2!=p1-p0)throw runtime_error("transport AP mismatch");
   if(!in_candidate(p0,r.T)||!in_candidate(p1,r.T)||!in_candidate(p2,r.T)||!in_candidate(p3,r.T))throw runtime_error("transport point absent");
   ostringstream ss;ss<<r.idx<<" "<<r.rank<<" "<<r.T<<" "<<r.su<<" "<<r.U<<" "<<h.x<<" "<<h.d<<" "<<h.z<<" "<<h.w<<" "<<h.used<<" "<<channel<<" "<<p0<<" "<<p1<<" "<<p2<<" "<<p3<<"\n";string text=ss.str();out<<text;hash_bytes(cert,text);
 }
 if(found!=EXPECTED_FOUND||first_found!=EXPECTED_FIRST_FOUND_INDEX||total!=EXPECTED_TOTAL_TRIALS||maxused!=EXPECTED_MAX_TRIALS||worst!=EXPECTED_WORST_INDEX||rows[worst].T!=EXPECTED_WORST_T||cert!=EXPECTED_SUCCESS_FNV)throw runtime_error("profile invariant mismatch");
 for(int i=0;i<EXPECTED_FIRST_FOUND_INDEX;i++)if(hits[i].ok)throw runtime_error("unexpected low-window hit");
 for(int i=EXPECTED_FIRST_FOUND_INDEX;i<512;i++)if(!hits[i].ok)throw runtime_error("transport-window sample unresolved");
 cout<<"verified: exact rectangle witnesses for all 284 residual samples in the k=4 transport window\n";
 cout<<"sample_count=512\nrectangle_covered=284\nsearch_unresolved_below_window=228\nfirst_covered_index=228\n";
 cout<<"covered_T_range="<<rows[228].T<<","<<rows.back().T<<"\n";
 cout<<"covered_abs_U_range="<<rows[371].U<<","<<rows[228].U<<" plus positive side through "<<rows.back().U<<"\n";
 cout<<hex<<"witness_fnv64="<<cert<<dec<<"\n";
 return 0;
}catch(const exception&e){cerr<<"error: "<<e.what()<<"\n";return 1;}}
