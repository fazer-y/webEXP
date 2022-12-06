# web技术实验5
202000810047 林鹏飞

## sqlite 命令行操作
### 一、创建数据库
sqlite3 courses.db

### 二、创建表
1. 教师表
```python
sqlite> create table teachers(
            tID int primary key, 
            tName text NOT NULL
        );
```

2. 课程表
```python
sqlite> create table courses(
            cID int primary key, 
            cName text NOT NULL
        );
```

3. 每周课程表
```python
sqlite> create table courseTable(
            weekDay int, 
            section text, 
            cID int, 
            tID int,
            classroom text, 
            primary key(weekDay, section)
            constraint fk_cID 
            foreign key(cID) 
            references courses(cID) 
            constraint fk_tID 
            foreign key (tID) 
            references teachers(tID)
        );
```

### 三、添加数据
1. 添加教师信息
```python
sqlite> INSERT INTO teachers(tID, tName) 
                    values(1, '刘猛');

sqlite> INSERT INTO teachers(tID, tName) 
                    values(2, '程杰'); 

sqlite> INSERT INTO teachers(tID, tName) 
                    values(3, '张亚涛');

sqlite> INSERT INTO teachers(tID, tName) 
                    values(4, '杨飞');   

sqlite> INSERT INTO teachers(tID, tName) 
                    values(5, '邹汶洋');   
sqlite> INSERT INTO teachers(tID, tName) 
                    values(6, '靳贺');   
```

2. 添加课程信息
```python
sqlite> INSERT INTO courses(cID, cName) 
                    values(1, 'web技术'); 

sqlite> INSERT INTO courses(cID, cName) 
                    values(2, '计算机网络');   

sqlite> INSERT INTO courses(cID, cName) 
                    values(3, '数字图像处理');

sqlite> INSERT INTO courses(cID, cName) 
                    values(4, '计算机图形学'); 

sqlite> INSERT INTO courses(cID, cName) 
                    values(5, '形势与政策');   

sqlite> INSERT INTO courses(cID, cName) 
                    values(6, '习近平新时代中国特色社会主义思想概论');
```
3. 添加课程表信息
```python
sqlite> INSERT INTO courseTable(weekDay, section, cID, tID, classroom) 
                    values(1, '1-2', 2, 2, '商学院448');             

sqlite> INSERT INTO courseTable(weekDay, section, cID, tID, classroom) 
                    values(2, '1-2', 3, 3, '商学院551'); 

sqlite> INSERT INTO courseTable(weekDay, section, cID, tID, classroom) 
                    values(2, '3-4', 4, 4, '图东教学楼222');  

sqlite> INSERT INTO courseTable(weekDay, section, cID, tID, classroom) 
                    values(3, '1-2(双周)', 3, 3, '商学院248');     

sqlite> INSERT INTO courseTable(weekDay, section, cID, tID, classroom) 
                    values(3, '3-4(5-8周)', 5, 5, '商学院248');  

sqlite> INSERT INTO courseTable(weekDay, section, cID, tID, classroom) 
                    values(3, '3-4(9-16周)', 6, 6, '商学院347'); 

sqlite> INSERT INTO courseTable(weekDay, section, cID, tID, classroom) 
                    values(4, '1-2', 2, 2, '商学院448');         

sqlite> INSERT INTO courseTable(weekDay, section, cID, tID, classroom) 
                    values(4, '3-4(单周)', 4, 4, '图东教学楼222');

sqlite> INSERT INTO courseTable(weekDay, section, cID, tID, classroom) 
                    values(5, '1-2', 1, 1, '海洋学院605');   
```