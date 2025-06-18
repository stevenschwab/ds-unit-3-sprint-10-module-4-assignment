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