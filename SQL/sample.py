# create table COURSE (id bigserial primary key, course_name varchar(50));

# create table student (id bigserial primary key, name varchar(50),course_id int,
# constraint fk_user foreign key (course_id) referenses (course.id))



# EXISTING TABLE ADDING FOREIGN KEY

# alter table student
# add column course_id int

# ADD CONSTRAINT
# alter table student
# add constraint fk_user
# foreign key (course_id)
# referenses (course.id)
# on delete cascade


# INNER JOIN
# selct * from students
# inner join course on students.couse_id = course.id


# LEFT JOIN
# select * from students
# left join course on students.course_id = course.id

# RIGHT JOIN
# select * from students
# right join course on student.course_id = course.id


# FULL OUTER JOIN
# select * from sudents
# full outer join course on student.course_id = course.id


# SELF JOIN
# select e1.name , e2.name from student as e1
# join student as e2 on e1.student.id = e2.student.id


