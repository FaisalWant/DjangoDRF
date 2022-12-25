from factory import DjangoModelFactory, Sequenct 
from ..models import Tag 


class TagFactory(DjangoModelFactory):
    name = Sequence(lambda n: f"name-{n}")

    class Meta: 
        model= Tag 
