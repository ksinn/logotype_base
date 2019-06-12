create table brend (
	id SERIAL,
	title varchar(100) not null unique,
	site varchar(255),
	product varchar(100) not null,
	industry varchar(100) not null,
	founded int not null,
	constraint brend_id primary key (id)
);

create table logotype (
	id SERIAL,
	brend_id int not null,
	high int,
	width int,
	type varchar(7),
	img text not null,
	constraint logo_id primary key (id),
	constraint logo_brend foreign key (brend_id) references brend(id) on delete cascade
);
