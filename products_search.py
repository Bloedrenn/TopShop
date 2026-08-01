# Имитация базы данных товаров (каталог)
PRODUCTS_CATALOG = [
    {"id": 1, "name": "Смартфон Apple iPhone 15", "category": "Электроника", "price": 85000},
    {"id": 2, "name": "Смартфон Samsung Galaxy S24", "category": "Электроника", "price": 79000},
    {"id": 3, "name": "Ноутбук ASUS Vivobook", "category": "Электроника", "price": 55000},
    {"id": 4, "name": "Беспроводные наушники", "category": "Аксессуары", "price": 4500},
    {"id": 5, "name": "Кожаный кошелек", "category": "Аксессуары", "price": 2900},
    {"id": 6, "name": "Кроссовки беговые", "category": "Обувь", "price": 6800},
    {"id": 7, "name": "Зимняя куртка", "category": "Одежда", "price": 12000},
    {"id": 8, "name": "Футболка хлопкeqweqовая", "category": "Одежда", "price": 1500},
]

def search_products(query="", category=None, max_price=None):
    """Ищет товары, категории и максимальной цене."""
    results = []
    query = query.lower().strip()

    for product in PRODUCTS_CATALOG:
        # 1. Поиск по ключевому слову (в названии или категории)
        if query and (query not in product["name"].lower() and query not in product["category"].lower()):
            continue
            
        # 2. Фильтр по точной категории (если указана)
        if category and product["category"].lower() != category.lower().strip():
            continue
            
        # 3. Фильтр по максимальной цене (если указана)
        if max_price and product["price"] > max_price:
            continue
            
        results.append(product)
        
    return results

def run_search_interface():
    """Консольный интерфейс для поиска товаров."""
    print("\n--- ПОИСК ТОВАРОВ ---")
    print("Оставьте поле пустым и нажмите Enter, чтобы пропустить фильтр.")
    
    query = input("Введите поисковый запрос (например, 'iphone' или 'одежда'): ")
    category = input("Категория (Электроника, Аксессуары, Обувь, Одежда): ")
    
    max_price_input = input("Максимальная цена (руб.): ").strip()
    max_price = int(max_price_input) if max_price_input.isdigit() else None

    # Запуск логики поиска
    found_items = search_products(query, category, max_price)

    # Вывод результатов
    print(f"\n🔎 Результаты поиска (Найдено: {len(found_items)}):")
    if not found_items:
        print("Ничего не найдено. Попробуйте изменить параметры поиска.")
        return

    print("-" * 50)
    for item in found_items:
        print(f"📦 [{item['category']}] {item['name']} — {item['price']} руб. (ID: {item['id']})")
    print("-" * 50)

if __name__ == "__main__":
    run_search_interface()
