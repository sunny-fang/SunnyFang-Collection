# Import dataset 
midwest = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")

# Prepare Data 
# Create as many colors as there are unique midwest['category']
state_list = np.unique(midwest['state'])
colors = [plt.cm.tab10(i/float(len(state_list)-1)) for i in range(len(state_list))]

# Draw Plot for Each Category
plt.figure(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')

for i, state_name in enumerate(state_list):
    plt.scatter('popwhite', 'popblack', 
                data=midwest.loc[midwest.state==state_name, :], 
                s=20, c=colors[i], label=str(state_name))

# Decorations
plt.gca().set(xlim=(0, 70000), ylim=(0, 7000),
              xlabel='WhitePop', ylabel='BlackPop')

plt.xticks(fontsize=12); plt.yticks(fontsize=12)
plt.title("Scatterplot of Midwest Area vs Population", fontsize=22)
plt.legend(fontsize=12)    
plt.show()