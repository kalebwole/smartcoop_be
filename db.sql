-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 29, 2024 at 08:33 AM
-- Server version: 5.7.15-log
-- PHP Version: 7.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smartscoop`
--

-- --------------------------------------------------------

--
-- Table structure for table `cooperative`
--

CREATE TABLE `cooperative` (
  `id` int(11) NOT NULL,
  `cooperativename` varchar(100) NOT NULL,
  `coop_id` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `logo` varchar(100) NOT NULL,
  `subscription` varchar(100) NOT NULL,
  `status` varchar(10) NOT NULL DEFAULT 'active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `cooperative`
--

INSERT INTO `cooperative` (`id`, `cooperativename`, `coop_id`, `email`, `password`, `logo`, `subscription`, `status`) VALUES
(3, 'fagrem1', '81b38cd0c8', 'jesusboyonline@gmail.com1', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '', '', 'active'),
(4, 'dddsssss', 'd50544f7ec', 'b@gmail.com', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', '', '', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `cooperative_members`
--

CREATE TABLE `cooperative_members` (
  `id` int(11) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phoneno` varchar(100) NOT NULL,
  `address` longtext NOT NULL,
  `staff_id` varchar(100) NOT NULL,
  `dob` datetime NOT NULL,
  `password` varchar(100) NOT NULL,
  `wallet` int(11) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL DEFAULT 'active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `cooperative_members`
--

INSERT INTO `cooperative_members` (`id`, `fullname`, `email`, `phoneno`, `address`, `staff_id`, `dob`, `password`, `wallet`, `photo`, `gender`, `status`) VALUES
(1, 'sam', 'email@gmail,com', '000000', '222222', '1233', '0000-00-00 00:00:00', '', 0, '', 'male', 'active'),
(2, 'Clement Samuel', 'jesusboyonline@gmail.com', '08138209953', '1 Adebayo', '1', '2024-06-28 00:00:00', '', 0, '', 'Male', 'active'),
(3, 'Akin Akin', 'contactketral@gmail.com', '09068263747', 'Oye-Egbo', '1', '0001-11-11 00:00:00', '', 0, '', 'Male', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `member_cooperatives`
--

CREATE TABLE `member_cooperatives` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `cooperative_id` varchar(100) NOT NULL,
  `date_added` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cooperative`
--
ALTER TABLE `cooperative`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cooperative_members`
--
ALTER TABLE `cooperative_members`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `member_cooperatives`
--
ALTER TABLE `member_cooperatives`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cooperative`
--
ALTER TABLE `cooperative`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `cooperative_members`
--
ALTER TABLE `cooperative_members`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `member_cooperatives`
--
ALTER TABLE `member_cooperatives`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
