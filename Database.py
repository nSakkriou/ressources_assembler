import sqlite3

class RowHistoryBuilder:

    SOURCE_INTERNET = "Internet"
    SOURCE_TWITTER = "Twitter"
    SOURCE_YOUTUBE = "Youtube"

    def __init__(self, title: str, url: str, source: str) -> None:
        self.title = title
        self.url = url
        self.source = source

        self.sourcePossible = [RowHistoryBuilder.SOURCE_INTERNET, RowHistoryBuilder.SOURCE_TWITTER, RowHistoryBuilder.SOURCE_YOUTUBE]

    def checkNotNull(self, item: str):
        if item == "":
            return False
        else:
            return True

    def escapeSpecialChar(self, item: str):
        return (
            item.replace("&", "&amp;").
            replace('"', "&quot;").
            replace("<", "&lt;").
            replace(">", "&gt;")
        )        

    def checkSource(self):
        if self.source in self.sourcePossible:
            return True
        else:
            return False

    def check(self):
        self.source = self.escapeSpecialChar(self.source)
        self.title = self.escapeSpecialChar(self.title)
        self.url = self.escapeSpecialChar(self.url)

        if self.checkNotNull(self.source) and self.checkNotNull(self.title) and self.checkNotNull(self.url):
            return True
        else:
            return False

    def build(self):
        if self.check():
            return True, RowHistory(self.title, self.url, self.source)
        else:
            return False, None

class RowHistory:
    def __init__(self, title: str, url: str, source: str) -> None:
        self.title = title
        self.url = url
        self.source = source

    def to_json(self):
        return {"title" : self.title, "url" : self.url, "source" : self.source}

class Database:

    def __init__(self, db_name="./database/history.db") -> None:
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def initTable(self, path_sql_file="./database/scripts/init.sql"):
        self.cur.executescript(path_sql_file)
        return True

    def addItem(self, row: RowHistory):
        self.cur.execute('INSERT INTO history (title, url, source) VALUES(?, ?, ?);', [row.title, row.url, row.source])
        self.conn.commit()
        return row.to_json()
    
if __name__ == "__main__":
    Database()