import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# データを読み込む
data = pd.read_csv('tdpi_n22080_s.csv')

# 相関行列を計算
correlation_matrix = data[['Ex', 'Ag', 'Co', 'Ne', 'Op']].corr()

# ヒートマップを作成
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Heatmap of personality data')
plt.savefig('heatmap_of_personality_data.png')
plt.show()

# 散布図マトリックスをカスタマイズして作成（回帰直線付き）
pairplot_fig = sns.pairplot(data[['Ex', 'Ag', 'Co', 'Ne', 'Op']], kind='reg', plot_kws={'line_kws':{'color':'red'}, 'scatter_kws': {'alpha': 0.1, 's': 10}})
pairplot_fig.fig.suptitle('Scatter Plot Matrix of personality data', y=1.02)
pairplot_fig.savefig('scatter_plot_matrix_of_personality_data.png')
plt.show()
