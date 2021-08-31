import numpy as np 
import pandas as pd 
# import matplotlib.pyplot as plt 
# import seaborn as sb #requires extension

# %matplotlib inline

pokemon = pd.read_csv('/content/pokemon.csv')
print(pokemon.shape)#prints no. of rows and columns in file
pokemon.head()#gives first 5 instanses
print(pokemon)#gives first five and last five not whole if its big
sb.countplot(data = pokemon, x = 'generation_id'); #generation id is is a column in the csv file, ; is given because if not goven it prints a pointer at top which is not what we need in out put
#if we dont want coloured bar graph
base_color = sc.colour_palette()[6]#there is a sequence of colors for which no.s are given
sb.countplot(data = pokemon, x = 'generation_id', color= base_color, order= gen_order);
gen_order = pokemon['generaion_id'].value_counts().index#gives the no. of apperances of each data in descending order
base_color=sb.colour_palette([2])
sb.countplot(data = 'type_1', color = base_color)
plt.xticks(rotation=90);#plotting names of type on xa axis vertically to avoid crowding
pokemon.isna()#to chk the missing data, it gives true where data is missing
pokemon.isna().sum()#gives the sum  that how many null values i.e missing values are there in a column
na_counts = pokemon.isna().sum()
base_color = sb.color_palette()[0]
sb.barplot(na_counts.index.values , na_counts, base_color = base_color)
plt.xticks(rotation=90); 


#***********PIE CHART

import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sb

# %matplotlib inline

df = pd.read_csv('/content/pokemon.csv')
print(df.shape)
df.head()
sorted_counts = df['generation_id'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,
        counterclock = False);
plt.axis('square');

#******this give piechart with hole in center
sorted_counts = df['generation_id'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,

        counterclock = False, wedgeprops = {'width' : 0.4});
plt.axis('square');

#*****HISTOGRAM
plt.hist(data = df, x = 'speed')
bins = np.arange(0, df['speed'].max()+1, 5)
plt.hist(data = df, x = 'speed', bins = bins)#this bins define the interval to  taek on x axis 
bin_edges = np.arange(0, df['speed'].max()+1, 5)
sb.distplot(df['speed'], bins = bin_edges, kde = False,
            hist_kws = {'alpha' : 1});
#alpha iss for brihtness or saturation


