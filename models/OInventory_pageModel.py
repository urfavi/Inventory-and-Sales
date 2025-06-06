from datetime import datetime

class InventoryModel:
    def __init__(self, database):
        self.database = database
        if not self.database.connection:
            self.database.connect()

    def get_all_products(self):
        query = """
            SELECT 
                p.product_id, 
                t.prod_type_name,
                p.product_name, 
                p.product_price,
                s.prod_spec_stock_qty,
                s.prod_spec_color,
                s.prod_spec_length_mm,
                s.prod_spec_thickness_mm,
                s.prod_spec_width_mm,
                s.prod_spec_other,
                p.product_source,
                p.product_created_at,
                p.product_updated_at
            FROM product p
            LEFT JOIN product_type t ON p.product_type_id = t.prod_type_id
            LEFT JOIN product_specification s ON p.product_id = s.product_id
            ORDER BY p.product_name;
        """
        try:
            cursor = self.database.connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall() # Fetch directly as tuples
            cursor.close()
            return rows
        except Exception as e:
            print(f"Error getting all products: {e}")
            return []

    def get_products_by_type(self, prod_type_name):
        query = """
            SELECT 
                p.product_id, 
                t.prod_type_name,
                p.product_name, 
                p.product_price,
                s.prod_spec_stock_qty,
                s.prod_spec_color,
                s.prod_spec_length_mm,
                s.prod_spec_thickness_mm,
                s.prod_spec_width_mm,
                s.prod_spec_other,
                p.product_source,
                p.product_created_at,
                p.product_updated_at
            FROM product p
            LEFT JOIN product_type t ON p.product_type_id = t.prod_type_id
            LEFT JOIN product_specification s ON p.product_id = s.product_id
            WHERE t.prod_type_name = %s
            ORDER BY p.product_name;
        """
        try:
            cursor = self.database.connection.cursor()
            cursor.execute(query, (prod_type_name,))
            rows = cursor.fetchall() # Fetch directly as tuples
            cursor.close()
            return rows
        except Exception as e:
            print(f"Error getting products by type: {e}")
            return []
    
    def get_product_type_id(self, prod_type_name):
        query = "SELECT prod_type_id FROM PRODUCT_TYPE WHERE prod_type_name = %s"
        cursor = self.database.connection.cursor()
        cursor.execute(query, (prod_type_name,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else None
    
    def get_product_by_id(self, product_id):
        query = """
            SELECT 
                p.product_id, 
                t.prod_type_name,
                p.product_name, 
                p.product_price,
                s.prod_spec_id,
                s.prod_spec_stock_qty,
                s.prod_spec_color,
                s.prod_spec_length_mm,
                s.prod_spec_thickness_mm,
                s.prod_spec_width_mm,
                s.prod_spec_other,
                p.product_source,
                p.product_created_at,
                p.product_updated_at
            FROM product p
            LEFT JOIN product_type t ON p.product_type_id = t.prod_type_id
            LEFT JOIN product_specification s ON p.product_id = s.product_id
            WHERE p.product_id = %s
        """
        try:
            cursor = self.database.connection.cursor()
            cursor.execute(query, (product_id,))
            result = cursor.fetchone()
            cursor.close()
            
            if result:
                columns = [
                    "product_id", "prod_type_name", "product_name", "product_price",
                    "prod_spec_id", "stock_qty", "color", "length_mm", 
                    "thickness_mm", "width_mm", "other", "product_source",
                    "product_created_at", "product_updated_at"
                ]
                product_dict = dict(zip(columns, result))

                product_dict['stock_qty'] = int(product_dict['stock_qty']) if product_dict['stock_qty'] else 0
                product_dict['length_mm'] = float(product_dict['length_mm']) if product_dict['length_mm'] else None
                product_dict['thickness_mm'] = float(product_dict['thickness_mm']) if product_dict['thickness_mm'] else None
                product_dict['width_mm'] = float(product_dict['width_mm']) if product_dict['width_mm'] else None

                return product_dict
            return None
        except Exception as e:
            print(f"Error getting product by ID: {e}")
            return None
    
    def get_product_name_by_id(self, product_id):
        """Fetches the product name from the product table given a product_id."""
        cursor = None # Initialize cursor outside try block
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT product_name FROM product WHERE product_id = %s", (product_id,))
            result = cursor.fetchone()
            return result['product_name'] if result else None
        except Exception as e:
            print(f"Error fetching product name for ID {product_id}: {e}")
            return None
        finally:
            if cursor:
                cursor.close()

    def validate_price(self, price_str):
        """Helper method to validate and convert price strings"""
        try:
            # Remove peso symbol and commas
            clean_price = price_str.strip().replace("₱", "").replace(",", "")
            return float(clean_price)
        except ValueError:
            raise ValueError("Please enter a valid price (e.g. ₱1,250.50)")
    
    def get_color_name(self, color_id):
        """Convert color ID to color name"""
        if color_id is None:
            return ""
        query = "SELECT color_name FROM colors WHERE color_id = %s"
        cursor = self.database.connection.cursor()
        cursor.execute(query, (color_id,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else str(color_id)  # Fallback to ID if name not found

    def insert_product(self, shop_id, product_type_id, name, price, source):
        try:
            # Validate price first
            validated_price = self.validate_price(price) if isinstance(price, str) else price
            if validated_price <= 0:
                raise ValueError("Price must be greater than zero")
            
            query = """
                INSERT INTO PRODUCT (
                    product_id, shop_id, product_type_id, product_name, 
                    product_price, product_source, product_created_at, product_updated_at
                ) VALUES (
                    CONCAT(LEFT(%s, 1), LPAD(NEXTVAL('product_seq')::text, 3, '0')),
                    %s, %s, %s, %s, %s, %s, %s
                )
                RETURNING product_id
            """
            now = datetime.now()
            prefix = name[0].upper()
            cursor = self.database.connection.cursor()
            cursor.execute(query, (
                prefix, shop_id, product_type_id, name, price, source, now, now
            ))
            product_id = cursor.fetchone()[0]
            self.database.connection.commit()
            cursor.close()
            return product_id
        except Exception as e:
            self.database.connection.rollback()
            print(f"Error inserting product: {e}")
            return None
    
    def get_product_source_by_type(self, prod_type_name):
        """
        Retrieves the 'source' information for a given product type.
        As per previous discussion, assuming 'source' is a fixed value.
        """
        return "J&J FACTORY-MOALBOAL"

    def insert_specification(self, shop_id, product_id, stock_qty, length=None, thickness=None, 
                        width=None, color=None, other=None):
        try:
            query = """
                INSERT INTO PRODUCT_SPECIFICATION (
                    shop_id, product_id, prod_spec_stock_qty, 
                    prod_spec_length_mm, prod_spec_thickness_mm, prod_spec_width_mm,
                    prod_spec_color, prod_spec_other, 
                    prod_spec_created_at, prod_spec_updated_at
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING prod_spec_id
            """
            now = datetime.now()

            stock_qty = int(stock_qty) if stock_qty else 0
            length = float(length) if length else None
            thickness = float(thickness) if thickness else None
            width = float(width) if width else None
            color = str(color) if color else None  # Ensure color is string
                
            # Use the connection's cursor directly if your Database class doesn't wrap execute() to return results
            cursor = self.database.connection.cursor()
            cursor.execute(query, (
                shop_id, product_id, stock_qty, 
                length, thickness, width,
                color, other,
                now, now
            ))
            
            spec_id = cursor.fetchone()[0]
            self.database.connection.commit()
            cursor.close()
            return spec_id
        except Exception as e:
            self.database.connection.rollback()
            print(f"Error inserting specification: {e}")
            return None

    def update_product(self, product_id, name, price, source):
        """Update product information in the database"""
        try:
            # Validate price first
            validated_price = self.validate_price(price) if isinstance(price, str) else price
            if validated_price <= 0:
                raise ValueError("Price must be greater than zero")
            query = """
                UPDATE product 
                SET product_name = %s,
                    product_price = %s,
                    product_source = %s,
                    product_updated_at = %s
                WHERE product_id = %s
            """
            now = datetime.now()
            cursor = self.database.connection.cursor()
            cursor.execute(query, (name, price, source, now, product_id))
            self.database.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error updating product: {e}")
            self.database.connection.rollback()
            return False

    def update_specification(self, product_id, stock_qty, length=None, thickness=None, 
                            width=None, color=None, other=None):
        """Update product specification in the database"""
        try:
            query = """
                UPDATE product_specification
                SET prod_spec_stock_qty = %s,
                    prod_spec_length_mm = %s,
                    prod_spec_thickness_mm = %s,
                    prod_spec_width_mm = %s,
                    prod_spec_color = %s,
                    prod_spec_other = %s,
                    prod_spec_updated_at = %s
                WHERE product_id = %s
            """
            now = datetime.now()
            cursor = self.database.connection.cursor()
            cursor.execute(query, (
                stock_qty,
                float(length) if length else None,
                float(thickness) if thickness else None,
                float(width) if width else None,
                color.strip() if color else None,
                other.strip() if other else None,
                now,
                product_id
            ))
            self.database.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error updating specification: {e}")
            self.database.connection.rollback()
            return False
    
    def search_products_by_name(self, search_query):
        """
        Searches for products by name using a LIKE query (case-insensitive).
        Returns a list of tuples, matching the column order expected by load_inventory_table.
        Aliases are removed for the same reason as get_all_products.
        """
        try:
            query = """
            SELECT
                p.product_id,
                t.prod_type_name,
                p.product_name,
                p.product_price,           -- This will be at index 3 in the tuple
                s.prod_spec_stock_qty,
                s.prod_spec_color,
                s.prod_spec_length_mm,
                s.prod_spec_thickness_mm,
                s.prod_spec_width_mm,
                s.prod_spec_other,
                p.product_source,
                p.product_created_at,
                p.product_updated_at
            FROM product p
            LEFT JOIN product_type t ON p.product_type_id = t.prod_type_id
            LEFT JOIN product_specification s ON p.product_id = s.product_id
            WHERE p.product_name ILIKE %s
            ORDER BY p.product_name;
            """
            cursor = self.database.connection.cursor()
            cursor.execute(query, ('%' + search_query + '%',))
            rows = cursor.fetchall() # Fetch directly as tuples
            cursor.close()
            return rows
        except Exception as e:
            print(f"Error searching products by name: {e}")
            return []


    # In models/InventoryModel.py

    def delete_product_by_id(self, product_id, shop_id=1):
        """Proper deletion that maintains history"""
        try:
            cursor = self.database.connection.cursor()

            # Step 1: Check for product_specification with explicit column selection
            cursor.execute("""
                SELECT ps.prod_spec_id, ps.prod_spec_stock_qty 
                FROM product_specification ps
                JOIN product p ON ps.product_id = p.product_id
                WHERE ps.product_id = %s AND ps.shop_id = %s
            """, (product_id, shop_id))
            spec_data = cursor.fetchone()

            if not spec_data or len(spec_data) < 2:
                return False, f"Product {product_id} not found or invalid specification data."

            spec_id = spec_data[0]
            old_qty = spec_data[1] if len(spec_data) > 1 else 0  # Default to 0 if qty not available

            # Rest of the method remains the same...
            # Step 2: Log DELETE
            cursor.execute("""
                INSERT INTO stock_history (
                    shop_id, user_acc_id, product_spec_id, product_id,
                    stk_hstry_old_stock_qty, stk_hstry_new_stock_qty,
                    stk_hstry_action, product_name, stk_hstry_updated_at 
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, 
                    (SELECT product_name FROM product WHERE product_id = %s), 
                    NOW())
            """, (shop_id, 1, spec_id, product_id, old_qty, 0, 'DELETE', product_id))

            # Step 3: Delete product data
            cursor.execute("DELETE FROM product_specification WHERE product_id = %s AND prod_spec_id = %s", (product_id, spec_id))
            cursor.execute("DELETE FROM product WHERE product_id = %s", (product_id,))

            self.database.connection.commit()
            return True, f"Product {product_id} successfully deleted and logged."

        except Exception as e:
            self.database.connection.rollback()
            return False, f"Delete failed for {product_id}: {e}"
        finally:
            cursor.close()

    def get_low_stock_products(self):
        query = """
            SELECT
                p.product_name,         -- This will be index 0 in the tuple
                ps.prod_spec_stock_qty  -- This will be index 1 in the tuple
            FROM
                product_specification ps
            JOIN
                product p ON ps.product_id = p.product_id AND ps.shop_id = p.shop_id
            WHERE
                ps.prod_spec_stock_qty < 20;
        """
        try:
            # fetch_all will return a list of tuples (e.g., [('Product A', 5), ('Product B', 8)])
            low_stock_items = self.database.fetch_all(query)
            
            return low_stock_items
        except Exception as e:
            print(f"Error fetching low stock items: {e}")
            return []
        
    def _convert_product_data(self, product_data):
        """Convert raw product data to proper types"""
        if isinstance(product_data, dict):
            # Convert dict values
            converted = {}
            for key, value in product_data.items():
                if key.endswith('_qty') or key == 'stock_qty':
                    converted[key] = int(value) if value is not None else 0
                elif key.endswith(('_mm', '_price')):
                    converted[key] = float(value) if value is not None else None
                elif key == 'color':
                    converted[key] = str(value) if value is not None else ""
                else:
                    converted[key] = value
            return converted
        return product_data