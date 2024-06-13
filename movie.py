# #python code to recommend movies
# import pickle
# import pandas as pd

# def recommend(movie):
#     movie_index = new_df[new_df['title']==movie].index[0]
#     distance = similarity[movie_index]
#     movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:6]
#     recomended_movies= []

#     for i in movie_list:
#         recomended_movies.append(new_df.iloc[i[0]][1])

#     return recomended_movies
        
    
# var = pickle.load(open('movies_dict.pkl','rb'))
# new_df = pd.DataFrame(var)
# similarity = pickle.load(open('similarity.pkl','rb'))
# new_df = var['title'].values
# print('Movie Recommendation System\n\n')
# user_input = input('Enter a Movie Name to generate recommendations :')
# recommendation = recommend(user_input)
# for i in recommendation:
#     # print(i)
#     print(f'The top 5 recommended movies are:\n{i}')


import streamlit as st