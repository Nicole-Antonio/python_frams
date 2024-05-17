-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 06, 2023 at 05:21 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kaonashi`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance_records`
--

CREATE TABLE `attendance_records` (
  `attendance_id` int(11) NOT NULL,
  `student_no` varchar(20) DEFAULT NULL,
  `full_name` varchar(100) DEFAULT NULL,
  `subject` varchar(50) NOT NULL,
  `attendance_status` varchar(20) DEFAULT NULL,
  `time` varchar(20) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendance_records`
--

INSERT INTO `attendance_records` (`attendance_id`, `student_no`, `full_name`, `subject`, `attendance_status`, `time`, `date`) VALUES
(6, '19-44270', ' Ma. Nicole G. Antonio', ' Data Structures and Algorithm', ' Present', ' 11:01:35', '07/07/2023');

-- --------------------------------------------------------

--
-- Table structure for table `student_information`
--

CREATE TABLE `student_information` (
  `student_id` int(11) NOT NULL,
  `student_no` varchar(20) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `program` varchar(100) NOT NULL,
  `subject` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_information`
--

INSERT INTO `student_information` (`student_id`, `student_no`, `full_name`, `program`, `subject`) VALUES
(7, '19-44270', 'Ma. Nicole G. Antonio', 'BSIT', 'Data Structures and Algorithm'),
(9, '19-45809', 'Roland KIm G. Gerna', 'BSIT', 'Data Structures and Algorithm'),
(10, '19-44290', 'Renato B. Orque Jr.', 'BSIT', 'Data Structures and Algorithm'),
(11, '19-44292', 'Petrus Lex C. Valles', 'BSIT', 'Data Structures and Algorithm'),
(12, '18-44222', 'Ruth Ella D. Tangara', 'BSIT', 'Data Structures and Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `userid` int(11) NOT NULL,
  `full_name` varchar(200) NOT NULL,
  `mobileno` varchar(15) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userid`, `full_name`, `mobileno`, `username`, `password`) VALUES
(1, 'Nicole Antonio', '09957782739', 'admin', 'admin'),
(2, 'Ruth Ella Tangara', '09999999', 'Ruth', 'Ruth');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendance_records`
--
ALTER TABLE `attendance_records`
  ADD PRIMARY KEY (`attendance_id`);

--
-- Indexes for table `student_information`
--
ALTER TABLE `student_information`
  ADD PRIMARY KEY (`student_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendance_records`
--
ALTER TABLE `attendance_records`
  MODIFY `attendance_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `student_information`
--
ALTER TABLE `student_information`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
