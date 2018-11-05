-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: stackoverflow
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `admin_id` int(8) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) NOT NULL,
  `email_id` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `country` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `mobile_no` varchar(10) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `date_of_birth` datetime(6) DEFAULT NULL,
  `date_of_reg` datetime(6) NOT NULL,
  `profile_pic` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `answer` (
  `ans_id` int(8) NOT NULL AUTO_INCREMENT,
  `user_id` int(8) NOT NULL,
  `question_id` int(8) NOT NULL,
  `ans_content` varchar(3000) NOT NULL,
  `votes` int(8) NOT NULL DEFAULT '0',
  `ans_date` datetime(6) NOT NULL,
  `answer_code` varchar(3000) DEFAULT NULL,
  `answer_image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ans_id`),
  KEY `answer_fk0` (`user_id`),
  KEY `answer_fk1` (`question_id`),
  CONSTRAINT `answer_fk0` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `answer_fk1` FOREIGN KEY (`question_id`) REFERENCES `questions` (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `answer_later`
--

DROP TABLE IF EXISTS `answer_later`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `answer_later` (
  `later_id` int(8) NOT NULL AUTO_INCREMENT,
  `question_id` int(8) NOT NULL,
  `user_id` int(8) NOT NULL,
  PRIMARY KEY (`later_id`),
  KEY `answer_later_fk0` (`question_id`),
  KEY `answer_later_fk1` (`user_id`),
  CONSTRAINT `answer_later_fk0` FOREIGN KEY (`question_id`) REFERENCES `questions` (`question_id`),
  CONSTRAINT `answer_later_fk1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer_later`
--

LOCK TABLES `answer_later` WRITE;
/*!40000 ALTER TABLE `answer_later` DISABLE KEYS */;
INSERT INTO `answer_later` VALUES (1,1,1),(2,1,1),(3,1,1);
/*!40000 ALTER TABLE `answer_later` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookmark`
--

DROP TABLE IF EXISTS `bookmark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookmark` (
  `bookmark_id` int(8) NOT NULL AUTO_INCREMENT,
  `question_id` int(8) NOT NULL,
  `user_id` int(8) NOT NULL,
  PRIMARY KEY (`bookmark_id`),
  KEY `bookmark_fk0` (`question_id`),
  KEY `bookmark_fk1` (`user_id`),
  CONSTRAINT `bookmark_fk0` FOREIGN KEY (`question_id`) REFERENCES `questions` (`question_id`),
  CONSTRAINT `bookmark_fk1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookmark`
--

LOCK TABLES `bookmark` WRITE;
/*!40000 ALTER TABLE `bookmark` DISABLE KEYS */;
/*!40000 ALTER TABLE `bookmark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `comment_id` int(8) NOT NULL AUTO_INCREMENT,
  `ans_id` int(8) NOT NULL,
  `user_id` int(8) NOT NULL,
  `comment_content` varchar(1500) NOT NULL,
  `comment_date` datetime(6) NOT NULL,
  PRIMARY KEY (`comment_id`),
  KEY `comment_fk0` (`ans_id`),
  KEY `comment_fk1` (`user_id`),
  CONSTRAINT `comment_fk0` FOREIGN KEY (`ans_id`) REFERENCES `answer` (`ans_id`),
  CONSTRAINT `comment_fk1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_us`
--

DROP TABLE IF EXISTS `contact_us`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contact_us` (
  `cu_id` int(11) NOT NULL AUTO_INCREMENT,
  `cu_name` varchar(30) NOT NULL,
  `cu_email_id` varchar(45) NOT NULL,
  `cu_mobile_no` varchar(45) NOT NULL,
  `cu_msg` varchar(500) NOT NULL,
  `cu_resolve` int(11) NOT NULL,
  PRIMARY KEY (`cu_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_us`
--

LOCK TABLES `contact_us` WRITE;
/*!40000 ALTER TABLE `contact_us` DISABLE KEYS */;
INSERT INTO `contact_us` VALUES (1,'Darshan','14ce049@charusat.edu.in','9558817087','hello\r\nlike your site\r\nthank you',0),(2,'Darshan','14ce049@charusat.edu.in','9558817087','hello\r\nlike your site\r\nthank you',0);
/*!40000 ALTER TABLE `contact_us` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `country` (
  `country_id` int(8) NOT NULL AUTO_INCREMENT,
  `country_name` varchar(30) NOT NULL,
  PRIMARY KEY (`country_id`),
  UNIQUE KEY `country_name` (`country_name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country`
--

LOCK TABLES `country` WRITE;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
INSERT INTO `country` VALUES (1,'India'),(2,'USA');
/*!40000 ALTER TABLE `country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `que_tag`
--

DROP TABLE IF EXISTS `que_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `que_tag` (
  `que_tag_id` int(8) NOT NULL AUTO_INCREMENT,
  `question_id` int(8) NOT NULL,
  `tag_id` int(8) NOT NULL,
  PRIMARY KEY (`que_tag_id`),
  KEY `que_tag_fk0` (`question_id`),
  KEY `que_tag_fk1` (`tag_id`),
  CONSTRAINT `que_tag_fk0` FOREIGN KEY (`question_id`) REFERENCES `questions` (`question_id`),
  CONSTRAINT `que_tag_fk1` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`tag_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `que_tag`
--

LOCK TABLES `que_tag` WRITE;
/*!40000 ALTER TABLE `que_tag` DISABLE KEYS */;
INSERT INTO `que_tag` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,2,1),(6,2,5),(7,2,6),(8,3,7),(9,3,6),(10,4,8),(11,5,8),(12,6,9);
/*!40000 ALTER TABLE `que_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `questions` (
  `question_id` int(8) NOT NULL AUTO_INCREMENT,
  `user_id` int(8) NOT NULL,
  `question_content` varchar(3000) NOT NULL,
  `title` varchar(1000) NOT NULL,
  `votes` int(8) NOT NULL DEFAULT '0',
  `delete_votes` int(8) NOT NULL DEFAULT '0',
  `que_date` datetime(6) NOT NULL,
  `views` int(8) NOT NULL DEFAULT '0',
  `question_image` varchar(100) DEFAULT NULL,
  `question_code` varchar(3000) DEFAULT NULL,
  PRIMARY KEY (`question_id`),
  KEY `questions_fk0` (`user_id`),
  CONSTRAINT `questions_fk0` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (1,1,'<p>dsakhasdjkhasjkdhkjashdjkadshjkashdjkhasdjk</p>','Problem in MYSQL',0,0,'2018-11-03 19:35:02.312203',0,NULL,NULL),(2,1,'<p>asdlkjasdljaslkdjlaskjdlkasjdklajdklajsdlkajsdklasjdlkasjdlkjasdkljasdkljklasjdklasjdklasjdklasjdklajskdljaskdljaskdljaskldjaskldjaskldjkasldjsakljdklasjdklsadjklasdjaskldjksaldjaskldjsadlkjaslkds</p>','Problem in MYSQL flask SQLAlchemy',0,0,'2018-11-03 19:35:35.707721',0,NULL,NULL),(3,2,'<p>askjdhaskjajsdhkjashdkjhdgjhghjgfdhagdsfhdadsgfhdghgdshfgahdsgfahjdsf</p>','SQL connection in python',0,0,'2018-11-03 19:37:48.843621',0,NULL,NULL),(4,2,'<br>','abcd',0,0,'2018-11-03 20:28:35.527399',0,NULL,NULL),(5,2,'<br>','abcd',0,0,'2018-11-03 20:29:30.687421',0,NULL,NULL),(6,2,'<br>','dvjas',0,0,'2018-11-03 20:29:50.227097',0,NULL,NULL);
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tag` (
  `tag_id` int(8) NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(50) NOT NULL,
  PRIMARY KEY (`tag_id`),
  UNIQUE KEY `tag_name` (`tag_name`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
INSERT INTO `tag` VALUES (3,'AngularJS'),(8,'bj'),(9,'bjadbskb'),(4,'Flask'),(1,'JAVA'),(2,'JS'),(6,'Python'),(7,'SQL'),(5,'SQLAlchemy');
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_id` int(8) NOT NULL AUTO_INCREMENT,
  `email_id` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) NOT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `mobile_no` varchar(10) DEFAULT NULL,
  `country_id` int(8) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `current_position` varchar(250) DEFAULT NULL,
  `college` varchar(200) DEFAULT NULL,
  `date_of_birth` datetime(6) NOT NULL,
  `up_votes` int(8) NOT NULL DEFAULT '0',
  `down_votes` int(8) NOT NULL DEFAULT '0',
  `date_of_reg` datetime(6) NOT NULL,
  `profile_pic` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email_id` (`email_id`),
  KEY `user_fk0` (`country_id`),
  CONSTRAINT `user_fk0` FOREIGN KEY (`country_id`) REFERENCES `country` (`country_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'sonivatsal111@gmail.com','abcd','Vatsal','R','Soni','Male','8511218967',1,NULL,NULL,'Developer','IIIT-H','2018-11-14 00:00:00.000000',0,0,'2018-11-03 19:33:45.316634','Screenshot (7).png'),(2,'darshan@gmail.com','abcd','Darshan','H','Kansagara','Male','',2,NULL,NULL,'Developer','IIIT-H','2018-11-13 00:00:00.000000',0,0,'2018-11-03 19:34:35.679112','Default.jpg'),(4,'kansagara.darshan97@gmail.com','darshan','Darshan','Hemantlal','Kansagara','Male','5558817087',1,NULL,NULL,'','','2012-06-01 00:00:00.000000',0,0,'2018-11-03 20:40:03.827255','Default.jpg');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-05 15:53:23
