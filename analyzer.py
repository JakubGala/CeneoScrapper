import numpy as np

stars = opinions.stars.value_counts().reindex(np.arange(0,5.5,0.5), fill_value = 0)

stars.plot.bar(color = "red")
plt.title("Gwiazdki")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.savefig("plots/{}.png".format(product_id))
plt.show()
plt.close()

recomm = opinions.recomm.value_counts(dropna = False).sort_index()
recomm.plot.pie(colors = ["red", "green", "blue"])

plt.show()