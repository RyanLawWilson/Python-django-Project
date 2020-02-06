from django.db import models

# Create your models here. - A model is a database schema


# Define the possible choices that type can be
TYPE_CHOICES = {
	('appetizers','appetizers'),
	('entrees','entrees'),
	('treats','treats'),
	('drinks','drinks'),
}


# Inheriting from Model - Create a table called products
# ***NOTE: don't make column names (class names for models) plural
class Product(models.Model):
	# Django automatically puts in an autoincrementing id

	# Create a column called type that can contain up to 60 characters
	# You can only create stuff from these choices
	type = models.CharField(max_length=60, choices=TYPE_CHOICES)

	# Create a column called name that can
	# - Contain up to 60 characters
	# - Entries will start empty
	# - On forms, you can leave the field blank
	# - The field will not be saved as null
	name = models.CharField(max_length=60, default="", blank=True, null=False)

	# Create a column called description that can
	# - Contain up to 300 characters
	# - No default text
	# - Be left blank on a form
	description = models.TextField(max_length=300, default="", blank=True)

	# Create a column called price that will
	# - Have a default value of 0.00
	# - Have a number that is 10,000 digits long (too long, I think)
	# - Have two decimal places (These are counted as digits.  We will have 9,998 digits to the left of the
	# 		decimal point and 2 digits to the right)
	price = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

	# Create a column called image that will
	# - Have up to 255 digits
	# - Have no default value
	# - Allowed to be left blank on a form
	image = models.CharField(max_length=255, default="", blank=True)

	# This is not explained
	objects = models.Manager()
	def __str__(self):
		return self.name

'''
	IF YOU EVER MODIFY YOUR MODEL (database),
	ALWAYS RUN THESE COMMANDS AFTERWARDS:
	python manage.py makemigrations		- Checks for any changes to files (I think)
	python manage.py migrate			- Commits those changes (I think)
'''





