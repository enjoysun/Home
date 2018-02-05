drop database house;
create database house charset=utf8;
use house;
create table tb_user_info(
	user_id bigint unsigned auto_increment comment '用户id,unsigned:无符号整数即取消负数范围',
	user_name varchar(64) not null comment '用户姓名',
	user_gender tinyint not null default 0 comment '用户性别默认0',
	user_age int null comment '年龄',
	user_mobile char(11) not null comment '手机号',
	user_img varchar(128) null comment '头像',
	user_passwd varchar(128) not null comment '密码',
	user_ctime datetime default current_timestamp comment '创建时间',
	user_utime datetime default current_timestamp on update current_timestamp comment '更新时间',
	primary key (user_id),
	unique (user_mobile) # 指定唯一，unique也做了 key (user_mobile)操作
) engine=InnoDB default charset=utf8 comment '用户表';

create table tb_area_info(
	area_id bigint unsigned not null auto_increment comment '区域id',
	area_name varchar(32) not null comment '区域名称',
	area_time datetime not null default current_timestamp comment '创建时间',
	primary key(area_id)
)engine=InnoDB default charset=utf8 comment '区域表';

create table tb_house_info(
	house_id bigint unsigned auto_increment comment '房屋id',
	house_user_id bigint unsigned not null comment '用户id',
	house_title varchar(128) not null comment '房屋名',
	house_price int unsigned not null default '0' comment '价格',
	house_area_id bigint unsigned not null comment '区域ID',
	house_address varchar(256) not null comment '地址',
	house_room_count tinyint unsigned not null default '1' comment '房间数',
	house_room_unit varchar(32)  not null comment '户型',
	house_acreage int unsigned not null default '0' comment '面积',
	house_beds varchar(64) not null default '' comment '床的配置',
	house_capacity tinyint unsigned not null default '1' comment '容纳人数',
	house_deposit int unsigned not null default '0' comment '押金',
	house_min_day int unsigned not null default '1' comment '最短入住时间',
	house_max_day int unsigned not null default '0' comment '最长入住时间',
	house_order_count int unsigned not null default '0' comment '下单数量',
	house_verify_status tinyint not null default '0' comment '审核状态：0-待审核，1-审核未通过，2-审核通过',
	house_online_status tinyint not null default '1' comment '0-下线，1-上线',
	house_index_image_url varchar(256) null comment '房屋主图片',
	house_description varchar(500) null comment '描述',
	house_ctime datetime not null default current_timestamp comment'插入时间',
	house_utime datetime not null default current_timestamp on update current_timestamp comment'更新时间',
	primary key (house_id),
	-- KEY 'hi_status'(house_verify_status,house_online_status),
	constraint foreign key (house_user_id) references tb_user_info(user_id),
	constraint foreign key (house_area_id) references tb_area_info(area_id)
) engine=InnoDB default charset=utf8 comment'房屋表';

create table tb_house_facility(
	hf_id bigint unsigned not null auto_increment comment 'id',
	hf_house_id bigint unsigned not null comment '房屋id',
	hf_facility_id int unsigned not null comment '房屋设施',
	hf_ctime datetime not null default current_timestamp comment'创建时间',
	primary key(hf_id),
	constraint foreign key (hf_house_id) references tb_house_info(house_id)
)engine=InnoDB default charset=utf8 comment '房屋设施表';


create table tb_facility_catelog(
	fc_id bigint unsigned not null auto_increment comment'id',
	fc_name varchar(32) not null comment'设施名称',
	fc_ctime datetime not null default current_timestamp comment'创建时间',
	primary key(fc_id)
)engine=InnoDB default charset=utf8 comment'设施型录表';

create table tb_order_info(
	order_id bigint unsigned not null auto_increment comment'订单id',
	order_house_id bigint unsigned not null comment'房屋id',
	order_user_id bigint unsigned not null comment'用户id',
	order_begin_date date not null comment'开始入住时间',
	order_end_date date not null comment'离开时间',
	order_days int unsigned not null default '1' comment'入住天数',
	order_house_price int unsigned not null comment'房屋单价',
	order_amount int unsigned not null comment'订单金额',
	order_status tinyint not null default '0' comment'订单状态：0-待接单，1-待支付，2-已支付，3-待评价，4-已完成，5-已取消，6-拒接单',
	order_comment text null comment'订单评价',
	order_utime datetime not null default current_timestamp on update current_timestamp comment'更改时间',
	order_ctime datetime not null default current_timestamp comment'创建时间',
	primary key(order_id),
	-- key 'o_status'(order_status),
	constraint foreign key(order_house_id) references tb_house_info(house_id),
	constraint foreign key(order_user_id) references tb_user_info(user_id)
)engine=InnoDB default charset=utf8 comment'订单表';

create table tb_img_info(
	img_id bigint unsigned auto_increment comment'图片id',
	img_house_id bigint unsigned not null comment'房屋id',
	img_url varchar(128) null comment'',
	img_ctime datetime not null default current_timestamp comment'',
	img_utime datetime not null default current_timestamp on update current_timestamp,
	primary key (img_id),
	constraint foreign key (img_house_id) references tb_house_info(house_id)
)engine=InnoDB default charset=utf8 comment'图片表';



