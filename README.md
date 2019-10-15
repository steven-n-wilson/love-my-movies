
# Love my movies

After having our own html, css setup from [Figma UIUX class ](https://www.figma.com/file/sW8aM7yjCGqxB6V3tvn7fw/Homework?node-id=0%3A1)

We are going to reuse this design to have a "Like/Dislike | Recommend/Not Recommend | Love/Hate" my Movies app

---
<!-- TOC -->

- [Love my movies](#love-my-movies)
- [Result](#result)
- [New movies html](#new-movies-html)
- [Some Examples](#some-examples)
  - [Discover Movies](#discover-movies)
  - [Movie Details](#movie-details)
  - [Trending Movies](#trending-movies)

<!-- /TOC -->


# Result

The app will look like this:

![Image](.docs/movies.png)

- You will display the movie poster as an icon. (`poster_path` field)
- Movie Title (`original_title` field)
- Free Field (choose wisely the field you wish to display)
- The movie plot/synopsis (`overview`)
- Two vote buttons (UP/DOWN) which will increase/decrease the vote_count
- Vote Count which will initialize at `vote_count`
- Feel free to modify the layout to add anything you want.


> here only one box is shown, obviously you will work with a variable list of movies.


# New movies html
We are going to use The Movie Database API 3 [TMDd](https://www.themoviedb.org/) to retrieve our initial data.

You better create your own account and respect the request limits, that I why I'm including some `.json` files already.

This is the [API's full URL](https://developers.themoviedb.org/3)

# Some Examples

## [Discover Movies](https://developers.themoviedb.org/3/discover/movie-discover)

The Request URL was

```bash
https://api.themoviedb.org/3/discover/movie?api_key=<<api_key>>&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1
```

> I replaced <<api_key>> with my own API_KEY

Which resulted in [discover_movies.json](discover_movies.json)

## [Movie Details](https://developers.themoviedb.org/3/movies/get-movie-details)

The Request URL was

```bash
https://api.themoviedb.org/3/movie/475557?api_key=<<api_key>>
```

Which gave me [joker_movie_details.json](joker_movie_details.json)

## [Trending Movies](https://developers.themoviedb.org/3/trending/get-trending)

Request URL was
```bash
https://api.themoviedb.org/3/trending/movie/week?api_key=<api_key>>
```

Which gave me [trending_movies.json](trending_movies.json)
