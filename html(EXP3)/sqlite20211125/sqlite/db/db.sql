CREATE TABLE student_info(
   stu_id INT PRIMARY KEY     NOT NULL,
   stu_name       VARCHAR(50) NOT NULL,
   stu_sex        CHAR(2)     NOT NULL,
   stu_age        INT         NOT NULL,
   stu_origin     VARCHAR(50) NOT NULL,
   stu_profession VARCHAR(50) NOT NULL
);
INSERT INTO student_info VALUES(201003001,'姜辽辽','男',20,'陇南','网络工程');
INSERT INTO student_info VALUES(201003002,'范超','男',19,'兰州','软件工程');
INSERT INTO student_info VALUES(201003003,'赵婷婷','女',18,'天水','软件工程');
INSERT INTO student_info VALUES(201003004,'高金鹏','男',21,'天水','服务外包');
INSERT INTO student_info VALUES(201003005,'王梓旭','女',19,'兰州','网络工程');
INSERT INTO student_info VALUES(201003006,'吕洁','女',19,'武威','服务外包');
INSERT INTO student_info VALUES(201003007,'许飞1','男',20,'陇南','网络工程');
INSERT INTO student_info VALUES(201003008,'马仲','男',22,'平凉','软件工程');
INSERT INTO student_info VALUES(201003009,'李博博','女',20,'张掖','服务外包');
INSERT INTO student_info VALUES(201003010,'李敏','女',18,'金昌','网络工程');
CREATE TABLE users(
username VARCHAR(50) PRIMARY KEY   NOT NULL,
pwd VARCHAR(50) NOT NULL
);
INSERT INTO users VALUES('admin','lm');
