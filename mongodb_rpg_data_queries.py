'''Queries for mongoDb'''

def count_rpg_characters(db):
    """
        Count all documents in the 'characters' collection.
    """
    try:
        return db.characters.count_documents({})
    except Exception as e:
        raise Exception(f"Error executing count_documents: {e}")
    
