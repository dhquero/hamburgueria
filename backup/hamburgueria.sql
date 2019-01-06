-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: hamburgueria
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `cliente` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `endereco` varchar(80) NOT NULL,
  `cidade` varchar(40) NOT NULL,
  `estado` char(2) NOT NULL,
  `pais` char(2) NOT NULL,
  `telefone` varchar(15) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `data_nascimento` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'Daniel','Rua das Flores, 205','Garça','SP','BR','(14) 98821-8372','92323112200','1995-06-17'),(2,'João','Rua Joaquina, 9933','Maília','SP','BR','(14) 99834-9283','56782948275','2000-09-12');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `colaborador`
--

DROP TABLE IF EXISTS `colaborador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `colaborador` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `endereco` varchar(80) NOT NULL,
  `cidade` varchar(40) NOT NULL,
  `estado` char(2) NOT NULL,
  `pais` char(2) NOT NULL,
  `telefone` varchar(15) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `data_nascimento` date NOT NULL,
  `funcao` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colaborador`
--

LOCK TABLES `colaborador` WRITE;
/*!40000 ALTER TABLE `colaborador` DISABLE KEYS */;
INSERT INTO `colaborador` VALUES (0,'Pedido online','x','x','x','x','x','x','2019-01-05','Sistema'),(1,'Joaquim','Av Brasil, 72','Marília','SP','BR','(11) 98823-4536','45389764013','1987-09-11','Administrador'),(2,'Maria','Al do Chá, 231','Garça','SP','BR','(12) 97283-0998','73894781234','1994-01-22','Garçom');
/*!40000 ALTER TABLE `colaborador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hamburguer`
--

DROP TABLE IF EXISTS `hamburguer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `hamburguer` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `valor` decimal(6,2) unsigned DEFAULT '0.00',
  `ingredientes` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hamburguer`
--

LOCK TABLES `hamburguer` WRITE;
/*!40000 ALTER TABLE `hamburguer` DISABLE KEYS */;
INSERT INTO `hamburguer` VALUES (1,'X-Salada',10.00,'Pão, salada, hamburguer'),(2,'X-Egg',12.30,'Pão, salada, hamburguer, ovo'),(3,'X-Bacon',11.40,'Pão, salada, hamburguer, bacon'),(4,'X-Tudo',15.45,'Pão, salada, hamburguer, ovo, bacon, batata palha');
/*!40000 ALTER TABLE `hamburguer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item_pedido`
--

DROP TABLE IF EXISTS `item_pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `item_pedido` (
  `id_pedido` int(11) unsigned NOT NULL,
  `id_hamburguer` int(11) unsigned NOT NULL,
  `quantidade` varchar(45) NOT NULL,
  `valor` decimal(6,2) unsigned NOT NULL DEFAULT '0.00',
  `observacao` text,
  UNIQUE KEY `idx_pedido_item` (`id_pedido`,`id_hamburguer`),
  KEY `fk_id_hamburguer_idx` (`id_hamburguer`),
  CONSTRAINT `fk_id_hamburguer` FOREIGN KEY (`id_hamburguer`) REFERENCES `hamburguer` (`id`),
  CONSTRAINT `fk_id_pedido` FOREIGN KEY (`id_pedido`) REFERENCES `pedido` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item_pedido`
--

LOCK TABLES `item_pedido` WRITE;
/*!40000 ALTER TABLE `item_pedido` DISABLE KEYS */;
INSERT INTO `item_pedido` VALUES (1,1,'2',14.23,NULL),(1,2,'1',10.20,NULL),(2,2,'1',10.50,NULL),(2,3,'2',11.45,NULL),(3,3,'2',0.00,'SEM MAIONESE'),(3,4,'3',0.00,'MAIS BATATA'),(16,1,'4',0.00,NULL),(16,3,'2',0.00,'SEM MOLHO'),(17,1,'2',0.00,'TIRAR CARNE'),(17,3,'2',0.00,NULL),(18,3,'2',0.00,'A'),(19,2,'3',0.00,'RETIRAR SALADA DE 1 UNDIADE'),(19,4,'3',0.00,NULL);
/*!40000 ALTER TABLE `item_pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedido`
--

DROP TABLE IF EXISTS `pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `pedido` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id_colaborador` int(10) unsigned DEFAULT NULL,
  `id_cliente` int(10) unsigned DEFAULT NULL,
  `data` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `observacao` text,
  `status` enum('aberto','em processamento','em entrega','finalizado') DEFAULT 'aberto',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `idx_cliente_data` (`id_cliente`,`data`),
  KEY `fk_id_colaborador_idx` (`id_colaborador`),
  CONSTRAINT `fk_id_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id`),
  CONSTRAINT `fk_id_colaborador` FOREIGN KEY (`id_colaborador`) REFERENCES `colaborador` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedido`
--

LOCK TABLES `pedido` WRITE;
/*!40000 ALTER TABLE `pedido` DISABLE KEYS */;
INSERT INTO `pedido` VALUES (1,1,1,'2019-01-05 10:37:07',NULL,'em processamento'),(2,2,2,'2019-01-05 10:37:21',NULL,'aberto'),(3,0,1,'2019-01-05 10:37:36','TESTE ALTERACAO','aberto'),(4,1,2,'2019-01-05 10:37:36',NULL,'aberto'),(5,1,1,'2019-01-05 10:45:45',NULL,'aberto'),(6,0,1,'2019-01-05 12:55:25',NULL,'aberto'),(16,0,1,'2019-01-05 18:10:27','PEDIDO 15','aberto'),(17,0,1,'2019-01-05 20:18:25','OI','aberto'),(18,0,1,'2019-01-06 11:39:59','ALTERACAO DO PEDIDO','aberto'),(19,0,1,'2019-01-06 13:11:47','LANCHES SEM CONDIMENTOS','aberto');
/*!40000 ALTER TABLE `pedido` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-06 13:19:12
