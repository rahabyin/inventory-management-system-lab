from app.api import get_product_by_barcode, search_products


def test_barcode_lookup():
    result = get_product_by_barcode("123456789")

    assert result is None or isinstance(result, dict)


def test_name_search():
    result = search_products("milk")

    assert isinstance(result, list)