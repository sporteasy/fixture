from builtins import object
from fixture import DataSet, style

class ValidNoRelationsData(DataSet):
    class one(object):
        char = "one"
        num = 1
    class two(object):
        char = "two"
        num = 2

class InvalidNoRelationsData(DataSet):
    class one(object):
        char = "one"
        invalid = 'test'
    class two(object):
        char = "two"
        some_other = 2

class AuthorData(DataSet):
    class Meta(object):
        django_model = 'app.Author'
    class frank_herbert(object):
        first_name = "Frank"
        last_name = "Herbert"
    class guido(object):
        first_name = "Guido"
        last_name = "Van rossum"
        
class BookData(DataSet):
    class Meta(object):
        django_model = 'app.Book'
    class dune(object):
        title = "Dune"
        author = AuthorData.frank_herbert
    
    class python(object):
        title = 'Python'
        author = AuthorData.guido
        
class ReviewerData(DataSet):
    class Meta(object):
        django_model = 'app.Reviewer'
    class ben(object):
        name = 'ben'
        reviewed = [BookData.dune, BookData.python]

class DjangoDataSetWithMeta(DataSet):
    class Meta(object):
        django_model = 'app.Author'
    class frank_herbert(object):
        first_name = "Frank"
        last_name = "Herbert"
    class guido(object):
        first_name = "Guido"
        last_name = "Van rossum"