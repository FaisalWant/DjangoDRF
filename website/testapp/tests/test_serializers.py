from django.db.models import SlugField 
from django_extensions.db.fields import AutoSlugField 


from hypothesis import assume, given 

from hypothesis.extra.django import (
	TestCase, 
	from_field, 
	from_model, 
	register_field_strategy, 
	)

import string 

from hypothesis.strategies import text 

from ..models import Tag 
from ..serializers import TagSerializer 


register_field_strategy(
	AutoSlugField, from_field(SlugField()))


class TagSerializerTests(TestCase): 
	""" Tests for new TagSerialzier""" 

	@given (
		text(
		alphabet= (string.ascii_letters+string.digits),
		min_size=1, 
		max_size= Tag._meta.get_field("name").max_length,
		)
	)

	
	def test_data_serialization(self, name): 
		""" Can we deserialize and serialize a Tag"""
		assume(name.strip()== name)
		s1_tag = TagSerializer(data={"name":name} )
		self.assertTrue(s1_tag.is_valid(), s1_tag.errors) 
		tag= s1_tag.save()
		s2_tag= TagSerializer(tag) 
		self.assertEqual(s2_tag.data["name"], name) 


	@given(from_model(Tag)) 


	def test_model_serialization(self, tag):
		""" can we serialze and deserialize a Tag""" 

		assume(tag.name.strip()== tag.name) 
		s1_tag = TagSerializer(tag) 
		self.assertEqual(tag.name, s1_tag.data["name"])
		self.assertEqual(tag.slug, s1_tag.data["slug"])

		tag.delete()

		s2_tag= TagSerializer(data= s1_tag.data) 
		self.assertTrue(s2_tag.is_valid(), s2_tag.errors) 
		new_tag= s2_tag.save()
		self.assertEqual(tag.name, new_tag.name) 
		self.assertEqual(tag.slug, new_tag.slug) 



