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
  `arts` varchar(200) NOT NULL,
  `sports` varchar(200) DEFAULT NULL,
  `studies` varchar(200) DEFAULT NULL,
  `classpresence` varchar(200) NOT NULL,
  `student_id` int(11) NOT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `area_of_interest` varchar(100) DEFAULT NULL,
  `about` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`academicid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `academic_performance` */

/*Table structure for table `attendence` */

DROP TABLE IF EXISTS `attendence`;

CREATE TABLE `attendence` (
  `attendenceid` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) NOT NULL,
  `student_id` int(11) NOT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`attendenceid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `attendence` */

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_id` int(50) DEFAULT NULL,
  `course_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`course_id`,`dept_id`,`course_name`) values (3,3,'bsc maths');

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `dept_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`dept_id`,`dept_name`) values (2,'SCIENCE'),(3,'BSC'),(4,'BA');

/*Table structure for table `examscheduling` */

DROP TABLE IF EXISTS `examscheduling`;

CREATE TABLE `examscheduling` (
  `exam_id` int(11) NOT NULL AUTO_INCREMENT,
  `examdate` date DEFAULT NULL,
  `examtime` varchar(50) DEFAULT NULL,
  `course_id` int(50) NOT NULL,
  `subject_id` int(50) NOT NULL,
  PRIMARY KEY (`exam_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `examscheduling` */

insert  into `examscheduling`(`exam_id`,`examdate`,`examtime`,`course_id`,`subject_id`) values (1,'2022-02-01','13:00',3,1);

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `fine` */

insert  into `fine`(`fineid`,`date`,`penaltyreason`,`due_amount`,`stud_id`) values (1,'2022-02-22','used mobilee','10000',1);

/*Table structure for table `institutionrules` */

DROP TABLE IF EXISTS `institutionrules`;

CREATE TABLE `institutionrules` (
  `ruleid` int(11) NOT NULL AUTO_INCREMENT,
  `rules` varchar(100) NOT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ruleid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `institutionrules` */

insert  into `institutionrules`(`ruleid`,`rules`,`date`) values (1,'no use of mobiles','2022-02-22');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`utype`) values (1,'admin','admin','ADMIN'),(2,'kim@gmail.com','3751','TEACHER'),(3,'jin@gmail.com','9179','PARENT');

/*Table structure for table `management_decisions` */

DROP TABLE IF EXISTS `management_decisions`;

CREATE TABLE `management_decisions` (
  `decisionid` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) NOT NULL,
  `title` varchar(50) NOT NULL,
  `file` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`decisionid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `management_decisions` */

insert  into `management_decisions`(`decisionid`,`date`,`title`,`file`) values (1,'2022-02-22','decision','/static/dimage/220222-125220.jpg');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`n_type`,`title`,`content`,`date`) values (1,'TEACHERS','studies','aaaaaaaa','2022-02-22');

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

insert  into `parent`(`parent_id`,`parent_name`,`email`,`phone`,`house`,`place`,`post`,`pin`,`occupation`,`relation_with_student`,`student_id`) values (3,'jin','jin@gmail.com','11111','hhh','eee','ooo','234','bussiness','father',1);

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `pta_meeting` */

/*Table structure for table `pta_members` */

DROP TABLE IF EXISTS `pta_members`;

CREATE TABLE `pta_members` (
  `PTA_MEMBER_ID` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(50) DEFAULT NULL,
  `position` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`PTA_MEMBER_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `pta_members` */

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staffid` int(11) NOT NULL AUTO_INCREMENT,
  `staff_name` varchar(50) DEFAULT NULL,
  `department` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `house` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `pin` varchar(50) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`staffid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staffid`,`staff_name`,`department`,`email`,`phone`,`qualification`,`house`,`place`,`pin`,`post`) values (2,'kim namjoon','BSC','kim@gmail.com','88','+2\r\ndegree','ddd','ww','wr','11');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`stud_id`,`first_name`,`last_name`,`course_id`,`semester`,`admission_number`,`quota`,`dob`) values (1,'kim taehyung','vv','3','2','77','community','2022-02-10');

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `subject_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(50) DEFAULT NULL,
  `semester` varchar(50) DEFAULT NULL,
  `courseid` int(11) DEFAULT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `subject` */

insert  into `subject`(`subject_id`,`subject_name`,`semester`,`courseid`) values (1,'maths','5',3);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
