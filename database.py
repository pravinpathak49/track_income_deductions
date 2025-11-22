from firebase_admin import firestore
import json
from datetime import datetime

def get_db():
    """Get Firestore database instance"""
    return firestore.client()

def init_db():
    """Initialize Firestore - no schema needed for NoSQL"""
    # Firestore doesn't require schema initialization
    # Collections are created automatically when first document is added
    pass

def add_entry(date, income, deductions, in_hand):
    """Add a new salary entry to Firestore"""
    db = get_db()
    entries_ref = db.collection('entries')
    
    entry_data = {
        'date': date,
        'income': income,
        'deductions': deductions,  # Firestore supports nested objects
        'in_hand': in_hand,
        'created_at': firestore.SERVER_TIMESTAMP
    }
    
    doc_ref = entries_ref.add(entry_data)
    return doc_ref[1].id  # Return the document ID

def get_all_entries():
    """Get all salary entries from Firestore, ordered by date descending"""
    db = get_db()
    entries_ref = db.collection('entries')
    
    # Query entries ordered by date descending
    docs = entries_ref.order_by('date', direction=firestore.Query.DESCENDING).stream()
    
    results = []
    for doc in docs:
        entry = doc.to_dict()
        entry['id'] = doc.id  # Add document ID to the entry
        results.append(entry)
    
    return results

def delete_entry(entry_id):
    """Delete a salary entry from Firestore"""
    db = get_db()
    db.collection('entries').document(entry_id).delete()

def get_entry(entry_id):
    """Get a single salary entry by ID"""
    db = get_db()
    doc = db.collection('entries').document(entry_id).get()
    
    if doc.exists:
        entry = doc.to_dict()
        entry['id'] = doc.id
        return entry
    return None

def update_entry(entry_id, date, income, deductions, in_hand):
    """Update an existing salary entry in Firestore"""
    db = get_db()
    entry_ref = db.collection('entries').document(entry_id)
    
    entry_data = {
        'date': date,
        'income': income,
        'deductions': deductions,
        'in_hand': in_hand,
        'updated_at': firestore.SERVER_TIMESTAMP
    }
    
    entry_ref.update(entry_data)
