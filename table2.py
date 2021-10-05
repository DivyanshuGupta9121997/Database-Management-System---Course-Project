from MySQLdb import connect

# Make the require tables
def maketables():
    try:
        print("ererere")
        c=connect("127.0.0.1","root","asd","project")
        print("ddddddd")
        d=c.cursor()
        print("345345")
        #different calls to different tables

        customer(d)
        employee(d)
        sanitary_item(d)
        building_material(d)
        sanitaryware_dealer(d)
        building_material_dealer(d)
        output_trans(d)

        orders(d)
        purchase_deal1(d)
        purchase_deal2(d)

        input_trans(d)
        service(d)
        includes_1(d)
        includes_2(d)

        vehicle(d)
        vehicle_service(d)

        c.commit()
        c.close()
        return True

    except:
        return False


def customer(cur):
    cur.execute(r'''
				create table if not exists customer
					(
						customer_id int(11) primary key not null,
						name varchar(50) not null,
                        email varchar(50) not null unique,
                        password varchar(50),
                        contact_no varchar(10),
                        occupation varchar(25),
                        address varchar(50)

					);
	''')
    pass

def employee(cur):
    cur.execute(r'''
				create table if not exists employee
					(
						emp_id int(11) primary key  ,
						name varchar(100),
                        email varchar(50),
                        contact_no varchar(10),
                        address varchar(50),
                        salary decimal(10,2),
                        curr_avail int,
                        date_of_hiring date

					);
	''')
    pass

def sanitary_item(cur):
    print("sanitary_item")
    cur.execute(r'''
				create table if not exists sanitary_item
					(
						item_id int(11) primary key  ,
						item_name varchar(100),
                        cost decimal(10,2),
                        current_stock int,
                        threshold int

					);
	''')
    pass

def building_material(cur):
    cur.execute(r'''
				create table if not exists building_material
					(
						item_id int(11) primary key  ,
						item_name varchar(100),
                        cost decimal(10,2),
                        current_stock decimal(5,2),
                        threshold decimal(5,2)

					);
	''')
    pass

def sanitaryware_dealer(cur):
    cur.execute(r'''
				create table if not exists sanitaryware_dealer
					(
						dealer_id int(11) primary key  ,
						dealer_name varchar(100),
                        email varchar(50),
                        contact_no varchar(10),
                        address varchar(50)

					);
	''')
    pass

def building_material_dealer(cur):
    cur.execute(r'''
				create table if not exists building_material_dealer
					(
						dealer_id int(11) primary key  ,
						dealer_name varchar(100),
                        email varchar(50),
                        contact_no varchar(10),
                        address varchar(50)

					);
	''')
    pass

def output_trans(cur):
    cur.execute(r'''
				create table if not exists output_trans
					(
						trans_id int(11) primary key  ,
    					payment_mode varchar(10),
                        date_of_payment date,
                        amount decimal(10,2),
                        account_no varchar(25),
                        bank_name varchar(25),
                        status int
					);
	''')
    pass

def orders(cur):
    cur.execute(r'''
				create table if not exists orders
					(
						order_id int(11) primary key  ,
                        customer_id int(11),
                        order_status int,
                        order_date date,
                        foreign key(customer_id)
							references customer(customer_id)
					);
	''')
    print("order complete")
    pass

#
def purchase_deal1(cur):
    cur.execute(r'''
				create table if not exists purchase_deal1
					(
						purchase_id int(11) primary key  ,
                        prod_id int(11),
                        trans_id int(11),
                        dealer_id int(11),
                        purchase_date date,
                        foreign key (prod_id)
							references building_material(item_id),
                        foreign key (trans_id)
							references output_trans(trans_id),
                        foreign key (dealer_id)
							references building_material_dealer(dealer_id)
					);
	''')
    pass

def purchase_deal2(cur):
    cur.execute(r'''
				create table if not exists purchase_deal2
					(
						purchase_id int(11) primary key  ,
                        prod_id int(11),
                        trans_id int(11),
                        dealer_id int(11),
                        purchase_date date,
                        foreign key(prod_id)
							references sanitary_item(item_id),
                        foreign key(trans_id)
							references output_trans(trans_id),
                        foreign key(dealer_id)
							references sanitaryware_dealer(dealer_id)
					);
	''')
    pass

def input_trans(cur):
    cur.execute(r'''
				create table if not exists input_trans
					(
						trans_id int(11) primary key  ,
                        order_id int(11),
    					payment_mode varchar(10),
                        date_of_payment date,
                        amount decimal(10,2),
                        account_no varchar(25),
                        bank_name varchar(25),
                        status int,

                        foreign key(order_id)
							references orders(order_id)

					);
	''')
    pass

def service(cur):
    cur.execute(r'''
				create table if not exists service
					(
						service_id int(11) primary key  ,
                        order_id int(11),
                        vendor_id int(11),
                        date_of_delivery date,
                        time_of_delivery timestamp,

                        foreign key (order_id)
							references orders(order_id),
                        foreign key (vendor_id)
							references employee(emp_id)

					);
	''')
    pass

def includes_1(cur):
    cur.execute(r'''
				create table if not exists includes_1
					(
                        order_id int(11),
                        product_id int(11),

                        primary key(order_id,product_id),

                        foreign key (order_id)
							references orders(order_id),
                        foreign key (product_id)
							references building_material(item_id)

					);
	''')
    pass

def includes_2(cur):
    print("includes_2")
    cur.execute(r'''
				create table if not exists includes_2
					(
                        order_id int(11),
                        product_id int(11),

                        primary key(order_id,product_id),

                        foreign key (order_id)
							references orders(order_id),
                        foreign key (product_id)
							references sanitary_item(item_id)

					);
	''')
    pass


def vehicle(cur):
    print("vehicle")
    cur.execute(r'''
				create table if not exists vehicle
					(
                        vehicle_id int(11) primary key  ,
                        registration_no varchar(25),
                        numberPlateInfo varchar(25)
					);
	''')
    pass

def vehicle_service(cur):
    print("vehicle_service")
    cur.execute(r'''
				create table if not exists vehicle_service
					(
                        vehicle_id int(11),
                        service_id int(11),

                        primary key(vehicle_id,service_id),

                        foreign key (vehicle_id)
                        	references vehicle(vehicle_id),
                        foreign key (service_id)
                        	references service(service_id)


					);
	''')
    pass



maketables()
