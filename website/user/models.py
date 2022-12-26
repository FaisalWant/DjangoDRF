from improved_user.model_mixins import AbstractUser 


class User(AbstractUser): 
	def __str__(self): 
		return self.email