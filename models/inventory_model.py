from models.database import Database
import psycopg2.extras

class InventoryModel:
    """Model for inventory-related database operations"""
    
    @staticmethod
    def get_all_products():
        """
        Get all products
        
        Returns:
            list: Products list
        """
        try:
            query = """
            SELECT p.product_id, p.product_name, p.product_price, 
                   pt.prod_type_name,
                   ps.prod_spec_stock_qty, ps.prod_spec_color, ps.prod_spec_other,
                   pd.prod_dimension_length_mm, pd.prod_dimension_width_mm, 
                   pd.prod_dimension_thickness_mm
            FROM product p
            JOIN product_type pt ON p.prod_type_id = pt.prod_type_id
            JOIN product_specification ps ON p.product_id = ps.product_id
            LEFT JOIN product_dimension pd ON ps.prod_spec_id = pd.prod_spec_id
            """
            
            result = Database.execute_query(query)
            return result
        except Exception as e:
            print(f"Get products error: {str(e)}")
            return []
    
    @staticmethod
    def get_products_by_type(type_name):
        """
        Get products by type name
        
        Args:
            type_name (str): Product type name
            
        Returns:
            list: Products list
        """
        try:
            query = """
            SELECT p.product_id, p.product_name, p.product_price, 
                   pt.prod_type_name,
                   ps.prod_spec_stock_qty, ps.prod_spec_color, ps.prod_spec_other,
                   pd.prod_dimension_length_mm, pd.prod_dimension_width_mm, 
                   pd.prod_dimension_thickness_mm
            FROM product p
            JOIN product_type pt ON p.prod_type_id = pt.prod_type_id
            JOIN product_specification ps ON p.product_id = ps.product_id
            LEFT JOIN product_dimension pd ON ps.prod_spec_id = pd.prod_spec_id
            WHERE pt.prod_type_name = %s
            """
            
            result = Database.execute_query(query, (type_name,))
            return result
        except Exception as e:
            print(f"Get products by type error: {str(e)}")
            return []
    
    @staticmethod
    def search_products(search_text):
        """
        Search products by name or description
        
        Args:
            search_text (str): Search text
            
        Returns:
            list: Products list
        """
        try:
            search_param = f"%{search_text}%"
            query = """
            SELECT p.product_id, p.product_name, p.product_price, 
                   pt.prod_type_name,
                   ps.prod_spec_stock_qty, ps.prod_spec_color, ps.prod_spec_other,
                   pd.prod_dimension_length_mm, pd.prod_dimension_width_mm, 
                   pd.prod_dimension_thickness_mm
            FROM product p
            JOIN product_type pt ON p.prod_type_id = pt.prod_type_id
            JOIN product_specification ps ON p.product_id = ps.product_id
            LEFT JOIN product_dimension pd ON ps.prod_spec_id = pd.prod_spec_id
            WHERE p.product_name ILIKE %s
               OR ps.prod_spec_other ILIKE %s
            """
            
            result = Database.execute_query(query, (search_param, search_param))
            return result
        except Exception as e:
            print(f"Search products error: {str(e)}")
            return []
            
    @staticmethod
    def get_product_type_id(type_name):
        """
        Get product type ID by name
        
        Args:
            type_name (str): Product type name
            
        Returns:
            int or None: Product type ID
        """
        try:
            query = """
            SELECT prod_type_id
            FROM product_type
            WHERE prod_type_name = %s
            """
            
            result = Database.execute_query(query, (type_name,), fetch_all=False)
            if result:
                return result['prod_type_id']
            return None
        except Exception as e:
            print(f"Get product type ID error: {str(e)}")
            return None
            
    @staticmethod
    def add_product(shop_id, type_name, name, price, stock_qty, color, length, width, thickness, other_info=None):
        """
        Add a new product
        
        Args:
            shop_id (int): Shop ID
            type_name (str): Product type name
            name (str): Product name
            price (float): Product price
            stock_qty (int): Stock quantity
            color (str): Product color
            length (int): Length in mm
            width (int): Width in mm
            thickness (int): Thickness in mm
            other_info (str, optional): Other product info
            
        Returns:
            int or None: New product ID if successful, None otherwise
        """
        conn = None
        try:
            conn = Database.get_connection()
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            
            # Start transaction
            conn.autocommit = False
            
            # Get product type ID
            cursor.execute("""
                SELECT prod_type_id
                FROM product_type
                WHERE prod_type_name = %s
            """, (type_name,))
            
            type_result = cursor.fetchone()
            if not type_result:
                raise Exception(f"Product type {type_name} not found")
                
            type_id = type_result['prod_type_id']
            
            # Insert product
            product_query = """
            INSERT INTO product (shop_id, prod_type_id, product_name, product_price, 
                               product_created_at, product_updated_at)
            VALUES (%s, %s, %s, %s, NOW(), NOW())
            RETURNING product_id
            """
            
            cursor.execute(product_query, (shop_id, type_id, name, price))
            product_id = cursor.fetchone()['product_id']
            
            # Insert product specification
            spec_query = """
            INSERT INTO product_specification (shop_id, product_id, prod_spec_stock_qty, 
                                             prod_spec_color, prod_spec_other,
                                             prod_spec_created_at, prod_spec_updated_at)
            VALUES (%s, %s, %s, %s, %s, NOW(), NOW())
            RETURNING prod_spec_id
            """
            
            cursor.execute(spec_query, (shop_id, product_id, stock_qty, color, other_info))
            prod_spec_id = cursor.fetchone()['prod_spec_id']
            
            # Insert product dimension
            if length or width or thickness:
                dimension_query = """
                INSERT INTO product_dimension (prod_spec_id, prod_dimension_length_mm, 
                                             prod_dimension_width_mm, prod_dimension_thickness_mm)
                VALUES (%s, %s, %s, %s)
                """
                
                cursor.execute(dimension_query, (prod_spec_id, length, width, thickness))
            
            # Commit transaction
            conn.commit()
            return product_id
            
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Add product error: {str(e)}")
            return None
        finally:
            if conn:
                conn.autocommit = True
                Database.release_connection(conn)
                
    @staticmethod
    def update_product(product_id, name=None, price=None, stock_qty=None, color=None, 
                      length=None, width=None, thickness=None, other_info=None):
        """
        Update product details
        
        Args:
            product_id (int): Product ID
            name (str, optional): Product name
            price (float, optional): Product price
            stock_qty (int, optional): Stock quantity
            color (str, optional): Product color
            length (int, optional): Length in mm
            width (int, optional): Width in mm
            thickness (int, optional): Thickness in mm
            other_info (str, optional): Other product info
            
        Returns:
            bool: Success status
        """
        conn = None
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            
            # Start transaction
            conn.autocommit = False
            
            # Update product base info if needed
            if name is not None or price is not None:
                update_parts = []
                params = []
                
                if name is not None:
                    update_parts.append("product_name = %s")
                    params.append(name)
                    
                if price is not None:
                    update_parts.append("product_price = %s")
                    params.append(price)
                
                update_parts.append("product_updated_at = NOW()")
                
                if update_parts:
                    product_query = f"""
                    UPDATE product
                    SET {', '.join(update_parts)}
                    WHERE product_id = %s
                    """
                    
                    params.append(product_id)
                    cursor.execute(product_query, tuple(params))
            
            # Update product specification if needed
            if stock_qty is not None or color is not None or other_info is not None:
                spec_update_parts = []
                spec_params = []
                
                if stock_qty is not None:
                    spec_update_parts.append("prod_spec_stock_qty = %s")
                    spec_params.append(stock_qty)
                    
                if color is not None:
                    spec_update_parts.append("prod_spec_color = %s")
                    spec_params.append(color)
                    
                if other_info is not None:
                    spec_update_parts.append("prod_spec_other = %s")
                    spec_params.append(other_info)
                
                spec_update_parts.append("prod_spec_updated_at = NOW()")
                
                if spec_update_parts:
                    spec_query = f"""
                    UPDATE product_specification
                    SET {', '.join(spec_update_parts)}
                    WHERE product_id = %s
                    """
                    
                    spec_params.append(product_id)
                    cursor.execute(spec_query, tuple(spec_params))
            
            # Update product dimensions if needed
            if length is not None or width is not None or thickness is not None:
                # First get the spec_id
                cursor.execute("""
                    SELECT prod_spec_id
                    FROM product_specification
                    WHERE product_id = %s
                """, (product_id,))
                
                spec_result = cursor.fetchone()
                if spec_result:
                    spec_id = spec_result[0]
                    
                    # Check if dimension record exists
                    cursor.execute("""
                        SELECT COUNT(*)
                        FROM product_dimension
                        WHERE prod_spec_id = %s
                    """, (spec_id,))
                    
                    has_dimensions = cursor.fetchone()[0] > 0
                    
                    if has_dimensions:
                        # Update existing dimensions
                        dim_update_parts = []
                        dim_params = []
                        
                        if length is not None:
                            dim_update_parts.append("prod_dimension_length_mm = %s")
                            dim_params.append(length)
                            
                        if width is not None:
                            dim_update_parts.append("prod_dimension_width_mm = %s")
                            dim_params.append(width)
                            
                        if thickness is not None:
                            dim_update_parts.append("prod_dimension_thickness_mm = %s")
                            dim_params.append(thickness)
                        
                        if dim_update_parts:
                            dim_query = f"""
                            UPDATE product_dimension
                            SET {', '.join(dim_update_parts)}
                            WHERE prod_spec_id = %s
                            """
                            
                            dim_params.append(spec_id)
                            cursor.execute(dim_query, tuple(dim_params))
                    else:
                        # Insert new dimensions
                        cursor.execute("""
                            INSERT INTO product_dimension (prod_spec_id, prod_dimension_length_mm, 
                                                         prod_dimension_width_mm, prod_dimension_thickness_mm)
                            VALUES (%s, %s, %s, %s)
                        """, (spec_id, length, width, thickness))
            
            # Commit transaction
            conn.commit()
            return True
            
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Update product error: {str(e)}")
            return False
        finally:
            if conn:
                conn.autocommit = True
                Database.release_connection(conn)
                
    @staticmethod
    def delete_product(product_id):
        """
        Delete a product
        
        Args:
            product_id (int): Product ID
            
        Returns:
            bool: Success status
        """
        try:
            query = """
            DELETE FROM product
            WHERE product_id = %s
            """
            
            result = Database.execute_query(query, (product_id,))
            return result > 0
        except Exception as e:
            print(f"Delete product error: {str(e)}")
            return False
    
    @staticmethod
    def get_low_stock_products(threshold=10):
        """
        Get products with low stock
        
        Args:
            threshold (int): Low stock threshold
            
        Returns:
            list: Low stock products
        """
        try:
            query = """
            SELECT p.product_id, p.product_name, p.product_price, 
                   pt.prod_type_name,
                   ps.prod_spec_stock_qty
            FROM product p
            JOIN product_type pt ON p.prod_type_id = pt.prod_type_id
            JOIN product_specification ps ON p.product_id = ps.product_id
            WHERE ps.prod_spec_stock_qty <= %s
            ORDER BY ps.prod_spec_stock_qty ASC
            """
            
            result = Database.execute_query(query, (threshold,))
            return result
        except Exception as e:
            print(f"Get low stock products error: {str(e)}")
            return []