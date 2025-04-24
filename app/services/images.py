from app.models import Image
from config import db

def create_image(url, image_type):
    image = Image(url=url, type=image_type)
    db.session.add(image)
    db.session.commit()
    return image.to_dict()

def get_all_images():
    images = Image.query.all()
    return [img.to_dict() for img in images]

def update_image_url(image_id, new_url):
    image = Image.query.get(image_id)
    if image:
        image.url = new_url
        db.session.commit()
        return image.to_dict()
    return None

def delete_image(image_id):
    image = Image.query.get(image_id)
    if image:
        db.session.delete(image)
        db.session.commit()
        return True
    return False

