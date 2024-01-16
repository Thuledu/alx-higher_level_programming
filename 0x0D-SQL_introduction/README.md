# SQL - Introduction
In this project, we began working on relational databases. I started practising introductory SQL data definitions and data manipulation language, making subqueries, and using functions.

## Tasks

**0. List databases**
  * MySQL script that lists all databases.

**1. Create a database**
  *  MySQL script that creates the database `hbtn_0c_0`.
  
**2. Delete a database**
  *  MySQL script that deletes the database `hbtn_0c_0`.

**3. List tables**
  * MySQL script that lists all tables.
  
**4. First table**
  * MySQL script that creates a table `first_table`.
  * Description:
    * `id`: INT
    * `name`: VARCHAR(256)

**5. Full description**
  * MySQL script that prints the full description of the table `first_table`.
  
**6. List all in table**
  * MySQL script that lists all rows of the table
  `first_table`.

**7. First add**
  * MySQL script that inserts a new row in the table `first_table`.
  * Description:
    * `id` = `89`
    * `name` = `Best School`

**8. Count 89**
  * MySQL script that displays the number records with `id = 89` in the table `first_table`.

**9. Full creation**
  * MySQL script that creates and fills a table `second_table`.
  * Description:
    * `id`: INT
    * `name`: VARCHAR(256)
    * `score`: INT
  * Records:
    * `id` = 1, `name` = "John", `score` = 10
    * `id` = 2, `name` = "Alex", `score` = 3
    * `id` = 3, `name` = "Bob", `score` = 14
    * `id` = 4, `name` = "George", `score` = 8

**10. List by best**
  * MySQL script that lists the `score` and `name` of all records of the table `second_table` in order of descending `score`.

**11. Select the best**
  * MySQL script that lists the `score` and `name` of all records with a `score >= 10` in the table `second_table` in order of descending score.

**12. Cheating is bad**
  * MySQL script that updates the score of Bob to 10 the table `second_table`.

**13. Score too low**
  * MySQL script that removes all records with a `score <= 5` in the table `second_table`.

**14. Average**
  * MySQL script that computes the average `score` of all records in the table `second_table`.

**15. Number by score**
  * MySQL script that lists the `score` and number of records with the same score in the table `second_table` in order of descending count.

**16. Say my name**
  * MySQL script that lists the `score` and `name` of all records in the table `second_table` in order of descending `score`.
  * Does not display rows without a `name` value.

**17. Go to UTF8**
  * MySQL script that converts the `hbtn_0c_0` database to UTF8.

**18. Temperatures #0**
  * MySQL script that displays the average temperature (Fahrenheit) by city in descending order.

**19. Temperatures #1**
  * MySQL script that displays the three cities with the highest average temperature from July to August in descending order.

**20. Temperature #2**
  * MySQL script that displays the max temperature of each state in order of state name.

