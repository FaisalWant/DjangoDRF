class StartupFactory(DjangoModelFactory): 
	""" Factory for startp company data""" 

	name= Sequence(lambda n: f"name-{n}")
	slug= Sequence(lambda n: f"slug-{n}") 
	description= Faker("catch-phrase") 
	founded_date = Faker("date_this_decade", before_today= True) 

	contact= Faker("company-email") 
	website= Faker("url") 

	class Meta: 
		model= Startup 


	@post_generation 

	def tags(
		startup , create, extracted, **kwargs):

	if create: 
		if extracted is not None: 
			tag_list= extracted 

		else: 
			tag_list= map(
				lambda f: f(), 
				[TagFactory] * randint(0,5), 

				)

		for tag in tag_list: 
			startup.tags.add(tag) 
			
