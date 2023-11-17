from app.utils.imports import app, Base, engine, StarletteHTTPException, PlainTextResponse, CORSMiddleware, FastAPI, creates

app = FastAPI()

app.include_router(creates.router)

origins = [
    "http://8000-coachhallso-fastapiauth-ncq61p1ghmk.ws-us106.gitpod.io"
]

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# tells me which error I have
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request,exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# @app.post("/product")
# def create(product: ProductSchema, db:Session = Depends(get_db)):
#     new_product = models.ProductModel(**product.dict())
#     db.add(new_product)
#     db.commit()
#     db.refresh(new_product)
#     return new_product

@app.get("/")
async def get_root():
    return {"message": "Welcome to Vanessify"}


# # main.py
# from fastapi import FastAPI, Depends, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from sqlalchemy.orm import Session
# from database import engine, SessionLocal
# from models import Category, Cuisine, MenuItem
# from pydantic import BaseModel
# from schemas import CategorySchema, CuisineSchema, MenuItemSchema


# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow all origins (you might want to restrict this in a production environment)
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all methods
#     allow_headers=["*"],  # Allow all headers
# )

# # Create tables
# Category.__table__.create(bind=engine, checkfirst=True)
# Cuisine.__table__.create(bind=engine, checkfirst=True)
# MenuItem.__table__.create(bind=engine, checkfirst=True)


# # Dependency to get the database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Route to insert data
# @app.get("/insert-data")
# def insert_data(db: Session = Depends(get_db)):
#     # Data to be inserted
#     data = [
#         {"id": 1, "title": "Eggs Benedict", "cuisine_type": "American", "category": "Breakfast", "description": "Two poached eggs, Canadian bacon and hollandaise", "price": 9.99, "spicy_level": 0},
#         {"id": 2, "title": "Beef Satay", "cuisine_type": "Thai", "category": "Appetizer", "description": "Marinated and grilled beef skewers served with a peanut dipping sauce", "price": 6.99, "spicy_level": 3},
#         {"id": 3, "title": "Chicken Caesar Salad", "cuisine_type": "Italian", "category": "Lunch", "description": "A classic salad of romaine lettuce, grilled chicken, croutons, and Caesar dressing", "price": 8.99, "spicy_level": 1},
#         {"id": 4, "title": "Pork Tacos", "cuisine_type": "Mexican", "category": "Dinner", "description": "Two soft tortillas filled with seasoned pork, onions, cilantro, and salsa", "price": 11.99, "spicy_level": 2},
#         {"id": 5, "title": "Green Curry", "cuisine_type": "Thai", "category": "Dinner", "description": "A spicy Thai curry made with coconut milk, green chilies, chicken, and vegetables", "price": 13.99, "spicy_level": 4},
#         {"id": 6, "title": "Bloody Mary", "cuisine_type": "American", "category": "Drink", "description": "A classic brunch cocktail made with vodka, tomato juice, and spices", "price": 7.99, "spicy_level": 1},
#         {"id": 7, "title": "Chips and Salsa", "cuisine_type": "Mexican", "category": "Appetizer", "description": "Freshly made salsa and crispy tortilla chips", "price": 5.99, "spicy_level": 0},
#         {"id": 8, "title": "Chicken Teriyaki Bowl", "cuisine_type": "Japanese", "category": "Lunch", "description": "Grilled chicken, vegetables, and teriyaki sauce", "price": 10.99, "spicy_level": 0},
#         {"id": 9, "title": "Shrimp and Grits", "cuisine_type": "Southern", "category": "Breakfast", "description": "Buttery grits topped with shrimp, bacon and a spicy Cajun cream sauce", "price": 12.99, "spicy_level": 3},
#         {"id": 10, "title": "Chicken Alfredo", "cuisine_type": "Italian", "category": "Dinner", "description": "Grilled chicken and fettuccine noodles tossed in a creamy Alfredo sauce", "price": 14.99, "spicy_level": 1},
#         {"id": 11, "title": "Fish and Chips", "cuisine_type": "British", "category": "Dinner", "description": "Beer-battered cod and crispy fries served with tartar sauce", "price": 12.99, "spicy_level": 0},
#         {"id": 12, "title": "Spicy Tuna Roll", "cuisine_type": "Japanese", "category": "Appetizer", "description": "A sushi roll filled with spicy tuna, avocado, and cucumber", "price": 8.99, "spicy_level": 4},
#         {"id": 13, "title": "Fruit Smoothie", "cuisine_type": "American", "category": "Drink", "description": "A refreshing blend of fresh fruit, yogurt, and honey", "price": 6.99, "spicy_level": 0},
#         {"id": 14, "title": "Meat Lover's Pizza", "cuisine_type": "Italian", "category": "Dinner", "description": "A pizza topped with pepperoni, sausage, bacon, and ham", "price": 15.99, "spicy_level": 1},
#         {"id": 15, "title": "Avocado Toast", "cuisine_type": "American", "category": "Breakfast", "description": "Toasted bread topped with mashed avocado, sliced tomatoes, and a poached egg", "price": 10.99, "spicy_level": 0},
#         {"id": 16, "title": "Caesar Salad", "cuisine_type": "Italian", "category": "Appetizer", "description": "A smaller portion of a classic Caesar salad", "price": 4.99, "spicy_level": 0},
#         {"id": 17, "title": "Steak Fajitas", "cuisine_type": "Mexican", "category": "Dinner", "description": "Sizzling strips of steak with peppers and onions, served with tortillas and rice", "price": 17.99, "spicy_level": 2},
#         {"id": 18, "title": "French Toast", "cuisine_type": "American", "category": "Breakfast", "description": "Thick slices of bread dipped in egg batter and fried, topped with powdered sugar", "price": 8.99, "spicy_level": 0},
#         {"id": 19, "title": "Chicken Wings", "cuisine_type": "American", "category": "Appetizer", "description": "Crispy fried chicken wings tossed in your choice of buffalo, barbecue or honey mustard", "price": 9.99, "spicy_level": 2},
#         {"id": 20, "title": "Penne alla Vodka", "cuisine_type": "Italian", "category": "Dinner", "description": "Penne pasta tossed in a creamy tomato vodka sauce with grilled chicken and spinach", "price": 13.99, "spicy_level": 0},
#         {"id": 21, "title": "Bagel and Lox", "cuisine_type": "American", "category": "Breakfast", "description": "A toasted bagel topped with smoked salmon, cream cheese, capers and red onion", "price": 11.99, "spicy_level": 0},
#         {"id": 22, "title": "Chicken Quesadilla", "cuisine_type": "Mexican", "category": "Appetizer", "description": "Grilled flour tortilla filled with chicken, cheese, and vegetables, served with sour cream and salsa", "price": 10.99, "spicy_level": 1},
#         {"id": 23, "title": "Pho", "cuisine_type": "Vietnamese", "category": "Lunch", "description": "Rice noodles in a flavorful broth with thinly sliced beef, bean sprouts, and fresh herbs", "price": 12.99, "spicy_level": 2},
#         {"id": 24, "title": "Grilled Cheese Sandwich", "cuisine_type": "American", "category": "Lunch", "description": "A classic sandwich with melted cheese between two slices of buttery bread, served with tomato soup", "price": 8.99, "spicy_level": 0},
#         {"id": 25, "title": "Crispy Calamari", "cuisine_type": "Italian", "category": "Appetizer", "description": "Golden-fried calamari served with a tangy marinara sauce", "price": 9.99, "spicy_level": 1},
#         {"id": 26, "title": "Hot and Sour Soup", "cuisine_type": "Chinese", "category": "Lunch", "description": "A spicy and tangy soup with chicken, tofu, and vegetables", "price": 6.99, "spicy_level": 4},
#         {"id": 27, "title": "Salmon Burger", "cuisine_type": "American", "category": "Dinner", "description": "A juicy salmon patty topped with avocado and a spicy mayo sauce, served on a brioche bun", "price": 13.99, "spicy_level": 2},
#         {"id": 28, "title": "Pad See Ew", "cuisine_type": "Thai", "category": "Lunch", "description": "Stir-fried wide rice noodles with chicken, broccoli, and egg in a sweet soy sauce", "price": 11.99, "spicy_level": 1},
#         {"id": 29, "title": "Baked Brie", "cuisine_type": "French", "category": "Appetizer", "description": "A creamy wheel of brie baked in puff pastry, served with crackers", "price": 12.99, "spicy_level": 0},
#         {"id": 30, "title": "Chicken Fingers", "cuisine_type": "American", "category": "Appetizer", "description": "Crispy fried chicken tenders served with your choice of dipping sauce", "price": 8.99, "spicy_level": 0},
#         {"id": 31, "title": "Tomato Basil Soup", "cuisine_type": "Italian", "category": "Lunch", "description": "A creamy tomato soup with fresh basil, served with a grilled cheese sandwich", "price": 7.99, "spicy_level": 0},
#         {"id": 32, "title": "Samosas", "cuisine_type": "Indian", "category": "Appetizer", "description": "Crispy pastry pockets filled with spiced potatoes and peas, served with a chutney", "price": 6.99, "spicy_level": 3},
#         {"id": 33, "title": "Chicken Tikka Masala", "cuisine_type": "Indian", "category": "Dinner", "description": "Grilled chicken in a creamy tomato-based sauce with aromatic spices, served with basmati rice and naan", "price": 15.99, "spicy_level": 2},
#         {"id": 34, "title": "Grilled Octopus", "cuisine_type": "Mediterranean", "category": "Appetizer", "description": "Tender and flavorful grilled octopus served with a lemon garlic sauce", "price": 12.99, "spicy_level": 1},
#         {"id": 35, "title": "Fajita Salad", "cuisine_type": "Mexican", "category": "Lunch", "description": "A salad topped with grilled chicken, peppers, onions, and avocado with tortilla chips", "price": 9.99, "spicy_level": 1},
#         {"id": 36, "title": "Caesar Wrap", "cuisine_type": "American", "category": "Lunch",
#          "description": "A wrap filled with grilled chicken, romaine lettuce, Parmesan cheese and Caesar dressing, served with fries",
#          "price": 10.99, "spicy_level": 0},
#         {"id": 37, "title": "Steak Salad", "cuisine_type": "American", "category": "Lunch",
#          "description": "A salad topped with grilled steak, mixed greens, cherry tomatoes and blue cheese, served with balsamic vinaigrette",
#          "price": 12.99, "spicy_level": 0},
#         {"id": 38, "title": "Chocolate Martini", "cuisine_type": "American", "category": "Drink",
#          "description": "A decadent cocktail made with chocolate liqueur, chocolate and cream",
#          "price": 9.99, "spicy_level": 0},
#         {"id": 39, "title": "Breakfast Burrito", "cuisine_type": "Mexican", "category": "Breakfast",
#          "description": "A flour tortilla filled with scrambled eggs, bacon, cheese, and salsa, served with hashbrowns",
#          "price": 9.99, "spicy_level": 1},
#         {"id": 40, "title": "Shrimp Cocktail", "cuisine_type": "American", "category": "Appetizer",
#          "description": "Freshly poached shrimp served with cocktail sauce and lemon wedges",
#          "price": 11.99, "spicy_level": 0},
#         {"id": 41, "title": "Chicken Caesar Salad", "cuisine_type": "American", "category": "Lunch",
#          "description": "Grilled chicken, romaine lettuce, croutons, and Parmesan cheese, tossed in a creamy Caesar dressing",
#          "price": 10.99, "spicy_level": 1},
#         {"id": 42, "title": "Beef Stroganoff", "cuisine_type": "Russian", "category": "Dinner",
#          "description": "Tender beef strips with mushrooms and onions in a creamy sour cream sauce, served over egg noodles",
#          "price": 18.99, "spicy_level": 1},
#         {"id": 43, "title": "Falafel Wrap", "cuisine_type": "Middle Eastern", "category": "Lunch",
#          "description": "Crispy falafel balls wrapped in a pita with hummus, lettuce, tomato, and tahini sauce",
#          "price": 9.99, "spicy_level": 1},
#         {"id": 44, "title": "Spinach and Feta Stuffed Chicken", "cuisine_type": "Mediterranean", "category": "Dinner",
#          "description": "Chicken breasts stuffed with spinach and feta cheese, served with roasted potatoes and vegetables",
#          "price": 19.99, "spicy_level": 1},
#         {"id": 45, "title": "Cheddar Bacon Burger", "cuisine_type": "American", "category": "Lunch",
#          "description": "Grilled beef patty with melted cheddar cheese, bacon, lettuce, tomato, and onion on a toasted bun",
#          "price": 12.99, "spicy_level": 2},
#         {"id": 46, "title": "Chicken Satay", "cuisine_type": "Thai", "category": "Appetizer",
#          "description": "Grilled chicken skewers with a spicy peanut sauce",
#          "price": 8.99, "spicy_level": 3},
#         {"id": 47, "title": "Kung Pao Chicken", "cuisine_type": "Chinese", "category": "Lunch",
#          "description": "Spicy stir-fry chicken with peanuts, vegetables, and chili peppers, served over rice",
#          "price": 13.99, "spicy_level": 4},
#         {"id": 48, "title": "Vegetable Stir-Fry", "cuisine_type": "Asian", "category": "Lunch",
#          "description": "Stir-fried vegetables with tofu and a soy sauce-based sauce, served over rice",
#          "price": 11.99, "spicy_level": 0},
#         {"id": 49, "title": "Garlic Shrimp", "cuisine_type": "Italian", "category": "Dinner",
#          "description": "Sautéed shrimp in a garlic and butter sauce, served with bread",
#          "price": 17.99, "spicy_level": 1},
#         {"id": 50, "title": "Fruit Salad", "cuisine_type": "International", "category": "Breakfast",
#          "description": "Assorted fresh fruits, such as melon, pineapple, berries, and grapes",
#          "price": 7.99, "spicy_level": 0},
#         {"id": 51, "title": "Chicken Enchiladas", "cuisine_type": "Mexican", "category": "Dinner",
#          "description": "Tender chicken and cheese rolled in tortillas, topped with enchilada sauce and melted cheese, served with rice and beans",
#          "price": 14.99, "spicy_level": 2},
#         {"id": 52, "title": "Lobster Bisque", "cuisine_type": "French", "category": "Appetizer",
#          "description": "Creamy soup made with lobster stock, cream, and chunks of lobster meat",
#          "price": 11.99, "spicy_level": 0},
#         {"id": 53, "title": "Capellini Pomodoro", "cuisine_type": "Italian", "category": "Lunch",
#          "description": "Angel hair pasta with fresh tomatoes, basil, garlic, and olive oil",
#          "price": 12.99, "spicy_level": 0},
#         {"id": 54, "title": "Pesto Chicken Panini", "cuisine_type": "Italian", "category": "Lunch",
#          "description": "Grilled chicken, mozzarella cheese, pesto, and sun-dried tomatoes on a pressed panini bread",
#          "price": 10.99, "spicy_level": 1},
#         {"id": 55, "title": "Tom Yum Soup", "cuisine_type": "Thai", "category": "Appetizer",
#          "description": "Spicy and sour soup with shrimp, lemongrass, galangal, lime juice, and chili peppers",
#          "price": 9.99, "spicy_level": 4},
#         {"id": 56, "title": "Steak Fajitas", "cuisine_type": "Mexican", "category": "Dinner",
#          "description": "Sizzling hot skillet of grilled steak strips, bell peppers, and onions, served with tortillas, guacamole, and sour cream",
#          "price": 20.99, "spicy_level": 2},
#         {"id": 57, "title": "Vegetable Lasagna", "cuisine_type": "Italian", "category": "Dinner",
#          "description": "Layers of pasta, tomato sauce, and assorted vegetables, baked with mozzarella cheese",
#          "price": 16.99, "spicy_level": 0},
#         {"id": 58, "title": "French Toast", "cuisine_type": "American", "category": "Breakfast",
#          "description": "Thick slices of bread soaked in a mixture of egg yolk",  
#          "price": 11.99, "spicy_level": 0},
#     ]

#     # Insert categories
#     for item in data:
#         category_name = item["category"]
#         category = db.query(Category).filter(Category.name == category_name).first()
#         if not category:
#             category = Category(name=category_name)
#             db.add(category)
#             db.commit()
#             db.refresh(category)

#     # Insert cuisines
#     for item in data:
#         cuisine_name = item["cuisine_type"]
#         cuisine = db.query(Cuisine).filter(Cuisine.name == cuisine_name).first()
#         if not cuisine:
#             cuisine = Cuisine(name=cuisine_name)
#             db.add(cuisine)
#             db.commit()
#             db.refresh(cuisine)

#     # Insert menu items
#     for item in data:
#         menu_item = MenuItem(**item)
#         db.add(menu_item)

#     db.commit()
#     return {"message": "Data inserted successfully!"}

# @app.get("/menus")
# def get_menus(db: Session = Depends(get_db)):
#     result = db.query(MenuItem, Category, Cuisine).join(Category, MenuItem.category_id == Category.id).join(Cuisine, MenuItem.cuisine_id == Cuisine.id).all()
#     pydantic_result = []

#     for menu_item, category, cuisine in result:
#         category_schema = CategorySchema(id=category.id, name=category.name)
#         cuisine_schema = CuisineSchema(id=cuisine.id, name=cuisine.name)

#         menu_item_schema = MenuItemSchema(
#             id=menu_item.id,
#             title=menu_item.title,
#             description=menu_item.description,
#             price=menu_item.price,
#             spicy_level=menu_item.spicy_level,
#             category=category_schema,
#             cuisine=cuisine_schema
#         )

#         pydantic_result.append(menu_item_schema)

#     return pydantic_result