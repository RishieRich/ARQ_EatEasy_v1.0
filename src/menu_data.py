# src/menu_data.py

"""
This module contains the static menu data for the restaurant.
It categorizes items and provides metadata like description and tags
to help the LLM and the logic layer match user intent.
"""

MENU = {
    "North Indian": [
        {
            "name": "Butter Chicken",
            "description": "Tender chicken cooked in a rich tomato and butter gravy.",
            "tags": ["non-veg", "mild", "creamy", "gluten", "dairy", "nuts"],
            "price": 350
        },
        {
            "name": "Paneer Butter Masala",
            "description": "Cottage cheese cubes in a rich tomato-butter sauce.",
            "tags": ["veg", "mild", "creamy", "gluten", "dairy", "nuts"],
            "price": 280
        },
        {
            "name": "Dal Makhani",
            "description": "Black lentils cooked overnight with butter and cream.",
            "tags": ["veg", "mild", "creamy", "dairy"],
            "price": 250
        },
        {
            "name": "Chana Masala",
            "description": "Chickpeas cooked in a spicy onion-tomato gravy.",
            "tags": ["veg", "spicy", "vegan_option"],
            "price": 220
        },
        {
            "name": "Rogan Josh",
            "description": "Aromatic lamb curry with Kashmiri spices.",
            "tags": ["non-veg", "spicy", "rich"],
            "price": 400
        },
        {
            "name": "Palak Paneer",
            "description": "Cottage cheese in a smooth spinach gravy.",
            "tags": ["veg", "mild", "healthy", "dairy"],
            "price": 270
        },
        {
            "name": "Tandoori Chicken",
            "description": "Chicken marinated in yogurt and spices, roasted in clay oven.",
            "tags": ["non-veg", "spicy", "dry", "dairy"],
            "price": 320
        },
        {
            "name": "Aloo Gobi",
            "description": "Potatoes and cauliflower cooked with turmeric and cumin.",
            "tags": ["veg", "mild", "home-style", "vegan"],
            "price": 200
        }
    ],
    "South Indian": [
        {
            "name": "Masala Dosa",
            "description": "Fermented rice crepe filled with spiced potato mash.",
            "tags": ["veg", "mild", "crispy", "vegan_option"],
            "price": 120
        },
        {
            "name": "Idli Sambar",
            "description": "Steamed rice cakes served with lentil stew.",
            "tags": ["veg", "mild", "healthy", "vegan", "steamed"],
            "price": 80
        },
        {
            "name": "Medu Vada",
            "description": "Crispy lentil chilled donuts served with chutney.",
            "tags": ["veg", "fried", "crispy", "vegan"],
            "price": 90
        },
        {
            "name": "Hyderabadi Biryani",
            "description": "Aromatic basmati rice cooked with chicken and spices.",
            "tags": ["non-veg", "spicy", "rice"],
            "price": 300
        },
        {
            "name": "Rava Dosa",
            "description": "Semolina crepe with onions and green chilies.",
            "tags": ["veg", "crispy", "gluten"],
            "price": 130
        },
        {
            "name": "Uttapam",
            "description": "Thick rice pancake topped with onions and tomatoes.",
            "tags": ["veg", "soft", "vegan"],
            "price": 110
        },
        {
            "name": "Chicken Chettinad",
            "description": "Spicy chicken curry from Chettinad region.",
            "tags": ["non-veg", "very-spicy", "coconut"],
            "price": 340
        },
        {
            "name": "Curd Rice",
            "description": "Soft mushy rice mixed with yogurt using tempering.",
            "tags": ["veg", "mild", "cold", "dairy"],
            "price": 100
        }
    ],
    "Maharashtrian": [
        {
            "name": "Misal Pav",
            "description": "Spicy sprout curry topped with farsan, served with bread.",
            "tags": ["veg", "very-spicy", "oily", "gluten"],
            "price": 150
        },
        {
            "name": "Vada Pav",
            "description": "Potato fritter in a bun with chutneys.",
            "tags": ["veg", "spicy", "fried", "gluten", "street-food"],
            "price": 50
        },
        {
            "name": "Puran Poli",
            "description": "Sweet flatbread stuffed with lentil and jaggery filling.",
            "tags": ["veg", "sweet", "gluten", "ghee", "dairy"],
            "price": 60
        },
        {
            "name": "Thalipeeth",
            "description": "Savory multi-grain pancake served with butter/yogurt.",
            "tags": ["veg", "mild", "healthy", "gluten", "dairy"],
            "price": 100
        },
        {
            "name": "Bharli Vangi",
            "description": "Stuffed baby eggplants in a peanut-based gravy.",
            "tags": ["veg", "spicy", "nuts", "vegan_option"],
            "price": 180
        },
        {
            "name": "Pithla Bhakri",
            "description": "Review gram flour curry served with sorghum bread.",
            "tags": ["veg", "mild", "home-style", "vegan"],
            "price": 140
        },
        {
            "name": "Sabudana Khichdi",
            "description": "Tapioca pearls tossed with peanuts and potatoes.",
            "tags": ["veg", "mild", "fasting-food", "nuts"],
            "price": 120
        },
        {
            "name": "Kolhapuri Chicken",
            "description": "Extremely spicy chicken curry with red chili paste.",
            "tags": ["non-veg", "very-spicy", "oily"],
            "price": 320
        }
    ],
    "Punjabi": [
        {
            "name": "Sarson Ka Saag",
            "description": "Mustard greens cooked with spices and ghee.",
            "tags": ["veg", "mild", "healthy", "dairy"],
            "price": 220
        },
        {
            "name": "Makki Di Roti",
            "description": "Cornmeal flatbread, best with Sarson Ka Saag.",
            "tags": ["veg", "gluten-free", "dairy"],
            "price": 40
        },
        {
            "name": "Chole Bhature",
            "description": "Spicy chickpea curry with fried fluffy bread.",
            "tags": ["veg", "spicy", "oily", "fried", "gluten"],
            "price": 180
        },
        {
            "name": "Rajma Chawal",
            "description": "Kidney beans in tomato gravy served with rice.",
            "tags": ["veg", "mild", "home-style"],
            "price": 160
        },
        {
            "name": "Amritsari Kulcha",
            "description": "Stuffed bread baked in tandoor.",
            "tags": ["veg", "mild", "gluten", "dairy"],
            "price": 70
        },
        {
            "name": "Lassi",
            "description": "Thick sweetened yogurt drink.",
            "tags": ["veg", "sweet", "dairy", "cold"],
            "price": 80
        },
        {
            "name": "Chicken Tikka",
            "description": "Boneless chicken marinated and roasted.",
            "tags": ["non-veg", "spicy", "dry", "dairy"],
            "price": 300
        },
        {
            "name": "Kadhi Pakora",
            "description": "Yogurt based curry with gram flour fritters.",
            "tags": ["veg", "sour", "dairy", "fried"],
            "price": 150
        }
    ],
    "Street Food": [
        {
            "name": "Pani Puri",
            "description": "Crispy hollow balls filled with spicy tamarind water.",
            "tags": ["veg", "spicy", "cold", "vegan"],
            "price": 60
        },
        {
            "name": "Bhel Puri",
            "description": "Puffed rice tossed with chutneys and veggies.",
            "tags": ["veg", "spicy", "light", "vegan"],
            "price": 70
        },
        {
            "name": "Samosa",
            "description": "Fried pastry with spicy potato filling.",
            "tags": ["veg", "fried", "gluten", "vegan_option"],
            "price": 20
        },
        {
            "name": "Pav Bhaji",
            "description": "Mashed vegetable curry served with buttered bun.",
            "tags": ["veg", "spicy", "buttery", "gluten", "dairy"],
            "price": 140
        },
        {
            "name": "Aloo Tikki",
            "description": "Potato patties topped with chutneys and yogurt.",
            "tags": ["veg", "fried", "dairy"],
            "price": 80
        },
        {
            "name": "Dahi Puri",
            "description": "Hollow balls filled with yogurt and chutneys.",
            "tags": ["veg", "sweet", "cold", "dairy"],
            "price": 90
        },
        {
            "name": "Momos",
            "description": "Steamed dumplings with veg or chicken filling.",
            "tags": ["veg_option", "non-veg_option", "steamed", "gluten"],
            "price": 100
        },
        {
            "name": "Kathi Roll",
            "description": "Wrap filled with roasted kebab and veggies.",
            "tags": ["veg_option", "non-veg_option", "gluten"],
            "price": 120
        }
    ],
    "Desserts": [
        {
            "name": "Gulab Jamun",
            "description": "Fried milk solids soaked in sugar syrup.",
            "tags": ["veg", "sweet", "fried", "dairy", "gluten"],
            "price": 80
        },
        {
            "name": "Rasgulla",
            "description": "Spongy cottage cheese balls in light syrup.",
            "tags": ["veg", "sweet", "dairy"],
            "price": 70
        },
        {
            "name": "Gajar Halwa",
            "description": "Carrot pudding cooked with milk and nuts.",
            "tags": ["veg", "sweet", "dairy", "nuts"],
            "price": 120
        },
        {
            "name": "Kheer",
            "description": "Rice pudding with cardamom and nuts.",
            "tags": ["veg", "sweet", "dairy", "nuts"],
            "price": 100
        },
        {
            "name": "Jalebi",
            "description": "Spiral fried batter soaked in syrup.",
            "tags": ["veg", "sweet", "fried", "gluten"],
            "price": 60
        },
        {
            "name": "Kulfi",
            "description": "Traditional indian ice cream.",
            "tags": ["veg", "sweet", "dairy", "frozen", "nuts"],
            "price": 80
        },
        {
            "name": "Rasmalai",
            "description": "Cottage cheese patties in sweetened milk.",
            "tags": ["veg", "sweet", "dairy", "nuts"],
            "price": 140
        },
        {
            "name": "Moong Dal Halwa",
            "description": "Rich lentil pudding with ghee.",
            "tags": ["veg", "sweet", "rich", "dairy", "nuts"],
            "price": 130
        }
    ],
    "Beverages": [
        {
            "name": "Masala Chai",
            "description": "Spiced milk tea.",
            "tags": ["veg", "hot", "dairy", "caffeine"],
            "price": 40
        },
        {
            "name": "Filter Coffee",
            "description": "Strong South Indian coffee.",
            "tags": ["veg", "hot", "dairy", "caffeine"],
            "price": 50
        },
        {
            "name": "Thandai",
            "description": "Cold milk drink with nuts and spices.",
            "tags": ["veg", "cold", "sweet", "dairy", "nuts"],
            "price": 100
        },
        {
            "name": "Mango Lassi",
            "description": "Yogurt drink with mango pulp.",
            "tags": ["veg", "cold", "sweet", "dairy"],
            "price": 110
        },
        {
            "name": "Jaljeera",
            "description": "Cumin spiced lemonade.",
            "tags": ["veg", "cold", "spicy", "vegan"],
            "price": 60
        },
        {
            "name": "Nimbu Pani",
            "description": "Fresh lime soda (sweet or salt).",
            "tags": ["veg", "cold", "vegan"],
            "price": 50
        },
        {
            "name": "Butter Milk (Chassa)",
            "description": "Spiced watered-down yogurt.",
            "tags": ["veg", "cold", "savory", "dairy"],
            "price": 40
        },
        {
            "name": "Badam Milk",
            "description": "Almond flavored milk.",
            "tags": ["veg", "hot", "sweet", "dairy", "nuts"],
            "price": 90
        }
    ]
}

def get_all_items_flat():
    """Helper to return a single list of all items for searching."""
    all_items = []
    for category, items in MENU.items():
        all_items.extend(items)
    return all_items
