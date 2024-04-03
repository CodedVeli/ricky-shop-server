from app import create_app

app = create_app

from .app.models.model import User, Product, Category, Order, db
users = [{
  "name": "Curtice",
  "password": "oE9!?EJCoy3",
  "email": "cgartenfeld0@topsy.com",
  "address": "Suite 38",
  "city": "Jiuhe",
  "phone": "144-762-2192"
}, {
  "name": "Corey",
  "password": "sA2@q!5r",
  "email": "civanyushin1@foxnews.com",
  "address": "Apt 1719",
  "city": "Bela Vista",
  "phone": "813-829-5968"
}, {
  "name": "Agneta",
  "password": "cY2~S7ByDcc",
  "email": "astaite2@cnbc.com",
  "address": "Suite 80",
  "city": "Juan L. Lacaze",
  "phone": "300-223-5814"
}, {
  "name": "Hastie",
  "password": "eB7$gzW6W",
  "email": "hprivett3@a8.net",
  "address": "Room 970",
  "city": "Kuala Terengganu",
  "phone": "886-214-0761"
}, {
  "name": "Candra",
  "password": "mD7|I+o%'SzB}a",
  "email": "cjansens4@apache.org",
  "address": "Apt 740",
  "city": "Orekhovo-Zuyevo",
  "phone": "503-227-9686"
}, {
  "name": "Elle",
  "password": "cL3_8\"G_",
  "email": "eforlonge5@fastcompany.com",
  "address": "Suite 93",
  "city": "Reno",
  "phone": "775-141-6301"
}, {
  "name": "Onfroi",
  "password": "hZ1/yZu+",
  "email": "opretsell6@washington.edu",
  "address": "Room 1547",
  "city": "Lisewo Malborskie",
  "phone": "609-939-0764"
}, {
  "name": "Salim",
  "password": "hD2{kS9##Owp?T_(",
  "email": "stromans7@diigo.com",
  "address": "Suite 46",
  "city": "Atarodangwautu",
  "phone": "359-127-0133"
}, {
  "name": "Julissa",
  "password": "mL8\"_}YIWp\"vfR40",
  "email": "jnapleton8@hibu.com",
  "address": "5th Floor",
  "city": "Serang",
  "phone": "552-262-3612"
}, {
  "name": "Koressa",
  "password": "dG1@2BkVFAt",
  "email": "kchiese9@webs.com",
  "address": "Room 1313",
  "city": "Villach",
  "phone": "325-708-4028"
}]
with app.app_context():
    db.session.add_all([User(**user) for user in users])
    db.session.commit()