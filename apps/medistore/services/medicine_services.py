from apps.medistore.models.medicines_model import Medicine

def get_all_medicines():
    return Medicine.objects.all()

def add_new_medicine(
    name,
    SKU,
    category_id=None,
    manufacturer='',
    cost_price=0,
    retail_price=0,
    stock_quantity=0,
    stock_alert_level=0,
    description='',
    is_prescription_required=False,
    classification='',
    age_group='',
    salt_composition='',
    dosage_strength='',
    manufacture_date=None,
    expiry_date=None,
):
    medicine = Medicine.objects.create(
        name=name,
        SKU=SKU,
        category_id=category_id,
        manufacturer=manufacturer,
        cost_price=cost_price,
        retail_price=retail_price,
        stock_quantity=stock_quantity,
        stock_alert_level=stock_alert_level,
        description=description,
        is_prescription_required=is_prescription_required,
        classification=classification,
        age_group=age_group,
        salt_composition=salt_composition,
        dosage_strength=dosage_strength,
        manufacture_date=manufacture_date,
        expiry_date=expiry_date,
    )
    return medicine
