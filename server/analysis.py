import geopandas as gpd
from sqlalchemy import create_engine
import os

from spatial_weights import contiguity_weights, knn_weights, distance_weights
from visualization import visualize_neighbors, visualize_local_moran
from moran import calculate_global_morans_I, calculate_local_morans_I

os.makedirs("output", exist_ok=True)

host = "localhost"
port = "5432"
dbname = "gme221_exer4"
user = "postgres"
password = "postgres"

conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

engine = create_engine(conn_str)

sql_query = """
SELECT gid, ass_ass_va, ass_market, geom
FROM public.assessed_parcels;
"""

gdf = gpd.read_postgis(sql_query, engine, geom_col="geom")

# print(gdf.head())
# print("CRS:", gdf.crs)

# w = distance_weights(gdf, 30)
# w = knn_weights(gdf)
w = contiguity_weights(gdf)

# print("Neighbors:", w.neighbors)
# visualize_neighbors(gdf, w)

attribute = "ass_ass_va"
# attribute = "ass_market"
moran_I, p_value = calculate_global_morans_I(gdf, w, attribute)
print("Global Moran's I:", moran_I)
print("p-value:", p_value)

gdf_local = calculate_local_morans_I(gdf, w, attribute)
# print(gdf_local.loc[gdf_local["cluster"] != "Not Significant"].head())

# gdf_local.to_file(
#     "output/spatial_clusters.geojson",
#     driver="GeoJSON"
# )

# print("Saved: output/spatial_clusters.geojson")

visualize_local_moran(gdf_local)