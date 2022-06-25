-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 25, 2022 at 06:47 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `soa_news`
--

-- --------------------------------------------------------

--
-- Table structure for table `cloud_storage`
--

CREATE TABLE `cloud_storage` (
  `id` int(11) NOT NULL,
  `Username` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cloud_storage`
--

INSERT INTO `cloud_storage` (`id`, `Username`, `Password`) VALUES
(1, 'askhid', '1'),
(2, 'a', '1');

-- --------------------------------------------------------

--
-- Table structure for table `file`
--

CREATE TABLE `file` (
  `id` int(11) NOT NULL,
  `file` varchar(20) NOT NULL,
  `file_path` varchar(20) NOT NULL,
  `id_user` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `file`
--

INSERT INTO `file` (`id`, `file`, `file_path`, `id_user`) VALUES
(1, 'New_Etika_Profesi_7_', 'file/New_Etika_Profe', '1'),
(2, 'hoax.jpg', 'file/hoax.jpg', '1');

-- --------------------------------------------------------

--
-- Table structure for table `news`
--

CREATE TABLE `news` (
  `id` int(11) NOT NULL,
  `name_news` varchar(100) NOT NULL,
  `path` varchar(100) NOT NULL,
  `deleted` int(11) NOT NULL,
  `length` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `news`
--

INSERT INTO `news` (`id`, `name_news`, `path`, `deleted`, `length`) VALUES
(1, 'sempak', 'kerj', 0, '2022-06-24'),
(2, 'tod.ico', 'news/a.ico', 0, '2022-06-25'),
(3, 'pr_responsi_2.docx', 'news/pr_responsi_2.docx', 1, '2022-06-25'),
(4, 'Tugas_Responsi_Algoritma.docx', 'news/Tugas_Responsi_Algoritma.docx', 0, '2022-06-25'),
(5, 'name', 'name', 2, '2022-05-03');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(20) NOT NULL,
  `username` varchar(11) NOT NULL,
  `password` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`) VALUES
(1, '0', 1),
(2, 'askhid', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cloud_storage`
--
ALTER TABLE `cloud_storage`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `file`
--
ALTER TABLE `file`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cloud_storage`
--
ALTER TABLE `cloud_storage`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `file`
--
ALTER TABLE `file`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `news`
--
ALTER TABLE `news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
