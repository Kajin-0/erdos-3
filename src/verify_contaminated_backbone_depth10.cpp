#include <algorithm>
#include <array>
#include <atomic>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>
#include <omp.h>
using namespace std;
namespace {
constexpr int L9=67108864;
constexpr int L10=536870912;
constexpr int R9=134217729;
constexpr uint64_t G10_FNV=0x3920bcc3f69c5c98ULL;
constexpr uint64_t S10_FNV=0x405b941a1f8b2580ULL;
constexpr uint64_t FNV_OFFSET=1469598103934665603ULL;
constexpr uint64_t FNV_PRIME=1099511628211ULL;
vector<int> uniq(vector<int>v){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());return v;}
vector<int> raw(const vector<int>&s,int R){vector<int>o;o.reserve(3*(s.size()+1));for(int k=0;k<3;k++)o.push_back(k*R);for(int x:s)for(int k=0;k<3;k++)o.push_back(x+k*R);return uniq(move(o));}
vector<int> tr(const vector<int>&v,int L){vector<int>o;o.reserve(v.size());for(int x:v)o.push_back(x+L);return o;}
vector<int> build_s9(){vector<int>H={0,1,2,16,17,18,21,22,23,26,27,28};vector<int>sc={64,256,2048,8192,32768};vector<int>Rs={61,303,1597,8195};vector<int>s;for(int x:H)s.push_back(64+x);s=uniq(move(s));for(int i=0;i<4;i++)s=tr(raw(s,Rs[i]),sc[i+1]);s=tr(raw(s,93476),262144);s=tr(raw(s,230164),1048576);s=tr(raw(s,2097164),8388608);s=tr(raw(s,16777217),L9);return s;}
int v2(int x){if(x<=0)throw invalid_argument("v2");return __builtin_ctz((unsigned)x);}
uint64_t fnv(const vector<int>&v){uint64_t h=FNV_OFFSET;for(int x:v){string t=to_string(x)+",";for(unsigned char b:t){h^=b;h*=FNV_PRIME;}}return h;}
pair<bool,array<int,4>> first4(const vector<int>&v,int ambient){vector<unsigned char>p((size_t)ambient);for(int x:v)p[x]=1;atomic<bool>found{false};array<int,4>w={0,0,0,0};int maximum=v.back();
#pragma omp parallel for schedule(dynamic,4)
for(int i=0;i<(int)v.size();i++){if(found.load(memory_order_relaxed))continue;int a=v[i],stop=upper_bound(v.begin()+i+1,v.end(),(maximum+a)/2)-v.begin();for(int j=i+1;j<stop;j++){int b=v[j],f=2*a-b;if(f<0)continue;int z=2*b-a;if(p[f]&&p[z]){bool expected=false;if(found.compare_exchange_strong(expected,true))w={f,a,b,z};break;}}}return {found.load(),w};}
void schedule(const vector<int>&s,int R){auto g=raw(s,R);unordered_set<int>w(g.begin(),g.end());vector<int>a={0};a.insert(a.end(),s.begin(),s.end());for(int x:a){for(int k=0;k<3;k++)if(!w.count(x+k*R))throw runtime_error("schedule failure");w.erase(x);}}
}
int main(){const auto s9=build_s9();if(s9.size()!=88572||s9.front()!=L9||s9.back()!=115267902)throw runtime_error("S9 geometry");const int twice=2*L9;auto g0=raw(s9,twice);auto bad=first4(g0,L10);if(!bad.first)throw runtime_error("R=2L9 unexpectedly valid");const array<int,4> expected={0,L9,2*L9,3*L9};for(int i=0;i<4;i++)if(!binary_search(g0.begin(),g0.end(),expected[i]))throw runtime_error("expected 2L witness absent");int first=0;for(int R=twice;R<=R9;R++){if(v2(R)%2)continue;auto g=raw(s9,R);if(g.size()!=3*(s9.size()+1)||g.back()>=L10)continue;if(!first4(g,L10).first){first=R;break;}}if(first!=R9)throw runtime_error("first exact continuation mismatch");auto g10=raw(s9,R9);if(v2(R9)!=0||g10.size()!=265719||g10.front()!=0||g10.back()!=383703360||fnv(g10)!=G10_FNV)throw runtime_error("G10 mismatch");if(first4(g10,L10).first)throw runtime_error("G10 has a 4-AP");schedule(s9,R9);vector<int>backbone;for(int x:g10)if(L9<=x&&x<2*L9)backbone.push_back(x);if(backbone!=s9)throw runtime_error("backbone not exact");auto s10=tr(g10,L10);if(s10.size()!=265719||s10.front()!=L10||s10.back()!=920574272||fnv(s10)!=S10_FNV)throw runtime_error("S10 mismatch");cout<<"verified: R=2L9 invalid and R9=134217729 first valid exact continuation\n";cout<<"R_2L_witness=0,67108864,134217728,201326592\n";cout<<"scale_factors=4,8,4,4,8,4,8,8,8\n";cout<<"state_size_S10=265719\n";cout<<"weighted_density_S10=265719/524288\n";cout<<"weighted_density_growth_S10_over_S9=88573/118096\n";cout<<"G10_fnv64=3920bcc3f69c5c98\n";cout<<"S10_fnv64=405b941a1f8b2580\n";}
