from sqlalchemy import create_engine, MetaData, Table, Column, String, select, or_, exc

def setup():
	db = create_engine('postgresql+psycopg2://emotiveai:emotiveai@localhost/postgres')
	metadata = MetaData(db, reflect=True)
	if not db.dialect.has_table(db, "customers"):
		customer_table = Table("customers", metadata, Column('PhoneNum', String, primary_key=True, nullable=False))
		customer_table.create()

	if not db.dialect.has_table(db, "data"):
		data_table = Table("data", metadata, Column('Field', String, primary_key=True, nullable=False), Column('Value', String, nullable=False))
		data_table.create()
		conn = db.connect()
		insert = data_table.insert().values(Field="keyword", Value="EmotiveAI")
		conn.execute(insert)
		insert = data_table.insert().values(Field="cresponse", Value="Thanks!")
		conn.execute(insert)
		insert = data_table.insert().values(Field="iresponse", Value="Wrong Response!")
		conn.execute(insert)
		conn.close()

	return db, metadata


def update_keywords(db, metadata, keyword, cresponse, iresponse):
	conn = db.connect()
	data_table = metadata.tables['data']
	insert = data_table.update().where(data_table.c.Field=="keyword").values(Value=keyword)
	conn.execute(insert)
	insert = data_table.update().where(data_table.c.Field=="cresponse").values(Value=cresponse)
	conn.execute(insert)
	insert = data_table.update().where(data_table.c.Field=="iresponse").values(Value=iresponse)
	conn.execute(insert)
	conn.close()


def add_customer(db, metadata, phoneNum):
	conn = db.connect()
	data_table = metadata.tables['customers']
	try:
		insert = data_table.insert().values(PhoneNum=phoneNum)
		conn.execute(insert)
		conn.close()
	except exc.IntegrityError:
		pass


def getData(db, metadata):
	conn = db.connect()
	data_table = metadata.tables['data']
	select_st = data_table.select().where(or_(data_table.c.Field=="keyword", data_table.c.Field=="cresponse", data_table.c.Field=="iresponse"))
	select_st = list(conn.execute(select_st))
	return select_st[0][1], select_st[1][1], select_st[2][1]


def check_if_contact_is_registered(db, metadata, number):
	conn = db.connect()
	cust_table = metadata.tables['customers']
	select_st = cust_table.select().where(cust_table.c.PhoneNum==number)
	select_st = conn.execute(select_st)
	conn.close()
	if len(list(select_st)) == 1:
		return True
	return False


def get_all_contacts(db, metadata):
	conn = db.connect()
	cust_table = metadata.tables['customers']
	select_st = select([cust_table])
	select_st = conn.execute(select_st)
	conn.close()
	return list(select_st)
