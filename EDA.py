-- What is the distribution of content types on the platform?
# Distribution of types of Contents on Netflix
print("Total contents uploaded :", df['type'].count())
group_types = df.groupby('type').size().reset_index(name='count')
print(group_types)

sns.countplot(x='type', hue = 'type', data=df, palette=sns.color_palette("colorblind", n_colors=2))
plt.title('Distribution of types of contents', fontsize=15)
plt.xlabel('Content Type', fontsize=12)
plt.ylabel('Count', fontsize=12)

ax = plt.gca()
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2., height + 0.1,
            '{:1.0f}'.format(height), ha="center") 
plt.show()


-- Which countries dominate in content production?
# Distribution of countries with most content
df_exploded_country = df.copy()
df_exploded_country.dropna(subset= ['country'], inplace= True)
df_exploded_country['country'] = df_exploded_country['country'].str.split(', ').apply(lambda x: [country.strip() for country in x])
df_exploded_country = df_exploded_country.explode('country')

country_counts = df_exploded_country['country'].value_counts().reset_index()
top_15_country = country_counts.head(15)
top_15_country

#Plot for top 10 countries providing contents
plt.figure(figsize=(12,6))
sns.barplot(x= 'country', hue='country',y = 'count', data= top_15_country )
plt.title('Distribution of content across countries ')
plt.xlabel("countries")
plt.xticks(rotation = 45 , ha  = 'right')
plt.ylabel("counts")

ax = plt.gca()
for p in  ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2., height + 0.1,
            '{:1.0f}'.format(height), ha="center") 
 plt.show()

type_counts_by_country = df_exploded_country.groupby(['country', 'type']).size().unstack(fill_value=0)
type_counts_by_country.columns = ['Movies', 'TV Shows']
type_counts_by_country = type_counts_by_country.reset_index()
type_counts_by_country['Total'] = type_counts_by_country['Movies'] + type_counts_by_country['TV Shows']
type_counts_by_country_filtered = type_counts_by_country.sort_values(by='Total', ascending=False).reset_index(drop=True)
type_counts_by_country_filtered = type_counts_by_country_filtered[type_counts_by_country_filtered['TV Shows'] > type_counts_by_country_filtered['Movies']]

melted_df = pd.melt(type_counts_by_country_filtered, id_vars='country', value_vars=['Movies', 'TV Shows'], var_name='Content Type', value_name='Count')

plt.figure(figsize=(14, 6))
sns.barplot(x='country', y='Count', hue='Content Type', data=melted_df , palette= sns.color_palette('pastel', n_colors=2))

ax = plt.gca()
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., height+0.1, '{:.1f}'.format(height), ha='center')

plt.title('The participation of Movies and TV Shows for selected countries')
plt.xlabel('Country')
plt.ylabel('Total Titles')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Types')
plt.show()


-- Which directors appear most frequently in Netflix productions?
#Top 15 directors
df_exploded_directors = df.copy()
df_exploded_directors.dropna(subset= ['director'], inplace= True)
df_exploded_directors['director'] = df_exploded_directors['director'].str.split(', ').apply(lambda x: [director.strip() for director in x])
df_exploded_directors = df_exploded_directors.explode('director')

director_counts = df_exploded_directors['director'].value_counts().reset_index()
top_15_director = director_counts.head(15)
top_15_director

plt.figure(figsize=(12,6))
sns.barplot(x= 'director', y = 'count', hue= 'director' , data= top_15_director, legend= False)
plt.title("Top directors")
plt.xlabel(" Directors")
plt.xticks(rotation = 45, ha = 'right')
plt.ylabel("Count")

ax = plt.gca()
for p in ax.patches:
   height = p.get_height()
   ax.text(p.get_x()+p.get_width()/2.0, height+0.1, '{:1.0f}'.format(height), ha = 'center')
    
plt.show()


-- What are the most popular genres and their co-occurrence patterns?
# Most common genres on Netflix

df_exploded_genres = df.copy()
df_exploded_genres['listed_in'] = df_exploded_genres['listed_in'].str.split(', ').apply(lambda x: [genre.strip() for genre in x])
df_exploded_genres = df_exploded_genres.explode('listed_in')

genre_counts = df_exploded_genres['listed_in'].value_counts().reset_index()
top_15_genres = genre_counts.head(15)
top_15_genres

plt.figure(figsize=(12,6))
sns.barplot(y='listed_in',x='count',data=top_15_genres, hue = 'listed_in' , palette=sns.color_palette("colorblind", n_colors=15))
plt.title('Most Common Genres on Netflix')
plt.xlabel('Count')
plt.ylabel('Genre')

ax = plt.gca()
for p in ax.patches:
    width = p.get_width()  # Get the width (value) of the bar
    height = p.get_y() + p.get_height() / 2.  # Get the center y-coordinate of the bar
    ax.text(width + 0.1, height,  # Annotate slightly to the right of the bar
            '{:1.0f}'.format(width),  # Display the value (width)
            va='center',  # Vertical alignment at the center of the bar
            ha='left')   
plt.show()


-- How does the release year compare to the date the content was added to the platform?
df_release_add = df[['release_year', 'date_added']].copy()
df_release_add.dropna(inplace=True)
df_release_add.head()
df_release_add['year_added'] = df_release_add['date_added'].str[-4:].astype('int64')
df_release_add.drop('date_added', axis=1, inplace=True)
df_release_add['release_add_diff'] = df_release_add['year_added'] - df_release_add['release_year']
df_release_add.head()
same_year_added_released = (df_release_add['release_year'] == df_release_add['year_added']).sum()
same_year_added_released
df_release_add_diff = df_release_add['release_add_diff'].value_counts().reset_index()
df_release_add_diff[df_release_add_diff['count'] > 100]['count'].sum()
filtered_data = df_release_add_diff[df_release_add_diff['count'] > 100]

plt.figure(figsize=(12, 6))
plt.bar(filtered_data['release_add_diff'], filtered_data['count'], edgecolor='black')

ax = plt.gca()
for p in ax.patches:
    height = p.get_height()
    plt.text(p.get_x() + p.get_width() / 2, height, f'{int(height)}', 
             ha='center', va='bottom', fontsize=10)

x_ticks = np.arange(filtered_data['release_add_diff'].min(), filtered_data['release_add_diff'].max() + 1)
plt.xticks(x_ticks, fontsize=10, rotation=0)
plt.title('Distribution of Release-Add Differences with More Than 100 Titles', fontsize=14)
plt.xlabel('Years Between Release and Addition', fontsize=12)
plt.ylabel('Number of Titles', fontsize=12)
plt.tight_layout()
plt.show()

#Trend of content release over year

df["date_added"] = df["date_added"].astype("datetime64[ns]")

df['year'] = df['date_added'].dt.year
df['month'] = df['date_added'].dt.month

year_count = df['year'].value_counts()
print(year_count)

yearly_movie_releases=df[df['type']=='Movie']['year'].value_counts().sort_index()
yearly_series_releases=df[df['type']=='TV Show']['year'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
plt.plot(yearly_movie_releases.index, yearly_movie_releases.values, label='Movies')
plt.plot(yearly_series_releases.index, yearly_series_releases.values, label='TV Shows')
plt.xlabel("Years")
plt.ylabel("Frequency of releases")
plt.grid(True)
plt.suptitle("Yearly releases of Movies and TV Shows on Netflix")
plt.legend()

plt.figure(figsize=(12, 6))
sns.countplot(x= 'year' , hue = 'type', data= df)
plt.title("Trend of adding content over time")
plt.xlabel("Years")
plt.xticks(rotation = 45)
plt.ylabel("count")

ax = plt.gca()
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2, height + 0.1, 
            '{:1.0f}'.format(height), ha = 'center')

plt.show()


#Trend of content release over months

monthly_movie_release = df[df['type']=='Movie']['month'].value_counts().sort_index()
monthly_series_release = df[df['type']=='TV Show']['month'].value_counts().sort_index()

plt.figure(figsize=(12,6))
plt.plot(monthly_movie_release.index, monthly_movie_release.values, label = "Movies")
plt.plot(monthly_series_release.index, monthly_series_release.values, label = "TV shows")
plt.xlabel("Months")
plt.ylabel("Number of releases")
plt.xticks(range(1,13),['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'])
plt.legend
plt.suptitle("Monthly release of Contents")


plt.show()


-- What are the dominating Show Ratings?
# Distribution of Ratings
count_ratings = df.groupby('rating').size().reset_index(name='count').sort_values(by = "count",ascending= False)
print(count_ratings)

plt.figure(figsize=(12,6))
sns.barplot(x = 'rating',
            y = 'count',
           hue = 'rating',
           data = count_ratings)
plt.title("Distribution of ratings")
plt.xlabel("Type of ratings")
plt.xticks(rotation = 45)
plt.ylabel("count")
ax = plt.gca()
for p in ax.patches:
   height = p.get_height()
   ax.text(p.get_x()+p.get_width()/2.0, height+0.1, '{:1.0f}'.format(height), ha = 'center')
plt.show()




movie_rating = df[df['type']=='Movie']['rating'].value_counts().sort_values(ascending= False)
print(movie_rating)
series_rating = df[df['type']=='TV Show']['rating'].value_counts().sort_values(ascending= False)
print(series_rating)

fig, ax = plt.subplots(1,2,figsize=(20,10))
sns.barplot(x = movie_rating.index,
            y = movie_rating.values,
           hue = movie_rating.index,
           ax=ax[0])
ax[0].set_title("Distribution of Movie ratings")
ax[0].set_xlabel("Type of ratings")
ax[0].tick_params(axis='x', rotation=45)
ax[0].set_ylabel("count")

for p in ax[0].patches:
   height = p.get_height()
   ax[0].text(p.get_x()+p.get_width()/2.0, height+0.1, '{:1.0f}'.format(height), ha = 'center')



sns.barplot(x = series_rating.index,
            y = series_rating.values,
           hue = series_rating.index,
           ax=ax[1])
ax[1].set_title("Distribution of TV shows ratings")
ax[1].set_xlabel("Type of ratings")
ax[1].tick_params(axis='x', rotation=45)
ax[1].set_ylabel("count")

for p in ax[1].patches:
   height = p.get_height()
   ax[1].text(p.get_x()+p.get_width()/2.0, height+0.1, '{:1.0f}'.format(height), ha="center")
plt.show()




