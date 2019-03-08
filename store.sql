-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 08, 2019 at 07:44 AM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `store`
--

-- --------------------------------------------------------

--
-- Table structure for table `fruits`
--

CREATE TABLE `fruits` (
  `item_id` int(10) NOT NULL,
  `item_name` varchar(50) NOT NULL,
  `price_per_kg` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fruits`
--

INSERT INTO `fruits` (`item_id`, `item_name`, `price_per_kg`) VALUES
(1, 'Green Apple', 200),
(2, 'Banana', 100),
(3, 'Mango', 200),
(4, 'Orange', 1000),
(5, 'Papaw', 200),
(6, 'Pineapple', 2000),
(7, 'Red Apple', 4000),
(8, 'Strawberry', 4000);

-- --------------------------------------------------------

--
-- Table structure for table `recieve`
--

CREATE TABLE `recieve` (
  `recieve_id` int(10) NOT NULL,
  `date` date NOT NULL,
  `company_name` varchar(50) NOT NULL,
  `user_id` int(10) NOT NULL,
  `quantity_kg` int(10) NOT NULL,
  `total_price` int(10) NOT NULL,
  `item_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `recieve`
--

INSERT INTO `recieve` (`recieve_id`, `date`, `company_name`, `user_id`, `quantity_kg`, `total_price`, `item_id`) VALUES
(1, '2019-01-12', 'daraz', 1, 200, 40000, 1),
(2, '2019-01-27', 'daraz', 38, 100, 2000, 1),
(5, '2019-01-25', 'daraz', 1, 200, 4000, 2),
(6, '2019-01-26', 'daraz', 38, 100, 2000, 2),
(7, '2019-01-18', 'daraz', 1, 100, 10000, 3),
(10, '2019-01-27', 'daraz', 40, 100, 2000, 4),
(11, '2019-01-07', 'daraz', 40, 10, 200, 4),
(12, '2019-01-23', 'daraz', 1, 100, 20000, 6),
(13, '2019-02-21', 'daraz', 40, 100, 20000, 7),
(14, '2019-01-27', 'daraz', 38, 400, 30000, 3);

-- --------------------------------------------------------

--
-- Table structure for table `stores`
--

CREATE TABLE `stores` (
  `store_id` int(10) NOT NULL,
  `item_id` int(10) NOT NULL,
  `item_name` varchar(20) NOT NULL,
  `quantity` int(10) NOT NULL,
  `total_price` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stores`
--

INSERT INTO `stores` (`store_id`, `item_id`, `item_name`, `quantity`, `total_price`) VALUES
(1, 1, 'Green Apple', 100, 20000),
(3, 2, 'Banana', 200, 7000),
(4, 3, 'Mango', 900, 89000),
(6, 4, 'Orange', 80, 1900),
(7, 6, 'Pineapple', 100, 20000),
(8, 7, 'Red Apple', 100, 20000);

-- --------------------------------------------------------

--
-- Table structure for table `supply`
--

CREATE TABLE `supply` (
  `sup_id` int(10) NOT NULL,
  `date` date NOT NULL,
  `company_name` varchar(20) NOT NULL,
  `item_id` int(10) NOT NULL,
  `quantity_kg` int(10) NOT NULL,
  `total_price` int(20) NOT NULL,
  `user_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `supply`
--

INSERT INTO `supply` (`sup_id`, `date`, `company_name`, `item_id`, `quantity_kg`, `total_price`, `user_id`) VALUES
(1, '2019-01-16', 'daraz', 1, 100, 20010, 1),
(2, '2019-01-22', 'daraz', 2, 100, 2000, 38),
(3, '2019-01-23', 'daraz', 2, 100, 1000, 1),
(4, '2019-01-20', 'daraz', 4, 10, 200, 39),
(5, '2019-01-20', 'daraz', 4, 20, 100, 40),
(6, '2019-01-28', 'daraz', 3, 100, 1000, 1);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(10) NOT NULL,
  `user_name` varchar(20) NOT NULL,
  `password` varchar(8) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `user_name`, `password`, `email`) VALUES
(1, 'D.D. Ranasinghe', '12345678', 'dinushi@gmail.com'),
(38, 'W.A.R Shehana', '12345678', 'rashmishehana@gmail.com'),
(39, 'A.V.P Sewwandi', '12345678', 'piyumika@gmail.com'),
(40, 'P.R.H.G Priyadarshan', '12345678', 'gayan@gmail.com'),
(41, 'Devindi Randeniya', '12345678', 'devindi@gmail.com'),
(42, 'Amana Randeniya', '12345678', 'amana@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fruits`
--
ALTER TABLE `fruits`
  ADD PRIMARY KEY (`item_id`);

--
-- Indexes for table `recieve`
--
ALTER TABLE `recieve`
  ADD PRIMARY KEY (`recieve_id`),
  ADD KEY `FK_item_id` (`item_id`),
  ADD KEY `FK_user_id` (`user_id`);

--
-- Indexes for table `stores`
--
ALTER TABLE `stores`
  ADD PRIMARY KEY (`store_id`),
  ADD KEY `FK_items_id` (`item_id`);

--
-- Indexes for table `supply`
--
ALTER TABLE `supply`
  ADD PRIMARY KEY (`sup_id`),
  ADD KEY `FK_item_ids` (`item_id`),
  ADD KEY `FK_user_ids` (`user_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `fruits`
--
ALTER TABLE `fruits`
  MODIFY `item_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `recieve`
--
ALTER TABLE `recieve`
  MODIFY `recieve_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `stores`
--
ALTER TABLE `stores`
  MODIFY `store_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `supply`
--
ALTER TABLE `supply`
  MODIFY `sup_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `recieve`
--
ALTER TABLE `recieve`
  ADD CONSTRAINT `FK_item_id` FOREIGN KEY (`item_id`) REFERENCES `fruits` (`item_id`),
  ADD CONSTRAINT `FK_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);

--
-- Constraints for table `stores`
--
ALTER TABLE `stores`
  ADD CONSTRAINT `FK_items_id` FOREIGN KEY (`item_id`) REFERENCES `fruits` (`item_id`);

--
-- Constraints for table `supply`
--
ALTER TABLE `supply`
  ADD CONSTRAINT `FK_item_ids` FOREIGN KEY (`item_id`) REFERENCES `fruits` (`item_id`),
  ADD CONSTRAINT `FK_user_ids` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
