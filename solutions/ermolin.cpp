#include <iostream>
#include <queue>
using namespace std;
using pii = pair<int, int>;

const int N = 100;
const int INF = 1000000;

int n, m;
char a[N][N];
char aOld[N][N];

int di[4] = { 0, 0, -1, 1 };
int dj[4] = { -1, 1, 0, 0 };
char dc[4] = { 'L', 'R', 'U', 'D' };

char was[N][N];
bool isolated = false;

inline bool isFree(int i, int j) {
	return a[i][j] == '.'
		|| a[i][j] == 'C'
		|| a[i][j] == 'U'
		|| a[i][j] == 'D';
}

vector<int> get_valid_dirs(int si, int sj) {
	vector<int> res;
	for (int dir = 0; dir < 4; dir++) {
		int i = si + di[dir];
		int j = sj + dj[dir];
		if (0 <= i && i < n &&
			0 <= j && j < m &&
			isFree(i, j))
			res.push_back(dir);
	}
	return res;
}


bool used[N][N];
bool cp[N][N];
int tin[N][N];
int fup[N][N];

int timer = 0;

void dfscp(int i, int j, int pi = -1, int pj = -1) {
    used[i][j] = true;
    tin[i][j] = fup[i][j] = timer++;
    int children = 0;
    for (int dir : get_valid_dirs(i, j)) {
        int ti = i + di[dir];
        int tj = j + dj[dir];
        if (ti == pi && tj == pj)  continue;
        if (used[ti][tj])
            fup[i][j] = min(fup[i][j], tin[ti][tj]);
        else {
            dfscp(ti, tj, i, j);
            fup[i][j] = min(fup[i][j], fup[ti][tj]);
            if (fup[ti][tj] >= tin[i][j] && pi != -1)
                cp[i][j] = true;
            ++children;
        }
    }
    if (pi == -1 && children > 1)
        cp[i][j] = true;
}

int dbfs(int i, int j) {
	if (cp[i][j]) {
		used[i][j] = true;
		int best = 0;
		for (int dir : get_valid_dirs(i, j)) {
			int ti = i + di[dir];
			int tj = j + dj[dir];
			if (!used[ti][tj])
				best = max(best, dbfs(ti, tj));
		}
		return best + 1;
	}
	vector<pii> cps;
	queue<pii> q;
	int res = 1;
	if (a[i][j] == 'C')
		res += 2;
	used[i][j] = true;
	q.push({i, j});
	while (!q.empty()) {
		int i = q.front().first;
		int j = q.front().second;
		q.pop();
		for (int dir : get_valid_dirs(i, j)) {
			int ti = i + di[dir];
			int tj = j + dj[dir];
			if (used[ti][tj])
				continue;
			used[ti][tj] = true;
			if (cp[ti][tj]) {
				cps.push_back({ti, tj});
			} else {
				res++;
				if (a[ti][tj] == 'C')
					res += 2;
				q.push({ti, tj});
			}
		}
	}
	int best = 0;
	for (auto& ij : cps)
		best = max(best, dbfs(ij.first, ij.second));
   	return best + res;
}

int heuristic2(int mi, int mj) {
	memset(used, 0, sizeof(used));
    memset(cp, 0, sizeof(cp));
    memset(tin, 0, sizeof(tin));
    memset(fup, 0, sizeof(fup));
	dfscp(mi, mj);
	memset(used, 0, sizeof(used));
	return dbfs(mi, mj);
}

int heuristic(int mi, int mj, int hi, int hj) {
	memset(was, 0, sizeof(was));
	int res = 0;
	was[mi][mj] = a[mi][mj];
	was[hi][hj] = a[hi][hj];
	queue<pii> q;
	q.push({mi, mj});
	q.push({hi, hj});
	while (!q.empty()) {
		int i = q.front().first;
		int j = q.front().second;
		q.pop();
		for (int dir : get_valid_dirs(i, j)) {
			int ni = i + di[dir];
			int nj = j + dj[dir];
			if (was[ni][nj]) continue;
			was[ni][nj] = was[i][j];
			q.push({ni, nj});
			res += (was[i][j] == was[mi][mj] ? 1 : -1) * (a[i][j] == 'C' ? 3 : 1);
		}
	}
	return res;
}

int dfs2(int mi, int mj, int cnt, bool make_move = false) {
	if (cnt == 0)
		return heuristic2(mi, mj);
	auto dirs = get_valid_dirs(mi, mj);
	if (dirs.size() == 0)
		return 0;
	int best_score = -INF;
	vector<int> best_moves;
	for (int dir : dirs) {
		int ti = mi + di[dir];
		int tj = mj + dj[dir];
		char old = a[ti][tj];
		a[ti][tj] = a[mi][mj];
		int score = 1 + dfs2(ti, tj, (cnt - 1) / dirs.size());
		if (old == 'C')
			score += 2;
		if (score > best_score) {
			best_score = score;
			best_moves.clear();
		}
		if (score == best_score) {
			best_moves.push_back(dir);
		}
		a[ti][tj] = old;
	}
	if (make_move) {
		int dir = best_moves[rand() % best_moves.size()];
		cout << dc[dir] << endl;
	}
	return best_score;
}

int dfs(int mi, int mj, int hi, int hj, int cnt, bool make_move = false) {
	if (cnt == 0)
		return heuristic(mi, mj, hi, hj);
	auto dirs = get_valid_dirs(mi, mj);
	if (dirs.size() == 0)
		return -dfs(hi, hj, mi, mj, cnt - 1) - 1;
	int best_score = -INF;
	vector<int> best_moves;
	for (int dir : dirs) {
		int ti = mi + di[dir];
		int tj = mj + dj[dir];
		char old = a[ti][tj];
		a[ti][tj] = a[mi][mj];
		int score = -dfs(hi, hj, mi + di[dir], mj + dj[dir], (cnt - 1) / dirs.size());
		if (old == 'C')
			score += 2;
		if (score > best_score) {
			best_score = score;
			best_moves.clear();
		}
		if (score == best_score) {
			best_moves.push_back(dir);
		}
		a[ti][tj] = old;
	}
	if (make_move) {
		int dir = best_moves[rand() % best_moves.size()];
		cout << dc[dir] << endl;
	}
	return best_score;
}

bool is_isolated(int i1, int j1, int i2, int j2) {
	static int was[N][N];
	memset(was, 0, sizeof(was));
	queue<pii> q;
	was[i1][j1] = 1;
	was[i2][j2] = 2;
	q.push({i1, j1});
	q.push({i2, j2});
	while (!q.empty()) {
		int i = q.front().first;
		int j = q.front().second;
		q.pop();
		for (int dir : get_valid_dirs(i, j)) {
			int ni = i + di[dir];
			int nj = j + dj[dir];
			if (was[ni][nj] == 0) {
				was[ni][nj] = was[i][j];
				q.push({ni, nj});
			} else if (was[i][j] != was[ni][nj]) {
				return false;
			}
		}
	}
	return true;
}

int main() {
	string s;
	cin >> s;
	char me = s[0];
	char he = 'R' + 'B' - me;
	cin >> n >> n >> m;
	while (true) {
		int mi, mj, hi, hj;
		for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++) {
			cin >> a[i][j];
			if (a[i][j] == me) {
				mi = i;
				mj = j;
			}
			if (a[i][j] == he) {
				hi = i;
				hj = j;
			}
		}
		if (isolated || (isolated = is_isolated(mi, mj, hi, hj)))
			dfs2(mi, mj, 256, true);
		else
			dfs(mi, mj, hi, hj, 512, true);
	}
}