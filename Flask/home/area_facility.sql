INSERT INTO `ih_area_info` (`name`) VALUES ('东城区'),('西城区'),('朝阳区'),('海淀区'),('昌平区'),
('丰台区'),('房山区'),('通州区'),('顺义区'),('大兴区'),('怀柔区'),('平谷区'),
('密云区'),('延庆区'),('石景山区');


INSERT INTO `ih_facility_info` (`name`) VALUES ('无线网络'),('热水淋浴'),('空调'),('暖气'),('允许抽烟'),
('饮水设备'),('牙具'),('香皂'),('拖鞋'),('手纸'),('毛巾'),('沐浴露、洗发露'),('冰箱'),('洗衣机'),
('电梯'),('允许做饭'),('允许带宠物'),('允许聚会'),('门禁系统'),('停车位'),('有线网络'),('电视'),('浴缸');


update ih_house_info set index_image_url = "" where id = 1;