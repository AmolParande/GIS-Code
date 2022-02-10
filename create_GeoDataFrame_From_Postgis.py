from sqlalchemy import create_engine
import geopandas as gpd
db_connection_url = "postgresql://caprod-cpp-pgmnr-005.flatns.net/mnr?user=mnr_ro&password=mnr_ro"
con = create_engine(db_connection_url)

postgreSQL_select_Query = """SELECT 
                          mnr_admin_area.feat_id::text, 
                          mnr_admin_area.feat_type, 
                          mnr_admin_area.name, 
                          mnr_admin_area.country_code_char3, 
                          mnr_admin_area.lang_code, 
                          mnr_admin_area.a8_admin_code,
                          mnr_admin_area.standard_lang,
                          mnr_admin_area.geom

                        FROM 
                          eur_cas.mnr_admin_area
                        WHERE 
                          mnr_admin_area.feat_type = 1111 AND 
                          (mnr_admin_area.country_code_char3 = 'FRA' OR
                          mnr_admin_area.country_code_char3 = '$'||Left('FRA',2)); """

gdf = gpd.GeoDataFrame.from_postgis(postgreSQL_select_Query , con)
gdf.to_file("/Users/parande/Documents/2_Python_Project/PYTHON_CODE_OUTPUT_DIR/AA.shp")