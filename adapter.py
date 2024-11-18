import json
import xml.etree.ElementTree as ET


class BookAdapter:
    @staticmethod
    def from_json(json_data):
        books = json.loads(json_data)
        return [{"title": b["title"], "author": b["author"]} for b in books]

    @staticmethod
    def from_xml(xml_data):
        root = ET.fromstring(xml_data)
        books = []
        for book in root.findall('book'):
            books.append({
                "title": book.find('title').text,
                "author": book.find('author').text
            })
        return books
