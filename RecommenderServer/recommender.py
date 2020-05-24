import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#helper functions
def get_title_from_index(df,index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(df,title):
    return df[df.title == title]["index"].values[0]

#Read csv file
def read_csv_file():
    return pd.read_csv("datasets/movie_dataset.csv")

def combine_features(row):
    try:
        return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']
    except:
        print( "Error:", row)

def compute_result(brand):
    df = read_csv_file()

    #Select features
    features = ['keywords', 'cast', 'genres', 'director']

    #Create column in dataframe which combines all selected features
    for feature in features:
        df[feature] = df[feature].fillna('')

    df["combined_features"] = df.apply(combine_features,axis=1)

    #Create count matrix from new combined column
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df["combined_features"])

    #Compute the cosine similarity based on the count_matrix
    cosine_sim = cosine_similarity(count_matrix)

    brand_user_likes = brand

    #Get index of this brand from its name
    movie_index = get_index_from_title(df,brand_user_likes)

    #Get similar brands
    similar_brands = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_brands = sorted(similar_brands,key=lambda x: x[1],reverse=True)
    # Print sorted movies
    #i = 0
    #for movie in sorted_similar_brands:
    #    print(get_title_from_index(df,movie[0]))
    #    i = i + 1
    #    if i > 50:
    #        break

    #build sublist
    movie_recommendations = []
    for movie in sorted_similar_brands[0:10]:
        movie_recommendations.append(get_title_from_index(df,movie[0]))

    return movie_recommendations