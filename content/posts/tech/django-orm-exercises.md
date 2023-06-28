---
title: "Ultimate Django ORM Cheatsheet + Exercises"
date: 2023-02-19T01:18:34+05:30
draft: false
cover: 
    image: blog/django-orm.png
    alt: Django ORM Cheatsheet + Exercises
    caption: Master the basics of Django ORM with this comprehensive cheatsheet and exercises to level up your skills in database querying, model relationships, aggregations, annotations, and more. 
description: "Master the basics of Django ORM with this comprehensive cheatsheet and exercises to level up your skills in database querying, model relationships, aggregations, annotations, and more."
tags: ["python", "django"]
showToc: true
tocOpen: true
---

## Querying Django Models with Examples

In Django, querying the database is an essential task when working with models. Django's QuerySet API provides an extensive range of methods to query the database efficiently.

In this article, we'll go over several examples of how to query Django models using the QuerySet API, along with code snippets that demonstrate the functionality of each method.

## Terminology

Let us first go over some of the terminology that is used in conjunction with the QuerySet API. The following terms are used in the examples below:

- **Models:** Django models are Python classes that define the structure and behavior of database tables. They encapsulate fields and relationships and provide methods to interact with the data.
- **QuerySets:** QuerySets are objects that allow you to retrieve, filter, and manipulate data from the database. They are lazy, meaning that they only fetch data when needed, and can be chained together to form complex queries.
- **Managers:** Managers provide methods for working with QuerySets. They allow you to create reusable queries and define custom methods to retrieve data from the database.
- **Fields:** Fields define the type of data that can be stored in a model's attribute or database column. They provide validation and conversion of input data and map to the appropriate SQL type.
- **Migrations:** Migrations allow you to modify the database schema and keep track of changes to models over time. They provide a convenient way to manage changes to the database schema and apply them to the database.
- **Database routers:** Database routers allow you to specify which database to use for different models or queries. They allow you to distribute data across multiple databases or use different databases for read and write operations.
- **Aggregation:** Aggregation provides methods for performing calculations on QuerySets, such as Sum, Count, Avg, and Max. They are used to retrieve statistics or summary information about the data in the database.
- **Annotations:** Annotations allow you to add calculated fields to QuerySets based on database functions or other fields. They are used to add computed or aggregated data to QuerySets.
- **Meta options:** Meta options provide additional settings for models, such as ordering, database table names, and unique constraints. They allow you to customize the behavior of models at the class level.

## Models Used in the Examples

The following models are used in the examples below. Take a look at the code to get a better understanding of the relationships between the models.

```py
from django.db import models

class Author(models.Model):
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)
  address = models.CharField(max_length=200, null=True)
  zipcode = models.IntegerField(null=True)
  telephone = models.CharField(max_length=100, null=True)
  recommendedby = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='recommended_authors', related_query_name='recommended_authors', null=True)
  joindate = models.DateField()
  popularity_score = models.IntegerField()
  followers = models.ManyToManyField('User', related_name='followed_authors', related_query_name='followed_authors')
  def __str__(self):
    return self.firstname + ' ' + self.lastname

class Books(models.Model):
  title = models.CharField(max_length=100)
  genre = models.CharField(max_length=200)
  price = models.IntegerField(null=True)
  published_date = models.DateField()
  author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books', related_query_name='books')
  publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='books', related_query_name='books')
  def __str__(self):
    return self.title

class Publisher(models.Model):
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)
  recommendedby = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True)
   joindate = models.DateField()
  popularity_score = models.IntegerField()
  def __str__(self):
    return self.firstname + ' ' + self.lastname

class User(models.Model):
  username = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  def __str__(self):
    return self.username
```

## QuerySet API Exercises

### Query 1: Fetching all books from the database

**Explanation**: The `all()` method returns all the records from the model it is called on. In this case, it will fetch all the records from the `Books` model. The `Books` model is assumed to be defined in the `main` app.

```py
result1 = Books.objects.all()
```

### Query 2: Fetching selected columns from the Books table

```py
result2 = Books.objects.all().values_list('title', 'published_date')
```

**Explanation**: The `values_list()` method is used to retrieve specific columns from the model. In this case, only the `title` and `published_date` columns are selected.

### Query 3: Filtering records based on a condition

```py
result3 = Authors.objects.all().filter(popularity_score=0).values_list('firstname', 'lastname')
```

**Explanation**: The `filter()` method is used to retrieve records that match a specific condition. In this case, the condition is that `popularity_score` should be equal to 0. The `values_list()` method is used to retrieve only the `firstname` and `lastname` fields from the retrieved records.

### Query 4: Filtering records based on multiple conditions

```py
result4 = Authors.objects.all().filter(firstname__startswith='a', popularity_score__gte=8).values_list('firstname', 'popularity_score')
```

**Explanation**: The `filter()` method is used to retrieve records that match multiple conditions. In this case, the conditions are that `firstname` should start with 'a' and `popularity_score` should be greater than or equal to 8. The `values_list()` method is used to retrieve only the `firstname` and `popularity_score` fields from the retrieved records.

### Query 5: Searching records based on a substring

```py
result5 = Authors.objects.all().filter(firstname__icontains='aa').values_list('firstname')
```

**Explanation**: The `filter()` method is used to retrieve records that contain a specific substring. In this case, the substring is 'aa'. The `values_list()` method is used to retrieve only the `firstname` field from the retrieved records. The `icontains` lookup is used to perform a case-insensitive search for the specified substring.

### Query 6: Retrieve authors with specific primary keys

```py
result6 = Authors.objects.all().filter(pk__in=[1, 3, 23, 43, 134, 25])
```

**Explanation**: The filter() method is used to retrieve authors with primary keys specified in the `pk__in` argument. The `pk` in `pk__in` stands for primary key. In this case, the primary keys are `[1, 3, 23, 43, 134, 25]`.

### Query 7: Retrieve authors who joined after a specific date

```py
result7 = Authors.objects.all().filter(joindate__gte=datetime.date(year=2012, month=9, day=1)).order_by('joindate').values_list('firstname', 'joindate')
```

**Explanation**: The filter() method is used to retrieve authors who joined after September 1, 2012, using the `joindate__gte` lookup. The `gte` in `joindate__gte` stands for greater than or equal to. The results are ordered by `joindate` in ascending order using the `order_by()` method. Only the `firstname` and `joindate` fields are selected using the `values_list()` method.

### Query 8: Retrieve distinct publisher last name

```py
result8 = Publishers.objects.all().order_by('lastname').values_list('lastname').distinct()[:10]
```

**Explanation**: The `distinct()` method is used to retrieve distinct last names of all publishers in ascending order using the `order_by()` method. Only the `lastname` field is selected using the `values_list()` method. The first 10 results are selected using slicing `[:10]`.

### Query 9: Retrieve the latest joined author and the earliest joined publisher

```py
result9 = [Authors.objects.all().order_by('joindate').last(),
        Publishers.objects.all().order_by('-joindate').first()]
```

**Explanation**: Two queries are executed here, one to retrieve the latest joined author and one to retrieve the earliest joined publisher. In the first query, the `last()` method is used to retrieve the latest joined author. In the second query, the `order_by('-joindate')` method is used to order the publishers by `joindate` in descending order, and the `first()` method is used to retrieve the earliest joined publisher.

### Query 10: Retrieve the first name, last name, and join date of the most recently joined author

```py
result10 = Authors.objects.all().order_by('-joindate').values_list('firstname', 'lastname', 'joindate').first()
```

**Explanation**: The `order_by('-joindate')` method is used to order the authors by `joindate` in descending order. Only the `firstname`, `lastname`, and `joindate` fields are selected using the `values_list()` method. The `first()` method is used to retrieve the first row of the resulting queryset, which contains the most recent joined author in the database.

### Query 11: Retrieve Authors Joined After 2013

```py
result11 = Authors.objects.all().filter(joindate__year__gte=2013)
```

**Explanation:** This query retrieves all authors who joined after 2013. The filter() method is used to specify the condition. Here, the joindate field is filtered by its year attribute to retrieve all authors who joined after 2013.

```py
result11 = Authors.objects.all().filter(joindate__year__gte=2013)
```

### Query 12: Calculate Total Price of Books Written by Popular Authors

```py
result12 = Books.objects.all().filter(author__popularity_score__gte=7).aggregate(total_book_price=Sum('price'))
```

**Explanation:** This query calculates the total price of all books written by authors with a popularity score of 7 or greater. The filter() method is used to filter the books based on the popularity_score of their respective authors. The aggregate() method is used to calculate the total price of all books using the Sum() function.

```py
result12 = Books.objects.all().filter(author__popularity_score__gte=7).aggregate(total_book_price=Sum('price'))
```

### Query 13: Retrieve Titles of Books Written by Authors with 'a' in their Firstname

```py
result13 = Books.objects.all().filter(author__firstname__icontains='a').values_list('title', flat=True)
```

**Explanation:** This query retrieves the titles of all books written by authors whose firstname contains the lowercase letter 'a'. The filter() method is used to filter the books based on the firstname of their respective authors. The values_list() method is used to retrieve only the title field of the resulting queryset. The flat=True parameter is used to return the resulting queryset as a flat list.

```py
result13 = Books.objects.all().filter(author__firstname__contains='a').values_list('title', flat=True)
```

### Query 14: Calculate Average Book Price of Selected Authors

```py
result14 = Books.objects.all().filter(author__pk__in=[1, 3, 4]).aggregate('price')
```

**Explanation:** This query calculates the average price of all books written by a selected group of authors. The filter() method is used to select the authors based on their primary key values. The aggregate() method is used to calculate the average price of all books using the Avg() function.

### Query 15: Retrieve first name of authors and their recommended author's first name

```py
result15 = Authors.objects.all().values_list('firstname', 'recommendedby__firstname')
```

**Explanation:**  This query uses the `values_list()` method to retrieve the first name of authors and their recommended author's first name. The `recommendedby__firstname` attribute is used to access the first name of the recommended author.

### Query 16: Retrieve authors whose books are published by a specific publisher

```py
result16 = Authors.objects.all().filter(books__publisher__pk=1)
```

**Explanation:** This query uses the `filter()` method to retrieve all authors whose books are published by a specific publisher. The `books__publisher__pk` attribute is used to access the publisher's primary key.

### Query 17: Add followers to an author

```py
user1 = Users.objects.create(username='user1', email='user1@test.com')
user2 = Users.objects.create(username='user2', email='user2@test.com')
user3 = Users.objects.create(username='user3', email='user3@test.com')
result17 = Authors.objects.get(pk=1).followers.add(user1, user2, user3)
```

**Explanation:** This query uses the `add()` method to add multiple followers to an author. The `get()` method is used to retrieve the author with the specified primary key.

### Query 18: Set followers for an author

```py
user1 = Users.objects.create(username='user1', email='user1@test.com')
result18 = Authors.objects.get(pk=2).followers.set(user1)
```

**Explanation**: This query uses the `set()` method to set the followers for an author. The `get()` method is used to retrieve the author with the specified primary key.

### Query 19: Add a follower to an author

```py
user1 = Users.objects.create(username='user1', email='user1@test.com')
result19 = Authors.objects.get(pk=1).followers.add(user1)
```

**Explanation**: This query uses the `add()` method to add a follower to an author. The `get()` method is used to retrieve the author with the specified primary key.

### Query 20: Remove a follower from an author

```py
user1 = Users.objects.create(username='user1', email='user1@test.com')
result20 = Authors.objects.get(pk=1).followers.remove(user1)
```

**Explanation**: This query uses the `remove()` method to remove a follower from an author. The `get()` method is used to retrieve the author with the specified primary key.

### Query 21: Retrieve the first names of all authors followed by the user with primary key (pk) equal to 1

```py
result21 = Users.objects.get(pk=1).followed_authors.all().values_list('firstname', flat=True)
```

 **Explanation:** This code uses a foreign key relationship between the `Users` and `Authors` models to retrieve all authors followed by a specific user with a primary key of 1. The `values_list` method with `flat=True` is used to return a flat list of only the first names of the authors.

### Query 22: Retrieve all authors who have books with titles containing the string "tle"

```py
result22 = Authors.objects.all().filter(books__title__icontains='tle')
```

 **Explanation:** This code uses a reverse foreign key relationship between the `Authors` and `Books` models to retrieve all authors who have books with titles containing the string "tle". The `filter` method is used to apply the filter condition. The `__icontains` lookup is used to perform a case-insensitive match on the book title.

### Query 23: Retrieve all authors whose first name starts with the letter "a" and either have a popularity score greater than 5 or joined the platform after the year 2014

  ```py
  result23 = Authors.objects.filter(Q(firstname__istartswith='a') & (Q(popularity_score__gt=5) | Q(joindate__year__gt=2014)))
  ```

   **Explanation:**  This code retrieves all authors whose first name starts with the letter "a" and satisfies at least one of the two conditions:

- popularity score greater than 5
- joined the platform after the year 2014. It uses the `filter` method with a combination of `Q` objects to create a complex query with multiple conditions. The `__istartswith` lookup is used to perform a case-insensitive match on the author's first name, and the `__gt` lookup is used to retrieve records with a value greater than the specified number or date.

### Query 24: Retrieve the author with primary key (pk) equal to 1

  ```py
  result24 = Authors.objects.all().get(pk=1)
  ```

   **Explanation:** This code retrieves the author record with a primary key (pk) equal to 1 using the `get` method. It assumes that the `Authors` model has a primary key field named `pk`.

### Query 25: Retrieve the first 10 authors in the database

  ```py
  result25 = Authors.objects.all().order_by('joindate')[:10]
  ```

   **Explanation:** This code retrieves the first 10 authors in the database using the slice notation `[:10]`. It returns a queryset containing the first 10 records from the `Authors` model in the order they were created.

### Query 26: Retrieve the first and last author in the database with a popularity score of 7

  ```py
  qs = Authors.objects.all().filter(popularity_scre=7)
  author1 = qs.first()
  author2 = qs.last()
  result26 = [author1, author2]
  ```

  **Explanation:** This query retrieves all the authors with a `popularity_score` of 7, then gets the first and last author in that queryset, and stores them in a list.

### Query 27: Retrieve all authors whose joindate year is greater than or equal to 2012, popularity_score is greater than or equal to 4, joindate day is greater than or equal to 12, and firstname starts with 'a'

  ```py
result27 = Authors.objects.all().filter(joindate__year__gte=2012, popularity_score__gte=4, joindate__day__gte=12, firstame__istartswith='a')
  ```

  **Explanation:** This query retrieves all the authors whose `joindate` year is greater than or equal to 2012, `popularity_score` is greater than or equal to 4, `joindate` day is greater than or equal to 12, and `firstname` starts with 'a'.

### Query 28: Retrieve all authors whose joindate year is not equal to 2012

  ```py
  result28 = Authors.objects.all().exclude(joindate__year=2012)
  ```

  **Explanation:** This query retrieves all the authors whose `joindate` year is not equal to 2012.

### Query 29: Retrieve the oldest `joindate` among all authors, the newest `joindate` among all authors, the average `popularity_score` of all authors, and the sum of `price` of all books

  ```py
  oldest_author = Authors.objects.all().aggregate(Min('joindate'))
  newest_author = Authors.objects.all().aggregate(Max('joindate'))
  avg_pop_score = Authors.objects.all().aggregate(Avg('popularity_score'))
  sum_price = Books.objects.all().aggregate(Sum('price'))
  result29 = [oldest_author, newest_author, avg_pop_score, sum_price]
  ```

  **Explanation:** This query retrieves the oldest `joindate` among all authors, the newest `joindate` among all authors, the average `popularity_score` of all authors, and the sum of `price` of all books, and stores them in a list.

### Query 30: Retrieve all authors who have not been recommended by anyone

  ```py
result30 = Authors.objects.all().filter(recommendedby__isnull=True)
  ```

  **Explanation**: This query selects all authors who have not been recommended by anyone (i.e., they don't have a `recommendedby` field value).

### Query 31: Retrieve all books that have an author, and all books that have an author who has not been recommended by anyone

  ```py
  one = Books.objects.all().filter(author__isnull=False)
  two = Books.objects.all().filter(author__isnull=False, author__recommender__isnull=True)
  result31 = [one, two]
  ```

  **Explanation**: This query retrieves all books that have an author (i.e., `author__isnull=False`). The first query in the list (`one`) retrieves all books with an author, while the second query (`two`) filters the first query to only include books where the author has not been recommended by anyone (i.e., `author__recommender__isnull=True`).

### Query 32: Calculate the sum of the price of all books authored by the author with primary key (pk) equal to 1

  ```py
result32 = Books.objects.all().filter(author__pk=1).aggregate(Sum('price'))
  ```

  **Explanation**: This query calculates the sum of the price of all books authored by the author with primary key (PK) equal to 1. It uses the `aggregate()` method to compute the sum, and the `Sum()` function to specify the aggregation operation.

### Query 33: Retrieve the title of the most recently published book

  ```py
result33 = Books.objects.all().order_by('published_date').last().title
  ```

  **Explanation**: This query retrieves the title of the most recently published book. It does so by first ordering all the books by their published date in ascending order, and then selecting the last book from this list.

### Query 34: Calculate the average price of all books

  ```py
result34 = Books.objects.all().aggregate(Avg('price'))
  ```

  **Explanation**: This query computes the average price of all the books in the database. It does so by using the `aggregate()` method on the queryset, with the `Avg()` function as the argument. The `Avg()` function is a database function that computes the average of a given column.

### Query 35: Calculate the maximum popularity score of all the publishers that have published a book written by the author with primary key 1

  ```py
result35 = Publishers.objects.filter(books__author__pk=1).aggregate(Max('popularity_score'))
  ```

  **Explanation**: This query computes the maximum popularity score of all the publishers that have published a book written by the author with primary key 1. It does so by first filtering the `Publishers` queryset by the books that have been authored by the author with primary key 1. Then, it uses the `aggregate()` method with the `Max()` function to compute the maximum popularity score of these publishers.

### Query 36: Count Authors with Books containing 'ab' in the title

  ```py
result36 = Authors.objects.filter(books__title__icontains='ab').count()
  ```

  **Explanation**: This query counts the number of authors who have written at least one book that contains 'ab' (case-insensitive) in the title.

### Query 37: Filter Authors by Number of Followers

  ```py
result37 = Authors.objects.annotate(f_count=Count('followers')).filter(f_count__gt=216)
  ```

  **Explanation**: This query annotates each author with the number of followers they have and then filters the authors to only include those with more than 216 followers.

### Query 38: Average Popularity Score of Authors who joined after 20th Sep 2014

  ```py
result38 = Authors.objects.filter(joindate__gt=datetime.date(year=2014, month=9, day=20)).aggregate(Avg('popularity_score'))
  ```

  **Explanation**: This query filters authors who joined after 20th Sep 2014 and then calculates the average popularity score of those authors.

### Query 39: Filter Books by Authors who have written more than 10 Books

  ```py
result39 = Books.objects.all().annotate(bk_count=Count('author__books')).filter(bk_count__gt=10).distinct()
  ```

  **Explanation**: This query annotates each book with the number of authors who have written the book, then filters the books to only include those written by authors who have written more than 10 books. The `distinct()` method is called to eliminate duplicate books that have multiple authors.

### Query 40: Filter Books by Title Count

  ```py
result40 = Books.objects.all().annotate(count_title=Count('title')).filter(count_title__gt=1)
  ```

  **Explanation**: This query annotates each book with the count of books that share the same title, then filters the books to only include those with a title count greater than 1. This could be useful, for example, to find books that have been republished under different titles.

## Conclusion

In conclusion, this Django ORM cheatsheet and exercises blog post provided an overview of the essential elements of Django's ORM. We covered models, querysets, managers, fields, migrations, database routers, aggregation, annotations, and meta options. Each of these elements plays a crucial role in developing robust and scalable applications with Django.

By working through the exercises, we learned how to use these elements to query and manipulate data from the database. These exercises provided practical examples of how to use Django's ORM to solve real-world problems.

Django's ORM is a powerful tool that provides a high-level, intuitive interface for interacting with databases. It enables developers to write concise and readable code while also handling complex queries and transactions. By mastering Django's ORM, developers can build robust, scalable, and maintainable applications with ease.
