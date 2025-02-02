-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2024-05-21 17:56:06
-- 伺服器版本： 10.4.32-MariaDB
-- PHP 版本： 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `card`
--

-- --------------------------------------------------------

--
-- 資料表結構 `card_book`
--

CREATE TABLE `card_book` (
  `CID` varchar(16) NOT NULL,
  `name` varchar(16) NOT NULL,
  `attack` int(11) NOT NULL,
  `denfse` int(11) NOT NULL,
  `effect` text NOT NULL,
  `own` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `card_book`
--

INSERT INTO `card_book` (`CID`, `name`, `attack`, `denfse`, `effect`, `own`) VALUES
('11443677', '青眼暴君龍', 3400, 2900, '「青眼白龍」＋龍族怪獸\r\n此卡用融合召喚以及以下方法才能從額外牌組特殊召喚。\r\n●把有融合怪獸裝備的1體我方「青眼白龍」解放之場合可以從額外牌組特殊召喚。\r\n①：場上之此卡不受陷阱卡的效果影響。\r\n②：此卡可以向對方怪獸全部各作1次攻擊。\r\n③：1回合1次，此卡進行戰鬥的傷害步驟結束時，以我方墓地1張陷阱卡為對象才能發動。\r\n該卡在我方魔法與陷阱區域放置。', 1),
('2129638', '青眼雙爆裂龍', 3000, 2500, '「青眼白龍」+「青眼白龍」 此卡僅能以融合召喚以及以下的方法特殊召喚。 \r\n●從我方的怪獸區域將上述卡片送入墓地才能從額外牌組特殊召喚。\r\n(1)：此卡不會被戰鬥破壞。\r\n(2)：此卡可以在1次戰鬥階段中向怪獸進行2次攻擊。\r\n(3)：此卡的攻擊沒有將對手怪獸戰鬥破壞的傷害步驟結束時可以發動。該對手怪獸除外。', 1),
('23995346', '青眼究極龍', 4500, 3800, '青眼白龍+青眼白龍+青眼白龍', 1),
('30576089', '青眼噴射龍', 3000, 0, '此卡名的①③效果1回合各僅能使用1次。\r\n我方場上或墓地有「青眼白龍」存在的場合才能把此卡效果發動。\r\n①：此卡於手牌﹒墓地存在，場上的卡被戰鬥﹒效果破壞的場合才能發動。此卡特殊召喚。\r\n②：此卡以外我方場上的卡不會被對方效果破壞。\r\n③：此卡進行戰鬥的傷害步驟開始時，以對方場上1張卡為對象才能發動。該卡回到原持有者手牌。', 1),
('38517737', '青眼亞白龍', 3000, 2500, '此卡不能通常召喚，從手札將1體「青眼白龍」給對手確認才能特殊召喚。\r\n1回合僅1次能以此方法將「青眼亞白龍」特殊召喚。 \r\n(1)：此卡於場上、墓地存在為限，卡名視為「青眼白龍」。 \r\n(2)： 1回合1次，可以對手場上1體怪獸為對象發動。 該怪獸破壞。 發動此效果的回合此卡不能攻擊。', 0),
('43228023', '青眼究極亞龍', 4500, 3800, '「青眼白龍」+「青眼白龍」+「青眼白龍」\r\n(1)：此卡於怪獸區存在為限，此卡不會被對手效果破壞，對手不能以此卡作為效果對象。\r\n(2)：1回合1次，以對手場上的卡片1枚為對象可發動。將該卡破壞。\r\n以原卡名為「青眼亞白龍」的怪獸為素材而將此卡融合召喚出場的場合，此效果的對象可取2枚或3枚。\r\n欲發動此效果的回合，此卡不能攻擊。', 1),
('55410871', '青眼混沌MAX龍', 4000, 0, '以「混沌型態」降臨。 此卡僅能以儀式召喚的方式特殊召喚。\r\n(1)： 此卡不會成為對手的卡片效果的對象，不會被對手的卡片效果破壞。\r\n(2)： 此卡向守備表示怪獸進行攻擊的場合，給予該攻擊力超過守備力的2倍數值的戰鬥傷害。', 1),
('56532353', '真青眼究極龍', 4500, 3800, '「青眼白龍」+「青眼白龍」+「青眼白龍」 「真青眼究極龍」的(1)效果1回合僅能使用2次。\r\n(1)： 以融合召喚方式出場的此卡進行攻擊的傷害步驟結束時，我方場上表側表示的卡片僅有此卡的場合，\r\n可以從額外牌組將1體「青眼」之名的融合怪獸送入墓地發動。 此卡可以繼續攻擊。\r\n(2)： 以我方場上的「青眼」之名的怪獸作為對象的魔法、陷阱、怪獸效果發動時，\r\n可以將墓地的此卡除外發動。 該發動無效並破壞。', 1),
('59822133', '青眼精靈龍', 2500, 3000, '協調+協調以外的「青眼」怪獸1體以上\r\n(1)：此卡於怪獸區存在為限，雙方不能將2體以上的怪獸同時特殊召喚。\r\n(2)：1回合1次，墓地的卡片效果發動時可發動。\r\n將其發動無效。\r\n(3)：在我方・對手回合，將同步召喚出場的此卡解放可發動。\r\n從額外牌組將「青眼精靈龍」以外的龍族・光屬性同步怪獸1體以守備表示特殊召喚。\r\n該怪獸在此回合的結束階段破壞。', 1),
('89631139', '青眼白龍', 3000, 2500, '以高攻擊力著稱的傳奇之龍。任何對手都能粉碎，其破壞力難以估計。', 1);

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `card_book`
--
ALTER TABLE `card_book`
  ADD PRIMARY KEY (`CID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
