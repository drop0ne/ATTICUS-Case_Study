from pathlib import Path
import math
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
d = pd.read_csv(ROOT / "data" / "problem_scores.csv")
att = d["ATTICUS_score"].to_numpy()
sol = d["Sol_raw_score"].to_numpy()
delta = att - sol

print("ATTICUS mean:", att.mean())
print("Sol raw mean:", sol.mean())
print("Mean paired delta:", delta.mean())
print("Median paired delta:", np.median(delta))
print("Wins:", (delta > 0).sum(), "-", (delta < 0).sum())

n = len(delta)
sd = delta.std(ddof=1)
se = sd / math.sqrt(n)
t = delta.mean() / se
p_t = 2 * (1 - stats.t.cdf(abs(t), df=n-1))
ci = stats.t.interval(.95, df=n-1, loc=delta.mean(), scale=se)
print("paired t p:", p_t)
print("95% t CI:", ci)
print("Wilcoxon:", stats.wilcoxon(delta, method="exact"))
print("Cohen dz:", delta.mean() / sd)
print("Mean delta excluding P09:", np.delete(delta, 8).mean())
print("10% trimmed mean:", stats.trim_mean(delta, .1))

fig, ax = plt.subplots(figsize=(10,5))
ax.bar(d["problem"], delta)
ax.axhline(0, linewidth=1)
ax.set_ylabel("ATTICUS − Sol raw score")
ax.set_xlabel("Problem")
ax.set_title("Paired score difference by problem")
fig.tight_layout()
fig.savefig(ROOT/"figures"/"atticus_sol_delta_by_problem_reproduced.png", dpi=180)
