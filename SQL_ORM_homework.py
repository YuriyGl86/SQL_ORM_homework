import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Stock, Shop, Sale

login = 'postgres'
password = ''
db_name = 'publisher'

DSN = f"postgresql://{login}:{password}@localhost:5432/{db_name}"
engine = sqlalchemy.create_engine(DSN)

# create_tables(engine)


Session = sessionmaker(bind=engine)
session = Session()

# with open('fixtures/tests_data.json', 'r') as fd:
#     data = json.load(fd)
#
# for record in data:
#     model = {
#         'publisher': Publisher,
#         'shop': Shop,
#         'book': Book,
#         'stock': Stock,
#         'sale': Sale,
#     }[record.get('model')]
#     session.add(model(id=record.get('pk'), **record.get('fields')))
# session.commit()

# publisher_name = input('Введите имя издателя: ')
for shop in session.query(Shop).join(Stock.shops).join(Book, Stock.id_book == Book.id).join(Publisher,
        Book.id_publisher == Publisher.id).filter(Publisher.name == input('Введите имя издателя: ')).all():
    print(shop)
