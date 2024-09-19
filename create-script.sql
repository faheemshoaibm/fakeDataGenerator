drop table customer;
create table customer(
	CustomerId INTEGER PRIMARY KEY GENERATED ALWAYS AS identity,
	CustomerName Varchar(255),
	CustomerAddress Varchar(255),
	CustomerSSN Varchar(255),
	CustomerCity varchar(255)
);

create table product(
	ProductId INTEGER PRIMARY KEY GENERATED ALWAYS AS identity,
	ProductName varchar(255)
);

create table orders(
	OrderId INTEGER PRIMARY KEY GENERATED ALWAYS AS identity,
	OrderTime timestamp,
	CustomerId integer,
	ProductId integer,
	OrderAmount decimal
);

-- insert into dev.customer(CustomerName,CustomerAddress,CustomerSSN,CustomerCity) values('Jennifer Henderson','36081 Coleman Ridges Apt. 296 West Trevor, NV 96031','409-39-1501','South Angelicatown');

select * from dev.customer;
select * from dev.product;
select * from orders o ;