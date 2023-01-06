import requests, pdfkit, slugify
from bs4 import BeautifulSoup
from Database import *

class Scrapper:

    def __init__(self, url: str) -> None:
        self.url = url 
        self.soup = self.getSoup()

    def getSoup(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, "html.parser")

        return soup

    def getSlug(self):

        title = self.getTitle()
        if title == "" or title == None:
            # If no title, make a slug with url
            return str(slugify.slugify(self.url.split("//")[1].split("/")))

        else:
            return slugify.slugify(self.getTitle())

    def getTitle(self):
        for title in self.soup.find_all("title"):
            return str(title.text)

    def genRowHistory(self):
        pass

    def build(url, database):
        pass


class TwitterScrap(Scrapper):

    def __init__(self, url: str) -> None:
        Scrapper.__init__(self, url)

    def genRowHistory(self):
        r = RowHistoryBuilder(self.getTitle(), self.url, RowHistoryBuilder.SOURCE_TWITTER)
        flag, row = r.build()
        
        if flag:
            return row
        else:
            return False

    def write_markdown(self):

        with open(self.getSlug() + ".md", "w") as f:
            f.write(
f"""
# {self.getTitle()}

url : {self.url}
"""
            )

    def build(url, database: Database):
        inst = YoutubeScrap(url)
        inst.write_markdown()
        row = inst.genRowHistory()

        database.addItem(row)


class YoutubeScrap(Scrapper):
    
    def __init__(self, url: str) -> None:
        Scrapper.__init__(self, url)
    
    def genRowHistory(self):
        r = RowHistoryBuilder(self.getTitle(), self.url, RowHistoryBuilder.SOURCE_YOUTUBE)
        flag, row = r.build()
        
        if flag:
            return row
        else:
            return False

    def write_markdown(self):

        with open(self.getSlug() + ".md", "w") as f:
            f.write(
f"""
# {self.getTitle()}

url : {self.url}
"""
            )

    def build(url, database: Database):
        inst = YoutubeScrap(url)
        inst.write_markdown()
        row = inst.genRowHistory()

        database.addItem(row)


class InternetScrap(Scrapper):

    def __init__(self, url) -> None:
        Scrapper.__init__(self, url)

    def genRowHistory(self):
        r = RowHistoryBuilder(self.getTitle(), self.url, RowHistoryBuilder.SOURCE_INTERNET)
        flag, row = r.build()
        
        if flag:
            return row
        else:
            return False


    def write_markdown(self):

        with open(self.getSlug() + ".md", "w") as f:
            f.write(
f"""
# {self.getTitle()}

url : {self.url}
"""
            )

    def build(url, database: Database):
        inst = InternetScrap(url)
        inst.write_markdown()
        row = inst.genRowHistory()

        database.addItem(row)


if __name__ == "__main__":
    db = Database()

    InternetScrap.build("https://www.geeksforgeeks.org/extract-title-from-a-webpage-using-python/", db)