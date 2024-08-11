sns.catplot(x="embark_town",hue="survived",col="pclass",data=df,kind="count",palette="Set2")
plt.show()