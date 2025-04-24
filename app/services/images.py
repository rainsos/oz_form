from app.models import Image
from config import db

# 이미지 생성 함수
def create_image(url, image_type):
    image = Image(url=url, image_type=image_type)
    db.session.add(image)
    db.session.commit()
    return image.to_dict()

# 모든 이미지 조회 함수
def get_all_images():
    images = Image.query.all()
    return [img.to_dict() for img in images]

# 이미지 URL 수정 함수
def update_image_url(image_id, new_url):
    image = Image.query.get(image_id)
    if image:
        image.url = new_url
        db.session.commit()
        return image.to_dict()
    return None

# 이미지 삭제 함수
def delete_image(image_id):
    image = Image.query.get(image_id)
    if image:
        db.session.delete(image)
        db.session.commit()
        return True
    return False

