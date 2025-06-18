'''Queries for mongoDb'''

def count_rpg_characters(db):
    """
        Count all documents in the 'characters' collection.
    """
    try:
        return db.characters.count_documents({})
    except Exception as e:
        raise Exception(f"Error executing count_rpg_characters count_documents: {e}")
    
def count_rpg_items(db):
    """
        Count all documents in the 'armory_item' collection.
    """
    try:
        return db.armory_item.count_documents({})
    except Exception as e:
        raise Exception(f"Error executing count_rpg_items count_documents: {e}")
    
def count_rpg_weapons(db):
    """
        Count how many items are weapons and how many aren't weapons.
    """
    try:
        weapons = db.armory_weapon.count_documents({})
        items = db.armory_item.count_documents({})
        return f"Weapons: {weapons}, Not Weapons: {items - weapons}"
    except Exception as e:
        raise Exception(f"Error executing count_rpg_weapons count_documents: {e}")
    
def count_items_per_character(db):
    """
        Count how many items each character has; return first 20 rows.
    """
    try:
        cursor = db.characters.find(
            {},
            { "name": 1, "item_count": {"$size": "$items"}, "_id": 0}
        ).limit(20)
        return list(cursor)
    except Exception as e:
        raise Exception(f"Error executing count_items_per_character query: {e}")
    
def count_weapons_per_character(db):
    """
        Count how many weapons each character has; return first 20 rows.
    """
    try:
        cursor = db.characters.find(
            {},
            { "name": 1, "weapon_count": {"$size": "$weapons"}, "_id": 0}
        ).limit(20)
        return list(cursor)
    except Exception as e:
        raise Exception(f"Error executing count_weapons_per_character query: {e}")
    
def avg_items_per_character(db):
    """
        Get the average item count per character
    """
    try:
        pipeline = [
            {"$project": {"item_count": {"$size": {"$ifNull": ["$items", []]}}}},
            {"$group": {"_id": None, "avg_item_count": {"$avg": "$item_count"}}},
            {"$project": {"avg_item_count": {"$round": ["$avg_item_count", 2]}}}
        ]
        result = db.characters.aggregate(pipeline)
        result_list = list(result)
        return result_list[0]["avg_item_count"] if result_list else 0.0
    except Exception as e:
        raise Exception(f"Error executing avg_items_per_character query: {e}")
    
def avg_weapons_per_character(db):
    """
        Get the average weapons per character
    """
    try:
        pipeline = [
            {"$project": {"weapon_count": {"$size": {"$ifNull": ["$weapons", []]}}}},
            {"$group": {"_id": None, "avg_weapon_count": {"$avg": "$weapon_count"}}},
            {"$project": {"avg_weapon_count": {"$round": ["$avg_weapon_count", 2]}}}
        ]
        result = db.characters.aggregate(pipeline)
        result_list = list(result)
        return result_list[0]["avg_weapon_count"] if result_list else 0.0
    except Exception as e:
        raise Exception(f"Error executing avg_weapons_per_character query: {e}")