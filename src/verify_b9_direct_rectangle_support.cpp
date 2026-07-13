#include <array>
#include <algorithm>
#include <atomic>
#include <climits>
#include <cstdint>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>
#include <omp.h>
using namespace std;
namespace {
constexpr int L8=8388608,L9=67108864,R8=16777217,S9MAX=115267902,UMAX=76583776;
constexpr uint64_t FNV_OFFSET=1469598103934665603ULL,FNV_PRIME=1099511628211ULL;
vector<int> uniq(vector<int>v){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());return v;}
vector<int> raw(const vector<int>&s,int R){vector<int>o;o.reserve(3*(s.size()+1));for(int k=0;k<3;k++)o.push_back(k*R);for(int x:s)for(int k=0;k<3;k++)o.push_back(x+k*R);return uniq(move(o));}
vector<int> tr(const vector<int>&v,int L){vector<int>o;o.reserve(v.size());for(int x:v)o.push_back(x+L);return o;}
vector<int> build_s8(){vector<int>H={0,1,2,16,17,18,21,22,23,26,27,28},sc={64,256,2048,8192,32768},Rs={61,303,1597,8195},s;for(int x:H)s.push_back(64+x);s=uniq(move(s));for(int i=0;i<4;i++)s=tr(raw(s,Rs[i]),sc[i+1]);s=tr(raw(s,93476),262144);s=tr(raw(s,230164),1048576);s=tr(raw(s,2097164),L8);return s;}
struct Data{vector<int>s8,A,g9,s9;};
Data data(){Data d;d.s8=build_s8();d.A={0};d.A.insert(d.A.end(),d.s8.begin(),d.s8.end());d.g9=raw(d.s8,R8);d.s9=tr(d.g9,L9);if(d.s9.size()!=88572||d.s9.front()!=L9||d.s9.back()!=S9MAX)throw runtime_error("S9 mismatch");return d;}
struct Stats{vector<int>cnt,mn,mx;};
Stats base_stats(const vector<int>&A){int M=A.back();Stats s;s.cnt.assign(M+1,0);s.mn.assign(M+1,INT_MAX);s.mx.assign(M+1,INT_MIN);
#pragma omp parallel
{vector<int>cnt(M+1),mn(M+1,INT_MAX),mx(M+1,INT_MIN);
#pragma omp for schedule(dynamic,8)
for(int i=0;i<(int)A.size();i++)for(int j=i+1;j<(int)A.size();j++){int d=A[j]-A[i];cnt[d]++;mn[d]=min(mn[d],A[i]);mx[d]=max(mx[d],A[i]);}
#pragma omp critical
for(int d=1;d<=M;d++)if(cnt[d]){s.cnt[d]+=cnt[d];s.mn[d]=min(s.mn[d],mn[d]);s.mx[d]=max(s.mx[d],mx[d]);}}
return s;}
void catalog(const Data&d,const Stats&st,int lower,int upper,vector<int>&ds,vector<int>&cs){int M=d.A.back(),n=d.A.size();vector<unsigned char>in(S9MAX+1);for(int x:d.s9)in[x]=1;for(int delta=1;delta<=S9MAX;delta++){long long c=0;int a0=INT_MAX,a1=INT_MIN;auto add=[&](long long cc,long long x,long long y){if(!cc)return;c+=cc;a0=min(a0,(int)x);a1=max(a1,(int)y);};if(delta<=M&&st.cnt[delta])add(3LL*st.cnt[delta],L9+st.mn[delta],L9+st.mx[delta]+2LL*R8);long long z=1LL*delta-R8,ad=llabs(z);if(ad<=M){long long oc=ad==0?n:st.cnt[ad];if(oc){int a=ad==0?0:(z>0?st.mn[ad]:st.mn[ad]+ad),b=ad==0?M:(z>0?st.mx[ad]:st.mx[ad]+ad);add(2*oc,L9+a,L9+b+R8);}}z=1LL*delta-2LL*R8;ad=llabs(z);if(ad<=M){long long oc=ad==0?n:st.cnt[ad];if(oc){int a=ad==0?0:(z>0?st.mn[ad]:st.mn[ad]+ad),b=ad==0?M:(z>0?st.mx[ad]:st.mx[ad]+ad);add(oc,L9+a,L9+b);}}if(in[delta])add(1,0,0);if(c<=lower||c>upper)continue;long long span=1LL*a1-a0;if(2LL*delta<=UMAX||2LL*delta-span<=UMAX){ds.push_back(delta);cs.push_back((int)c);}}}
vector<int> materialize(const Data&d,const Stats&st,const vector<int>&ds,const vector<int>&cs,vector<uint64_t>&off){vector<int>id(S9MAX+1,-1);for(int i=0;i<(int)ds.size();i++)id[ds[i]]=i;off.assign(ds.size()+1,0);for(size_t i=0;i<ds.size();i++)off[i+1]=off[i]+cs[i];vector<atomic<uint64_t>>cur(ds.size());for(size_t i=0;i<ds.size();i++)cur[i]=off[i];vector<int>x(off.back());auto put=[&](int delta,int a){if(delta>0&&delta<=S9MAX){int k=id[delta];if(k>=0)x[cur[k].fetch_add(1,memory_order_relaxed)]=a;}};int n=d.A.size();
#pragma omp parallel for schedule(dynamic,8)
for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){int q=d.A[j]-d.A[i];if(q<=S9MAX&&id[q]>=0){put(q,L9+d.A[i]);put(q,L9+d.A[i]+R8);put(q,L9+d.A[i]+2*R8);}}
#pragma omp parallel for schedule(dynamic,8)
for(int ia=0;ia<n;ia++){int a=d.A[ia];for(int b:d.A){int q=R8+b-a;if(q>0&&q<=S9MAX&&id[q]>=0){put(q,L9+a);put(q,L9+a+R8);}q=2*R8+b-a;if(q>0&&q<=S9MAX&&id[q]>=0)put(q,L9+a);}}
for(int g:d.g9)put(L9+g,0);for(size_t i=0;i<ds.size();i++)if(cur[i]!=off[i+1])throw runtime_error("start fill mismatch");return x;}
long long count_bits(const vector<uint64_t>&b){long long n=0;for(uint64_t q:b)n+=__builtin_popcountll(q);return n;}
void mark(vector<uint64_t>&b,long long x){if(x>0&&x<=UMAX)b[x>>6]|=1ULL<<(x&63);}
struct Stage{int lo,hi;long long groups,starts,ops,covered,total,zero;};
Stage run_band(const Data&d,const Stats&st,int lo,int hi,vector<uint64_t>&global){vector<int>ds,cs;catalog(d,st,lo,hi,ds,cs);vector<uint64_t>off;auto starts=materialize(d,st,ds,cs,off);int nth=omp_get_max_threads();size_t words=global.size();vector<vector<uint64_t>>local(nth,vector<uint64_t>(words));vector<long long>opsv(nth);
#pragma omp parallel
{int tid=omp_get_thread_num();auto&support=local[tid];long long ops=0;
#pragma omp for schedule(dynamic,32)
for(int k=0;k<(int)ds.size();k++){int delta=ds[k],c=cs[k];int*x=starts.data()+off[k];sort(x,x+c);for(int i=0;i<c;i++)for(int j=0;j<=i;j++){long long D=1LL*x[i]-x[j],p=2LL*delta+D,m=2LL*delta-D;if(p>0&&p<=UMAX)support[p>>6]|=1ULL<<(p&63);if(m>0&&m<=UMAX)support[m>>6]|=1ULL<<(m&63);ops++;}}opsv[tid]=ops;}
long long ops=0;vector<uint64_t>band(words);for(int t=0;t<nth;t++){ops+=opsv[t];for(size_t w=0;w<words;w++)band[w]|=local[t][w];}long long covered=count_bits(band);for(size_t w=0;w<words;w++)global[w]|=band[w];long long total=count_bits(global);return {lo,hi,(long long)ds.size(),(long long)starts.size(),ops,covered,total,UMAX-total};}
void add_special(const Stats&st,vector<uint64_t>&global){int M=st.cnt.size()-1;auto emit=[&](long long delta,long long D){mark(global,2*delta+D);mark(global,2*delta-D);};for(int d=0;d<=M;d++){if(d&&st.cnt[d]==0)continue;emit(R8,d);emit(R8,llabs(1LL*R8+d));emit(R8,llabs(1LL*R8-d));emit(2LL*R8,d);}}
uint64_t fnv_list(const vector<int>&v){uint64_t h=FNV_OFFSET;for(int x:v){string t=to_string(x)+",";for(unsigned char c:t){h^=c;h*=FNV_PRIME;}}return h;}
struct RNG{uint64_t x;uint64_t next(){x^=x<<7;x^=x>>9;return x;}};struct Hit{bool ok=false;int a=0,d=0,z=0,w=0;long long used=0;};
}

struct Expected {int lo,hi; long long groups,starts,ops,covered;};
const Expected EXPECTED[]={{0,16,1491233,12479508,76206084,18732316},{16,32,1130717,28639718,389597167,38187592},{32,64,1777456,86449011,2222186841,61265926},{64,128,2302548,217231839,10738742213,73937604},{128,256,2356421,434911006,41870738292,76407456},{256,300,567838,161226381,22995501791,76264912},{300,350,334951,108588614,17672142223,76227713},{350,400,385029,145105838,27450979298,76361145},{400,450,365112,157297454,33975401607,76488055},{450,512,225954,109965601,26843231018,76465778}};
void save_bits(const string&p,const vector<uint64_t>&b){FILE*f=fopen(p.c_str(),"wb");if(!f)throw runtime_error("cannot write "+p);long long low=0;uint64_t n=b.size();fwrite(&low,8,1,f);fwrite(&n,8,1,f);fwrite(b.data(),8,n,f);fclose(f);}
pair<long long,vector<uint64_t>> load_bits(const string&p){FILE*f=fopen(p.c_str(),"rb");if(!f)throw runtime_error("cannot open "+p);long long low;uint64_t n;if(fread(&low,8,1,f)!=1||fread(&n,8,1,f)!=1)throw runtime_error("bad header");vector<uint64_t>b(n);if(fread(b.data(),8,n,f)!=n)throw runtime_error("truncated");fclose(f);return {low,move(b)};}
uint64_t fnv_text(const string&s){uint64_t h=FNV_OFFSET;for(unsigned char c:s){h^=c;h*=FNV_PRIME;}return h;}
bool find_difference(int*x,int c,long long D,int&lo,int&hi){if(D<0)return false;if(D==0){lo=hi=x[0];return true;}int i=0,j=1;while(j<c){long long q=1LL*x[j]-x[i];if(q==D){lo=x[i];hi=x[j];return true;}if(q<D)j++;else{if(++i==j)j++;}}return false;}
int main(int argc,char**argv){try{if(argc<2)throw runtime_error("mode required");string mode=argv[1];
 if(mode=="band"){
  if(argc!=5)throw runtime_error("band LO HI OUT");int lo=stoi(argv[2]),hi=stoi(argv[3]);auto d=data();auto st=base_stats(d.A);vector<uint64_t>g((UMAX+64LL)/64);auto r=run_band(d,st,lo,hi,g);const Expected*e=nullptr;for(auto&x:EXPECTED)if(x.lo==lo&&x.hi==hi)e=&x;if(!e||r.groups!=e->groups||r.starts!=e->starts||r.ops!=e->ops||r.covered!=e->covered)throw runtime_error("band invariant mismatch");save_bits(argv[4],g);cout<<"verified_band="<<lo<<","<<hi<<" groups="<<r.groups<<" starts="<<r.starts<<" ops="<<r.ops<<" covered="<<r.covered<<"\n";
 } else if(mode=="special"){
  if(argc!=3)throw runtime_error("special OUT");auto d=data();auto st=base_stats(d.A);vector<uint64_t>g((UMAX+64LL)/64);add_special(st,g);long long c=count_bits(g);if(c!=20682803)throw runtime_error("special invariant mismatch");save_bits(argv[2],g);cout<<"verified_special_support="<<c<<"\n";
 } else if(mode=="reduce"){
  if(argc<5)throw runtime_error("reduce ZERO_OUT UNION_OUT BITSETS...");vector<uint64_t>g;for(int i=4;i<argc;i++){auto [low,b]=load_bits(argv[i]);if(low!=0)throw runtime_error("low mismatch");if(g.empty())g.assign(b.size(),0);if(g.size()!=b.size())throw runtime_error("size mismatch");for(size_t w=0;w<g.size();w++)g[w]|=b[w];}long long covered=count_bits(g);vector<int>zeros;for(int U=1;U<=UMAX;U++)if(!((g[U>>6]>>(U&63))&1ULL))zeros.push_back(U);if(covered!=76581484||zeros.size()!=2292||zeros.front()!=4||zeros.back()!=76561920)throw runtime_error("union invariant mismatch");ofstream out(argv[2]);string text;for(int U:zeros){string row=to_string(U)+"\n";out<<row;text+=row;}out.close();if(fnv_text(text)!=0x0954213145a3dba7ULL)throw runtime_error("zero-list hash mismatch");save_bits(argv[3],g);cout<<"verified_union_covered="<<covered<<" terminal_zero_count="<<zeros.size()<<" zero_fnv64="<<hex<<fnv_text(text)<<dec<<"\n";
 } else if(mode=="target"){
  if(argc!=6)throw runtime_error("target LO HI TARGETS OUT");int lo=stoi(argv[2]),hi=stoi(argv[3]);ifstream tin(argv[4]);vector<int>targets;int u;while(tin>>u)targets.push_back(u);auto d=data();auto st=base_stats(d.A);vector<int>ds,cs;catalog(d,st,lo,hi,ds,cs);vector<uint64_t>off;auto starts=materialize(d,st,ds,cs,off);vector<atomic<int>>done(targets.size());struct TW{int delta=0,a=0,b=0;};vector<TW>w(targets.size());
#pragma omp parallel for schedule(dynamic,16)
for(int k=0;k<(int)ds.size();k++){int delta=ds[k],c=cs[k];int*x=starts.data()+off[k];sort(x,x+c);for(int t=0;t<(int)targets.size();t++){if(done[t])continue;long long D=llabs(2LL*delta-targets[t]);int a,b;if(find_difference(x,c,D,a,b)){int expected=0;if(done[t].compare_exchange_strong(expected,1))w[t]={delta,a,b};}}}
  ofstream out(argv[5]);int found=0;for(int t=0;t<(int)targets.size();t++){if(!done[t]){out<<targets[t]<<" FAIL\n";continue;}found++;int delta=w[t].delta,a=w[t].a,b=w[t].b,x,y;if(targets[t]<=2LL*delta){x=a;y=b;}else{x=b;y=a;}if(y!=x+2LL*delta-targets[t])throw runtime_error("target orientation mismatch");out<<targets[t]<<" "<<x<<" "<<x+delta<<" "<<y<<" "<<y+delta<<" "<<delta<<"\n";}cout<<"target_band="<<lo<<","<<hi<<" groups="<<ds.size()<<" starts="<<starts.size()<<" found="<<found<<" remaining="<<targets.size()-found<<"\n";
 } else if(mode=="final7"){
  if(argc!=3)throw runtime_error("final7 WITNESS_FILE");ifstream in(argv[2]);vector<array<long long,5>>rows;long long U,a,b,c,dv;string text;while(in>>U>>a>>b>>c>>dv){rows.push_back({U,a,b,c,dv});text+=to_string(U)+" "+to_string(a)+" "+to_string(b)+" "+to_string(c)+" "+to_string(dv)+"\n";}const vector<int>expected={11892397,27493106,43809995,73170196,74090852,76468444,76561920};if(rows.size()!=7||fnv_text(text)!=0xd2c19c77b1792c42ULL)throw runtime_error("final7 file invariant mismatch");auto dat=data();unordered_set<long long>B;B.insert(0);for(int x:dat.s9)B.insert(x);for(size_t i=0;i<rows.size();i++){auto r=rows[i];if(r[0]!=expected[i])throw runtime_error("final7 U mismatch");long long gap=r[2]-r[1];if(gap<=0||r[4]-r[3]!=gap||r[3]!=r[1]+2*gap-r[0])throw runtime_error("final7 rectangle equation mismatch");for(int j=1;j<=4;j++)if(!B.count(r[j]))throw runtime_error("final7 point absent");}cout<<"verified_final_large_fiber_witnesses=7 fnv64="<<hex<<fnv_text(text)<<dec<<"\n";
 } else if(mode=="terminal"){
  if(argc!=4)throw runtime_error("terminal ZERO_LIST WITNESS_OUT");ifstream in(argv[2]);vector<int>zeros;int U;while(in>>U)zeros.push_back(U);if(zeros.size()!=2292||zeros.front()!=4||zeros.back()!=76561920)throw runtime_error("zero list mismatch");auto d=data();vector<int>B={0};B.insert(B.end(),d.s9.begin(),d.s9.end());unordered_set<int>P(B.begin(),B.end());vector<Hit>hits(zeros.size());
#pragma omp parallel for schedule(dynamic,1)
for(int i=0;i<(int)zeros.size();i++){int u=zeros[i];RNG rng{88172645463325252ULL^((uint64_t)u*0x9e3779b97f4a7c15ULL)};Hit h;for(long long q=0;q<1000000;q++){int a=B[rng.next()%B.size()],b=B[rng.next()%B.size()];if(a==b)continue;if(a>b)swap(a,b);int gap=b-a;long long z=1LL*a+2LL*gap-u,w=z+gap;if(z<0||w<0||z>INT_MAX||w>INT_MAX)continue;if(P.count((int)z)&&P.count((int)w)){h={true,a,gap,(int)z,(int)w,q+1};break;}}hits[i]=h;}
  ofstream out(argv[3]);vector<int>failed;long long total=0,mx=0;int mxu=0;string text;for(size_t i=0;i<zeros.size();i++){auto h=hits[i];if(!h.ok){failed.push_back(zeros[i]);continue;}if(!P.count(h.a)||!P.count(h.a+h.d)||!P.count(h.z)||!P.count(h.w)||h.z!=h.a+2*h.d-zeros[i]||h.w!=h.z+h.d)throw runtime_error("witness mismatch");string row=to_string(zeros[i])+" "+to_string(h.a)+" "+to_string(h.a+h.d)+" "+to_string(h.z)+" "+to_string(h.w)+" "+to_string(h.used)+"\n";out<<row;text+=row;total+=h.used;if(h.used>mx){mx=h.used;mxu=zeros[i];}}out.close();const vector<int>expected={11892397,27493106,43809995,73170196,74090852,76468444,76561920};if(failed!=expected||total!=134920545||mx!=887134||mxu!=5601876||fnv_text(text)!=0x63be7ecdc206eeb7ULL)throw runtime_error("terminal invariant mismatch");cout<<"explicit_witnesses="<<zeros.size()-failed.size()<<" unresolved="<<failed.size()<<" witness_fnv64="<<hex<<fnv_text(text)<<dec<<" total_trials="<<total<<" maximum_trials="<<mx<<" at_U="<<mxu<<"\n";cout<<"unresolved=";for(size_t i=0;i<failed.size();i++)cout<<(i?",":"")<<failed[i];cout<<"\n";
 } else throw runtime_error("bad mode");return 0;}catch(const exception&e){cerr<<"error: "<<e.what()<<"\n";return 1;}}
