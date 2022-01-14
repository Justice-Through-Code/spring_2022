# Outline

We're going to learn how to:

-   Structure relational databases
-   Save data in a database in a way that's easy to understand
-   Query data from a database using basic Structured Query Language (SQL)

# How do web applications save data?

-   When web applications need to store data, they write the data to a database
-   Once the data is in the database, we can query it later to find the information we need
-   If the database is well-organized, it's easy to add new records, update existing records, and write queries for
    the information we need
-   If the database is poorly organized, all of those tasks become more difficult

# An example: Spotify / Apple Music

<img width="1341" alt="image" src="https://user-images.githubusercontent.com/34491412/135902782-fa2dc870-ee90-40c4-86fb-efb4691dec1b.png">

-   The data behind Spotify has a structure. There are:
    -   Songs
    -   Artists
    -   Albums
-   There is a lot more data/details that make up Spotify, but these are the basics
-   Displayed simply, here's how we might store information about Beatles songs:

| Song               | Artist      | Album      |
| ------------------ | ----------- | ---------- |
| Here Comes the Sun | The Beatles | Abbey Road |
| Come Together      | The Beatles | Abbey Road |
| Let It Be          | The Beatles | Let It Be  |
| Yesterday          | The Beatles | Help!      |
| Hey Jude           | The Beatles | "1"        |

<!--
# One Option: Document-based Storage

- For a simple application, we might store the data directly in the format above without changing it at all
- Storing data directly all together is called document-based storage
- There are some websites that use document-based storage successfully! But we'll look at the limitations of
  document-based databases and why most websites use other approaches
- You might hear about technologies like MongoDB or terms like "NoSQL" to describe document-based databases

# The Challenges of Document-based Approaches


Document-based storage comes with limitations:
- If The Beatles change their name to `The Beetles`, I have to query and update each record
  individually in order to update the Artist name
- What if I want to add more details to my Song list? Like `Year Released: 1969` or `Band Members: John, Paul,
  Ringo, & George`? Using document-based storage, I'd have to update each Song one-by-one.
- The Beatles wrote nearly 200 songs! That's a lot of documents I have to update!

For applications of any serious complexity, document-based storage becomes a challenge because it makes it
difficult to query, update, and add information.
-->

## New requirements

Web applications are always evolving, consider these new requirements that might affect how we store data in our database:

-   Artist name change to "The Beetles"
    -   Update every row where `Artist = The Beatles` to "The Beetles"
-   New artist with same name
    -   How do you differentiate artists when adding, updating rows?

# Key insight: Create relationships between objects

-   `The Beatles` are just one band. If they change their name or we need to update the band members, we should
    only need to update `The Beatles` and then the changes should apply everywhere.
-   We can make that possible using relationships between various types of objects in our database.

## Creating an "Artists" table in our database

Imagine we have a separate table in our database for Artists:

| Name        |
| ----------- |
| The Beatles |

Now, let's give each Artist its own unique ID. Using unique IDs is a good practice so that we always have a
unique key to identify a given record in our database:

### Artists

| ID  | Name        |
| --- | ----------- |
| 1   | The Beatles |
| 2   | The Beetles |

## Adding a Foreign Key to the Artists table

Next, in our Songs table, let's replace all our references to `The Beatles` with `Artist #1`:

| Song               | ArtistId | Album      |
| ------------------ | -------- | ---------- |
| Here Comes the Sun | 1        | Abbey Road |
| Come Together      | 1        | Abbey Road |
| Let It Be          | 1        | Let It Be  |
| Yesterday          | 1        | Help!      |
| Hey Jude           | 1        | "1"        |
| Hey JTC            | 2        | 125 Street |

Finally, since it's best practice, let's give each song a unique ID as well:

### Songs

| ID  | Song               | ArtistId | Album      |
| --- | ------------------ | -------- | ---------- |
| 1   | Here Comes the Sun | 1        | Abbey Road |
| 2   | Come Together      | 1        | Abbey Road |
| 3   | Let It Be          | 1        | Let It Be  |
| 4   | Yesterday          | 1        | Help!      |
| 5   | Hey Jude           | 1        | "1"        |
| 6   | Hey JTC            | 2        | 125 Street |

-   When we use an ID to refer to an object in a different table, that ID is called a "Foreign Key"
-   Now, when we need to update `The Beatles` we only need to make a single update to the `Artists` table.
-   Since the `Songs` table uses foreign keys, all of the references to `Artist #1` point to the correct,
    current version of `The Beatles` always!

# Relational Databases, defined

-   This pattern of using relationships between objects in a database is the key insight behind Relational
    Databases
-   Relational databases use the relationships between objects to make information easier to query and maintain
-   They require fewer queries in order to update data than document-based databases
-   Relational databases power the majority of the internet, including the world's biggest websites

# You should know...

-   A system used to maintain relational databases is a relational database management system (RDBMS)
-   Popular RDBMS technologies:
    -   MySQL
    -   PostgresSQL
    -   Microsoft SQL Server
-   Many relational database systems have an option of using the SQL (Structured Query Language) for querying and maintaining the database
-   SQL is its own programming language for accessing data. We won't worry about learning the details of SQL in
    this course, but learning SQL can be very valuable for backend or data-intensive jobs.

# Back to Spotify: What other relationships exist?

Looking at our `Songs` table, are there other objects we could separate into their own tables?

| ID  | Song               | ArtistId | Album      |
| --- | ------------------ | -------- | ---------- |
| 1   | Here Comes the Sun | 1        | Abbey Road |
| 2   | Come Together      | 1        | Abbey Road |
| 3   | Let It Be          | 1        | Let It Be  |
| 4   | Yesterday          | 1        | Help!      |
| 5   | Hey Jude           | 1        | "1"        |

-   The `Album` column seems like another good candidate to change into its own table.
-   What if we need to update an album name or want to add details about the release date to the Album?
-   Let's move Albums to their own table and update the `Songs` table:

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

### Artists

| ID  | Name        |
| --- | ----------- |
| 1   | The Beetles |
| 2   | The Beetles |

# One-to-many relationship

The relationships we've created between tables so far are called one-to-many relationships:

-   One row in the `Artists` table is referenced in multiple rows in the `Songs` table using `ArtistId` foreign key
-   One row in the `Albums` table is referenced in multiple rows in the `Songs` table using `AlbumId` foreign key

# Many-to-many relationship

## New requirements

Keeping track of members. For e.g., The Beatles has four members.

At first glance this might seem like another one-to-many relationship but here's the catch: Paul is also a member of Wings.

### Members

| ID  | Name   |
| --- | ------ |
| 1   | John   |
| 2   | Paul   |
| 3   | Ringo  |
| 4   | George |

### Artists

| ID  | Name        |
| --- | ----------- |
| 1   | The Beetles |
| 2   | The Beetles |
| 3   | Wings       |

Trying to `ArtistID #3` to `Paul` repeat `ID` and `Name` from our original entry

### Members

| ID  | Name   | ArtistID |
| --- | ------ | -------- |
| 1   | John   | 1        |
| 2   | Paul   | 1        |
| 3   | Ringo  | 1        |
| 4   | George | 1        |
| 2   | Paul   | 3        |

This is known as a many-to-many relationship. We can solve this by creating a `ArtistMember`:

### ArtistMember

| ID  | MemberID | ArtistID |
| --- | -------- | -------- |
| 1   | 2        | 1        |
| 2   | 2        | 3        |

We have essentially broken the many-to-many relationships into two one-to-many relationships!

# Relationships make things easier & harder

-   When you're designing any application for the first time, you'll have to think carefully about the problem
    and how you want to structure the underlying data
-   If you structure the relationships in your database poorly, it can be difficult to extend your data model
    when new requirements arise for your application
-   A large part of a backend engineer's job is thinking about how to store data safely and effectively in a way
    that's both easy to query and easy to extend when the app has new requirements

# How do we query songs?

While we won't get into the details of SQL in this course, it's useful to see what SQL looks like in order to
query for information in a relational database.

To query for `Songs`, we can perform a `SELECT` operation:

```sql
SELECT ID, Song, ArtistId, AlbumId FROM songs;
```

| ID  | Song               | ArtistId | AlbumId |
| --- | ------------------ | -------- | ------- |
| 1   | Here Comes the Sun | 1        | 1       |
| 2   | Come Together      | 1        | 1       |
| 3   | Let It Be          | 1        | 2       |
| 4   | Yesterday          | 1        | 3       |
| 5   | Hey Jude           | 1        | 4       |

We can filter the query using a `WHERE` clause:

```sql
SELECT ID, Song, ArtistId, AlbumId
FROM songs
WHERE Song = "Let It Be";
```

| ID  | Song      | ArtistId | AlbumId |
| --- | --------- | -------- | ------- |
| 3   | Let It Be | 1        | 2       |

We can use `JOIN` clauses to join together information from multiple tables:

```sql
SELECT songs.ID, songs.Song, artists.Name AS ArtistName, albums.Name as AlbumName, albums.YearReleased
    FROM songs
    JOIN artists ON songs.ArtistId = artists.ID
    JOIN albums ON songs.AlbumId = albums.ID;
```

| ID  | Song               | ArtistName  | AlbumName  | YearReleased |
| --- | ------------------ | ----------- | ---------- | ------------ |
| 1   | Here Comes the Sun | The Beatles | Abbey Road | 1969         |
| 2   | Come Together      | The Beatles | Abbey Road | 1969         |
| 3   | Let It Be          | The Beatles | Let It Be  | 1970         |
| 4   | Yesterday          | The Beatles | Help!      | 1965         |
| 5   | Hey Jude           | The Beatles | "1"        | 2000         |

We can create new records by issuing an `INSERT INTO` command. "You've Got to Hide Your Love Away" was a song by The
Beatles on the album _Help!_

```sql
INSERT INTO songs (Song, ArtistID, AlbumID)
    VALUES ("You've Got to Hide Your Love Away", 1, 3);
```

We can update records using an `UPDATE` command. Note: You should almost always include a `WHERE` clause to
limit which records you're updating. Otherwise, you could update them all at once!

```sql
UPDATE albums
    SET YearReleased = "2021"
    WHERE Name = "Abbey Road";
```

SQL can get very complex with all sorts of commands for filtering, ordering, and updating records across
related tables. These are the basics, though, and they will get you pretty far.

# Conclusion

If we were building Spotify, from here we could add more Artists, Albums, and Songs all with interlinking
relationships!

Here's what we learned today...

We structured a relational database. It included:

-   Objects (aka Models) we needed to store with a defined schema
-   Relationships between objects, using Foreign Keys

We added and queried data using SQL, a language made for relational databases.

_But writing SQL can be difficult and challenging to maintain, especially in large projects. What if we could
interact with the database directly in Python?_

In future lessons, we'll take a look at how we can do that in Django
