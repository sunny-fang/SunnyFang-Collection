# Scatter plot with linear regression line of best fit


# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
df_select = df.loc[df.cyl.isin([4,8]), :]

# Plot
sns.set_style("white")
#gridobj = sns.lmplot(x="displ", y="hwy", hue="cyl", data=df_select, 
#                     height=7, aspect=1.6, robust=True, palette='tab10', 
#                     scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))
gridobj = sns.lmplot(x="displ", y="hwy", hue="cyl", data=df_select, 
                     aspect=1.6, robust=True, palette='tab10', 
                     scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))

# Decorations
gridobj.set(xlim=(0.5, 7.5), ylim=(0, 50))
plt.title("Scatterplot with line of best fit grouped by number of cylinders", fontsize=20)
plt.show()