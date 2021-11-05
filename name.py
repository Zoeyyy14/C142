from flask import Flask, jsonify, request
from storage import all_movies,liked_movies,did_not_watch,not_liked_movies
from demographicfiltering import output
from contentfiltering import get_recommandations
app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    movie_data={
        "title":all_movies[0][19],
        "release_date":all_movies[0][13],
        "duration":all_movies[0][15],
        "rating":all_movies[0][20],
        "overview":all_movies[0][19]
    }
    return jsonify({
        "data": movie_data,
        "status": "success"
    })

@app.route("/liked-movie", methods=["POST"])
def liked_movie():
    #all_movies = all_movies[1:]
    movie = all_movies[0]
    liked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-movie", methods=["POST"])
def unliked_movie():
    movie = all_movies[0]
    #all_movies = all_movies[1:]
    not_liked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch():
    movie = all_movies[0]
    #all_movies = all_movies[1:]
    did_not_watch.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular-movie")
def popular_movie():
    movie_data=[]
    for movie in output:
        _d={
            "title":movie[0],
            "release_date":movie[1],
            "duration":movie[2],
            "rating":movie[3],
            "overview":movie[4]
        }
        movie_data.append(_d)
    return jsonify({
         "data": movie_data,
         "status": "success"
    })

@app.route("/recommanded-movie")
def recommanded_movie():
    all_recommanded=[]
    for liked_movie in liked_movies:
        output=get_recommandations(liked_movie[19])
        for data in output:
            all_recommanded.append(data)
    import itertools
    all_recommanded.sort()
    all_recommanded=list(all_recommanded for all_recommanded, _ in itertools.groupby(all_recommanded))
    movie_data=[]
    for recommanded in all_recommanded:
        _d={
            "title":recommanded[0],
            "release_date":recommanded[1],
            "duration":recommanded[2],
            "rating":recommanded[3],
            "overview":recommanded[4]
        }
        movie_data.append(_d)
    return jsonify({
         "data": movie_data,
         "status": "success"
    })
if __name__ == "__main__":
  app.run()