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
#### Distribution of Content Types on Netflix
![output](https://github.com/user-attachments/assets/17ac057e-b67f-444c-9629-1c55c09c16d4)

- **Movies** dominate the platform, making up approximately **69.6% (6131 contents)** of all contents.
- **TV Shows** account for the remaining **30.4% (2676 contents)**.

#### Most common Genres on Netflix
![Genres](https://github.com/user-attachments/assets/8dcad298-1ea8-40b8-b810-57b356bbedbf)

- The most frquently occurring genres on Netflix are :- International Movies, Dramas, Comedies, Action & Adventure, and Documentaries.

#### Trend of content released over years
![trend_years](https://github.com/user-attachments/assets/ff4073af-454b-4f1c-834d-f6d51fe7ca23)

- Since 2015, there has been a marked increase in the volume of content added.
- On 2019 and 2020, there has been a notable surge.

#### Trend of content added over month
![trend_movies](https://github.com/user-attachments/assets/b200b7d9-f113-41e1-aef7-d2f7361b844b)

- The number of added contents seems to follow a seasonal trend.
- **July** and **December** are the months with most addition of contents.





  




  
