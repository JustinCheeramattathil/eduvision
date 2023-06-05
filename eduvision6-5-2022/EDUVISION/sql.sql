/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - eduvision
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`eduvision` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `eduvision`;

/*Table structure for table `academic_performance` */

DROP TABLE IF EXISTS `academic_performance`;

CREATE TABLE `academic_performance` (
  `academicid` int(11) NOT NULL AUTO_INCREMENT,
  `academicperformance` varchar(200) NOT NULL,
  `academicbehaviour` varchar(200) NOT NULL,
  `classpresence` varchar(200) NOT NULL,
  `student_id` int(11) NOT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`academicid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `academic_performance` */

/*Table structure for table `attendencetable` */

DROP TABLE IF EXISTS `attendencetable`;

CREATE TABLE `attendencetable` (
  `attendenceid` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) NOT NULL,
  `student_id` int(11) NOT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`attendenceid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `attendencetable` */

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaintid` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) NOT NULL,
  `parent_id` int(50) NOT NULL,
  `complaint` varchar(200) DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL,
  `reply_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaintid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaintid`,`date`,`parent_id`,`complaint`,`reply`,`reply_date`) values (1,'2',20220210,'hgghg','pending','pending'),(2,'2',20220210,'hai','pending','pending'),(3,'2022-02-10',2,'hello','pending','pending');

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `dep_name` varchar(50) DEFAULT NULL,
  `course_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`course_id`,`dep_name`,`course_name`) values (1,'cs','bsc cs'),(2,'cs','msc cs');

/*Table structure for table `examscheduling` */

DROP TABLE IF EXISTS `examscheduling`;

CREATE TABLE `examscheduling` (
  `exam_id` int(11) NOT NULL AUTO_INCREMENT,
  `examdate` date DEFAULT NULL,
  `examtime` varchar(50) DEFAULT NULL,
  `course_id` int(50) NOT NULL,
  `subject_id` int(50) NOT NULL,
  PRIMARY KEY (`exam_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `examscheduling` */

insert  into `examscheduling`(`exam_id`,`examdate`,`examtime`,`course_id`,`subject_id`) values (2,'2022-02-15','4:40',2,2);

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedbackid` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) NOT NULL,
  `parent_id` int(11) NOT NULL,
  `feedback` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`feedbackid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

/*Table structure for table `fine` */

DROP TABLE IF EXISTS `fine`;

CREATE TABLE `fine` (
  `fineid` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) NOT NULL,
  `penaltyreason` varchar(200) DEFAULT NULL,
  `due_amount` varchar(50) NOT NULL,
  `stud_id` int(50) NOT NULL,
  PRIMARY KEY (`fineid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `fine` */

insert  into `fine`(`fineid`,`date`,`penaltyreason`,`due_amount`,`stud_id`) values (1,'2022-01-07','aa','aa',0),(2,'2022-01-07','werty','1234',2),(3,'2022-01-07','asdf','123',6),(4,'2022-01-11','sdfghjk,','ertyuk',5),(5,'2022-01-16','dfghjk','45678',5),(6,'2022-01-29','dfghjk','1234',0),(7,'2022-01-31','sdfgh','4567',0),(8,'2022-01-31','fddddddddddddd','2',1),(9,'2022-02-04','gkhgkdghkdhf','646747646',7),(10,'2022-02-09','dsgferhgdfhdftererd','45546436',2);

/*Table structure for table `institutionrules` */

DROP TABLE IF EXISTS `institutionrules`;

CREATE TABLE `institutionrules` (
  `ruleid` int(11) NOT NULL AUTO_INCREMENT,
  `rules` varchar(100) NOT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ruleid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `institutionrules` */

insert  into `institutionrules`(`ruleid`,`rules`,`date`) values (7,'dfghjkl','2022-02-02');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`utype`) values (1,'admin','admin','ADMIN'),(2,'thomasjustin2203@gmail.com','6852','PARENT'),(3,'adfsgdg@gmail.com','5891','staff'),(5,'thomasjustin2203@gmail.com','2994','staff'),(6,'hi@gmail.com','1613','PARENT'),(7,'thomasjustin2203@gmail.com','1846','PARENT'),(8,'adfsgdg@gmail.com','4992','staff'),(9,'adfsgdg@gmail.com','8551','staff'),(10,'adfsgdg@gmail.com','1809','PARENT'),(11,'adfsgdg@gmail.com','8554','PARENT'),(12,'steve123@gmail.com','4715','PARENT'),(13,'thomasjustin2203@gmail.com','1298','PARENT'),(14,'thomasjustin2203@gmail.com','9968','PARENT');

/*Table structure for table `management_decisions` */

DROP TABLE IF EXISTS `management_decisions`;

CREATE TABLE `management_decisions` (
  `decisionid` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) NOT NULL,
  `title` varchar(50) NOT NULL,
  `file` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`decisionid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `management_decisions` */

insert  into `management_decisions`(`decisionid`,`date`,`title`,`file`) values (4,'2022-02-09','justincbdfhgd','/static/dimage/220209-105550.jpg');

/*Table structure for table `marks` */

DROP TABLE IF EXISTS `marks`;

CREATE TABLE `marks` (
  `markid` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(50) NOT NULL,
  `subject_id` int(11) NOT NULL,
  `marks` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`markid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `marks` */

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `n_type` varchar(100) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `content` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`n_type`,`title`,`content`,`date`) values (4,'PARENTS','dfghjk','trtyujikol;','2022-01-15'),(5,'PTA','fghjk','exa,m\r\n','2022-01-15'),(6,'PARENTS','university exams','qwertyuiopasdfghjklzxcvbnmmmmmm','2022-01-15'),(7,'TEACHERS','Admin','dfghjk','2022-01-16'),(8,'TEACHERS','fghjk','ghjkl;ghjkl','2022-01-21'),(9,'TEACHERS','Admin','gfhjk','2022-01-29'),(10,'PTA','dchxcjhnxcg','dfg','2022-01-29'),(11,'TEACHERS','wer','wer','2022-01-29'),(12,'TEACHERS','sdfg','dfghj','2022-01-29'),(13,'TEACHERS','dchxcjhnxcg','fghj','2022-01-29'),(14,'PTA','hgfiu','hfjhkjbkl','2022-02-02');

/*Table structure for table `parent` */

DROP TABLE IF EXISTS `parent`;

CREATE TABLE `parent` (
  `parent_id` int(11) DEFAULT NULL,
  `parent_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `house` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` varchar(50) DEFAULT NULL,
  `occupation` varchar(50) DEFAULT NULL,
  `relation_with_student` varchar(50) DEFAULT NULL,
  `student_id` int(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `parent` */

insert  into `parent`(`parent_id`,`parent_name`,`email`,`phone`,`house`,`place`,`post`,`pin`,`occupation`,`relation_with_student`,`student_id`) values (6,'george','hi@gmail.com','9743231822','dgffhgh','der','zxc','123','dsa','Father',15),(10,'george','adfsgdg@gmail.com','9743231822','dgffhgh','der','zxc','123','dsa','Father',1),(13,'mathew','thomasjustin2203@gmail.com','1233445','Admin','thomas','fzsdfgsgd','3456','sdfgggn','father',4);

/*Table structure for table `pta_meeting` */

DROP TABLE IF EXISTS `pta_meeting`;

CREATE TABLE `pta_meeting` (
  `meeting_id` int(11) NOT NULL AUTO_INCREMENT,
  `meetingdate` varchar(50) NOT NULL,
  `meetingtime` varchar(50) NOT NULL,
  `meetingplace` varchar(50) NOT NULL,
  `agenda` varchar(50) DEFAULT NULL,
  `decision_taken` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`meeting_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `pta_meeting` */

insert  into `pta_meeting`(`meeting_id`,`meetingdate`,`meetingtime`,`meetingplace`,`agenda`,`decision_taken`) values (1,'2022-02-15','23456','fghj','mnbvc','asd'),(2,'','10:01','muttam','annual jubilie','sdfghjertyujk'),(3,'Admin','4567','xghn','sdfghj','werty'),(4,'2022-01-11','9:30 am','xghn','sfhk','dgfhj'),(5,'22/08/21','1:20','dfgh','dfgh','cvbn'),(6,'2022-01-27','4','g','gt','hjj'),(7,'2022-02-16','4:40','jfgjfg','fhfjsj','fhdfjsj');

/*Table structure for table `pta_members` */

DROP TABLE IF EXISTS `pta_members`;

CREATE TABLE `pta_members` (
  `PTA_MEMBER_ID` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(50) DEFAULT NULL,
  `position` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`PTA_MEMBER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `pta_members` */

insert  into `pta_members`(`PTA_MEMBER_ID`,`member_id`,`position`) values (2,4,'aaaa'),(3,0,''),(4,11,'president'),(5,5,'qwerty'),(6,8,'Admin'),(7,9,'awrwqe'),(8,10,'asdfg'),(9,13,'asdfg'),(10,14,'sdsfdsf'),(11,14,'dfhh');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staffid` int(11) DEFAULT NULL,
  `staff_name` varchar(50) DEFAULT NULL,
  `department` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `house` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staffid`,`staff_name`,`department`,`email`,`phone`,`qualification`,`house`,`place`,`post`,`pin`) values (5,'justin','dchxcjhnxcg','thomasjustin2203@gmail.com','1233445','dghdhgfhg','vj','adfsgdg','0',4567),(8,'dfhfghf','hjfhsd','adfsgdg@gmail.com','1233445','dhsds','dfhsdhsdh','dhdffhdsh','774',0),(9,'just','csddfg','adfsgdg@gmail.com','1233445','gdgsdgsdg','gdfgdgdshsh','gsddh','456',0);

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `stud_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `course_id` varchar(50) DEFAULT NULL,
  `semester` varchar(50) DEFAULT NULL,
  `admission_number` varchar(50) DEFAULT NULL,
  `quota` varchar(50) DEFAULT NULL,
  `dob` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`stud_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`stud_id`,`first_name`,`last_name`,`course_id`,`semester`,`admission_number`,`quota`,`dob`) values (1,'moushmitha','r chandran','1','3','345','merit','2022-02-15'),(2,'albin ','thomas','1','3','123','merit','2002-03-23'),(3,'steve','george','2','3','23','merit','2022-02-14'),(4,'ann','mathew','2','3','12','merit','2022-02-22'),(5,'john','mathew','2','3','1234','merit','2022-02-10');

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `subject_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(50) DEFAULT NULL,
  `semester` varchar(50) DEFAULT NULL,
  `courseid` int(11) DEFAULT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `subject` */

insert  into `subject`(`subject_id`,`subject_name`,`semester`,`courseid`) values (1,'ds','3',1),(2,'cs','2',2),(3,'sdfg','4',3);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
