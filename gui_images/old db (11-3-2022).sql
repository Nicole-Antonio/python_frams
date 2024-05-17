-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 03, 2022 at 04:39 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

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
  `last_name` varchar(100) DEFAULT NULL,
  `attendance_status` varchar(20) DEFAULT NULL,
  `time` varchar(20) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `student_information`
--

CREATE TABLE `student_information` (
  `student_id` int(11) NOT NULL,
  `student_no` varchar(20) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `program` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student_information`
--

INSERT INTO `student_information` (`student_id`, `student_no`, `first_name`, `middle_name`, `last_name`, `program`) VALUES
(1, '18-41785', 'Ruth Ella', 'Dulfo', 'Tangara', 'BSIT'),
(4, '19-44270', 'Ma. Nicole', 'Gulpric', 'Antonio', 'BSIT'),
(7, '19-44444', 'Joshua', 'Rivera', 'Habla', 'BSIT'),
(8, '19-45809', 'Roland Kim', 'Gapud', 'Gerna', 'BSCS'),
(22, '18-41786', 'Kassandra', 'Dela Cruz', 'Lopez', 'BSIT'),
(23, '19-46801', 'Krishanel', 'Ola', 'Reyes', 'BSCS'),
(24, '19-45732', 'Laramie', 'Cabais', 'Abug', 'BSCS'),
(25, '19-45541', 'Lorraine alexandra', 'Pecenio', 'Maiso', 'BSCS'),
(26, '19-45593', 'Christine joy', 'Discaya', 'Galvez', 'BSCS'),
(27, '19-45187', 'Glen Bernard', 'Vichozo', 'Asistio', 'BSCS'),
(28, '19 46637', 'Mike Lyxen', 'Ecleo', 'Gagala', 'BSCS'),
(29, '19-46377', 'Joan', 'Yape', 'Caratay', 'BSCS'),
(30, '19-46574', 'Mark Joseph', 'Cruda', 'Orale', 'Bscs'),
(31, '19-46611', 'Alita', 'Valdenor', 'Badaran', 'BSCS'),
(32, '19-45829', 'Zikki Anne', 'Ditalo', 'De Luna', 'BSCS'),
(33, '19-46467', 'Ruel', 'Flores', 'Mananquil', 'BSCS'),
(34, '19-45316', 'Brent Kerr', 'Ladiao', 'Cafe', 'BSCS'),
(35, '19-45199', 'Eric ', 'Juanite', 'Baris', 'BSCS'),
(36, '19-43843', 'Carl Jonhson', 'Arca', 'Laguitan', 'BSCS'),
(37, '19-45953', 'Lara', 'Orcuse', 'Oplado', 'BSCS'),
(38, '19-45954', 'Angel Clarisse', 'Mananquil', 'Geradila', 'BSCS'),
(39, '18-42780', 'Sheena', 'Diamsay', 'Abucay', 'BSCS'),
(40, '18-42268', 'Franchesca', 'Borja', 'Operario', 'BSCS'),
(41, '18-42934', 'Kiezelyn', 'Cidro', 'Tegio', 'BSCS'),
(42, '19-46570', 'Dianne', 'Duron', 'Casilliano', 'BSCS'),
(43, '19-44503', 'Lovely', 'Palce', 'Buenafe', 'BSCS'),
(44, '19-44163', 'Vic Robert', 'Bo', 'Buenafe', 'BSCS'),
(45, '19-45886', 'Karen Joy', 'Cidro', 'Aludo', 'BSCS'),
(46, '19-46824', 'Abegail', 'Verana', 'Capas', 'BSCS'),
(47, '19-46598', 'Jovelyn', 'Ebayan', 'Nofies', 'BSCS'),
(48, '19-47178', 'Warren', 'Ato', 'Anos', 'BSCS'),
(49, '19-46469', 'Rona', 'Aguirre', 'Ausa', 'BSCS'),
(50, '19-44180', 'Ivan', 'Cidro', 'Nakpil', 'BSCS '),
(51, '19 - 46438', 'Cedrix Jhon ', 'Abenales', 'Busa', 'BSCS'),
(52, '19-47015', 'Lorenz', 'Robredillo', 'Duquez', 'BSCS'),
(53, '19-45097', 'Delian', 'Acopio', 'Bueno', 'BSCS'),
(54, '09-24214', 'Jesica', 'Arre', 'Diga', 'BSCS'),
(55, '19-44915', 'Ma. Terissa', 'Lopinac', 'Lubat', 'BSCS'),
(56, '19-44805', 'Jay-ar', 'Adesas', 'Sumbilla', 'BSCS'),
(57, '19-44624', 'Anna Lyn', 'Delima', 'Caluracan', 'BSCS'),
(59, '19-44292', 'Petrus Lex', 'Cinco', 'Valles', 'BSIT');

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userid`, `full_name`, `mobileno`, `username`, `password`) VALUES
(1, 'Nicole Antonio', '09957782739', 'admin', 'admin');

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
  MODIFY `attendance_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `student_information`
--
ALTER TABLE `student_information`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
