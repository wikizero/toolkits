# coding:utf-8
from peewee import *

db = MySQLDatabase('world', user='root', charset='utf8mb4', password='root', host='localhost')


class Info(Model):
	info_id = CharField(max_length=18, primary_key=True)
	url = CharField(max_length=100)
	release_date = DateField()
	title = CharField(max_length=50)
	sold_times = IntegerField()
	price = FloatField()
	account_type = CharField(max_length=12)
	level = IntegerField()
	bind_info = CharField(max_length=50)
	desc = CharField(max_length=250)
	soul_num = IntegerField()
	cost_performance = IntegerField()  # soul_num/price
	status = CharField(max_length=10)  # on-sale  sold-out  remove
	sold_date = DateField()

	class Meta:
		database = db


class SwordInfo(Model):
	info_id = CharField(max_length=18, primary_key=True)
	url = CharField(max_length=100)
	release_date = DateField()
	title = CharField(max_length=50)
	sold_times = IntegerField()
	price = FloatField()
	account_type = CharField(max_length=12)
	level = IntegerField()
	bind_info = CharField(max_length=50)
	desc = CharField(max_length=250)
	country = CharField(max_length=10)
	power = CharField(max_length=10)
	status = CharField(max_length=10)  # on-sale  sold-out  remove
	sold_date = DateField()

	class Meta:
		database = db

# db.connect()
# db.drop_tables([SwordInfo])
# db.create_tables([SwordInfo])
