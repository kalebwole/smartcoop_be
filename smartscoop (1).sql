-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 07, 2024 at 08:22 PM
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
(4, 'dddsssss', 'd50544f7ec', 'b@gmail.com', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', '', '', 'active'),
(5, 'dddaa', 'a4bee3df43', 'studen1t@gmail.com', '4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8', '', '', 'active');

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
(2, 'Clement Samuel', 'jesusboyonline@gmail.com', '08138209953', '1 Adebayo', '1', '2024-06-28 00:00:00', '', 100000, '', 'Male', 'active'),
(3, 'Akin Akin', 'contactketral@gmail.com', '09068263747', 'Oye-Egbo', '2', '0001-11-11 00:00:00', '', 0, '', 'Male', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `coop_loantypes`
--

CREATE TABLE `coop_loantypes` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `interest_rate` varchar(100) NOT NULL,
  `loan_type` varchar(100) NOT NULL,
  `availability` varchar(100) NOT NULL,
  `coop_id` varchar(100) NOT NULL,
  `requiredAmount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `coop_loantypes`
--

INSERT INTO `coop_loantypes` (`id`, `title`, `interest_rate`, `loan_type`, `availability`, `coop_id`, `requiredAmount`) VALUES
(8, 'Normal', '10', 'straigthLine', 'members', 'd50544f7ec', 0),
(9, 'Emergency', '15', 'straigthLine', 'all', 'd50544f7ec', 0),
(10, 'Special Loan', '15', 'straigthLineUpfront', 'all', 'd50544f7ec', 0),
(11, 'Commodity - Rice', '2', 'reducing', 'all', 'd50544f7ec', 0),
(12, 'Commodity - House Projects', '10', 'reducing', 'members', 'd50544f7ec', 50);

-- --------------------------------------------------------

--
-- Table structure for table `loan_application`
--

CREATE TABLE `loan_application` (
  `id` int(11) NOT NULL,
  `loan_id` varchar(20) NOT NULL,
  `coop_id` varchar(20) NOT NULL,
  `staff_id` varchar(20) NOT NULL,
  `principal` int(11) NOT NULL,
  `tenure` int(11) NOT NULL,
  `loan_type` int(11) NOT NULL,
  `total_interest` int(11) NOT NULL,
  `monthly_interest` int(11) NOT NULL,
  `monthly_repayment` int(11) NOT NULL,
  `amount_disbursed` int(11) NOT NULL,
  `amount_paid` int(11) NOT NULL,
  `total_loan` int(11) NOT NULL,
  `approved_status` varchar(20) NOT NULL DEFAULT 'not approved',
  `approved_date` datetime NOT NULL,
  `request_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` varchar(20) NOT NULL DEFAULT 'not active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `loan_application`
--

INSERT INTO `loan_application` (`id`, `loan_id`, `coop_id`, `staff_id`, `principal`, `tenure`, `loan_type`, `total_interest`, `monthly_interest`, `monthly_repayment`, `amount_disbursed`, `amount_paid`, `total_loan`, `approved_status`, `approved_date`, `request_date`, `status`) VALUES
(1, '6452076696', 'd50544f7ec', '1', 100000, 13, 0, 10829, 833, 8333, 100000, 0, 110829, 'not approved', '0000-00-00 00:00:00', '2024-07-07 21:10:16', 'not active');

-- --------------------------------------------------------

--
-- Table structure for table `loan_payment_history`
--

CREATE TABLE `loan_payment_history` (
  `id` int(11) NOT NULL,
  `loan_id` int(11) NOT NULL,
  `amount_to_pay` int(11) NOT NULL,
  `amount_paid` int(11) NOT NULL,
  `staff_id` varchar(100) NOT NULL,
  `coop_id` varchar(100) NOT NULL,
  `next_due` datetime NOT NULL,
  `status` varchar(100) NOT NULL DEFAULT 'not paid'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `loan_payment_history`
--

INSERT INTO `loan_payment_history` (`id`, `loan_id`, `amount_to_pay`, `amount_paid`, `staff_id`, `coop_id`, `next_due`, `status`) VALUES
(1, 2147483647, 0, 0, '1', 'd50544f7ec', '2024-08-06 00:00:00', 'not paid'),
(2, 2147483647, 8333, 0, '1', 'd50544f7ec', '2024-09-05 00:00:00', 'not paid'),
(3, 2147483647, 8333, 0, '1', 'd50544f7ec', '2024-10-05 00:00:00', 'not paid'),
(4, 2147483647, 8333, 0, '1', 'd50544f7ec', '2024-11-04 00:00:00', 'not paid'),
(5, 2147483647, 8333, 0, '1', 'd50544f7ec', '2024-12-04 00:00:00', 'not paid'),
(6, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-01-03 00:00:00', 'not paid'),
(7, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-02-02 00:00:00', 'not paid'),
(8, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-03-04 00:00:00', 'not paid'),
(9, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-04-03 00:00:00', 'not paid'),
(10, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-05-03 00:00:00', 'not paid'),
(11, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-06-02 00:00:00', 'not paid'),
(12, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-07-02 00:00:00', 'not paid'),
(13, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-08-01 00:00:00', 'not paid'),
(14, 2147483647, 0, 0, '1', 'd50544f7ec', '2024-08-06 00:00:00', 'not paid'),
(15, 2147483647, 8333, 0, '1', 'd50544f7ec', '2024-09-05 00:00:00', 'not paid'),
(16, 2147483647, 8333, 0, '1', 'd50544f7ec', '2024-10-05 00:00:00', 'not paid'),
(17, 2147483647, 8333, 0, '1', 'd50544f7ec', '2024-11-04 00:00:00', 'not paid'),
(18, 2147483647, 8333, 0, '1', 'd50544f7ec', '2024-12-04 00:00:00', 'not paid'),
(19, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-01-03 00:00:00', 'not paid'),
(20, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-02-02 00:00:00', 'not paid'),
(21, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-03-04 00:00:00', 'not paid'),
(22, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-04-03 00:00:00', 'not paid'),
(23, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-05-03 00:00:00', 'not paid'),
(24, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-06-02 00:00:00', 'not paid'),
(25, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-07-02 00:00:00', 'not paid'),
(26, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-08-01 00:00:00', 'not paid'),
(27, 2147483647, 0, 0, '1', 'd50544f7ec', '2024-08-06 00:00:00', 'not paid'),
(28, 2147483647, 8333, 0, '1', 'd50544f7ec', '2024-09-05 00:00:00', 'not paid'),
(29, 2147483647, 8333, 0, '1', 'd50544f7ec', '2024-10-05 00:00:00', 'not paid'),
(30, 2147483647, 8333, 0, '1', 'd50544f7ec', '2024-11-04 00:00:00', 'not paid'),
(31, 2147483647, 8333, 0, '1', 'd50544f7ec', '2024-12-04 00:00:00', 'not paid'),
(32, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-01-03 00:00:00', 'not paid'),
(33, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-02-02 00:00:00', 'not paid'),
(34, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-03-04 00:00:00', 'not paid'),
(35, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-04-03 00:00:00', 'not paid'),
(36, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-05-03 00:00:00', 'not paid'),
(37, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-06-02 00:00:00', 'not paid'),
(38, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-07-02 00:00:00', 'not paid'),
(39, 2147483647, 8333, 0, '1', 'd50544f7ec', '2025-08-01 00:00:00', 'not paid');

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
-- Indexes for table `coop_loantypes`
--
ALTER TABLE `coop_loantypes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `loan_application`
--
ALTER TABLE `loan_application`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `loan_payment_history`
--
ALTER TABLE `loan_payment_history`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `cooperative_members`
--
ALTER TABLE `cooperative_members`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `coop_loantypes`
--
ALTER TABLE `coop_loantypes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `loan_application`
--
ALTER TABLE `loan_application`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `loan_payment_history`
--
ALTER TABLE `loan_payment_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;
--
-- AUTO_INCREMENT for table `member_cooperatives`
--
ALTER TABLE `member_cooperatives`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
