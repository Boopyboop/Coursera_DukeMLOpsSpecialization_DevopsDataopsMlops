# feature_store.py
"""Lightweight SQLite-backed feature store prototype."""

import os
import sqlite3
from typing import Dict, Any, Optional

DB_PATH = os.environ.get("FEATURE_DB", "data/feature_store.db")


class FeatureStore:
    """A minimal feature store using SQLite."""

    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._init_schema()

    def _init_schema(self) -> None:
        c = self.conn.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS features (
                entity_id TEXT,
                feature_key TEXT,
                feature_value TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (entity_id, feature_key)
            )
            """
        )
        self.conn.commit()

    def upsert(self, entity_id: str, features: Dict[str, Any]) -> None:
        """Upsert a set of features for an entity."""
        c = self.conn.cursor()
        for key, value in features.items():
            c.execute(
                """
                INSERT INTO features(entity_id, feature_key, feature_value)
                VALUES (?, ?, ?)
                ON CONFLICT(entity_id, feature_key) DO UPDATE SET
                  feature_value = excluded.feature_value,
                  updated_at = CURRENT_TIMESTAMP
                """,
                (entity_id, key, str(value)),
            )
        self.conn.commit()

    def get(self, entity_id: str) -> Dict[str, str]:
        """Return all features for a single entity."""
        c = self.conn.cursor()
        c.execute(
            "SELECT feature_key, feature_value FROM features WHERE entity_id = ?",
            (entity_id,),
        )
        rows = c.fetchall()
        return {k: v for k, v in rows}

    def close(self) -> None:
        self.conn.close()


if __name__ == "__main__":
    # small demo
    fs = FeatureStore()
    fs.upsert("global", {"f0": 1.2, "f1": "A"})
    print(fs.get("global"))
    fs.close()
