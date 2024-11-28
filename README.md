# Netflix_EDA

## 📝 Introduction 
Netflix is a popular streaming service that offers a vast catalog of movies, TV shows, and original contents.This project focuses on analyzing data related to the content available on the Netflix platform. As a junior data analyst, I will use the Netflix dataset to explore the dataset to identify trends in types of productions, countries of origin, genre popularity, and relationships between creators and actors.

## 💡 Objective
In this project, we’ll be working with a Netflix dataset to load, clean, analyze, and visualize the data. We’ll use Python libraries like Pandas, Matplotlib, and Seaborn to get the job done. The main goal is to dig into the dataset and uncover some interesting insights.

## ⚙ Approach/Steps
### 1. Ask
**Business Task -**  to uncover key trends within the dataset and prepare visualizations and insights that could serve as a foundation for further research into the Netflix streaming platform.

As a junior data analyst, my focus is on answering the following questions:-
> 1. What is the distribution of content types on the platform?
> 2. Which countries dominate in content production?
> 3. Which directors appear most frequently in Netflix productions?
> 4. What are the most popular genres and their co-occurrence patterns?
> 5. How does the release year compare to the date the content was added to the platform?

### 2. Prepare
#### 🔗 Quick Links
**Data Source:** [NETFLIX](https://www.kaggle.com/datasets/shivamb/netflix-shows/data) <br>

**Tools:** <br>
- Data Wrangling - Excel & Python.
- Exploratory Data analysis - Python
- Data visualization - [Tableau](https://public.tableau.com/app/profile/sangeet.banik/viz/Netflix_EDA/Dashboard1)

### 3. Process
The original dataset has 8,807 rows and 12 columns. To get it ready for analysis, a few steps were taken to clean and prepare the data.

| **No.**|  **Variable**       |  **Description**                                        |
|--------|------------------   | --------------------------------------------------------|
| 1      | show_id             | Unique ID assigned to each show                         |
| 2      | type                | Movie and TV Show                                       |
| 3      | title               | Title o the show                                        |
| 4      | director            | Name of Director                                        |
| 5      | cast                | Name of the actors                                      |
| 6      | country             | Production country name                                 |
| 7      | date_added          | Date when the content was added on Netflix              |
| 8      | release_year        | Year when the content was released                      |
| 9      | rating              | Show rating                                             |
| 10     | duration            | Duration o the show                                     |
| 11     | listed_in           | Genres of the show                                      |
| 12     | description         | Details of the show                                     |          

#### Data Wrangling
My initial step was to check the individual tables one by one using Excel to determine the **data type** and to  uncover any **missing values, outliers, inconsistencies, and errors** within the tables. 
- **Missing values** : Some columns, such as *director, cast, country, date_added, rating, and duration*, contain missing values.
- **Inconsistency**  : The country column often includes multiple countries for a single title. To analyze content by production country more effectively, we applied a transformation.

### 4. Analyze
> 1. What is the distribution of content types on the platform?
#### Distribution of Content Types on Netflix
![output](https://github.com/user-attachments/assets/17ac057e-b67f-444c-9629-1c55c09c16d4)

- **Movies** dominate the platform, making up approximately **69.6% (6131 contents)** of all contents.
- **TV Shows** account for the remaining **30.4% (2676 contents)**.

> 2. Which countries dominate in content production?
#### Top countries that produce contents on Netlfix
![countries](https://github.com/user-attachments/assets/215ebcfe-987e-4666-9765-d89be086dd0d)

-The Top countries are:-
  - United States
  - India
  - United Kingdom
  - Canada
  - France
  - Japan
  - South Korea
  - Germany
  - Mexico
  - Spain

![countries_compare](https://github.com/user-attachments/assets/801ca0e4-153a-498d-a7e1-39b573ee2f5a)


- Interestingly, there are some countries where TV Shows dominate over Movies. These include:
  - Japan
  - South Korea
  - Taiwan
  - Colombia
  - Singapore 




> 3. Which directors appear most frequently in Netflix productions?
#### Top 10 Directors on Netflix
![directors](https://github.com/user-attachments/assets/b2be27c6-e3f2-447e-ba9d-8982922f452a)

- The most frequently featured directors and their contributions to Netflix’s catalog.
  - Rajiv Chilaka
  - Raúl Campos
  - Jan Suter
  - Marcus Raboy
  - Suhas Kadav
  - Jay Karas
  - Cathy Garcia-Molina
  - Martin Scorsese
  - Jay Chapman
  - Youssef Chahine

> 4. What are the most popular genres?

#### Most common Genres on Netflix
![Genres](https://github.com/user-attachments/assets/55a98c2c-34fa-43c4-8a65-70b668ec3d79)


- The most frquently occurring genres on Netflix are :-
  - International Movies
  - Dramas
  - Comedies
  - International TV Shows
  - Documentaries
  - Action & Adventure.


> 5. How does the release year compare to the date the content was added to the platform?
#### Distribution of Release-Add Differences with More Than 100 Titles
![distribution of relaese add diff](https://github.com/user-attachments/assets/ee98f793-f62f-4875-b9e0-7800515eaf35)

**Immediate Access:** A large number of titles, especially Netflix Originals, are made available on the platform in the same year they’re produced, showcasing Netflix’s emphasis on delivering fresh and original content.

**Timeless Classics:** The platform also adds many older titles, enhancing its library with a rich variety of classic and diverse options for viewers.

#### Trend of content released over years
![trend_years](https://github.com/user-attachments/assets/ff4073af-454b-4f1c-834d-f6d51fe7ca23)

- Since 2015, there has been a marked increase in the volume of content added.
- On 2019 and 2020, there has been a notable surge.

#### Trend of content added over month
![trend_movies](https://github.com/user-attachments/assets/b200b7d9-f113-41e1-aef7-d2f7361b844b)

- The number of added contents seems to follow a seasonal trend.
- **July** and **December** are the months with most addition of contents.

> 6. What are the dominating Show Ratings?
#### Distribution of content Ratings
![ratings](https://github.com/user-attachments/assets/e65789a8-915b-4f73-aa72-d0aa01280fd2)

- Overall Distribution:
  - TV-MA leads the ratings, making up a significant portion of Netflix’s catalog.
  - TV-14 and TV-PG follow, showing that Netflix appeals to a wide audience but primarily targets mature viewers.
#### Distibution of Ratings by Type
![movie_and_TV_ratings](https://github.com/user-attachments/assets/5924db35-1342-48b7-92d1-5ee2507ff4f2)


- Ratings by Type:
  - Movies tend to have a broader range of ratings, including R and PG-13, reflecting traditional film ratings.
  - TV Shows are dominated by TV-MA and TV-14, highlighting a focus on episodic content for adults and teens.

### 5. Share
![NETFLIX dasboard](https://github.com/user-attachments/assets/552d5066-ef60-4c3d-9951-351bb3030d33)



View [NETFLIX Dashboard](https://public.tableau.com/app/profile/sangeet.banik/viz/Netflix_EDA/Dashboard1).

**Insights**
> 1. *Movies* dominate the platform, making up approximately *69.6%* of all titles, whereas, *TV Shows* account for the remaining *30.4%*.
> 2. Majority of Netflix content originates from a few key countries and are mostly *Movies*. But, interestingly, there are some countries where *TV Shows* dominate over Movies. This indicates that in many highly developed Asian countries, there is a stronger focus on creating TV shows, likely driven by cultural preferences and a commitment to catering to local markets.
> 3. Netflix stays competitive in the streaming market by quickly adding titles right after production, especially Netflix Originals.
> 4. By featuring older titles, Netflix caters to a wide audience with diverse preferences.
> 5. Netflix's catalog focuses on mature audiences, with *TV-MA* dominating. However, it offers diverse content for all ages. Regional ratings like NR deserve deeper analysis for global market insights.
> 6. The popularity of *International Movies* and *TV Shows* highlights Netflix's efforts to grow its global audience.





  
