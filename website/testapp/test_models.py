from django.test import TestCase 

from ..models import Tag 

class TagModelTestDemo(TestCase): 
	""" Tests for the Tag modeL""" 
	def test_concrete_fields(self): 
		field_name=[

		field.name for field in Tag._meta.get_fields()

		]
		expected_field_names=[ "id", "name", "slug"] 

		self.assertEqual(field_name, expected_field_names) 



	def test_name_uniqueness(self): 
		""" Are Tags with identical names disallowed""" 

		kwargs= dict(name="a") 
		Tag.objects.create(**kwargs) 
		with self.assertRaises(IntegrityError): 
			Tag.objects.create(**kwargs) 


	def test_list_order(self): 
		""" Are tags ordered by name""" 

		Tag.objects.create(name="b") 
		Tag.objects.create(name="D")
		Tag.objects.create(name="c")
		Tag.objects.create(name="a")

		tag_name_list= list(
			Tag.objects.values_list("name", flat=True)
			)

		expected_name_list=["D", "a", "b", "c"]
		self.assertEqual(tag_name_list, expected_name_list) 