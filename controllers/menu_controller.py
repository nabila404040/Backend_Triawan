from flask import jsonify, request
from config.database import get_db
from models.menu_model import Menu
from sqlalchemy.orm import Session

def get_all_menu():
    db: Session = next(get_db())
    data = db.query(Menu).all()
    return jsonify([{
        "id_menu": m.id_menu,
        "name": m.name,
        "price": m.price,
        "category": m.category,
        "image_url": m.image_url
    } for m in data])

def add_menu():
    db: Session = next(get_db())
    body = request.json

    new_data = Menu(
        name=body["name"],
        price=body["price"],
        category=body["category"],
        image_url=body["image_url"]
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return jsonify({
        "message": "Data menu berhasil ditambahkan",
        "data": {
            "id_menu": new_data.id_menu,
            "name": new_data.name,
            "price": new_data.price,
            "category": new_data.category,
            "image_url": new_data.image_url
        }
    })

def update_menu(id_menu):
    db: Session = next(get_db())
    body = request.json

    menu = db.query(Menu).filter(Menu.id_menu == id_menu).first()
    if not menu:
        return jsonify({"message": "Menu tidak ditemukan"}), 404

    menu.name = body.get("name", menu.name)
    menu.price = body.get("price", menu.price)
    menu.category = body.get("category", menu.category)
    menu.image_url = body.get("image_url", menu.image_url)

    db.commit()
    db.refresh(menu)

    return jsonify({
        "message": "Data menu berhasil diperbarui",
        "data": {
            "id_menu": menu.id_menu,
            "nama_makanan": menu.name,
            "price": menu.price,
            "category": menu.category,
            "image_url": menu.image_url
        }
    }), 200

def delete_menu(id_menu):
    db: Session = next(get_db())
    menu = db.query(Menu).filter(Menu.id_menu == id_menu).first()
    if not menu:
        return jsonify({"message": "Menu tidak ditemukan"}), 404

    db.delete(menu)
    db.commit()

    return jsonify({"message": f"Data menu dengan id {id_menu} berhasil dihapus"}), 200