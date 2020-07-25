# DRF-API-Server

## Technology
- Framework : Django 3.0.2, DjangoRestFramework3.11
- Language : Python 3.7.4
- Database : SQLite3
- OS : Window10
- IDE : VsCode

## Execution

### Repogitory Clone

```
$ git clone https://github.com/ParkHyeonChae/DRF-API-Server.git
```

### Install PIP

```
$ pip install -r requirements.txt
```

### DB Migration

```
$ python manage.py makemigrations
$ python manage.py migrate
```
### CreateSuperUser

```
$ python manage.py createsuperuser
```

### Runserver

```
$ python manage.py runserver
```


## HTTP GET

| **Endpoint**               | Description                                                  |
| -------------------------- | ------------------------------------------------------------ |
| http://127.0.0.1:8000/api/ | Used to list and search through out all the available movies. Can sort, filter, search and order the results |

###### 

### Endpoint Parameters

| Parameter | Required | Type                                 | Default | Description                                                  |
| --------- | -------- | ------------------------------------ | ------- | ------------------------------------------------------------ |
| limit     | X        | *Integer between 1 - 50 (inclusive)* | 20      | The limit of results per page that has been set              |
| page      | X        | *Integer (Unsigned)*                 | 1       | Used to see the next page of movies, eg limit=15 and page=2 will show you movies 15-30 |
| genre     | X        | *String*                             | All     | Used to filter by a given genre                              |
| sort_by   | X        | *String (title, year, rating)*       | id      | Sorts the results by choosen value                           |
| order_by  | X        | *String (desc, asc)*                 | desc    | Orders the results by either Ascending or Descending order   |

###### 

### Examples

| METHOD | URL                                                       | Description                                                  |
| ------ | --------------------------------------------------------- | ------------------------------------------------------------ |
| GET    | http://127.0.0.1:8000/api/?sort_by=title&limit=10&page=10 | Returns ten tenth page movies in title order using JSON format |

###### 



## HTTP POST

| **Endpoint**               | Description                                                  |
| -------------------------- | ------------------------------------------------------------ |
| http://127.0.0.1:8000/api/ | Enter the title, release screen, video, genre and description of the movie and save it in DB |

###### 

### Endpoint Parameters

| Parameter | Required | Type      | Default | Description                          |
| --------- | -------- | --------- | ------- | ------------------------------------ |
| title     | O        | *String*  | -       | Enter the title of the movie.        |
| year      | O        | *Integer* | -       | Enter the release year of the movie. |
| rating    | O        | *Float*   | -       | Enter the movie's rating.            |
| genre     | O        | *String*  | -       | Enter the genre of the movie.        |
| summary   | O        | *String*  | -       | Enter a description for the movie.   |

###### 

### Examples

| METHOD | URL                                                          | Description                        |
| ------ | ------------------------------------------------------------ | ---------------------------------- |
| POST   | http://127.0.0.1:8000/api/?title=test&year=2015&rating=9.1&genre=Action&summary=test | Save to DB as requested parametert |

