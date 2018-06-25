-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: workshop
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.16.04.1

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
-- Table structure for table `runinfo`
--

DROP TABLE IF EXISTS `runinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `runinfo` (
  `run_number` int(10) unsigned NOT NULL,
  `run_type` tinytext,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `time_mins` float(8,3) DEFAULT NULL,
  `note` text NOT NULL,
  `target` tinytext,
  `beam_energy` float(10,3) DEFAULT NULL,
  `momentum` float(10,4) DEFAULT NULL,
  `angle` float(8,3) DEFAULT NULL,
  `charge` float(10,2) DEFAULT NULL,
  `event_count` int(10) unsigned DEFAULT NULL,
  `raster_x` float(3,2) DEFAULT NULL,
  `raster_y` float(3,2) DEFAULT NULL,
  `prescale_T1` int(10) unsigned DEFAULT NULL,
  `prescale_T2` int(10) unsigned DEFAULT NULL,
  `prescale_T3` int(10) unsigned DEFAULT NULL,
  `prescale_T4` int(10) unsigned DEFAULT NULL,
  `prescale_T5` int(10) unsigned DEFAULT NULL,
  `prescale_T6` int(10) unsigned DEFAULT NULL,
  `prescale_T7` int(10) unsigned DEFAULT NULL,
  `prescale_T8` int(10) unsigned DEFAULT NULL,
  `T1_count` int(10) DEFAULT NULL,
  `T2_count` int(10) DEFAULT NULL,
  `T3_count` int(10) DEFAULT NULL,
  `T4_count` int(10) DEFAULT NULL,
  `T5_count` int(10) DEFAULT NULL,
  `T6_count` int(10) DEFAULT NULL,
  `T7_count` int(10) DEFAULT NULL,
  `T8_count` int(10) DEFAULT NULL,
  `comment` text,
  `end_comment` text,
  `modify_time` datetime DEFAULT NULL,
  PRIMARY KEY (`run_number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `runinfo`
--

LOCK TABLES `runinfo` WRITE;
/*!40000 ALTER TABLE `runinfo` DISABLE KEYS */;
INSERT INTO `runinfo` VALUES (1212,'Production',NULL,NULL,20.220,'created from logbook','He3',10589.900,3.1002,17.584,NULL,4781239,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'3-He, XA, YA, XB, YB = 1.6, 0.5, 3.3, 0.0 ps1, 2, 3, = 1, 1, 1, 20 micro amps, raster on','Run_type=Production,target_type=He3,comment_text=3-He, XA, YA, XB, YB = 1.6, 0.5, 3.3, 0.0 ps1, 2, 3, = 1, 1, 1, 20 micro amps, raster on','2018-06-24 23:25:07'),(1213,'Production',NULL,NULL,23.190,'created from logbook','H2',10589.900,3.1003,17.584,NULL,6687965,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'1-H, XA, YA, XB, YB = 1.6, 0.5, 3.3, 0.0 ps1, 2, 3, = 1, 1, 1, 20 micro amps, raster on','Run_type=Production,target_type=H2,comment_text=1-H, XA, YA, XB, YB = 1.6, 0.5, 3.3, 0.0 ps1, 2, 3, = 1, 1, 1, 20 micro amps, raster on','2018-06-24 23:15:24'),(1215,'Production',NULL,NULL,30.224,'created from logbook','T2',10589.900,3.1002,17.584,NULL,9643234,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'3-H=T_2, XA, YA, XB, YB = 1.6, 0.5, 3.3, 0.0 ps1, 2, 3, = 1, 1, 1, 20 micro amps, raster on','Run_type=Production,target_type=T2,comment_text=3-H=T_2, XA, YA, XB, YB = 1.6, 0.5, 3.3, 0.0 ps1, 2, 3, = 1, 1, 1, 20 micro amps, raster on','2018-06-25 10:02:36'),(1217,'Production',NULL,NULL,28.804,'created from logbook','MT',10591.500,3.1002,17.584,NULL,5938315,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,' XA, YA, XB, YB = 1.6, 0.5, 3.3, 0.0 ps1, 2, 3, = 1, 1, 1, 20 micro amps, raster on','Run_type=Production,target_type=MT,comment_text= XA, YA, XB, YB = 1.6, 0.5, 3.3, 0.0 ps1, 2, 3, = 1, 1, 1, 20 micro amps, raster on','2018-06-25 10:02:55'),(1219,'Production',NULL,NULL,30.274,'created from logbook','He3',10591.500,3.1003,17.585,NULL,5619615,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'XA, YA, XB, YB = 1.6, 0.5, 3.3, 0.0 ps1, 2, 3, = 1, 1, 1, 20 micro amps, raster on, FADC mode 10','Run_type=Production,target_type=He3,comment_text=XA, YA, XB, YB = 1.6, 0.5, 3.3, 0.0 ps1, 2, 3, = 1, 1, 1, 20 micro amps, raster on,','2018-06-25 10:02:43'),(2324,'Optics',NULL,NULL,33.241,'created from logbook','Optics',0.000,3.8500,17.587,NULL,209582,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Optics step 1 but with optics target : Q1 at 847.46','Run_type=Optics,target_type=Optics,comment_text=Optics step 1 but with optics target : Q1 at 847.46','2018-06-25 10:02:47');
/*!40000 ALTER TABLE `runinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-25 10:19:54
