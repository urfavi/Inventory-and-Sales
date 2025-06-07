from PyQt5.QtWidgets import QMessageBox

class StockHistoryModel:
    def __init__(self, database_connection):
        self.db = database_connection
        # You might want to add a check here to ensure self.db is connected
        # if not self.db.is_connected():
        #    print("Warning: Database not connected in StockHistoryModel.__init__")

    # This method is for WRITING history to the DB
    def add_history_entry(self, shop_id, user_acc_id, product_spec_id, product_id, product_name,
                          stk_hstry_old_stock_qty, stk_hstry_new_stock_qty,
                          stk_hstry_action):
        try:
            query = """
            INSERT INTO stock_history (
                shop_id,
                user_acc_id,
                product_spec_id,
                product_id,
                product_name,
                stk_hstry_old_stock_qty,
                stk_hstry_new_stock_qty,
                stk_hstry_action,
                stk_hstry_updated_at
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW())
            """
            # There are 8 %s placeholders here.
            # We need to pass exactly 8 values in the tuple.

            self.db.execute(query, (
                shop_id,
                user_acc_id,
                product_spec_id,
                product_id,
                product_name,
                stk_hstry_old_stock_qty,
                stk_hstry_new_stock_qty,
                stk_hstry_action,
                # NOW() handles stk_hstry_updated_at, so it's not in this Python tuple
            ))

            self.db.commit() # This commit is handled by your Database class's commit method
            print(f"History logged: {stk_hstry_action} for Product ID: {product_id} ({product_name})")
            return True

        except Exception as e:
            self.db.rollback() # This rollback is handled by your Database class's rollback method
            print(f"History log FAILED: {e}")
            return False

    def get_stock_history(self, product_type: str = None, shop_id: int = None, limit: int = 500) -> list:
        """
        Get stock history with optional product type and shop_id filtering.
        The `product_type` parameter should correspond to `prod_type_name` in the database.
        """
        base_query = """
            SELECT
                sh.stk_hstry_id,
                sh.user_acc_id AS user_id,
                u.user_acc_username,
                sh.stk_hstry_action AS action_type,
                sh.product_name,
                sh.stk_hstry_old_stock_qty AS old_quantity,
                sh.stk_hstry_new_stock_qty AS new_quantity,
                sh.stk_hstry_updated_at AS timestamp
            FROM
                stock_history sh
            LEFT JOIN
                user_account u ON sh.user_acc_id = u.user_acc_id
            LEFT JOIN
                product p ON sh.product_id = p.product_id
            LEFT JOIN
                product_type pt ON p.product_type_id = pt.prod_type_id
            {where_clause}
            ORDER BY
                sh.stk_hstry_updated_at DESC
            LIMIT %s;
        """

        where_conditions = []
        params = []

        if product_type:
            where_conditions.append("pt.prod_type_name = %s")
            params.append(product_type)

        if shop_id is not None: # Use is not None for 0 or None checks
            where_conditions.append("sh.shop_id = %s")
            params.append(shop_id)

        where_clause = ""
        if where_conditions:
            where_clause = "WHERE " + " AND ".join(where_conditions)

        # The LIMIT parameter always comes last in positional arguments
        params.append(limit)

        query = base_query.format(where_clause=where_clause)

        # --- CRITICAL DEBUG PRINTS (Good to keep for development, remove for production) ---
        print(f"DEBUG: FINAL SQL QUERY BEING EXECUTED:\n{query}")
        print(f"DEBUG: FINAL QUERY PARAMETERS: {params}")
        print(f"DEBUG: Number of parameters: {len(params)}")
        # --- END CRITICAL DEBUG PRINTS ---

        try:
            results = self.db.fetch_all(query, params)
            return results
        except Exception as e:
            print(f"Error fetching stock history: {e}")
            return []
        
    def delete_history_entry(self, history_id: int) -> bool:
        """Delete a stock history entry by its ID"""
        try:
            query = "DELETE FROM stock_history WHERE stk_hstry_id = %s"
            self.db.execute(query, (history_id,))
            self.db.commit()
            print(f"Deleted stock history entry with ID: {history_id}")
            return True
        except Exception as e:
            self.db.rollback()
            print(f"Failed to delete stock history entry: {e}")
            return False
    
    def delete_all_history_entries(self, shop_id=None):
        """Delete all records from the stock_history table.
        
        Args:
            shop_id: Optional shop_id to limit deletion to a specific shop
            
        Returns:
            bool: True if deletion succeeded, False otherwise
        """
        try:
            query = "DELETE FROM stock_history"
            params = None
            
            if shop_id is not None:  # If you want to limit to specific shop
                query += " WHERE shop_id = %s"
                params = (shop_id,)
                
            self.db.execute(query, params)
            self.db.commit()
            print("All stock history records deleted successfully")
            return True
            
        except Exception as e:
            self.db.rollback()
            print(f"Failed to delete all history entries: {e}")
            return False