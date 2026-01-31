from apps.medistore.models.category_model import Category

def get_all_category():
    return Category.objects.filter(is_active=True)