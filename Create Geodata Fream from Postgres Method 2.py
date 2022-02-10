import pandas as pds
import psycopg2
import geopandas as gpd
from sqlalchemy import create_engine


# Create an engine instance

alchemyEngine   = create_engine('postgresql+psycopg2://caprod-cpp-pgmnr-005.flatns.net/mnr?user=mnr_ro&password=mnr_ro', pool_recycle=3600);
# Connect to PostgreSQL server

dbConnection    = alchemyEngine.connect();

postgreSQL_select_Query = """SELECT 
                          mnr_admin_area.feat_id::text, 
                          mnr_admin_area.feat_type, 
                          mnr_admin_area.name, 
                          mnr_admin_area.country_code_char3, 
                          mnr_admin_area.lang_code, 
                          mnr_admin_area.a8_admin_code,
                          mnr_admin_area.standard_lang,
                          ST_AsText(mnr_admin_area.geom) as geom
                        FROM 
                          eur_cas.mnr_admin_area
                        WHERE 
                          mnr_admin_area.feat_type = 1111 AND 
                          (mnr_admin_area.country_code_char3 = 'FRA' OR
                          mnr_admin_area.country_code_char3 = '$'||Left('FRA',2)); """

# Read data from PostgreSQL database table and load into a DataFrame instance

dataFrame = pds.read_sql(postgreSQL_select_Query, dbConnection);

gs = gpd.GeoSeries.from_wkt(dataFrame['geom'])
pds.set_option('display.expand_frame_repr', False);

# Print the DataFrame

GeoDB = gpd.GeoDataFrame(dataFrame, geometry=gs, crs="EPSG:4326")


GeoDB.to_file("/Users/parande/Documents/2_Python_Project/PYTHON_CODE_OUTPUT_DIR/AAAA.shp")


dbConnection.close();

