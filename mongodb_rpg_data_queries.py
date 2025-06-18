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