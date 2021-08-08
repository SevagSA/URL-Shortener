import random
import string


def shortcode_generator(length, chars=string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(length))


def create_shortcode(instance, size=6):
    shortcode = shortcode_generator(size)
    if instance.__class__.objects.filter(shortcode=shortcode).exists():
        return create_shortcode(instance, size)
    return shortcode
