from io import BytesIO

from PIL import Image
from django.core.files import File


class Filters:
    FILTER_TYPES = [
        ('animals & pets', 'animals & pets'),
        ('anime', 'anime'),
        ('art & design', 'art & design'),
        ('auto & technique', 'auto & technique'),
        ('blogging', 'blogging'),
        ('cartoons', 'cartoons'),
        ('celebrity', 'celebrity'),
        ('dance', 'dance'),
        ('fashion & beauty', 'fashion & beauty'),
        ('food & kitchen', 'food & kitchen'),
        ('gaming', 'gaming'),
        ('live pictures', 'live pictures'),
        ('mashup', 'mashup'),
        ('memes', 'memes'),
        ('movies & TV', 'movies & TV'),
        ('music', 'music'),
        ('nature & travel', 'nature & travel'),
        ('science & technology', 'science & technology'),
        ('sports', 'sports'),
        ('stand-up & Jokes', 'stand-up & Jokes'),
    ]

    @classmethod
    def get_filter_types(cls):
        return cls.FILTER_TYPES


class Woman_or_man:
    Sex = [
        ('Man', 'Man'),
        ('Woman', 'Woman')
    ]

    @classmethod
    def get_woman_or_man(cls):
        return cls.Sex


def resized_every_photo(model_field, photo_name):
    try:
        img = Image.open(model_field)
        if img.width > img.height:
            img = img.resize((480, 300))
        else:
            img = img.resize((300, 480))
        output = BytesIO()
        if img.format == 'JPEG':
            img.save(output, format='JPEG')
            resized_photo = File(output, str(photo_name) + '.jpg')
        else:
            img.save(output, format='PNG')
            resized_photo = File(output, str(photo_name) + '.png')
        return resized_photo
    except Exception as e:
        print(f"Error: {e}")
        return None, None, None
