class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = None
        self.title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
        
    @title.setter
    def title(self, value):
        if self._title is not None:
            return 
        if not isinstance(value, str):
            return  
        if len(value) < 5 or len(value) > 50:
            return  
        self._title = value
        
    @property
    def author(self):
        return self._author
        
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be of type Author")
        self._author = value
        
    @property
    def magazine(self):
        return self._magazine
        
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        self._magazine = value
        
        
class Author:
    def __init__(self, name):
        self._name = None
        self.name = name  
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            return  
        if len(value) == 0:
            return  
        if self._name is not None:
            return  
        self._name = value
        
    def articles(self):
        return [article for article in Article.all if article.author == self]
        
    def magazines(self):
        return list({article.magazine for article in self.articles()})
        
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
        
    def topic_areas(self):
        if not self.articles():
            return None
        return list({magazine.category for magazine in self.magazines()})
        
class Magazine:
    all = []
    
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name  
        self.category = category  
        Magazine.all.append(self)
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            return  
        if len(value) < 2 or len(value) > 16:
            return  
        self._name = value
        
    @property
    def category(self):
        return self._category
        
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            return  
        if len(value) == 0:
            return  
        self._category = value
        
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        
    def contributors(self):
        return list({article.author for article in self.articles()})
        
    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]
        
    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        contributing = [author for author, count in author_counts.items() if count > 2]
        return contributing if contributing else None
        
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))