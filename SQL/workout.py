# DELETE THE TABLE
# DROP TABLE _______(TABLE NAME)


# HOW TO USE TRUNCATE 
# truncate table ____(table name)


# HOW TO INSERT THE data
# insert into ___(table name) (fields.....) values(datas....)


# DELETE THE ROW DATA
# delete from ___(table name) where id = 1



# CREATE TABLE
# create table students (id bigserial primary key, name varchar(40), age int);


# CREATE TABLE WITH FOREIGN KEY
# create table department (id bigserial primary key, course varchar(20),student_id int, constraint fk_user foreign key (student_id) references students(id));

# INNER JOIN
# select students.name, department.course from students inner join department on department.student_id = students.id;


# LEFT JOIN
# select students.name, department.course from students left join department on department.student_id = students.id;

# RIGHT JOIN
# select students.name,department.course from students right join department on students.student_id = department.id



