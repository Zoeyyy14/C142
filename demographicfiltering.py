import pandas as pd
import numpy as np
df=pd.read_csv("final.csv")

C=df["vote_average"].mean()
m=df["vote_count"].quantile(0.9)
q_movie=df.copy().loc[df["vote_count"]>=m]

def rating(x,m=m,C=C):
  v=x["vote_count"]
  R=x["vote_average"]
  return ((v/(v+m))*R)+((m/(v+m))*C)
q_movie["score"]=q_movie.apply(rating,axis=1)
q_movie=q_movie.sort_values("score",ascending=False)
output=q_movie[["original_title","poster_link","vote_average","release_date","runtime","overview"]].head(20).values.tolist()