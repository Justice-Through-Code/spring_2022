# Spotify Challenge

Before getting started with the challenge, let's peek into all the tables in the Spotify database:

### Artists

| ID  | Name        |
| --- | ----------- |
| 1   | The Beatles |
| 2   | The Beetles |

### Albums

| ID  | Name       | YearReleased |
| --- | ---------- | ------------ |
| 1   | Abbey Road | 1969         |
| 2   | Let It Be  | 1970         |
| 3   | Help!      | 1965         |
| 4   | "1"        | 2000         |
| 5   | 125 Street | 2021         |

### Songs

| ID  | Song               | ArtistId | AlbumId |
| --- | ------------------ | -------- | ------- |
| 1   | Here Comes the Sun | 1        | 1       |
| 2   | Come Together      | 1        | 1       |
| 3   | Let It Be          | 1        | 2       |
| 4   | Yesterday          | 1        | 3       |
| 5   | Hey Jude           | 1        | 4       |
| 6   | Hey JTC            | 2        | 5       |

### Members

| ID  | Name   | ArtistID |
| --- | ------ | -------- |
| 1   | John   | 1        |
| 2   | Paul   | 1        |
| 3   | Ringo  | 1        |
| 4   | George | 1        |
| 2   | Paul   | 3        |

### ArtistMembers

| ID  | MemberID | ArtistID |
| --- | -------- | -------- |
| 1   | 2        | 1        |
| 2   | 2        | 3        |

## We're in great shape but we're missing a key ingredient: Musical Genres!

In the `Songs` table we've added another column called `Genre`.

### Songs

| ID  | Song               | ArtistId | AlbumId | Genre   |
| --- | ------------------ | -------- | ------- | ------- |
| 1   | Here Comes the Sun | 1        | 1       | Rock    |
| 2   | Come Together      | 1        | 1       | Rock    |
| 3   | Let It Be          | 1        | 2       | Rock    |
| 4   | Yesterday          | 1        | 3       | Rock    |
| 5   | Hey Jude           | 1        | 4       | Rock    |
| 6   | Hey JTC            | 2        | 5       | Hip Hop |

You will notice that we're repeating `Rock` a number of times. This may not seem like a problem but consider the following:

-   If we had to rename `Rock` and our `Songs` table contained a **million** `Rock` songs, the time to complete such a change would be very long!
-   If we also wanted to assign a genre to an album in the `Albums` table in a similar way, we would have repeated data in multiple tables

# Question 1

a) Briefly describe a better way of modeling genre data in the database to avoid some of the issues listed above. You can assume for the sake of simplicity there can be only one genre per song.
**Tip**: _Before answering, use pen and paper to sketch out the possibilities. Does your solution involve new table(s), column(s), row(s), relationship(s)?_

b) What relationship best describes how genre relates to songs in your answer to Question 1a?

# Question 2

What changes would you make to the modeling of genre data if we could assign more than one genre to a song?
