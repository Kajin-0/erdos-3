#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>
#include <omp.h>
using namespace std;
namespace {
constexpr int L8=8388608,L9=67108864,L10=536870912,R8=16777217,R9=134217729,UMAX=76583776;
constexpr long long CAP=5000000;
constexpr int EXPECTED_K[5]={0,8,23,212,269};
constexpr long long EXPECTED_TOTAL=58459477,EXPECTED_MAX=2465835;
constexpr int EXPECTED_WORST_INDEX=47,EXPECTED_WORST_T=344872741;
constexpr uint64_t EXPECTED_WITNESS_FNV=0x85bfaba25312486bULL;
constexpr uint64_t FNV_OFFSET=1469598103934665603ULL,FNV_PRIME=1099511628211ULL;
vector<int> uniq(vector<int>v){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());return v;}
vector<int> raw(const vector<int>&s,int R){vector<int>o;o.reserve(3*(s.size()+1));for(int k=0;k<3;k++)o.push_back(k*R);for(int x:s)for(int k=0;k<3;k++)o.push_back(x+k*R);return uniq(move(o));}
vector<int> tr(const vector<int>&v,int L){vector<int>o;o.reserve(v.size());for(int x:v)o.push_back(x+L);return o;}
vector<int> build_s8(){vector<int>H={0,1,2,16,17,18,21,22,23,26,27,28},sc={64,256,2048,8192,32768},Rs={61,303,1597,8195},s;for(int x:H)s.push_back(64+x);s=uniq(move(s));for(int i=0;i<4;i++)s=tr(raw(s,Rs[i]),sc[i+1]);s=tr(raw(s,93476),262144);s=tr(raw(s,230164),1048576);s=tr(raw(s,2097164),L8);return s;}
struct RNG{uint64_t x;uint64_t next(){x^=x<<7;x^=x>>9;return x;}};
struct Row{int idx;long long rank;int T;};
struct Hit{bool ok=false;int k=0,sign=0,U=0,x=0,d=0,z=0,w=0;long long used=0;};
void hash_bytes(uint64_t&h,const string&s){for(unsigned char c:s){h^=c;h*=FNV_PRIME;}}
array<int,4> digits(const string&s){return {s[0]-'0',s[1]-'0',s[2]-'0',s[3]-'0'};}
}
int main(int argc,char**argv){try{
 if(argc!=3)throw runtime_error("usage: verify_depth10_residual_multik_rectangle_profile SAMPLE_FILE OUTPUT");
 auto s8=build_s8();auto s9=tr(raw(s8,R8),L9);vector<int>B9={0};B9.insert(B9.end(),s9.begin(),s9.end());unordered_set<int>p9(B9.begin(),B9.end());
 auto s10=tr(raw(s9,R9),L10);unordered_set<long long>base10;base10.reserve((s10.size()+1)*2);base10.insert(0);for(int x:s10)base10.insert(x);
 ifstream in(argv[1]);if(!in)throw runtime_error("cannot open sample");string line;getline(in,line);vector<Row>rows;while(getline(in,line)){istringstream ss(line);Row r;long long su,au;if(!(ss>>r.idx>>r.rank>>r.T>>su>>au))throw runtime_error("bad sample row");rows.push_back(r);}if(rows.size()!=512)throw runtime_error("sample count mismatch");
 vector<Hit>hits(rows.size());
 #pragma omp parallel for schedule(dynamic,1)
 for(int i=0;i<(int)rows.size();i++){
   vector<pair<int,int>> choices;for(int k=1;k<=4;k++){int U=abs(rows[i].T-k*R9);if(U<=UMAX)choices.push_back({U,k});}sort(choices.begin(),choices.end());
   Hit h;
   for(auto [U,k]:choices){RNG rng{88172645463325252ULL^((uint64_t)U*0x9e3779b97f4a7c15ULL)^((uint64_t)k*0xd1b54a32d192ed03ULL)};for(long long t=0;t<CAP;t++){int a=B9[rng.next()%B9.size()],b=B9[rng.next()%B9.size()];if(a==b)continue;if(a>b)swap(a,b);int d=b-a;long long z=1LL*a+2LL*d-U,w=z+d;if(z<0||w<0||z>INT32_MAX||w>INT32_MAX)continue;if(p9.count((int)z)&&p9.count((int)w)){h={true,k,rows[i].T>=k*R9?1:-1,U,a,d,(int)z,(int)w,t+1};break;}}if(h.ok)break;}
   hits[i]=h;
 }
 const string plus_mu[5]={"","1100","2200","1201","0202"};
 const string minus_mu[5]={"","0011","0022","1021","2020"};
 auto in_candidate=[&](long long q,int T){for(int layer=0;layer<3;layer++)if(base10.count(q-1LL*layer*T))return true;return false;};
 ofstream out(argv[2]);if(!out)throw runtime_error("cannot open output");
 int kcount[5]={};long long total=0,maxused=0;int worst=-1;uint64_t cert=FNV_OFFSET;
 for(int i=0;i<512;i++){
   auto&r=rows[i];auto&h=hits[i];if(!h.ok)throw runtime_error("sample unresolved");kcount[h.k]++;total+=h.used;if(h.used>maxused){maxused=h.used;worst=i;}
   if(!p9.count(h.x)||!p9.count(h.x+h.d)||!p9.count(h.z)||!p9.count(h.w)||h.z!=h.x+2*h.d-h.U||h.w!=h.z+h.d)throw runtime_error("ancestor rectangle mismatch");
   string lam=h.sign>0?"0011":"0112";string mu=h.sign>0?plus_mu[h.k]:minus_mu[h.k];auto ld=digits(lam),md=digits(mu);long long b[4]={h.x,h.x+h.d,h.z,h.w},p[4];for(int j=0;j<4;j++)p[j]=1LL*L10+b[j]+1LL*md[j]*R9+1LL*ld[j]*r.T;
   long long q=p[1]-p[0];if(q<=0||p[2]-p[1]!=q||p[3]-p[2]!=q)throw runtime_error("transport AP mismatch");for(long long y:p)if(!in_candidate(y,r.T))throw runtime_error("transport point absent");
   ostringstream ss;ss<<r.idx<<" "<<r.rank<<" "<<r.T<<" "<<h.k<<" "<<h.sign<<" "<<h.U<<" "<<h.x<<" "<<h.d<<" "<<h.z<<" "<<h.w<<" "<<h.used<<" "<<lam<<"/"<<mu<<" "<<p[0]<<" "<<p[1]<<" "<<p[2]<<" "<<p[3]<<"\n";string text=ss.str();out<<text;hash_bytes(cert,text);
 }
 if(total!=EXPECTED_TOTAL||maxused!=EXPECTED_MAX||worst!=EXPECTED_WORST_INDEX||rows[worst].T!=EXPECTED_WORST_T)throw runtime_error("search statistics mismatch");
 for(int k=1;k<=4;k++)if(kcount[k]!=EXPECTED_K[k])throw runtime_error("channel count mismatch");
 if(cert!=EXPECTED_WITNESS_FNV)throw runtime_error("witness hash mismatch");
 cout<<"verified: all 512 exact residual samples have explicit k=1..4 rectangle transports\n";for(int k=1;k<=4;k++)cout<<"k"<<k<<"_count="<<kcount[k]<<"\n";cout<<"total_trials="<<total<<"\nmaximum_trials="<<maxused<<" at_index="<<worst<<" T="<<rows[worst].T<<"\n";cout<<hex<<"witness_fnv64="<<cert<<dec<<"\n";return 0;
}catch(const exception&e){cerr<<"error: "<<e.what()<<"\n";return 1;}}
