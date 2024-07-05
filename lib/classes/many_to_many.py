class Article:
    all=[]
    def __init__(self, author, magazine, title):
        if isinstance(magazine, Magazine):
            self.magazine = magazine
        if isinstance(author, Author):
             self.author = author
       
        self.title = title
       
        author.articles().append(self)
        magazine.articles().append(self)
        Article.all.append(self)
    @property
    def title(self):
            return self._title
    @title.setter
    def title(self,title):
        if not hasattr(self, "title"):
                if len(title) >= 5 and len(title) <= 50:
                    self._title = title

    
        
class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
       if not hasattr(self, "name"):
        if len(name) > 0:
            self._name = name
    
    def articles(self):
        return self._articles
    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        true_or_false = [magazine.category for magazine in self.magazines()]
        if true_or_false:
            return true_or_false
        else:
            return None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name, str):
            if len(name) >= 2 and len(name) <= 16:
                self._name = name

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self,category):
        if isinstance(category, str):
            if len(category) > 0:
                self._category = category
    def articles(self):
        return self._articles
    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        true_or_false = [article.title for article in self._articles]
        if true_or_false:
            return true_or_false
        else:
            return None
    
    def contributing_authors(self):
        new_lis = [article.author for article in self._articles]
        new_authors = []
        for author in self.contributors():
            if new_lis.count(author) >= 2:
                new_authors.append(author)

        
        if new_authors:
            return new_authors
        else:
            return None
        
        
        
        
        
        
        # return a list of all the authors who have made 2 or more articles
        # must be type Author
        #return none if it has 0
        # author1 = set([article.author for article in self._articles])
        # author2 = set([article.author for article in self.article])
        # # lis = set(self.article) & set(self._articles)
        # lis1 = [i for i, j in zip(author1,author2) if i == j]
        # [article.author for article in self.contributors() if self._articles ]
        # if author1 & author2:
        #     return list(author1)
        # else:
        #     return None

      
        # if lis1:
        #     return lis1
        # else:
        #     return None
        
           
