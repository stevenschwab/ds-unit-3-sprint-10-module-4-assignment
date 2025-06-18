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